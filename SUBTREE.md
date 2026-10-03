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

Local overlays: the local skill and directory are renamed to
`anthropic-frontend-design`, and the skill is manual-only in both Claude Code
and Codex. After updates, preserve the `name` and
`disable-model-invocation: true` fields in `SKILL.md` and
`policy.allow_implicit_invocation: false` in `agents/openai.yaml`.

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

Local overlay: this skill is manual-only in both Claude Code and Codex. Preserve
`disable-model-invocation: true` in `SKILL.md` and
`policy.allow_implicit_invocation: false` in `agents/openai.yaml` after updates.

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

## `skills/thermo-nuclear-code-quality-review`

- Source: https://github.com/cursor/plugins/tree/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review
- Imported from: `3347cbab5b54136f6fba0994c3a01a56f7fb7fca`
- Permalink: https://github.com/cursor/plugins/tree/3347cbab5b54136f6fba0994c3a01a56f7fb7fca/cursor-team-kit/skills/thermo-nuclear-code-quality-review
- Ref: `3347cbab5b54136f6fba0994c3a01a56f7fb7fca`
- Upstream subdirectory: `cursor-team-kit/skills/thermo-nuclear-code-quality-review`
- Split commit: `8bcb307f4e7a7b7e9cf51996e1fcc236df0f36bc`
- Mode: `--squash`
- Local path: `skills/thermo-nuclear-code-quality-review`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/cursor/plugins.git <ref>
git worktree add /private/tmp/cursor-plugins-thermo FETCH_HEAD
git -C /private/tmp/cursor-plugins-thermo subtree split -P cursor-team-kit/skills/thermo-nuclear-code-quality-review HEAD -b tmp-cursor-thermo-nuclear-code-quality-review-split
git subtree pull --prefix=skills/thermo-nuclear-code-quality-review /private/tmp/cursor-plugins-thermo tmp-cursor-thermo-nuclear-code-quality-review-split --squash
git worktree remove /private/tmp/cursor-plugins-thermo
git branch -D tmp-cursor-thermo-nuclear-code-quality-review-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

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

## Locally maintained copies

### `skills/grill-me`

- Source: https://github.com/mattpocock/skills/blob/60aa99c0230fbac087514ba5fca2ae6e519965fe/grill-me/SKILL.md
- Source snapshot: `60aa99c0230fbac087514ba5fca2ae6e519965fe`
- Initially copied in local commit: `cb7c6587bb664e14da85c4b9ed3bce1a71431619`
- Local divergence began in commit: `fb2dd08dd86f53e9af41a1b96456a5940d2c641a`
- Local path: `skills/grill-me`
- Update policy: **do not update from upstream**

This is a maintained local fork, not a subtree. Upstream later moved `grill-me`
and changed it into a manual-only wrapper around `grilling`; this fork retains
its distinct interview behavior. It is manual-only in both Claude Code and
Codex through `disable-model-invocation: true` in `SKILL.md` and
`policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
