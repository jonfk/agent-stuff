#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml>=6"]
# ///
"""Symlink each skill of the groups selected in profiles.yaml into the harness
skill folders (~/.claude/skills, ~/.agents/skills). Run with --help."""

from __future__ import annotations

import argparse
import json
import os
import re
import socket
import sys
from dataclasses import dataclass, field
from typing import Callable, Iterable, Optional, TextIO

import yaml

TARGETS = {
    "claude": (".claude", "skills"),
    "agents": (".agents", "skills"),
}

PROFILES_FILE = "profiles.yaml"
HOSTNAME = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_-]*")
GROUP_DIRECTORY = re.compile(r"skills(-.+)?")
FRONTMATTER = re.compile(r"---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.S)

EXIT_OK = 0
EXIT_CONFLICT = 1
EXIT_INVALID = 2

DRY_RUN_VERBS = {"linked": "link", "repointed": "repoint", "removed": "remove"}


class Invalid(Exception):
    """Carries every problem found, so one run reports them all."""

    def __init__(self, problems: str | Iterable[str]):
        self.problems = [problems] if isinstance(problems, str) else list(problems)
        super().__init__("\n".join(self.problems))


@dataclass
class Config:
    # profile name => target key => {skill name => skill directory}
    plans: dict[str, dict[str, dict[str, str]]]
    warnings: list[str]


@dataclass
class GroupScan:
    skills: dict[str, str] = field(default_factory=dict)
    # Why the group itself is unusable; reported for each profile listing it.
    problem: Optional[str] = None
    skill_errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def run(
    argv: list[str],
    root: str,
    out: Optional[TextIO] = None,
    err: Optional[TextIO] = None,
    hostname: Optional[str] = None,
) -> int:
    """Returns the process exit status. `root` is the repo root holding
    profiles.yaml and the group directories."""
    out = out or sys.stdout
    err = err or sys.stderr
    try:
        return _run(argv, root, out, err, hostname)
    except Invalid as error:
        report_invalid(error, err)
        return EXIT_INVALID


def report_invalid(error: Invalid, err: TextIO) -> None:
    for problem in unique(error.problems):
        print(f"error: {problem}", file=err)
    print("Nothing was changed.", file=err)


def _run(argv, root, out, err, hostname) -> int:
    options = parse_options(argv)
    root = os.path.realpath(root)
    config = load_config(root)
    for warning in config.warnings:
        print(f"warning: {warning}", file=err)
    if options.check:
        return report_check(config, out)

    home = os.path.abspath(os.path.expanduser(options.home or "~"))
    host = (options.host or hostname or detect_hostname()).lower()
    if not host:
        raise Invalid("could not determine the hostname; pass --host NAME")

    profile_name = f"hosts.{host}" if f"hosts.{host}" in config.plans else "default"
    targets = [(key, os.path.join(home, *parts)) for key, parts in TARGETS.items()]
    errors = [problem for _key, target in targets if (problem := target_problem(target))]
    if errors:
        raise Invalid(errors)

    if profile_name == "default":
        listed = f"not listed in {PROFILES_FILE}, using profile default"
    else:
        listed = f"profile {profile_name}"
    suffix = " (dry run, nothing changed)" if options.dry_run else ""
    print(f"host {host}: {listed}{suffix}", file=out)

    plan = config.plans[profile_name]
    conflicts = sum(apply(key, target, plan[key], root, options.dry_run, out) for key, target in targets)
    return EXIT_OK if conflicts == 0 else EXIT_CONFLICT


class _Parser(argparse.ArgumentParser):
    def error(self, message):  # argparse would print usage and exit
        raise Invalid(message)


def parse_options(argv: list[str]) -> argparse.Namespace:
    parser = _Parser(
        prog="link_skills.py",
        allow_abbrev=False,
        description=(
            "Links each skill of the groups profiles.yaml selects for this host into "
            "<home>/.claude/skills and <home>/.agents/skills. Prunes only symlinks that "
            "point inside this repo; never touches anything else. Every profile is "
            "validated on every run, and any error stops the run before a change."
        ),
    )
    parser.add_argument("--host", metavar="NAME", help="use this host's profile (default: the short hostname)")
    parser.add_argument("--home", metavar="DIR", help="home directory holding the targets (default: $HOME)")
    parser.add_argument("-n", "--dry-run", action="store_true", help="print what would change; change nothing")
    parser.add_argument(
        "--check", action="store_true", help="validate profiles.yaml and every skill it selects; change nothing"
    )
    options = parser.parse_args(argv)
    if options.host is not None and not options.host.strip():
        raise Invalid("--host needs a name")
    return options


def detect_hostname() -> str:
    """The short hostname, as `hostname -s` prints it."""
    return socket.gethostname().split(".")[0]


def report_check(config: Config, out: TextIO) -> int:
    print(f"{PROFILES_FILE} is valid: {len(config.plans)} profile(s)", file=out)
    for name, plan in config.plans.items():
        counts = ", ".join(f"{key} {len(plan[key])} skills" for key in TARGETS)
        print(f"  {name}: {counts}", file=out)
    return EXIT_OK


def unique(items: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(items))


def q(value: object) -> str:
    """Quotes a value for a message: strings in double quotes, the rest as Python shows it."""
    return json.dumps(value) if isinstance(value, str) else repr(value)


# ---- profiles.yaml ---------------------------------------------------------


def load_config(root: str) -> Config:
    """Validates the whole file, every profile, and every skill a profile
    selects. Raises Invalid listing every problem."""
    path = os.path.join(root, PROFILES_FILE)
    if not os.path.isfile(path):
        raise Invalid(f"missing {path}")

    errors: list[str] = []
    warnings: list[str] = []
    with open(path, encoding="utf-8") as file:
        profiles = profile_table(parse_yaml(file.read(), errors), errors)

    scans: dict[str, GroupScan] = {}
    plans = {
        name: {
            key: desired_links(root, f"{name}.{key}", profile[key], scans, errors, warnings) for key in TARGETS
        }
        for name, profile in profiles.items()
    }
    warnings.extend(unused_group_warnings(root, profiles))

    if errors:
        raise Invalid(errors)
    return Config(plans, unique(warnings))


def parse_yaml(text: str, errors: list[str]) -> object:
    try:
        document = yaml.compose(text, Loader=yaml.SafeLoader)
        if document is None:
            raise Invalid(f"{PROFILES_FILE}: file is empty")
        duplicate_keys(document, errors, set())
        return yaml.safe_load(text)
    except yaml.YAMLError as error:
        raise Invalid(f"{PROFILES_FILE}: invalid YAML ({' '.join(str(error).split())})") from error


def duplicate_keys(node: yaml.Node, errors: list[str], visited: set[int]) -> None:
    """YAML keeps the last of two equal keys without complaint, which would
    silently drop a profile or a target."""
    if id(node) in visited:  # an anchor can be reached more than once
        return
    visited.add(id(node))

    if isinstance(node, yaml.MappingNode):
        seen: dict[str, int] = {}
        for key, value in node.value:
            if isinstance(key, yaml.ScalarNode) and key.value != "<<":
                line = key.start_mark.line + 1
                if key.value in seen:
                    errors.append(
                        f"{PROFILES_FILE}: line {line}: duplicate key {q(key.value)} "
                        f"(first on line {seen[key.value]})"
                    )
                else:
                    seen[key.value] = line
            duplicate_keys(key, errors, visited)
            duplicate_keys(value, errors, visited)
    elif isinstance(node, yaml.SequenceNode):
        for child in node.value:
            duplicate_keys(child, errors, visited)


def profile_table(data: object, errors: list[str]) -> dict[str, dict]:
    """Returns profile name ("default", "hosts.<name>") => valid profile."""
    if not isinstance(data, dict):
        errors.append(f"{PROFILES_FILE}: must be a mapping with `default` and `hosts`")
        return {}

    unknown = [key for key in data if key not in ("default", "hosts")]
    if unknown:
        errors.append(
            f"{PROFILES_FILE}: unknown top-level key(s) {', '.join(map(q, unknown))}; "
            "only `default` and `hosts` are allowed"
        )

    table: dict[str, object] = {}
    if "default" in data:
        table["default"] = data["default"]
    else:
        errors.append(f"{PROFILES_FILE}: missing the `default` profile, used by hosts not listed under `hosts`")

    hosts = data.get("hosts")
    if isinstance(hosts, dict):
        for host, profile in hosts.items():
            if not (isinstance(host, str) and HOSTNAME.fullmatch(host)):
                errors.append(
                    f"{PROFILES_FILE}: hosts: {q(host)} is not a short hostname as `hostname -s` prints it "
                    "(letters, digits, hyphens, no dots; quote a name YAML reads as another type)"
                )
                continue
            name = f"hosts.{host.lower()}"
            if name in table:
                errors.append(
                    f"{PROFILES_FILE}: hosts: {q(host)} is listed twice (hostnames match case-insensitively)"
                )
                continue
            table[name] = profile
    elif hosts is not None:
        errors.append(f"{PROFILES_FILE}: hosts must be a mapping of hostname to profile")

    return {name: profile for name, profile in table.items() if valid_profile(name, profile, errors)}


def valid_profile(name: str, profile: object, errors: list[str]) -> bool:
    targets = " and ".join(TARGETS)
    if not isinstance(profile, dict):
        errors.append(f"{PROFILES_FILE}: {name} must be a mapping with {targets}")
        return False

    before = len(errors)
    unknown = [key for key in profile if key not in TARGETS]
    if unknown:
        errors.append(
            f"{PROFILES_FILE}: {name} has unknown target(s) {', '.join(map(q, unknown))}; "
            f"only {targets} are allowed"
        )

    for key in TARGETS:
        if key not in profile:
            errors.append(f"{PROFILES_FILE}: {name} must list {key} (use [] for none)")
            continue

        groups = profile[key]
        if not (isinstance(groups, list) and all(isinstance(group, str) and group.strip() for group in groups)):
            errors.append(f"{PROFILES_FILE}: {name}.{key} must be a list of group directory names")
            continue

        repeated = unique(group for group in groups if groups.count(group) > 1)
        if repeated:
            errors.append(f"{PROFILES_FILE}: {name}.{key} lists {', '.join(repeated)} more than once")
    return len(errors) == before


# ---- groups and skills -----------------------------------------------------


def desired_links(
    root: str, label: str, groups: list[str], scans: dict[str, GroupScan], errors: list[str], warnings: list[str]
) -> dict[str, str]:
    """Maps skill name => absolute skill directory for one target of one profile."""
    found: dict[str, tuple[str, str]] = {}
    for group in groups:
        if group not in scans:
            scans[group] = scan_group(root, group)
        scan = scans[group]
        if scan.problem:
            errors.append(f"{label}: {scan.problem}")
        errors.extend(scan.skill_errors)
        warnings.extend(scan.warnings)
        for name, path in scan.skills.items():
            if name in found:
                errors.append(f"{label}: skill {q(name)} is in both {found[name][0]} and {group}")
            else:
                found[name] = (group, path)
    return {name: path for name, (_group, path) in found.items()}


def scan_group(root: str, group: str) -> GroupScan:
    scan = GroupScan()
    if os.path.isabs(group) or ".." in group.split("/"):
        scan.problem = f"group {q(group)} must be a directory inside the repo"
        return scan

    directory = os.path.join(root, group)
    if not os.path.isdir(directory):
        scan.problem = f"unknown group {q(group)} (no directory {directory})"
        return scan

    for name in sorted(os.listdir(directory)):
        skill = os.path.join(directory, name)
        if name.startswith(".") or not os.path.isdir(skill):
            continue

        manifest = os.path.join(skill, "SKILL.md")
        if not os.path.isfile(manifest):
            scan.warnings.append(f"{group}/{name} has no SKILL.md; it is not linked")
            continue

        problem = manifest_problem(manifest, name)
        if problem:
            scan.skill_errors.append(f"{group}/{name}/SKILL.md: {problem}")
        else:
            scan.skills[name] = skill

    if not scan.skills and not scan.skill_errors:
        scan.problem = f"group {q(group)} has no skills (no <skill>/SKILL.md in {directory})"
    return scan


def manifest_problem(manifest: str, directory_name: str) -> Optional[str]:
    """A harness identifies a skill by its frontmatter name, while the link and
    the duplicate check use the directory name, so the two must agree."""
    with open(manifest, encoding="utf-8") as file:
        match = FRONTMATTER.match(file.read())
    if not match:
        return "missing YAML frontmatter"

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as error:
        return f"invalid YAML frontmatter ({' '.join(str(error).split())})"
    if not isinstance(frontmatter, dict):
        return "frontmatter must be a mapping"

    name = frontmatter.get("name")
    if name == directory_name:
        return None
    return f"frontmatter name {q(name)} must match its directory name {q(directory_name)}"


def unused_group_warnings(root: str, profiles: dict[str, dict]) -> list[str]:
    used = {group for profile in profiles.values() for key in TARGETS for group in profile[key]}
    return [
        f"group {name} is not used by any profile in {PROFILES_FILE}"
        for name in sorted(os.listdir(root))
        if GROUP_DIRECTORY.fullmatch(name) and os.path.isdir(os.path.join(root, name)) and name not in used
    ]


# ---- targets ---------------------------------------------------------------


def link_destination(path: str) -> str:
    """Where a symlink points, as an absolute path, without resolving further links."""
    return os.path.abspath(os.path.join(os.path.dirname(path), os.readlink(path)))


def target_problem(target: str) -> Optional[str]:
    if os.path.islink(target):
        return f"{target} is a symlink to {link_destination(target)}; replace it with a real directory"
    if os.path.exists(target) and not os.path.isdir(target):
        return f"{target} exists and is not a directory"
    return None


def owned(link_dest: str, root: str) -> bool:
    return link_dest == root or link_dest.startswith(root + os.sep)


def apply(key: str, target: str, desired: dict[str, str], root: str, dry_run: bool, out: TextIO) -> int:
    """Applies (or with dry_run, prints) one target's plan. Returns its conflicts."""
    counts = dict.fromkeys(("linked", "repointed", "removed", "unchanged", "conflicts"), 0)
    lines: list[str] = []

    def act(verb: str, detail: str, action: Optional[Callable[[], None]] = None) -> None:
        counts[verb] += 1
        if verb != "unchanged":
            lines.append(f"  {'would ' + DRY_RUN_VERBS[verb] if dry_run else verb} {detail}")
        if action and not dry_run:
            action()

    if not dry_run and not os.path.isdir(target):
        os.makedirs(target)
    existing = sorted(os.listdir(target)) if os.path.isdir(target) else []

    for name in existing:
        path = os.path.join(target, name)
        if name in desired or not os.path.islink(path):
            continue
        dest = link_destination(path)
        if owned(dest, root):
            act("removed", f"{name} (was {dest})", lambda: os.unlink(path))

    for name, skill in desired.items():
        path = os.path.join(target, name)

        def repoint() -> None:
            os.unlink(path)
            os.symlink(skill, path)

        if not os.path.lexists(path):
            act("linked", f"{name} -> {skill}", lambda: os.symlink(skill, path))
        elif os.path.islink(path) and owned(link_destination(path), root):
            current = link_destination(path)
            if current == skill:
                act("unchanged", name)
            else:
                act("repointed", f"{name} -> {skill} (was {current})", repoint)
        else:
            counts["conflicts"] += 1
            lines.append(f"  conflict {name}: {path} exists and is not a link into this repo; skipped")

    summary = ", ".join(f"{verb} {count}" for verb, count in counts.items())
    print(f"{key} ({target}): {summary}", file=out)
    for line in lines:
        print(line, file=out)
    return counts["conflicts"]


if __name__ == "__main__":
    script = os.path.abspath(__file__)
    sys.exit(run(sys.argv[1:], root=os.path.dirname(os.path.dirname(script))))
