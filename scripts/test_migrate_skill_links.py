#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml>=6"]
# ///
"""Tests for migrate_skill_links.py. Run with: scripts/test_migrate_skill_links.py

Temporary, like the script it tests.
"""

from __future__ import annotations

import io
import os
import shutil
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True

import link_skills  # noqa: E402
import migrate_skill_links  # noqa: E402
from test_link_skills import PROFILES, snapshot  # noqa: E402


class MigrateSkillLinksTest(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp(prefix="migrate-skill-links-test"))
        self.addCleanup(shutil.rmtree, self.tmp)
        self.repo = os.path.join(self.tmp, "repo")
        self.home = os.path.join(self.tmp, "home")
        self.skill("skills", "tdd")
        self.skill("skills-t3", "council")
        self.skill("skills-non-t3", "council")
        self.write_profiles(PROFILES)
        os.makedirs(self.repo_path("skills/synced/bucket"))
        os.makedirs(self.repo_path("skills/old-name"))
        os.makedirs(self.repo_path("skills/notes/kept"))

    def test_converts_both_legacy_symlinks_and_links_skills(self):
        self.legacy_link("claude")
        self.legacy_link("agents")

        status, out, err = self.migrate("--host", "euclid")

        self.assertEqual(0, status, err)
        for key in ("claude", "agents"):
            self.assertFalse(os.path.islink(self.target(key)))
            self.assertTrue(os.path.isdir(self.target(key)))
            self.assertEqual(self.repo_path("skills/tdd"), os.readlink(os.path.join(self.target(key), "tdd")))
            self.assertEqual(
                self.repo_path("skills-t3/council"), os.readlink(os.path.join(self.target(key), "council"))
            )
        self.assertTrue(os.path.isdir(os.path.join(self.target("claude"), "synced", "bucket")))
        self.assertFalse(os.path.exists(self.repo_path("skills/synced")))
        self.assertFalse(os.path.exists(os.path.join(self.target("agents"), "synced")))
        self.assertFalse(os.path.exists(self.repo_path("skills/old-name")), "empty leftover folder is removed")
        self.assertTrue(os.path.isdir(self.repo_path("skills/notes/kept")), "non-empty folder is kept")
        self.assertRegex(out, r"note: .*/skills/notes is not a skill and not empty")

    def test_running_again_changes_nothing(self):
        self.legacy_link("claude")
        self.legacy_link("agents")
        self.migrate("--host", "euclid")
        before = snapshot(self.home, self.repo)

        status, out, _err = self.migrate("--host", "euclid")

        self.assertEqual(0, status)
        self.assertEqual(before, snapshot(self.home, self.repo))
        self.assertIn("already a real directory, left as is", out)

    def test_fresh_host_without_legacy_links_just_links(self):
        status, out, err = self.migrate()

        self.assertEqual(0, status, err)
        self.assertIn("not there yet", out)
        self.assertEqual(
            self.repo_path("skills-non-t3/council"), os.readlink(os.path.join(self.target("claude"), "council"))
        )
        self.assertTrue(os.path.isdir(self.repo_path("skills/synced")), "synced stays when claude was not legacy")

    def test_symlink_to_another_checkout_is_refused_and_nothing_changes(self):
        other = os.path.join(self.tmp, "other-checkout", "skills")
        os.makedirs(other)
        self.legacy_link("claude")
        os.makedirs(os.path.dirname(self.target("agents")))
        os.symlink(other, self.target("agents"))
        before = snapshot(self.home, self.repo)

        status, _out, err = self.migrate()

        self.assertEqual(2, status)
        self.assertIn("not to this checkout's", err)
        self.assertIn("Nothing was changed", err)
        self.assertEqual(before, snapshot(self.home, self.repo))

    def test_invalid_profiles_stop_the_migration_before_any_change(self):
        self.legacy_link("claude")
        self.write_profiles("default:\n  claude: [nope]\n  agents: []\n")
        before = snapshot(self.home, self.repo)

        status, _out, err = self.migrate()

        self.assertEqual(2, status)
        self.assertIn('unknown group "nope"', err)
        self.assertEqual(before, snapshot(self.home, self.repo))

    def test_dry_run_changes_nothing(self):
        self.legacy_link("claude")
        self.legacy_link("agents")
        before = snapshot(self.home, self.repo)

        status, out, _err = self.migrate("--dry-run")

        self.assertEqual(0, status)
        self.assertEqual(before, snapshot(self.home, self.repo))
        self.assertIn("would replace the symlink", out)
        self.assertRegex(out, r"would move .*/skills/synced to .*/\.claude/skills/synced")
        self.assertRegex(out, r"would remove the empty folder .*/skills/old-name")
        self.assertIn("would then run link_skills.py", out)

    def test_synced_stays_in_the_repo_when_claude_was_already_a_real_directory(self):
        os.makedirs(os.path.join(self.target("claude"), "synced", "theirs"))
        self.legacy_link("agents")

        status, out, err = self.migrate()

        self.assertEqual(0, status, err)
        self.assertTrue(os.path.isdir(self.repo_path("skills/synced/bucket")))
        self.assertTrue(os.path.isdir(os.path.join(self.target("claude"), "synced", "theirs")))
        self.assertFalse(os.path.exists(os.path.join(self.target("agents"), "synced")))
        self.assertIn("synced is left in place", out)

    # ---- helpers -----------------------------------------------------------

    def migrate(self, *args: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        status = migrate_skill_links.run(
            ["--home", self.home, *args], root=self.repo, out=out, err=err, hostname="testhost"
        )
        return status, out.getvalue(), err.getvalue()

    def skill(self, group: str, name: str) -> None:
        directory = self.repo_path(f"{group}/{name}")
        os.makedirs(directory)
        with open(os.path.join(directory, "SKILL.md"), "w", encoding="utf-8") as file:
            file.write(f"---\nname: {name}\n---\n")

    def write_profiles(self, text: str) -> None:
        with open(self.repo_path("profiles.yaml"), "w", encoding="utf-8") as file:
            file.write(text)

    def legacy_link(self, key: str) -> None:
        os.makedirs(os.path.dirname(self.target(key)), exist_ok=True)
        os.symlink(self.repo_path("skills"), self.target(key))

    def target(self, key: str) -> str:
        return os.path.join(self.home, *link_skills.TARGETS[key])

    def repo_path(self, relative: str) -> str:
        return os.path.join(self.repo, relative)


if __name__ == "__main__":
    unittest.main()
