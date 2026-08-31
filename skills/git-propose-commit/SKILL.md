---
name: git-propose-commit
description: Propose one or more git commit plans without creating commits. Use when the user asks for commit message suggestions, commit structure, or ways to split current changes.
---

# Propose Git Commits

Inspect the current changes and understand both their intent and implementation. Review several previous commits and use them as examples of the repository's conventions for scopes, wording, capitalization, and body style.

Use Conventional Commits for every proposed subject. Make the subject, body, and overall message length proportional to the importance and complexity of the change. A simple change may need only a subject. A significant or critical change should include a body that explains the intent and why the change matters, rather than merely repeating the diff.

## Consider commit structure

Decide whether the changes form one coherent commit or can be separated into independently meaningful, reviewable, and revertible commits. Keep supporting tests and documentation with the change they explain or verify.

When more than one commit structure is genuinely defensible, propose distinct options. Consider alternatives such as:

- one combined commit versus a sequence of focused commits
- different sensible boundaries for splitting the changes
- a different ordering when dependencies between commits allow it

For each option, provide the proposed commit subject and any body it needs. For a multi-commit option, show the commits in order, identify which changes belong in each, and briefly explain the trade-off of that structure. Do not manufacture alternatives that produce effectively the same history; if only one structure makes sense, propose only that one.

This skill is proposal-only. Do not stage changes or create commits.
