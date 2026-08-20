# SUBTREE.md

The following repositories were vendored using `git subtree`.

## `vendor/example-lib`

- **Upstream:** `https://github.com/org/example-lib.git`
- **Permalink:** `https://github.com/org/example-lib/tree/abc1234/examples/`
- **Ref:** `main`
- **Last imported:** `abc1234`
- **Mode:** `--squash`
- **Local path:** `vendor/example-lib`

### Update

```sh
git subtree pull \
  --prefix=vendor/example-lib \
  https://github.com/org/example-lib.git \
  main \
  --squash
```

## Maintenance groups

Only include this section when multiple subtrees must be maintained together.

### `example-lib-group`

- **Reason:** The members depend on each other and must use matching upstream code.
- **Members:**
  - `vendor/example-lib`
  - `vendor/example-lib-adapters`
- **Constraint:** Import every member from the same upstream ref or commit and update every member as part of the same change.
