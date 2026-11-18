#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml>=6"]
# ///
"""Check that README.md documents every tracked skill, with the right names
and totals, and that manual-only settings agree between Claude Code and Codex."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
# README section heading => group directories whose skills it must document.
GROUPS = {
    "Shared skill inventory": ["skills"],
    "Host-specific skill variants": ["skills-t3", "skills-non-t3"],
}
FRONTMATTER = re.compile(r"---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.S)
INVENTORY_ROW = re.compile(r"\|\s*\[`([^`]+)`\]\(([^)]+)\)\s*\|")
TOTALS = re.compile(
    r"contains (\d+) tracked skills: (\d+) broadly useful skills.*?and (\d+) host-specific variants", re.S
)


def manifests(groups: list[str]) -> list[Path]:
    return sorted(manifest for group in groups for manifest in ROOT.glob(f"{group}/*/SKILL.md"))


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def yaml_error(error: yaml.YAMLError) -> str:
    return " ".join(str(error).split())


def main() -> int:
    errors: list[str] = []
    readme = README.read_text(encoding="utf-8")
    all_manifests = manifests([group for groups in GROUPS.values() for group in groups])

    # Skill directory => frontmatter name (None when it could not be read).
    names: dict[str, object] = {}
    frontmatters: dict[str, dict] = {}
    for manifest in all_manifests:
        directory = relative(manifest.parent)
        names[directory] = None
        match = FRONTMATTER.match(manifest.read_text(encoding="utf-8"))
        if not match:
            errors.append(f"{relative(manifest)}: missing YAML frontmatter")
            continue
        try:
            frontmatter = yaml.safe_load(match.group(1))
        except yaml.YAMLError as error:
            errors.append(f"{relative(manifest)}: invalid YAML frontmatter ({yaml_error(error)})")
            continue
        if not isinstance(frontmatter, dict):
            errors.append(f"{relative(manifest)}: frontmatter must be a mapping")
            continue

        name = frontmatter.get("name")
        if not (isinstance(name, str) and name):
            errors.append(f"{relative(manifest)}: frontmatter name must be a non-empty string")
        frontmatters[directory] = frontmatter
        names[directory] = name

    # Manual-only must be set for both harnesses or for neither.
    for manifest in all_manifests:
        directory = relative(manifest.parent)
        frontmatter = frontmatters.get(directory)
        if frontmatter is None:
            continue

        claude_manual_only = frontmatter.get("disable-model-invocation") is True
        codex_manual_only = False
        openai_manifest = manifest.parent / "agents" / "openai.yaml"
        if openai_manifest.is_file():
            try:
                openai_config = yaml.safe_load(openai_manifest.read_text(encoding="utf-8"))
            except yaml.YAMLError as error:
                errors.append(f"{relative(openai_manifest)}: invalid YAML ({yaml_error(error)})")
                continue
            if not isinstance(openai_config, dict):
                errors.append(f"{relative(openai_manifest)}: configuration must be a mapping")
                continue
            policy = openai_config.get("policy")
            codex_manual_only = isinstance(policy, dict) and policy.get("allow_implicit_invocation") is False

        if claude_manual_only != codex_manual_only:
            errors.append(
                f"{directory}: manual-only invocation must set both "
                "SKILL.md disable-model-invocation: true and "
                "agents/openai.yaml policy.allow_implicit_invocation: false"
            )

    # Each README section must list exactly its groups' skills, by frontmatter name.
    lines = readme.splitlines()
    documented: set[str] = set()
    for heading, groups in GROUPS.items():
        if f"### {heading}" not in lines:
            errors.append(f"README.md: missing {json.dumps(heading)} section")
            continue
        heading_line = lines.index(f"### {heading}")

        entries = []
        for offset, line in enumerate(lines[heading_line + 1 :]):
            if line.startswith("### "):
                break
            match = INVENTORY_ROW.match(line)
            if match:
                entries.append((match.group(1), match.group(2), heading_line + offset + 2))

        expected = [relative(manifest.parent) for manifest in manifests(groups)]
        listed = [directory for _name, directory, _line in entries]
        for directory in expected:
            if directory not in listed:
                errors.append(f"README.md: {heading} does not document {directory}")
        for directory in listed:
            if directory not in expected:
                errors.append(f"README.md: {heading} links missing skill {directory}")

        for documented_name, directory, line_number in entries:
            if directory in documented:
                errors.append(f"README.md:{line_number}: duplicate inventory link for {directory}")
            documented.add(directory)

            manifest_name = names.get(directory)
            if manifest_name and documented_name != manifest_name:
                errors.append(
                    f"README.md:{line_number}: documents {json.dumps(documented_name)}, "
                    f"but {directory}/SKILL.md is named {json.dumps(manifest_name)}"
                )

    shared_count = len(manifests(GROUPS["Shared skill inventory"]))
    variant_count = len(manifests(GROUPS["Host-specific skill variants"]))
    totals = TOTALS.search(readme)
    if totals:
        documented_counts = [int(count) for count in totals.groups()]
        actual_counts = [shared_count + variant_count, shared_count, variant_count]
        if documented_counts != actual_counts:
            errors.append(
                f"README.md: documents skill totals {'/'.join(map(str, documented_counts))}, "
                f"expected {'/'.join(map(str, actual_counts))}"
            )
    else:
        errors.append("README.md: missing tracked/shared/variant skill totals")

    if errors:
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(
        f"Skill inventory is current: {shared_count + variant_count} skills "
        f"({shared_count} shared, {variant_count} host-specific variants)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
