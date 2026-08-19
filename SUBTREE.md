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
- Pinned upstream commit: `84fdeffd12f2ee307994d1eb6feb48173b6e0502`
- Update policy: **atomic**

Each member remains a separate subtree because it comes from a different upstream
subdirectory, but the four members are one update cohort. Fetch upstream once,
split every member from the same fetched commit, apply and review all four subtree
updates together, and commit them as one change. Refresh the pinned commit above
and every member's subtree metadata in this file and `README.md`.

Do not advance one member independently. If a member needs to remain pinned or
receive local changes, explicitly document it as a local fork and remove it from
this cohort first.

## `skills/grilling`

- Source: https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling
- Imported from: `84fdeffd12f2ee307994d1eb6feb48173b6e0502`
- Permalink: https://github.com/mattpocock/skills/tree/84fdeffd12f2ee307994d1eb6feb48173b6e0502/skills/productivity/grilling
- Ref: `main`
- Upstream subdirectory: `skills/productivity/grilling`
- Split commit: `30a6da0b967a0ea92f6df3d6a15a2001f1437355`
- Mode: `--squash`
- Local path: `skills/grilling`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-grilling FETCH_HEAD
git subtree split -P skills/productivity/grilling -b tmp-mattpocock-grilling-split
git switch main
git subtree pull --prefix=skills/grilling tmp-mattpocock-grilling-split --squash
git branch -D tmp-mattpocock-skills-grilling tmp-mattpocock-grilling-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

## `skills/domain-modeling`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling
- Imported from: `84fdeffd12f2ee307994d1eb6feb48173b6e0502`
- Permalink: https://github.com/mattpocock/skills/tree/84fdeffd12f2ee307994d1eb6feb48173b6e0502/skills/engineering/domain-modeling
- Ref: `main`
- Upstream subdirectory: `skills/engineering/domain-modeling`
- Split commit: `71e05dbeb1334d8bd1ab8fe15ab9203ab2409596`
- Mode: `--squash`
- Local path: `skills/domain-modeling`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-domain-modeling FETCH_HEAD
git subtree split -P skills/engineering/domain-modeling -b tmp-mattpocock-domain-modeling-split
git switch main
git subtree pull --prefix=skills/domain-modeling tmp-mattpocock-domain-modeling-split --squash
git branch -D tmp-mattpocock-skills-domain-modeling tmp-mattpocock-domain-modeling-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

## `skills/codebase-design`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design
- Imported from: `84fdeffd12f2ee307994d1eb6feb48173b6e0502`
- Permalink: https://github.com/mattpocock/skills/tree/84fdeffd12f2ee307994d1eb6feb48173b6e0502/skills/engineering/codebase-design
- Ref: `main`
- Upstream subdirectory: `skills/engineering/codebase-design`
- Split commit: `1cc8b7c4e89c3fc70506b717ee4d07acabbc21ad`
- Mode: `--squash`
- Local path: `skills/codebase-design`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-codebase-design FETCH_HEAD
git subtree split -P skills/engineering/codebase-design -b tmp-mattpocock-codebase-design-split
git switch main
git subtree pull --prefix=skills/codebase-design tmp-mattpocock-codebase-design-split --squash
git branch -D tmp-mattpocock-skills-codebase-design tmp-mattpocock-codebase-design-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

## `skills/grill-with-docs`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs
- Imported from: `84fdeffd12f2ee307994d1eb6feb48173b6e0502`
- Permalink: https://github.com/mattpocock/skills/tree/84fdeffd12f2ee307994d1eb6feb48173b6e0502/skills/engineering/grill-with-docs
- Ref: `main`
- Upstream subdirectory: `skills/engineering/grill-with-docs`
- Split commit: `0e806c0ad9c983e9434868788e33d55ac4476dc6`
- Mode: `--squash`
- Local path: `skills/grill-with-docs`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-grill-with-docs FETCH_HEAD
git subtree split -P skills/engineering/grill-with-docs -b tmp-mattpocock-grill-with-docs-split
git switch main
git subtree pull --prefix=skills/grill-with-docs tmp-mattpocock-grill-with-docs-split --squash
git branch -D tmp-mattpocock-skills-grill-with-docs tmp-mattpocock-grill-with-docs-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

## `skills/improve-codebase-architecture`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture
- Imported from: `84fdeffd12f2ee307994d1eb6feb48173b6e0502`
- Permalink: https://github.com/mattpocock/skills/tree/84fdeffd12f2ee307994d1eb6feb48173b6e0502/skills/engineering/improve-codebase-architecture
- Ref: `main`
- Upstream subdirectory: `skills/engineering/improve-codebase-architecture`
- Split commit: `07dbb0d3c1388b5dc07f4b19254ecc9856cc0f55`
- Mode: `--squash`
- Local path: `skills/improve-codebase-architecture`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-improve-codebase-architecture FETCH_HEAD
git subtree split -P skills/engineering/improve-codebase-architecture -b tmp-mattpocock-improve-codebase-architecture-split
git switch main
git subtree pull --prefix=skills/improve-codebase-architecture tmp-mattpocock-improve-codebase-architecture-split --squash
git branch -D tmp-mattpocock-skills-improve-codebase-architecture tmp-mattpocock-improve-codebase-architecture-split
```

After updating vendored code, refresh the commit, split commit, and permalink here and in `README.md`.

## `skills/tdd`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd
- Imported from: `733d312884b3878a9a9cff693c5886943753a741`
- Permalink: https://github.com/mattpocock/skills/tree/733d312884b3878a9a9cff693c5886943753a741/skills/engineering/tdd

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills FETCH_HEAD
git subtree split -P skills/engineering/tdd -b tmp-mattpocock-tdd-split
git switch main
git subtree pull --prefix=skills/tdd tmp-mattpocock-tdd-split --squash
git branch -D tmp-mattpocock-skills tmp-mattpocock-tdd-split
```

