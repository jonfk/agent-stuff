#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml>=6"]
# ///
"""One-time migration from the legacy setup, where ~/.claude/skills and
~/.agents/skills were each a symlink to this repo's whole skills/ folder, to
real directories filled by link_skills.py. Run with --help.

Temporary: delete this script, its test, and the README section that mentions
it once every host has been migrated.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from typing import Callable, Optional, TextIO

import link_skills
from link_skills import EXIT_OK, Invalid

# Folder the Claude desktop app writes into ~/.claude/skills.
CLAUDE_OWNED = "synced"

LEGACY = "legacy"
DIRECTORY = "directory"
MISSING = "missing"


def run(
    argv: list[str],
    root: str,
    out: Optional[TextIO] = None,
    err: Optional[TextIO] = None,
    hostname: Optional[str] = None,
) -> int:
    """Returns the process exit status."""
    out = out or sys.stdout
    err = err or sys.stderr
    try:
        return _run(argv, root, out, err, hostname)
    except Invalid as error:
        link_skills.report_invalid(error, err)
        return link_skills.EXIT_INVALID


def _run(argv, root, out, err, hostname) -> int:
    options = parse_options(argv)
    root = os.path.realpath(root)
    legacy = os.path.join(root, "skills")
    home = os.path.abspath(os.path.expanduser(options.home or "~"))
    dry_run = options.dry_run

    # Validate first: removing the legacy links and then failing to link would
    # leave the harnesses with no skills at all.
    link_skills.load_config(root)

    targets = {key: os.path.join(home, *parts) for key, parts in link_skills.TARGETS.items()}
    states = {}
    problems = []
    for key, target in targets.items():
        states[key], problem = target_state(target, legacy)
        if problem:
            problems.append(problem)
    if problems:
        raise Invalid(problems)

    def say(line: str) -> None:
        print(f"would {line}" if dry_run else line, file=out)

    for key, target in targets.items():
        if states[key] == LEGACY:
            say(f"replace the symlink {target} with a real directory")
            if not dry_run:
                os.unlink(target)
                os.mkdir(target)
        else:
            status = "not there yet" if states[key] == MISSING else "already a real directory"
            print(f"{target}: {status}, left as is", file=out)

    move_claude_owned(legacy, targets["claude"], states["claude"], dry_run, say, out)
    clean_leftovers(legacy, dry_run, say, out)

    link_args = ["--home", home]
    if options.host:
        link_args += ["--host", options.host]
    if dry_run:
        print(f"would then run link_skills.py {' '.join(link_args)}", file=out)
        return EXIT_OK
    return link_skills.run(link_args, root=root, out=out, err=err, hostname=hostname)


class _Parser(argparse.ArgumentParser):
    def error(self, message):  # argparse would print usage and exit
        raise Invalid(message)


def parse_options(argv: list[str]) -> argparse.Namespace:
    parser = _Parser(
        prog="migrate_skill_links.py",
        allow_abbrev=False,
        description=(
            "Replaces the legacy whole-folder symlinks <home>/.claude/skills and "
            "<home>/.agents/skills with real directories, moves the Claude desktop "
            f"app's skills/{CLAUDE_OWNED} folder out of the repo into <home>/.claude/skills, "
            "removes empty leftover folders from skills/, then runs link_skills.py. "
            "Safe to run again. Run it from the checkout the symlinks point to."
        ),
    )
    parser.add_argument("--host", metavar="NAME", help="passed to link_skills.py (default: the short hostname)")
    parser.add_argument("--home", metavar="DIR", help="home directory holding the targets (default: $HOME)")
    parser.add_argument("-n", "--dry-run", action="store_true", help="print what would change; change nothing")
    return parser.parse_args(argv)


def target_state(target: str, legacy: str) -> tuple[Optional[str], Optional[str]]:
    """Returns (state, None), or (None, why the target can't be migrated)."""
    if os.path.islink(target):
        dest = link_skills.link_destination(target)
        resolved = os.path.realpath(target) if os.path.exists(target) else dest
        if resolved == legacy:
            return LEGACY, None
        return None, (
            f"{target} is a symlink to {dest}, not to this checkout's {legacy}. "
            "Run this script from the checkout it points to, or fix the link by hand."
        )
    if os.path.isdir(target):
        return DIRECTORY, None
    if os.path.exists(target):
        return None, f"{target} exists and is not a directory"
    return MISSING, None


def move_claude_owned(
    legacy: str, claude_target: str, claude_state: str, dry_run: bool, say: Callable[[str], None], out: TextIO
) -> None:
    source = os.path.join(legacy, CLAUDE_OWNED)
    if not os.path.isdir(source) or os.path.isfile(os.path.join(source, "SKILL.md")):
        return

    # A converted target is a new, empty directory, so the move cannot collide.
    dest = os.path.join(claude_target, CLAUDE_OWNED)
    if claude_state == LEGACY:
        say(f"move {source} to {dest}")
        if not dry_run:
            shutil.move(source, dest)
    else:
        print(
            f"note: {source} is left in place, because {claude_target} did not point at this repo; "
            "move or delete it by hand",
            file=out,
        )


def clean_leftovers(legacy: str, dry_run: bool, say: Callable[[str], None], out: TextIO) -> None:
    """Empty folders are left behind when a skill is renamed or removed
    upstream, since git does not track directories."""
    for name in sorted(os.listdir(legacy)):
        path = os.path.join(legacy, name)
        if name.startswith(".") or name == CLAUDE_OWNED or os.path.islink(path) or not os.path.isdir(path):
            continue
        if os.path.isfile(os.path.join(path, "SKILL.md")):
            continue

        if not os.listdir(path):
            say(f"remove the empty folder {path}")
            if not dry_run:
                os.rmdir(path)
        else:
            print(f"note: {path} is not a skill and not empty; left in place", file=out)


if __name__ == "__main__":
    script = os.path.abspath(__file__)
    sys.exit(run(sys.argv[1:], root=os.path.dirname(os.path.dirname(script))))
