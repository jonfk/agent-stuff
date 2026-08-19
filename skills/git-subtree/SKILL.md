---
name: git-subtree
description: Use only when editing a SUBTREE.md file. A SUBTREE.md file manages documentation and metadata about vendored external code in a repo.
---

# Git Subtree Vendoring

1. Confirm the upstream URL, ref, optional upstream subdirectory, and local destination path. If anything important cannot be found, ask.
2. Check `git status --short` before changing files.
3. Vendor or update with `git subtree`, usually with `--squash`. If vendoring an upstream subdirectory, split that subdirectory first.
4. Document the subtree in `SUBTREE.md`.

Use `skills/git-subtree/SUBTREE.md` as the format reference. Include upstream URL, ref, last imported commit, mode, local path, and update command.

If a `SUBTREE.md` already exists, update the one closest to the vendored subtree. If none exists, create one at the repository root unless the user instructed otherwise.
