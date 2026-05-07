# Pi Extension Subtrees

This directory vendors Pi extensions with `git subtree`. Each extension should live under `pi-extensions/<name>` and have an entry below that records its source repository, branch, imported commit, local prefix, and import date.

## Updating

To update an existing subtree, run:

```bash
git subtree pull --prefix=pi-extensions/<name> <source-url> <branch> --squash -m "chore: update <name> subtree"
```

After updating, edit this file with the new upstream commit and update date. You can verify the upstream commit with:

```bash
git ls-remote <source-url> <branch>
```

## Extensions

### pi-telegram

- Local path: `pi-extensions/pi-telegram`
- Source repository: https://github.com/llblab/pi-telegram
- Source branch: `main`
- Imported commit: `c1b253aeb05604e3adc70bf8642011fea1113c2c`
- Imported commit URL: https://github.com/llblab/pi-telegram/commit/c1b253aeb05604e3adc70bf8642011fea1113c2c
- Import date: 2026-05-07 09:04 America/Toronto
- Import method: squashed `git subtree add`
- Import command:

```bash
git subtree add --prefix=pi-extensions/pi-telegram https://github.com/llblab/pi-telegram main --squash -m "feat: add pi-telegram subtree"
```

Update command:

```bash
git subtree pull --prefix=pi-extensions/pi-telegram https://github.com/llblab/pi-telegram main --squash -m "chore: update pi-telegram subtree"
```