## `skills/prototype`

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype
- Imported from: `aaf2453fbdfe7a15c07f11d861224f34ab4b53cb`
- Permalink: https://github.com/mattpocock/skills/tree/aaf2453fbdfe7a15c07f11d861224f34ab4b53cb/skills/engineering/prototype
- Ref: `main`
- Mode: `--squash`
- Local path: `skills/prototype`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills FETCH_HEAD
git subtree split -P skills/engineering/prototype -b tmp-mattpocock-prototype-split
git switch main
git subtree pull --prefix=skills/prototype tmp-mattpocock-prototype-split --squash
git branch -D tmp-mattpocock-skills tmp-mattpocock-prototype-split
```

## `skills/teach`

- Source: https://github.com/mattpocock/skills/tree/main/skills/productivity/teach
- Imported from: `694fa30311e02c2639942308513555e61ee84a6f`
- Permalink: https://github.com/mattpocock/skills/tree/694fa30311e02c2639942308513555e61ee84a6f/skills/productivity/teach
- Ref: `main`
- Upstream subdirectory: `skills/productivity/teach`
- Split commit: `9e5df69a8fde2b866a28e61dbc8782e780e0a131`
- Mode: `--squash`
- Local path: `skills/teach`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/mattpocock/skills.git main
git switch -c tmp-mattpocock-skills-teach FETCH_HEAD
git subtree split -P skills/productivity/teach -b tmp-mattpocock-teach-split
git switch main
git subtree pull --prefix=skills/teach tmp-mattpocock-teach-split --squash
git branch -D tmp-mattpocock-skills-teach tmp-mattpocock-teach-split
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

## `pi-extensions/pi-telegram`

- Source: https://github.com/llblab/pi-telegram
- Imported from: `c1b253aeb05604e3adc70bf8642011fea1113c2c`
- Permalink: https://github.com/llblab/pi-telegram/tree/c1b253aeb05604e3adc70bf8642011fea1113c2c

Update with a normal subtree pull:

```bash
git subtree pull --prefix=pi-extensions/pi-telegram https://github.com/llblab/pi-telegram main --squash
```

After updating vendored code, refresh the commit and permalink here and in `README.md`.

## `pi-extensions/preset`

- Source: https://github.com/richardgill/pi-extensions/tree/main/extensions/preset
- Imported from: `7e09e5371d8a7fa8d90adc91273503b68bcf6c61`
- Permalink: https://github.com/richardgill/pi-extensions/tree/7e09e5371d8a7fa8d90adc91273503b68bcf6c61/extensions/preset
- Ref: `main`
- Mode: `--squash`
- Local path: `pi-extensions/preset`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/richardgill/pi-extensions.git main
git switch -c tmp-richardgill-pi-extensions FETCH_HEAD
git subtree split -P extensions/preset -b tmp-richardgill-preset-split
git switch main
git subtree pull --prefix=pi-extensions/preset tmp-richardgill-preset-split --squash
git branch -D tmp-richardgill-pi-extensions tmp-richardgill-preset-split
```

After updating vendored code, refresh the commit and permalink here and in `README.md`.

## `pi-extensions/pi-inline-skills`

- Source: https://github.com/tifandotme/pi-extensions/tree/master/packages/pi-inline-skills
- Imported from: `b58f061992941a10b7f4a731915b512401b422bf`
- Permalink: https://github.com/tifandotme/pi-extensions/tree/b58f061992941a10b7f4a731915b512401b422bf/packages/pi-inline-skills
- Ref: `master`
- Mode: `--squash`
- Local path: `pi-extensions/pi-inline-skills`

This is a subtree of an upstream subdirectory, not the upstream repo root. To update it, split the upstream subdirectory first:

```bash
git fetch https://github.com/tifandotme/pi-extensions.git master
git switch -c tmp-tifandotme-pi-extensions FETCH_HEAD
git subtree split -P packages/pi-inline-skills -b tmp-tifandotme-pi-inline-skills-split
git switch main
git subtree pull --prefix=pi-extensions/pi-inline-skills tmp-tifandotme-pi-inline-skills-split --squash
git branch -D tmp-tifandotme-pi-extensions tmp-tifandotme-pi-inline-skills-split
```

After updating vendored code, refresh the commit and permalink here and in `README.md`.

## Not Yet Documented As Subtrees

- `skills/grill-me`
- `skills/frontend-design`
