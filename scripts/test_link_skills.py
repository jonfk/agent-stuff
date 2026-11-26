#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml>=6"]
# ///
"""Tests for link_skills.py. Run with: scripts/test_link_skills.py"""

from __future__ import annotations

import io
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest

sys.dont_write_bytecode = True

import link_skills  # noqa: E402

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "link_skills.py")

PROFILES = """\
default:
  claude: [skills, skills-non-t3]
  agents: [skills]
hosts:
  euclid:
    claude: [skills, skills-t3]
    agents: [skills, skills-t3]
"""


def snapshot(*directories: str) -> list[tuple[str, str]]:
    """Every entry under the directories, with link destinations, to compare before and after."""
    entries = []
    for directory in directories:
        for current, dirnames, filenames in os.walk(directory):
            for name in dirnames + filenames:
                path = os.path.join(current, name)
                if os.path.islink(path):
                    kind = os.readlink(path)
                else:
                    kind = "directory" if os.path.isdir(path) else "file"
                entries.append((path, kind))
    return sorted(entries)


class LinkSkillsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp(prefix="link-skills-test"))
        self.addCleanup(shutil.rmtree, self.tmp)
        self.repo = os.path.join(self.tmp, "repo")
        self.home = os.path.join(self.tmp, "home")
        self.skill("skills", "tdd")
        self.skill("skills", "pr")
        self.skill("skills-t3", "council")
        self.skill("skills-non-t3", "council")
        os.makedirs(self.repo_path("skills/not-a-skill"))
        self.write_profiles(PROFILES)

    # ---- linking -----------------------------------------------------------

    def test_host_profile_links_each_skill_into_both_targets(self):
        status, out, _err = self.run_links("--host", "euclid")

        self.assertEqual(0, status, out)
        self.assertEqual(self.repo_path("skills-t3/council"), os.readlink(self.claude("council")))
        self.assertEqual(self.repo_path("skills-t3/council"), os.readlink(self.agents("council")))
        self.assertEqual(self.repo_path("skills/tdd"), os.readlink(self.claude("tdd")))
        self.assertFalse(os.path.lexists(self.claude("not-a-skill")))
        self.assertIn("host euclid: profile hosts.euclid", out)

    def test_unlisted_host_falls_back_to_default(self):
        status, out, _err = self.run_links("--host", "work-laptop")

        self.assertEqual(0, status, out)
        self.assertIn("host work-laptop: not listed in profiles.yaml, using profile default", out)
        self.assertEqual(self.repo_path("skills-non-t3/council"), os.readlink(self.claude("council")))
        self.assertFalse(os.path.lexists(self.agents("council")))
        self.assertEqual(self.repo_path("skills/pr"), os.readlink(self.agents("pr")))

    def test_hostname_is_matched_case_insensitively(self):
        status, out, _err = self.run_links(hostname="EUCLID")

        self.assertEqual(0, status, out)
        self.assertEqual(self.repo_path("skills-t3/council"), os.readlink(self.claude("council")))

    def test_prunes_only_links_into_the_repo(self):
        self.run_links("--host", "euclid")
        other = os.path.join(self.tmp, "elsewhere", "theirs")
        os.makedirs(other)
        os.symlink(other, self.claude("theirs"))
        os.symlink(self.repo_path("skills/gone"), self.claude("gone"))  # dangling, owned
        os.symlink(self.repo_path("skills/tdd"), self.claude("tdd-alias"))  # owned, undesired

        status, out, _err = self.run_links("--host", "euclid")

        self.assertEqual(0, status, out)
        self.assertEqual(other, os.readlink(self.claude("theirs")))
        self.assertFalse(os.path.lexists(self.claude("gone")))
        self.assertFalse(os.path.lexists(self.claude("tdd-alias")))
        self.assertIn("removed 2", out)

    def test_switching_profile_removes_and_repoints_owned_links(self):
        self.run_links("--host", "euclid")

        status, out, _err = self.run_links("--host", "other")

        self.assertEqual(0, status, out)
        self.assertEqual(self.repo_path("skills-non-t3/council"), os.readlink(self.claude("council")))
        self.assertFalse(os.path.lexists(self.agents("council")))
        self.assertIn("repointed 1", out)

    def test_real_directory_and_foreign_link_are_conflicts_left_alone(self):
        os.makedirs(os.path.join(self.claude("tdd"), "keep"))
        os.makedirs(self.claude("synced"))
        os.makedirs(os.path.dirname(self.agents("pr")))
        os.symlink("/nowhere/pr", self.agents("pr"))

        status, out, _err = self.run_links("--host", "euclid")

        self.assertEqual(1, status)
        self.assertTrue(os.path.isdir(os.path.join(self.claude("tdd"), "keep")))
        self.assertFalse(os.path.islink(self.claude("tdd")))
        self.assertTrue(os.path.isdir(self.claude("synced")))
        self.assertEqual("/nowhere/pr", os.readlink(self.agents("pr")))
        self.assertIn("conflict tdd", out)
        self.assertIn("conflict pr", out)
        self.assertEqual(self.repo_path("skills/pr"), os.readlink(self.claude("pr")))

    def test_symlinked_target_is_refused(self):
        os.makedirs(os.path.join(self.home, ".claude"))
        os.symlink(self.repo_path("skills"), os.path.join(self.home, ".claude", "skills"))

        status, _out, err = self.run_links("--host", "euclid")

        self.assertEqual(2, status)
        self.assertIn("replace it with a real directory", err)
        self.assertTrue(os.path.islink(os.path.join(self.home, ".claude", "skills")))
        self.assertFalse(os.path.lexists(os.path.join(self.home, ".agents")), "agents target must not be created")

    def test_dry_run_changes_nothing(self):
        self.run_links("--host", "euclid")
        os.symlink(self.repo_path("skills/gone"), self.claude("gone"))
        before = snapshot(self.home)

        status, out, _err = self.run_links("--host", "other", "--dry-run")

        self.assertEqual(0, status, out)
        self.assertEqual(before, snapshot(self.home))
        self.assertIn("would repoint council", out)
        self.assertIn("would remove gone", out)

    def test_dry_run_on_fresh_home_creates_nothing(self):
        status, out, _err = self.run_links("--dry-run")

        self.assertEqual(0, status, out)
        self.assertFalse(os.path.lexists(self.home))
        self.assertIn("would link tdd", out)

    def test_second_run_is_a_no_op(self):
        self.run_links("--host", "euclid")
        before = snapshot(self.home)

        status, out, _err = self.run_links("--host", "euclid")

        self.assertEqual(0, status)
        self.assertEqual(before, snapshot(self.home))
        unchanged = "linked 0, repointed 0, removed 0, unchanged 3, conflicts 0"
        self.assertRegex(out, rf"claude .*{unchanged}")
        self.assertRegex(out, rf"agents .*{unchanged}")

    def test_cli_entry_point(self):
        scripts = self.repo_path("scripts")
        os.makedirs(scripts)
        shutil.copy(SCRIPT, scripts)

        result = subprocess.run(
            [sys.executable, os.path.join(scripts, "link_skills.py"), "--host", "euclid", "--home", self.home],
            capture_output=True,
            text=True,
        )

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("profile hosts.euclid", result.stdout)
        self.assertEqual(self.repo_path("skills-t3/council"), os.readlink(self.claude("council")))

    # ---- validation --------------------------------------------------------

    def test_duplicate_skill_name_is_an_error_and_changes_nothing(self):
        self.write_profiles(
            """
            default:
              claude: [skills, skills-t3, skills-non-t3]
              agents: [skills]
            """
        )

        status, _out, err = self.run_links()

        self.assertEqual(2, status)
        self.assertIn('default.claude: skill "council" is in both skills-t3 and skills-non-t3', err)
        self.assertFalse(os.path.lexists(self.home))

    def test_unknown_group_is_an_error(self):
        self.write_profiles("default:\n  claude: [skills, nope]\n  agents: []\n")

        status, _out, err = self.run_links()

        self.assertEqual(2, status)
        self.assertIn('default.claude: unknown group "nope"', err)
        self.assertFalse(os.path.lexists(self.home))

    def test_malformed_profile_is_an_error(self):
        self.write_profiles("default:\n  claude: skills\n  agents: []\n")

        status, _out, err = self.run_links()

        self.assertEqual(2, status)
        self.assertIn("default.claude must be a list", err)
        self.assertFalse(os.path.lexists(self.home))

    def test_profile_missing_a_target_is_an_error(self):
        self.write_profiles("default:\n  claude: [skills]\n")

        status, _out, err = self.run_links()

        self.assertEqual(2, status)
        self.assertIn("default must list agents", err)

    def test_every_profile_is_validated_not_only_this_hosts(self):
        self.write_profiles(
            """
            default:
              claude: [skills, skills-non-t3]
              agents: [skills]
            hosts:
              euclid:
                claude: [skills, skills-t3]
                agents: [skills, skills-t3]
              prim:
                claude: [skills, skills-t4]
                agents: [skills, skills-t3, skills-non-t3]
            """
        )

        status, _out, err = self.run_links("--host", "euclid")

        self.assertEqual(2, status)
        self.assertIn('hosts.prim.claude: unknown group "skills-t4"', err)
        self.assertIn('hosts.prim.agents: skill "council" is in both skills-t3 and skills-non-t3', err)
        self.assertFalse(os.path.lexists(self.home))

    def test_all_problems_are_reported_in_one_run(self):
        self.write_profiles(
            """
            default:
              claude: [skills]
            hosts:
              euclid:
                claude: skills
                agents: []
                codex: [skills]
            extra: 1
            """
        )

        status, _out, err = self.run_links()

        self.assertEqual(2, status)
        self.assertIn('unknown top-level key(s) "extra"', err)
        self.assertIn("default must list agents", err)
        self.assertIn('hosts.euclid has unknown target(s) "codex"', err)
        self.assertIn("hosts.euclid.claude must be a list", err)
        self.assertIn("Nothing was changed", err)

    def test_duplicate_yaml_keys_are_an_error(self):
        self.write_profiles(
            """
            default:
              claude: [skills]
              agents: [skills]
            hosts:
              euclid:
                claude: [skills, skills-t3]
                agents: [skills]
              euclid:
                claude: [skills]
                agents: [skills]
                agents: []
            """
        )

        status, _out, err = self.run_links()

        self.assertEqual(2, status)
        self.assertIn('line 8: duplicate key "euclid" (first on line 5)', err)
        self.assertIn('line 11: duplicate key "agents" (first on line 10)', err)

    def test_hostnames_differing_only_by_case_are_an_error(self):
        self.write_profiles(
            """
            default: {claude: [skills], agents: [skills]}
            hosts:
              euclid: {claude: [skills], agents: [skills]}
              Euclid: {claude: [skills], agents: []}
            """
        )

        status, _out, err = self.run_links()

        self.assertEqual(2, status)
        self.assertIn('"Euclid" is listed twice', err)

    def test_host_keys_must_be_short_hostnames(self):
        self.write_profiles(
            """
            default: {claude: [skills], agents: [skills]}
            hosts:
              no: {claude: [skills], agents: [skills]}
              euclid.local: {claude: [skills], agents: [skills]}
            """
        )

        status, _out, err = self.run_links()

        self.assertEqual(2, status)
        self.assertIn("hosts: False is not a short hostname", err)
        self.assertIn('hosts: "euclid.local" is not a short hostname', err)

    def test_missing_default_profile_is_an_error(self):
        self.write_profiles("hosts:\n  euclid: {claude: [skills], agents: [skills]}\n")

        status, _out, err = self.run_links("--host", "euclid")

        self.assertEqual(2, status)
        self.assertIn("missing the `default` profile", err)
        self.assertFalse(os.path.lexists(self.home))

    def test_empty_or_broken_file_is_an_error(self):
        for text in ("", "default: [unclosed\n", "- just\n- a list\n"):
            with self.subTest(text=text):
                self.write_profiles(text)

                status, _out, err = self.run_links()

                self.assertEqual(2, status)
                self.assertIn("profiles.yaml", err)
                self.assertFalse(os.path.lexists(self.home))

    def test_group_listed_twice_is_an_error(self):
        self.write_profiles("default:\n  claude: [skills, skills]\n  agents: []\n")

        status, _out, err = self.run_links()

        self.assertEqual(2, status)
        self.assertIn("default.claude lists skills more than once", err)

    def test_group_without_skills_is_an_error(self):
        os.makedirs(self.repo_path("skills-empty"))
        self.write_profiles("default:\n  claude: [skills, skills-empty]\n  agents: []\n")

        status, _out, err = self.run_links()

        self.assertEqual(2, status)
        self.assertIn('default.claude: group "skills-empty" has no skills', err)

    def test_skill_whose_frontmatter_name_differs_from_its_directory_is_an_error(self):
        self.write(self.repo_path("skills/tdd/SKILL.md"), "---\nname: test-driven\n---\n")
        os.makedirs(self.repo_path("skills/broken"))
        self.write(self.repo_path("skills/broken/SKILL.md"), "no frontmatter here\n")

        status, _out, err = self.run_links()

        self.assertEqual(2, status)
        self.assertIn(
            'skills/tdd/SKILL.md: frontmatter name "test-driven" must match its directory name "tdd"', err
        )
        self.assertIn("skills/broken/SKILL.md: missing YAML frontmatter", err)
        self.assertFalse(os.path.lexists(self.home))

    def test_warns_about_folders_without_a_skill_and_unused_groups(self):
        self.skill("skills-spare", "extra")

        status, _out, err = self.run_links("--host", "euclid")

        self.assertEqual(0, status)
        self.assertIn("warning: skills/not-a-skill has no SKILL.md; it is not linked", err)
        self.assertIn("warning: group skills-spare is not used by any profile", err)
        self.assertEqual(2, len(err.splitlines()), err)

    def test_check_validates_without_touching_the_home(self):
        status, out, _err = self.run_links("--check")

        self.assertEqual(0, status)
        self.assertIn("profiles.yaml is valid: 2 profile(s)", out)
        self.assertIn("hosts.euclid: claude 3 skills, agents 3 skills", out)
        self.assertIn("default: claude 3 skills, agents 2 skills", out)
        self.assertFalse(os.path.lexists(self.home))

        self.write_profiles("default:\n  claude: [nope]\n  agents: []\n")
        status, _out, _err = self.run_links("--check")
        self.assertEqual(2, status)

    def test_unexpected_arguments_are_an_error(self):
        for args in (("euclid",), ("--hots", "euclid"), ("--host", " ")):
            with self.subTest(args=args):
                status, _out, err = self.run_links(*args)

                self.assertEqual(2, status)
                self.assertIn("Nothing was changed", err)
                self.assertFalse(os.path.lexists(self.home))

    # ---- helpers -----------------------------------------------------------

    def run_links(self, *args: str, hostname: str = "testhost") -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        status = link_skills.run(["--home", self.home, *args], root=self.repo, out=out, err=err, hostname=hostname)
        return status, out.getvalue(), err.getvalue()

    def skill(self, group: str, name: str) -> None:
        directory = self.repo_path(f"{group}/{name}")
        os.makedirs(directory)
        self.write(os.path.join(directory, "SKILL.md"), f"---\nname: {name}\n---\n")

    def write_profiles(self, text: str) -> None:
        self.write(self.repo_path("profiles.yaml"), textwrap.dedent(text).lstrip("\n"))

    def write(self, path: str, text: str) -> None:
        with open(path, "w", encoding="utf-8") as file:
            file.write(text)

    def repo_path(self, relative: str) -> str:
        return os.path.join(self.repo, relative)

    def claude(self, name: str) -> str:
        return os.path.join(self.home, ".claude", "skills", name)

    def agents(self, name: str) -> str:
        return os.path.join(self.home, ".agents", "skills", name)


if __name__ == "__main__":
    unittest.main()
