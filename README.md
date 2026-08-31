
## Skills

The repository contains 20 tracked skills: 17 broadly useful skills under `skills/`
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
| [`anthropic-frontend-design`](skills/anthropic-frontend-design) | **Manual-only** | [anthropics/skills @ `0a64e39`](https://github.com/anthropics/skills/tree/0a64e398ec6bb34a494f0c347e8ccae53a862f8e/skills/frontend-design); split `8279059`; locally renamed |
| [`codebase-design`](skills/codebase-design) | Implicit | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/codebase-design); split `afd7936` |
| [`create-design-doc`](skills/create-design-doc) | **Manual-only** | Local |
| [`domain-modeling`](skills/domain-modeling) | Implicit | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/domain-modeling); split `e7bce7a` |
| [`fix-with-subagents`](skills/fix-with-subagents) | **Manual-only** | Local |
| [`frontend-design-mitsuhiko`](skills/frontend-design-mitsuhiko) | **Manual-only** | [mitsuhiko/agent-stuff @ `b861028`](https://github.com/mitsuhiko/agent-stuff/tree/b861028c706edf3e3f983cde09dd8cc8549ec948/skills/frontend-design), locally renamed |
| [`git-create-commit`](skills/git-create-commit) | Implicit | Local |
| [`git-propose-commit`](skills/git-propose-commit) | Implicit | Local |
| [`git-subtree`](skills/git-subtree) | Implicit | Local |
| [`grill-me`](skills/grill-me) | **Manual-only** | Maintained local fork of [mattpocock/skills @ `60aa99c`](https://github.com/mattpocock/skills/blob/60aa99c0230fbac087514ba5fca2ae6e519965fe/grill-me/SKILL.md); diverged locally at `fb2dd08` and must not be updated from upstream |
| [`grill-with-docs`](skills/grill-with-docs) | **Manual-only** | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/grill-with-docs); split `70b6090` |
| [`grilling`](skills/grilling) | **Manual-only** | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/productivity/grilling); split `132f55a`; local manual-only policy |
| [`improve-codebase-architecture`](skills/improve-codebase-architecture) | **Manual-only** | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/improve-codebase-architecture); split `2d8ac8c` |
| [`prototype`](skills/prototype) | Implicit | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/prototype); split `56dafec` |
| [`tdd`](skills/tdd) | Implicit | [mattpocock/skills @ `885e2ca`](https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/tdd); split `54cfb36` |
| [`thermo-nuclear-code-quality-review`](skills/thermo-nuclear-code-quality-review) | **Manual-only** | [cursor/plugins @ `3347cba`](https://github.com/cursor/plugins/tree/3347cbab5b54136f6fba0994c3a01a56f7fb7fca/cursor-team-kit/skills/thermo-nuclear-code-quality-review), substantially rewritten locally |
| [`yt-transcribe`](skills/yt-transcribe) | Implicit | Local |

The `skills` directory contains broadly useful skills and is suitable for linking as
`.agents/skills` so every agent can discover it.

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

## Pi Extensions

This repository contains independently installable Pi extensions.

From the repository root, install the extensions locally:

```bash
pi install ./pi-extensions/pi-telegram
pi install ./pi-extensions/pi-inline-skills
pi install ./pi-extensions/preset
```

Vendored code subtree metadata and update notes live in [`SUBTREE.md`](SUBTREE.md).

- [`pi-telegram`](pi-extensions/pi-telegram) - Telegram bridge for Pi, from [llblab/pi-telegram](https://github.com/llblab/pi-telegram) at [`c1b253a`](https://github.com/llblab/pi-telegram/commit/c1b253aeb05604e3adc70bf8642011fea1113c2c)
- [`preset`](pi-extensions/preset) - Preset extension for Pi, vendored from [richardgill/pi-extensions/extensions/preset](https://github.com/richardgill/pi-extensions/tree/7e09e5371d8a7fa8d90adc91273503b68bcf6c61/extensions/preset) at [`7e09e53`](https://github.com/richardgill/pi-extensions/commit/7e09e5371d8a7fa8d90adc91273503b68bcf6c61)
- [`pi-inline-skills`](pi-extensions/pi-inline-skills) - Inline `$skill` autocomplete for Pi, vendored from [tifandotme/pi-extensions/packages/pi-inline-skills](https://github.com/tifandotme/pi-extensions/tree/b58f061992941a10b7f4a731915b512401b422bf/packages/pi-inline-skills) at [`b58f061`](https://github.com/tifandotme/pi-extensions/commit/b58f061992941a10b7f4a731915b512401b422bf)


## Inspiration

Inspired by https://github.com/mitsuhiko/agent-stuff. I want to gather interesting skills, prompts, commands, etc.

- [web-browser skill](https://github.com/mitsuhiko/agent-stuff/blob/main/skills/web-browser/SKILL.md): Is apparently better than playwright MCP at browser interactions. Want to try it out. [permalink](https://github.com/mitsuhiko/agent-stuff/blob/063815263cb1031acfa73e12c86f01281dfac5e2/skills/web-browser/SKILL.md)
- [anthropics/skills/frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md): According to Theo from T3gg, he uses this with a prompt that asks for up to 5 unique designs when creating a new design. Something to try. [permalink](https://github.com/anthropics/skills/blob/a5bcdd7e58cdff48566bf876f0a72a2008dcefbc/skills/frontend-design/SKILL.md)
- [mattpocock's skills](https://github.com/mattpocock/skills/) Matt Pocock has a lot of pretty useful and insightful skills.
- [badlogic/pi-skills](https://github.com/badlogic/pi-skills) from the creator of Pi
