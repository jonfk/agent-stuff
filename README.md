
## Skills

The repository contains 22 tracked skills: 19 broadly useful skills under `skills/`
and 3 opt-in fiction skills under `skill-packs/fiction/`.

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

### Shared skill inventory

| Skill | Codex invocation | Origin |
| --- | --- | --- |
| [`anthropic-frontend-design`](skills/anthropic-frontend-design) | **Manual-only** | [anthropics/skills @ `3337550`](https://github.com/anthropics/skills/tree/33375500bcea98d610eb30ce10ac4e59b89c390d/skills/frontend-design); split `2aa4de6`; locally renamed |
| [`codebase-design`](skills/codebase-design) | Implicit | [mattpocock/skills @ `c55ee46`](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/codebase-design); split `afd7936` |
| [`create-design-doc`](skills/create-design-doc) | **Manual-only** | Local |
| [`domain-modeling`](skills/domain-modeling) | Implicit | [mattpocock/skills @ `c55ee46`](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/domain-modeling); split `e7bce7a` |
| [`fix-with-subagents`](skills/fix-with-subagents) | **Manual-only** | Local |
| [`git-create-commit`](skills/git-create-commit) | Implicit | Local |
| [`git-propose-commit`](skills/git-propose-commit) | Implicit | Local |
| [`git-reshape-history`](skills/git-reshape-history) | **Manual-only** | Local |
| [`git-subtree`](skills/git-subtree) | Implicit | Local |
| [`grill-me`](skills/grill-me) | **Manual-only** | Maintained local fork of [mattpocock/skills @ `60aa99c`](https://github.com/mattpocock/skills/blob/60aa99c0230fbac087514ba5fca2ae6e519965fe/grill-me/SKILL.md); diverged locally at `fb2dd08` and must not be updated from upstream |
| [`grill-with-docs`](skills/grill-with-docs) | **Manual-only** | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/grill-with-docs); split `70b6090` |
| [`grilling`](skills/grilling) | **Manual-only** | [mattpocock/skills @ `c55ee46`](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/grilling); split `69b3e82`; local manual-only policy |
| [`handoff`](skills/handoff) | **Manual-only** | [mattpocock/skills @ `d81f3a1`](https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/handoff); split `dec8c57` |
| [`improve-codebase-architecture`](skills/improve-codebase-architecture) | **Manual-only** | [mattpocock/skills @ `c55ee46`](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/improve-codebase-architecture); split `2d8ac8c` |
| [`prototype`](skills/prototype) | Implicit | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/prototype); split `56dafec` |
| [`show-me`](skills/show-me) | **Manual-only** | [humanlayer/skills @ `ca7c808`](https://github.com/humanlayer/skills/tree/ca7c8088db69e315a8b2deea43820270457f8f3c/plugins/show-me/skills/show-me); split `e6bc310`; local manual-only policy |
| [`tdd`](skills/tdd) | Implicit | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/tdd); split `54cfb36` |
| [`thermo-nuclear-code-quality-review`](skills/thermo-nuclear-code-quality-review) | **Manual-only** | [cursor/plugins @ `3347cba`](https://github.com/cursor/plugins/tree/3347cbab5b54136f6fba0994c3a01a56f7fb7fca/cursor-team-kit/skills/thermo-nuclear-code-quality-review), substantially rewritten locally |
| [`yt-transcribe`](skills/yt-transcribe) | Implicit | Local |

Vendored code subtree metadata and update notes live in [`SUBTREE.md`](SUBTREE.md).

The `skills` directory contains broadly useful skills and is suitable for linking as
`.agents/skills` so every agent can discover it.

`handoff` is a standalone Matt Pocock skill that writes a conversation summary to
the OS temporary directory, references existing artifacts, and suggests skills
for the next agent. It has no required skill dependencies and can be updated
independently of the architecture suite. Upstream also includes it in the
`mattpocock-skills` Claude Code plugin; its router and documentation recommend it
for moving between prototype, teaching, and planning sessions. See
[`SUBTREE.md`](SUBTREE.md#skillshandoff) for the dependency and packaging review.

### Opt-in skill packs

Specialized skills live outside the shared `skills` directory so they can be enabled
only for projects that need them.

| Skill | Codex invocation | Origin |
| --- | --- | --- |
| [`fiction-codex`](skill-packs/fiction/fiction-codex) | Implicit when the pack is enabled | Local |
| [`fiction-plain-draft`](skill-packs/fiction/fiction-plain-draft) | Implicit when the pack is enabled | Local |
| [`fiction-revision`](skill-packs/fiction/fiction-revision) | Implicit when the pack is enabled | Local |

Validate the inventory links, documented totals, and skill frontmatter with
`ruby scripts/check-skill-inventory.rb`.

When a project needs a complete pack, use a small linking script or package manager
to populate its real `.agents/skills` directory from both `skills/*` and the selected
pack. This creates an overlay of skill sources and avoids maintaining links by hand.

### Manual-only skills

Some skills should only run when explicitly requested, usually because they are workflow-specific and would be noisy if auto-selected. Support both agent conventions:

- Claude Code: add `disable-model-invocation: true` to `SKILL.md` frontmatter.
- Codex: add `policy.allow_implicit_invocation: false` to `agents/openai.yaml`.

Keep both settings together for shared skills so manual invocation works in both tools.

## Inspiration

Inspired by https://github.com/mitsuhiko/agent-stuff. I want to gather interesting skills, prompts, commands, etc.

- [web-browser skill](https://github.com/mitsuhiko/agent-stuff/blob/main/skills/web-browser/SKILL.md): Is apparently better than playwright MCP at browser interactions. Want to try it out. [permalink](https://github.com/mitsuhiko/agent-stuff/blob/063815263cb1031acfa73e12c86f01281dfac5e2/skills/web-browser/SKILL.md)
- [anthropics/skills/frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md): According to Theo from T3gg, he uses this with a prompt that asks for up to 5 unique designs when creating a new design. Something to try. [permalink](https://github.com/anthropics/skills/blob/a5bcdd7e58cdff48566bf876f0a72a2008dcefbc/skills/frontend-design/SKILL.md)
- [mattpocock's skills](https://github.com/mattpocock/skills/) Matt Pocock has a lot of pretty useful and insightful skills.
- [badlogic/pi-skills](https://github.com/badlogic/pi-skills) from the creator of Pi
