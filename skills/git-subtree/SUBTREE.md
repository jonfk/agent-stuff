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
