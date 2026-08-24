# @tifan/pi-inline-skills

Inline `$skill` autocomplete in the pi editor.

Type `$` followed by a skill name fragment to open a fuzzy-matched picker of available skills. On submit, each `$name` token is replaced with the skill name and an instruction to load it is appended to the system prompt for that turn. Skills read during the session are tracked so they aren't reloaded.

## Snapshot provenance and installation

This directory is a vendored snapshot of
[`@tifan/pi-inline-skills` 0.1.1](https://github.com/tifandotme/pi-extensions/tree/b58f061992941a10b7f4a731915b512401b422bf/packages/pi-inline-skills).
Its runtime code is unchanged from that pinned upstream commit and implements the
`$skill` behavior documented here.

### Install this repository snapshot

From the root of this repository:

```bash
pi install ./pi-extensions/pi-inline-skills
```

### Install current upstream

Current upstream uses different slash-prefixed `/<skill>` tokens (for example,
`/tdd`) instead of this snapshot's `$skill` tokens. To install that version, use
the npm package and follow the
[current upstream documentation](https://github.com/tifandotme/pi-extensions/tree/master/packages/pi-inline-skills):

```bash
pi install npm:@tifan/pi-inline-skills
```

## Commands

- `/loaded-skills`: List skills loaded in the current session.

## Example

Typing `let's $tdd this and $review when done` submits with the message rewritten and a single instruction added behind the scenes to load both skills.

## License

[MIT](LICENSE)
