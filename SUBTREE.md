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

## Not Yet Documented As Subtrees

- `skills/grill-me`
- `skills/frontend-design`
- `skills/improve-codebase-architecture`
- `skills/grill-with-docs`
