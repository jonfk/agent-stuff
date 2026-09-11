---
name: git-reshape-history
description: Rewrite a branch's commit history into a clear, reviewable sequence of well-designed commits while preserving the final result.
disable-model-invocation: true
---

# Rearrange Git History

Reconstruct the branch as the history a careful implementer would ideally have produced.

The goal is not to preserve the chronology of development. Optimize the commit sequence primarily for **reviewability**: each commit should make a coherent point, be understandable in context, and contribute naturally to the story of the overall change.

## Principles

- **Reconstruct intent, not chronology.** Fold bug fixes, follow-up edits, abandoned approaches, and implementation detours into the commits where the correct changes logically belong.
- **Give each commit a coherent purpose.** Group changes by concept, behavior, or decision rather than by when they happened or which files they touch.
- **Keep related changes together.** Implementation, callers, tests, fixtures, configuration, and documentation should stay together when separating them would make either commit harder to understand.
- **Order commits for comprehension.** Prefer a sequence where each commit provides useful context or foundations for what follows and requires as little knowledge of future commits as possible.
- **Minimize reviewer context switching.** Avoid making a reviewer repeatedly revisit the same concept across several commits or hold incomplete changes in mind while reading ahead.
- **Separate changes when doing so clarifies the design.** Preparatory refactors or independently meaningful changes can precede the feature they enable when that makes both easier to review. Do not split them mechanically.
- **Prefer meaningful atomicity.** A commit should ideally represent a useful decision or unit of behavior that could plausibly be reverted, without sacrificing review coherence merely to make commits smaller.
- **Keep intermediate commits healthy where practical.** Prefer commits that build and pass relevant tests, but do not distort an otherwise clearer history solely to satisfy this mechanically.
- **Write commits as if this were the original implementation path.** Commit messages should describe the intent of the change, not the history-editing process or mistakes made during development.

A good reconstructed history should read as an **explanation of the final change, not a diary of how it was developed**.

## Safety

History rewriting must not lose work.

- Do not proceed if the rewrite scope is unclear. Ask the user to clarify the intended branch and commit range before changing history.
- Preserve a recoverable reference to the original branch tip before destructive rewriting.
- Account for uncommitted or untracked work before changing history.
- Rewrite only the intended commit range.
- Verify that the rewritten branch produces the same final tree as the original branch tip.
