# Vendored Code

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
- `skills/improve-codebase-architecture`
- `skills/grill-with-docs`
