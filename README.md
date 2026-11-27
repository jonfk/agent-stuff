
## Skills

The repository contains 22 tracked skills: 20 broadly useful skills under `skills/`
and 2 host-specific variants under `skills-t3/` and `skills-non-t3/`. See
[Installing skills](#installing-skills) for how each host selects them.

Codex can invoke a skill implicitly when the task matches its `description`. A
skill is manual-only in Codex when `agents/openai.yaml` sets
`policy.allow_implicit_invocation: false`; it can still be invoked explicitly
with `$skill-name`. "Implicit" means eligible for automatic selection, not that
Codex will select it for every matching prompt. See the
[official skill invocation documentation](https://learn.chatgpt.com/docs/build-skills#how-chatgpt-and-codex-use-skills).

### Matt Pocock architecture suite

These skills form one cooperating architecture workflow imported directly from
[`mattpocock/skills`](https://github.com/mattpocock/skills):

- `improve-codebase-architecture` orchestrates the architecture review.
- `codebase-design` supplies the deep-module vocabulary and design principles.
- `domain-modeling` maintains the resulting domain language and decisions.
- `grilling` drives the interactive design discussion.

Treat these four skills as an **atomic update cohort**. They evolve together
upstream and cross-reference one another, so update and review all four from the
same upstream commit. Do not advance one member independently unless it is being
intentionally separated and documented as a local fork. See
[`SUBTREE.md`](SUBTREE.md) for the pinned upstream snapshot and update procedure.

### Matt Pocock retro pair

`retro` and `writing-for-agents` are imported together from
[`mattpocock/skills`](https://github.com/mattpocock/skills):

- `retro` reviews a coding session and proposes improvements to the agent's
  environment: navigation pointers, automated checks, coding standards,
  steering files, and tooling.
- `writing-for-agents` is the style and structure reference for skills,
  `AGENTS.md`, `CLAUDE.md`, and other documents agents consume.

`retro` loads `writing-for-agents` on every run, so treat the pair as an
**atomic update cohort** pinned to one upstream commit. It is independent of the
architecture suite. See [`SUBTREE.md`](SUBTREE.md#matt-pocock-retro-pair) for the
update procedure and dependency review.

### Shared skill inventory

| Skill | Codex invocation | Origin |
| --- | --- | --- |
| [`anthropic-frontend-design`](skills/anthropic-frontend-design) | Implicit | [anthropics/skills @ `3337550`](https://github.com/anthropics/skills/tree/33375500bcea98d610eb30ce10ac4e59b89c390d/skills/frontend-design); split `2aa4de6`; locally renamed |
| [`codebase-design`](skills/codebase-design) | Implicit | [mattpocock/skills @ `c55ee46`](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/codebase-design); split `afd7936` |
| [`create-design-doc`](skills/create-design-doc) | **Manual-only** | Local |
| [`domain-modeling`](skills/domain-modeling) | Implicit | [mattpocock/skills @ `c55ee46`](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/domain-modeling); split `e7bce7a` |
| [`fix-with-subagents`](skills/fix-with-subagents) | **Manual-only** | Local |
| [`git-create-commit`](skills/git-create-commit) | Implicit | Local |
| [`git-propose-commit`](skills/git-propose-commit) | Implicit | Local |
| [`git-reshape-history`](skills/git-reshape-history) | **Manual-only** | Local |
| [`git-subtree`](skills/git-subtree) | Implicit | Local |
| [`grill-with-docs`](skills/grill-with-docs) | **Manual-only** | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/grill-with-docs); split `70b6090` |
| [`grilling`](skills/grilling) | Implicit | [mattpocock/skills @ `c55ee46`](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/grilling); split `69b3e82` |
| [`handoff`](skills/handoff) | **Manual-only** | [mattpocock/skills @ `d81f3a1`](https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/handoff); split `dec8c57` |
| [`improve-codebase-architecture`](skills/improve-codebase-architecture) | **Manual-only** | [mattpocock/skills @ `c55ee46`](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/improve-codebase-architecture); split `2d8ac8c` |
| [`pr`](skills/pr) | Implicit | [mattpocock/skills @ `5863806`](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/pr); split `f938d8e` |
| [`prototype`](skills/prototype) | Implicit | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/prototype); split `56dafec` |
| [`retro`](skills/retro) | **Manual-only** | [mattpocock/skills @ `59db609`](https://github.com/mattpocock/skills/tree/59db609eb1e18aaf59b63284d0e52255aff0c63c/skills/engineering/retro); split `796ead9`; requires `writing-for-agents` |
| [`show-me`](skills/show-me) | **Manual-only** | [humanlayer/skills @ `ca7c808`](https://github.com/humanlayer/skills/tree/ca7c8088db69e315a8b2deea43820270457f8f3c/plugins/show-me/skills/show-me); split `e6bc310`; local manual-only policy |
| [`tdd`](skills/tdd) | Implicit | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/tdd); split `54cfb36` |
| [`writing-for-agents`](skills/writing-for-agents) | Implicit | [mattpocock/skills @ `59db609`](https://github.com/mattpocock/skills/tree/59db609eb1e18aaf59b63284d0e52255aff0c63c/skills/productivity/writing-for-agents); split `3bbd7f4` |
| [`yt-transcribe`](skills/yt-transcribe) | Implicit | Local |

Vendored code subtree metadata and update notes live in [`SUBTREE.md`](SUBTREE.md).

`handoff` is a standalone Matt Pocock skill that writes a conversation summary to
the OS temporary directory, references existing artifacts, and suggests skills
for the next agent. It has no required skill dependencies and can be updated
independently of the architecture suite. Upstream also includes it in the
`mattpocock-skills` Claude Code plugin; its router and documentation recommend it
for moving between prototype, teaching, and planning sessions. See
[`SUBTREE.md`](SUBTREE.md#skillshandoff) for the dependency and packaging review.

### Host-specific skill variants

Both variants are named `council`; a host's profile selects at most one per
harness folder.

| Skill | Codex invocation | Origin |
| --- | --- | --- |
| [`council`](skills-t3/council) | Implicit | Local; runs every member through T3 Code's orchestrator, for Claude Code or Codex in T3 Code; inspired by [t3dotgg/tstack @ `1085050`](https://github.com/t3dotgg/tstack/blob/1085050f3baed1ac724caa4a8166145fb2ac88af/skills/council/SKILL.md) |
| [`council`](skills-non-t3/council) | Implicit | Local, Claude Code only; runs members as Claude subagents plus `codex exec`; inspired by [t3dotgg/tstack @ `1085050`](https://github.com/t3dotgg/tstack/blob/1085050f3baed1ac724caa4a8166145fb2ac88af/skills/council/SKILL.md) |

Validate the inventory links, documented totals, and skill frontmatter with
`scripts/check_skill_inventory.py`.

### Manual-only skills

Some skills should only run when explicitly requested, usually because they are workflow-specific and would be noisy if auto-selected. Support both agent conventions:

- Claude Code: add `disable-model-invocation: true` to `SKILL.md` frontmatter.
- Codex: add `policy.allow_implicit_invocation: false` to `agents/openai.yaml`.

Keep both settings together for shared skills so manual invocation works in both tools.

## Installing skills

`~/.claude/skills` (Claude Code) and `~/.agents/skills` (Codex) are real
directories holding one symlink per skill, so each host loads only the skills
its profile selects. Harness-owned content, such as the Claude desktop app's
`synced` folder, lives there too, outside the repo.

- **Groups** are repo-root directories whose immediate children holding a
  `SKILL.md` are skills: `skills` (shared), `skills-t3` (T3 Code hosts), and
  `skills-non-t3` (other hosts). The subtree skills must stay under `skills/`,
  since `git subtree` is pinned to their `skills/<name>` prefix.
- **[`profiles.yaml`](profiles.yaml)** maps each short hostname (`hostname -s`,
  lowercased) to the groups linked into its `claude` and `agents` targets;
  unlisted hosts use `default`. A skill name appearing in two groups for one
  target is an error.
- **`scripts/link_skills.py`** applies the profile: `--host NAME` picks another
  profile, `--home DIR` uses another home directory, and `--dry-run` prints the
  changes without making them. It owns only symlinks pointing inside this repo:
  it creates, repoints, and prunes those, and reports anything else occupying a
  skill's name as a conflict, leaving it untouched.

`just link-skills` runs `scripts/link_skills.py` and passes its arguments
through.

Edits to an existing skill are live through its link. Re-run
`just link-skills` after adding, removing, or renaming a skill, or changing
`profiles.yaml`.

### Setting up a new host

1. Install [uv](https://docs.astral.sh/uv/), and optionally [just](https://just.systems).
2. Clone this repo where it will stay. The links point into the checkout, and
   after a move `link_skills.py` treats the old links as someone else's and
   reports them as conflicts. To move it, delete the links into the old path
   (`find ~/.claude/skills ~/.agents/skills -maxdepth 1 -lname '<old path>/*' -delete`,
   where `<old path>` is the fully resolved path that `readlink` shows on any of
   the links), then run `just link-skills` from the new location.
3. If the host needs something other than `default`, add it under `hosts` in
   [`profiles.yaml`](profiles.yaml), keyed by `hostname -s` in lowercase.
4. Run `just link-skills --dry-run` to preview, then `just link-skills`. It
   creates `~/.claude/skills` and `~/.agents/skills` if they are missing; if
   either is a symlink, replace it with a real directory first.

The T3 group is selected by host, not by harness: on `euclid` and `prim`,
Claude Code or Codex run outside T3 Code also load the T3 `council`, which
needs T3 Code's orchestrator tools.

### Validation

Every run validates the whole of `profiles.yaml` and every skill any profile
selects, not only this host's profile, so a mistake made for another host is
caught where it is written. All problems are reported together, and any error
stops the run before a single link changes. `scripts/link_skills.py --check`
runs the validation alone.

Errors:

- The file is empty, is not valid YAML, has a key other than `default` and
  `hosts`, or lacks `default`.
- A key appears twice in one mapping. YAML would silently keep the last.
- A host key is not a short hostname (it has a dot, or YAML reads it as another
  type, such as `no`), or two host keys differ only by case.
- A profile lacks `claude` or `agents` (use `[]` for none), has another key, or
  lists something that is not a list of group names.
- A group is listed twice for one target, is not a directory in the repo, or
  holds no skills.
- A skill name is in two groups selected for one target.
- A `SKILL.md` has no valid frontmatter, or its `name` differs from its
  directory name.
- A target is a symlink or a file, not a real directory.

Warnings, which do not stop the run:

- A folder in a group has no `SKILL.md`, so it is not linked.
- A `skills` or `skills-*` directory is not used by any profile.

A host missing from `hosts` is not an error: the first output line says it is
not listed and is using `default`.

Tests: `scripts/test_link_skills.py`.

## Inspiration

Inspired by https://github.com/mitsuhiko/agent-stuff. I want to gather interesting skills, prompts, commands, etc.

- [web-browser skill](https://github.com/mitsuhiko/agent-stuff/blob/main/skills/web-browser/SKILL.md): Is apparently better than playwright MCP at browser interactions. Want to try it out. [permalink](https://github.com/mitsuhiko/agent-stuff/blob/063815263cb1031acfa73e12c86f01281dfac5e2/skills/web-browser/SKILL.md)
- [anthropics/skills/frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md): According to Theo from T3gg, he uses this with a prompt that asks for up to 5 unique designs when creating a new design. Something to try. [permalink](https://github.com/anthropics/skills/blob/a5bcdd7e58cdff48566bf876f0a72a2008dcefbc/skills/frontend-design/SKILL.md)
- [mattpocock's skills](https://github.com/mattpocock/skills/) Matt Pocock has a lot of pretty useful and insightful skills.
- [badlogic/pi-skills](https://github.com/badlogic/pi-skills) from the creator of Pi
