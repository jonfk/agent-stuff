# TODO

- [ ] Remove this TODO.md file once all todos are done
- [x] Remove the `upstream audit`, `update recommendation`, `removed skills`, `to try` sections from README
- [ ] Check that README docs is up to date.

## Skill updates

Upstream status and mergeability were verified on 2026-08-19. A clean subtree
merge was tested in a disposable clone; it does not imply that the upstream
behavior has been reviewed and accepted.

- [x] `codebase-design` — **Mergeability: clean subtree merge (tested).** UPDATE from upstream. update the required documentation
- [x] `domain-modeling` — **Mergeability: clean subtree merge (tested).** UPDATE from upstream. update the required documentation
- [x] `frontend-design` — **Not Mergeable. Remove current version and re-subtree the upstream version from https://github.com/anthropics/skills/tree/main/skills/frontend-design** rename to anthropic-frontend-design and make it manual only.
- [x] `grill-me` The local skill intentionally diverges, while upstream is now a manual-only wrapper around `grilling`. Document that this skill should no longer be updated from upstream. Lock in where the divergence started and document where it was sourced. Make it manual only invokation.
- [x] `grill-with-docs` — **Mergeability: clean subtree merge (tested).** Update from upstream. update the required docs and make it manual only invokation.
- [x] `grilling` — **Mergeability: clean subtree merge (tested).** Update from upstream. update the required docs and make it manual only invocation.
- [x] `improve-codebase-architecture` — **Mergeability: clean subtree merge (tested).** Update from upstream. update the required docs. Make sure it is still manual only invocation.
- [x] `prototype` — **Mergeability: clean subtree merge (tested).** Update from upstream.
- [x] `tdd` — **Mergeability: clean subtree merge (tested).** Update from upstream.

Use the per-skill subtree commands in [`SUBTREE.md`](SUBTREE.md). After an update,
refresh its imported commit, split commit, and permalink in `SUBTREE.md` and
[`README.md`](README.md).
