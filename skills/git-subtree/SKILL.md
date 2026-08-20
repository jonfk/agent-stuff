---
name: git-subtree
description: Create or maintain SUBTREE.md metadata for code managed with git subtree. Use only when a SUBTREE.md file is encountered, needs editing, or needs to be created, or when explicitly invoked.
---

# Git Subtree Vendoring

Use `git subtree` to vendor external code into a repository and record the vendoring metadata in `SUBTREE.md`.

Use [SUBTREE.md](SUBTREE.md) as the format reference. Include the upstream URL, permalink, ref, last imported commit, mode, local path, and update command.

1. Confirm the upstream URL, ref, optional upstream subdirectory, and local destination path. If anything important cannot be found, ask.
2. Check `git status --short` before changing files.
3. Vendor or update with `git subtree`. Use `--squash` by default. If vendoring an upstream subdirectory, split that subdirectory first.
4. Create or update the subtree's record in `SUBTREE.md`.

If a `SUBTREE.md` already exists, update the one closest to the vendored subtree. If none exists, create one at the repository root unless the user instructed otherwise.

## Maintenance Groups

Some subtrees are interdependent and must target the same upstream ref or commit. Treat them as a maintenance group and update every member together.

Record each group once in the `Maintenance groups` section of `SUBTREE.md`; do not duplicate the group on individual subtree records. Include the reason for the grouping, every member's local path, and the shared-target constraint.
