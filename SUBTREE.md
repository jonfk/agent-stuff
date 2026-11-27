# Vendored Code

## Update cohorts

### Matt Pocock architecture suite

The following skills form one cooperating architecture workflow and are vendored
directly from [`mattpocock/skills`](https://github.com/mattpocock/skills):

- `skills/improve-codebase-architecture`
- `skills/codebase-design`
- `skills/domain-modeling`
- `skills/grilling`

- Upstream: https://github.com/mattpocock/skills.git
- Ref: `main`
- Pinned upstream commit: `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`
- Update policy: **atomic**

Each member remains a separate subtree because it comes from a different upstream
subdirectory, but the four members are one update cohort. Fetch upstream once,
split every member from the same fetched commit, apply and review all four subtree
updates together, and commit them as one change. Refresh the pinned commit above
and every member's subtree metadata in this file and `README.md`.

Do not advance one member independently. Narrow, documented packaging overlays
such as invocation policy may remain in the cohort and must be preserved after
updates. If a member needs behavioral changes or a different upstream pin,
document it as a local fork and remove it from this cohort first.

### Matt Pocock retro pair

`retro` loads `writing-for-agents` on every run, so the two skills are vendored
together from [`mattpocock/skills`](https://github.com/mattpocock/skills):

- `skills/retro`
- `skills/writing-for-agents`

- Upstream: https://github.com/mattpocock/skills.git
- Ref: `main`
- Pinned upstream commit: `59db609eb1e18aaf59b63284d0e52255aff0c63c`
- Update policy: **atomic**

`retro`'s first step invokes the `writing-for-agents` skill, and it uses that
skill's definitions to judge no-op instructions and skills before it writes
anything. Upstream declines to make that load lazy (see
[`.out-of-scope/lazy-load-writing-for-agents.md`](https://github.com/mattpocock/skills/blob/59db609eb1e18aaf59b63284d0e52255aff0c63c/.out-of-scope/lazy-load-writing-for-agents.md)).
Split both members from the same fetched commit, review both subtree updates
together, and commit them as one change. Refresh the pinned commit above and
both members' subtree metadata in this file and `README.md`.

Do not advance one member independently, and do not remove `writing-for-agents`
while `retro` remains vendored. This pair is independent of the architecture
suite and may use a different upstream pin.

To update the pair:

```bash
git fetch https://github.com/mattpocock/skills.git main
git worktree add --detach /private/tmp/mattpocock-skills-retro FETCH_HEAD
git -C /private/tmp/mattpocock-skills-retro subtree split -P skills/engineering/retro HEAD -b tmp-mattpocock-retro-split
git -C /private/tmp/mattpocock-skills-retro subtree split -P skills/productivity/writing-for-agents HEAD -b tmp-mattpocock-writing-for-agents-split
git subtree pull --prefix=skills/retro /private/tmp/mattpocock-skills-retro tmp-mattpocock-retro-split --squash
git subtree pull --prefix=skills/writing-for-agents /private/tmp/mattpocock-skills-retro tmp-mattpocock-writing-for-agents-split --squash
git worktree remove /private/tmp/mattpocock-skills-retro
git branch -D tmp-mattpocock-retro-split tmp-mattpocock-writing-for-agents-split
```

## `skills/anthropic-frontend-design`

- Source: https://github.com/anthropics/skills/tree/main/skills/frontend-design
- Imported from: `33375500bcea98d610eb30ce10ac4e59b89c390d`
- Permalink: https://github.com/anthropics/skills/tree/33375500bcea98d610eb30ce10ac4e59b89c390d/skills/frontend-design
- Ref: `main`
- Upstream subdirectory: `skills/frontend-design`
- Split commit: `2aa4de6b0460a55797f4ad07c26ecff6c0a54996`
- Mode: `--squash`
- Local path: `skills/anthropic-frontend-design`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/anthropics/skills.git main
git switch -c tmp-anthropics-skills-frontend-design FETCH_HEAD
git subtree split -P skills/frontend-design -b tmp-anthropics-frontend-design-split
git switch -
git subtree pull --prefix=skills/anthropic-frontend-design . tmp-anthropics-frontend-design-split --squash
git branch -D tmp-anthropics-skills-frontend-design tmp-anthropics-frontend-design-split
```

Local overlay: the local skill and directory are renamed to
`anthropic-frontend-design`. After updates, preserve the `name` field in
`SKILL.md`. The skill keeps upstream's default invocation, so models can invoke
it implicitly in both Claude Code and Codex.

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

## `skills/grilling`

- Source: https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling
- Imported from: `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`
- Permalink: https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/grilling
- Ref: `main`
- Upstream subdirectory: `skills/productivity/grilling`
- Split commit: `69b3e82ccfbf85f552b80ef665989efdee27c31a`
- Mode: `--squash`
- Local path: `skills/grilling`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-grilling FETCH_HEAD
git subtree split -P skills/productivity/grilling -b tmp-mattpocock-grilling-split
git switch -
git subtree pull --prefix=skills/grilling . tmp-mattpocock-grilling-split --squash
git branch -D tmp-mattpocock-skills-grilling tmp-mattpocock-grilling-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

The skill keeps upstream's default invocation, so models can invoke it
implicitly in both Claude Code and Codex. All files are imported unchanged.

## `skills/handoff`

- Source: https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff
- Upstream: https://github.com/mattpocock/skills.git
- Imported from: `d81f3a183412e71a5b1e84ca21bc1a35eea03a60`
- Permalink: https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/productivity/handoff
- Ref: `main`
- Upstream subdirectory: `skills/productivity/handoff`
- Split commit: `dec8c574ac946399627b339e951b4ace00ba1648`
- Mode: `--squash`
- Local path: `skills/handoff`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git worktree add --detach /private/tmp/mattpocock-skills-handoff FETCH_HEAD
git -C /private/tmp/mattpocock-skills-handoff subtree split -P skills/productivity/handoff HEAD -b tmp-mattpocock-handoff-split
git subtree pull --prefix=skills/handoff /private/tmp/mattpocock-skills-handoff tmp-mattpocock-handoff-split --squash
git worktree remove /private/tmp/mattpocock-skills-handoff
git branch -D tmp-mattpocock-handoff-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

### Dependencies and packaging

Reviewed at the imported upstream commit:

- The subtree contains only `SKILL.md` and `agents/openai.yaml`. It has no
  scripts, external assets, setup requirements, or required named skill
  dependencies. Its suggested-skills section is chosen for the next task.
- It is manual-only upstream in both Claude Code and Codex through
  `disable-model-invocation: true` and
  `policy.allow_implicit_invocation: false`. Both files are imported unchanged.
- None of the existing local skills references `handoff`. It does not require
  updating those skills or joining the Matt Pocock architecture update cohort.
- Upstream's
  [`ask-matt`](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/engineering/ask-matt/SKILL.md)
  router recommends handoffs into and out of prototype sessions. Upstream docs
  also describe optional composition with
  [`teach`](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/docs/productivity/teach.md)
  and
  [`wayfinder`](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/docs/engineering/wayfinder.md).
  These are workflow recommendations, not shared-version constraints.
- The upstream
  [`mattpocock-skills` Claude Code plugin](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/.claude-plugin/plugin.json)
  bundles `handoff` with the engineering and productivity skills. This subtree
  imports just the standalone skill, without the plugin or companion skills.
- Upstream also has a separate in-progress
  [`claude-handoff`](https://github.com/mattpocock/skills/blob/d81f3a183412e71a5b1e84ca21bc1a35eea03a60/skills/in-progress/claude-handoff/SKILL.md)
  that launches a background Claude agent. It is neither a dependency of
  `handoff` nor included in this import.

## `skills/retro`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/retro
- Upstream: https://github.com/mattpocock/skills.git
- Imported from: `59db609eb1e18aaf59b63284d0e52255aff0c63c`
- Permalink: https://github.com/mattpocock/skills/tree/59db609eb1e18aaf59b63284d0e52255aff0c63c/skills/engineering/retro
- Ref: `main`
- Upstream subdirectory: `skills/engineering/retro`
- Split commit: `796ead9f6f368553789d220f10de54b6428d5e95`
- Mode: `--squash`
- Local path: `skills/retro`

This is a subtree of an upstream subdirectory and a member of the
[Matt Pocock retro pair](#matt-pocock-retro-pair). Update it only with that
cohort's procedure, together with `skills/writing-for-agents`.

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

### Dependencies and packaging

Reviewed at the imported upstream commit:

- The subtree contains only `SKILL.md` and `agents/openai.yaml`. It has no
  scripts, external assets, or setup requirements. Both files are imported
  unchanged.
- It is manual-only upstream in both Claude Code and Codex through
  `disable-model-invocation: true` and
  `policy.allow_implicit_invocation: false`.
- It requires `writing-for-agents`, which is vendored alongside it as
  `skills/writing-for-agents`.
- It assumes a review stage that reads a `CODING_STANDARDS.md`. No skill ships
  that file; `retro` proposes creating it the first time it finds a
  judgement-call rule. Upstream's
  [`code-review`](https://github.com/mattpocock/skills/tree/59db609eb1e18aaf59b63284d0e52255aff0c63c/skills/engineering/code-review)
  skill is the reviewer it most often tunes. That skill is not vendored here
  and differs from Claude Code's built-in `/code-review`. This is a workflow
  recommendation, not a shared-version constraint.
- The upstream
  [`mattpocock-skills` Claude Code plugin](https://github.com/mattpocock/skills/blob/59db609eb1e18aaf59b63284d0e52255aff0c63c/.claude-plugin/plugin.json)
  bundles `retro` with the engineering and productivity skills. This subtree
  imports just the standalone skill.

## `skills/writing-for-agents`

- Source: https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents
- Upstream: https://github.com/mattpocock/skills.git
- Imported from: `59db609eb1e18aaf59b63284d0e52255aff0c63c`
- Permalink: https://github.com/mattpocock/skills/tree/59db609eb1e18aaf59b63284d0e52255aff0c63c/skills/productivity/writing-for-agents
- Ref: `main`
- Upstream subdirectory: `skills/productivity/writing-for-agents`
- Split commit: `3bbd7f45e1f82a3846162d7c9134f00a55bc799f`
- Mode: `--squash`
- Local path: `skills/writing-for-agents`

This is a subtree of an upstream subdirectory and a member of the
[Matt Pocock retro pair](#matt-pocock-retro-pair). Update it only with that
cohort's procedure, together with `skills/retro`.

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

### Dependencies and packaging

Reviewed at the imported upstream commit:

- The subtree contains `SKILL.md`, `SKILL-MECHANICS.md`, and
  `agents/openai.yaml`. It has no scripts, external assets, setup
  requirements, or named skill dependencies. All files are imported unchanged.
- It keeps upstream's default invocation, so models can invoke it implicitly
  in both Claude Code and Codex when creating or editing skills, `AGENTS.md`,
  or `CLAUDE.md`.

## `skills/domain-modeling`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling
- Imported from: `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`
- Permalink: https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/domain-modeling
- Ref: `main`
- Upstream subdirectory: `skills/engineering/domain-modeling`
- Split commit: `e7bce7aa4058f69dd903202390764117d6f343c7`
- Mode: `--squash`
- Local path: `skills/domain-modeling`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-domain-modeling FETCH_HEAD
git subtree split -P skills/engineering/domain-modeling -b tmp-mattpocock-domain-modeling-split
git switch -
git subtree pull --prefix=skills/domain-modeling . tmp-mattpocock-domain-modeling-split --squash
git branch -D tmp-mattpocock-skills-domain-modeling tmp-mattpocock-domain-modeling-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

## `skills/codebase-design`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design
- Imported from: `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`
- Permalink: https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/codebase-design
- Ref: `main`
- Upstream subdirectory: `skills/engineering/codebase-design`
- Split commit: `afd7936f40d5b9f7667ebe6f38e85fbc8bc41d6e`
- Mode: `--squash`
- Local path: `skills/codebase-design`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-codebase-design FETCH_HEAD
git subtree split -P skills/engineering/codebase-design -b tmp-mattpocock-codebase-design-split
git switch -
git subtree pull --prefix=skills/codebase-design . tmp-mattpocock-codebase-design-split --squash
git branch -D tmp-mattpocock-skills-codebase-design tmp-mattpocock-codebase-design-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

## `skills/grill-with-docs`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs
- Imported from: `885e2ca4d842d139e9aef4e48d366c63cb1b8013`
- Permalink: https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/grill-with-docs
- Ref: `main`
- Upstream subdirectory: `skills/engineering/grill-with-docs`
- Split commit: `70b6090e254b07cf376a40033d44bcf6cff9fff4`
- Mode: `--squash`
- Local path: `skills/grill-with-docs`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-grill-with-docs FETCH_HEAD
git subtree split -P skills/engineering/grill-with-docs -b tmp-mattpocock-grill-with-docs-split
git switch -
git subtree pull --prefix=skills/grill-with-docs . tmp-mattpocock-grill-with-docs-split --squash
git branch -D tmp-mattpocock-skills-grill-with-docs tmp-mattpocock-grill-with-docs-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

## `skills/improve-codebase-architecture`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture
- Imported from: `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`
- Permalink: https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/improve-codebase-architecture
- Ref: `main`
- Upstream subdirectory: `skills/engineering/improve-codebase-architecture`
- Split commit: `2d8ac8c6a475d0ff81895743dc102b9a531464e5`
- Mode: `--squash`
- Local path: `skills/improve-codebase-architecture`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-improve-codebase-architecture FETCH_HEAD
git subtree split -P skills/engineering/improve-codebase-architecture -b tmp-mattpocock-improve-codebase-architecture-split
git switch -
git subtree pull --prefix=skills/improve-codebase-architecture . tmp-mattpocock-improve-codebase-architecture-split --squash
git branch -D tmp-mattpocock-skills-improve-codebase-architecture tmp-mattpocock-improve-codebase-architecture-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

## `skills/tdd`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd
- Imported from: `885e2ca4d842d139e9aef4e48d366c63cb1b8013`
- Permalink: https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/tdd
- Ref: `main`
- Upstream subdirectory: `skills/engineering/tdd`
- Split commit: `54cfb36c807d6ce276a5675c3b31dc9cfcf196b8`
- Mode: `--squash`
- Local path: `skills/tdd`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-tdd FETCH_HEAD
git subtree split -P skills/engineering/tdd -b tmp-mattpocock-tdd-split
git switch -
git subtree pull --prefix=skills/tdd . tmp-mattpocock-tdd-split --squash
git branch -D tmp-mattpocock-skills-tdd tmp-mattpocock-tdd-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

## `skills/prototype`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype
- Imported from: `885e2ca4d842d139e9aef4e48d366c63cb1b8013`
- Permalink: https://github.com/mattpocock/skills/tree/885e2ca4d842d139e9aef4e48d366c63cb1b8013/skills/engineering/prototype
- Ref: `main`
- Upstream subdirectory: `skills/engineering/prototype`
- Split commit: `56dafec78765f00989c6075dc5393e9a49a4ae68`
- Mode: `--squash`
- Local path: `skills/prototype`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-prototype FETCH_HEAD
git subtree split -P skills/engineering/prototype -b tmp-mattpocock-prototype-split
git switch -
git subtree pull --prefix=skills/prototype . tmp-mattpocock-prototype-split --squash
git branch -D tmp-mattpocock-skills-prototype tmp-mattpocock-prototype-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

## `skills/pr`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/pr
- Upstream: https://github.com/mattpocock/skills.git
- Imported from: `5863806dd4e15c63174bee4e7515a4256792ecfa`
- Permalink: https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/pr
- Ref: `main`
- Upstream subdirectory: `skills/engineering/pr`
- Split commit: `f938d8e24360d25a1f21a27f138865c441a11688`
- Mode: `--squash`
- Local path: `skills/pr`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git worktree add --detach /private/tmp/mattpocock-skills-pr FETCH_HEAD
git -C /private/tmp/mattpocock-skills-pr subtree split -P skills/engineering/pr HEAD -b tmp-mattpocock-pr-split
git subtree pull --prefix=skills/pr /private/tmp/mattpocock-skills-pr tmp-mattpocock-pr-split --squash
git worktree remove /private/tmp/mattpocock-skills-pr
git branch -D tmp-mattpocock-pr-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

### Dependencies and packaging

Reviewed at the imported upstream commit:

- The subtree contains `SKILL.md`, `CREDITS.md`, and `agents/openai.yaml`. It
  has no scripts, external assets, setup requirements, or required named skill
  dependencies.
- It keeps upstream's default invocation, so models can invoke it implicitly
  in both Claude Code and Codex when writing a PR body.

Local overlay: the Evidence section's screenshot line in `SKILL.md` asks for
screenshots of visual changes whenever tools allow, and to tell the user when
no screenshot tool is available. Preserve that line after updates. All other
files are imported unchanged.
- Its Summary guidance is copied from humanlayer's `show-me` (see
  `CREDITS.md`), which is also vendored here as `skills/show-me`. The content
  is duplicated, not referenced, so the two can be updated independently.
- It asks for domain language from `GLOSSARY.md`. Upstream renamed its
  `CONTEXT.md` convention to `GLOSSARY.md`, but the architecture suite here is
  pinned before that rename and still writes `CONTEXT.md`. This is a naming
  mismatch, not a shared-version constraint.

## `skills/show-me`

- Source: https://github.com/humanlayer/skills/tree/main/plugins/show-me/skills/show-me
- Imported from: `ca7c8088db69e315a8b2deea43820270457f8f3c`
- Permalink: https://github.com/humanlayer/skills/tree/ca7c8088db69e315a8b2deea43820270457f8f3c/plugins/show-me/skills/show-me
- Ref: `main`
- Upstream subdirectory: `plugins/show-me/skills/show-me`
- Split commit: `e6bc3106e4b3fd98c352bae5537b638e814fa9bf`
- Mode: `--squash`
- Local path: `skills/show-me`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/humanlayer/skills.git main
git worktree add /private/tmp/humanlayer-skills-show-me FETCH_HEAD
git -C /private/tmp/humanlayer-skills-show-me subtree split -P plugins/show-me/skills/show-me HEAD -b tmp-humanlayer-show-me-split
git subtree pull --prefix=skills/show-me /private/tmp/humanlayer-skills-show-me tmp-humanlayer-show-me-split --squash
git worktree remove /private/tmp/humanlayer-skills-show-me
git branch -D tmp-humanlayer-show-me-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

Local overlay: this skill is manual-only in both Claude Code and Codex. Preserve
`disable-model-invocation: true` in `SKILL.md` and
`policy.allow_implicit_invocation: false` in `agents/openai.yaml` after updates.
