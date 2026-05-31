
## Skills

- [`grill-me`](skills/grill-me) - planning interview from [mattpocock/skills](https://github.com/mattpocock/skills/blob/60aa99c0230fbac087514ba5fca2ae6e519965fe/grill-me/SKILL.md)
- [`frontend-design`](skills/frontend-design) - from [anthropics/skills](https://github.com/anthropics/skills/blob/d230a6dd6eb1a0dbee9fec55e2f00a96e28dff81/skills/frontend-design/SKILL.md)
- [`design-iterations`](skills/design-iterations) - Frontend design concepts exploration
- [`improve-codebase-architecture`](skills/improve-codebase-architecture) - from [mattpocock/skills](https://github.com/mattpocock/skills/tree/b843cb5ea74b1fe5e58a0fc23cddef9e66076fb8/skills/engineering/improve-codebase-architecture)
- [`grill-with-docs`](skills/grill-with-docs) - from [mattpocock/skills](https://github.com/mattpocock/skills/tree/733d312884b3878a9a9cff693c5886943753a741/skills/engineering/grill-with-docs)
- [`tdd`](skills/tdd) - from [mattpocock/skills](https://github.com/mattpocock/skills/tree/733d312884b3878a9a9cff693c5886943753a741/skills/engineering/tdd)
- [`prototype`](skills/prototype) - from [mattpocock/skills](https://github.com/mattpocock/skills/tree/aaf2453fbdfe7a15c07f11d861224f34ab4b53cb/skills/engineering/prototype)
- [`to-prd`](skills/to-prd) - Inspired by [mattpocock/skills](https://github.com/mattpocock/skills/blob/733d312884b3878a9a9cff693c5886943753a741/skills/engineering/to-prd/SKILL.md) with modifications

### To try

- [`frontend-design`](https://github.com/mitsuhiko/agent-stuff/blob/b861028c706edf3e3f983cde09dd8cc8549ec948/skills/frontend-design/SKILL.md)

## Pi Extensions

This repo is a Pi package for extensions only. Skills are intentionally not exposed through the Pi package manifest because they are managed separately with `skills.sh`.

Install the extension package from git:

```bash
pi install git:github.com/jonfk/agent-stuff
```

Vendored code subtree metadata and update notes live in [`SUBTREE.md`](SUBTREE.md).

- [`pi-telegram`](pi-extensions/pi-telegram) - Telegram bridge for Pi, from [llblab/pi-telegram](https://github.com/llblab/pi-telegram) at [`c1b253a`](https://github.com/llblab/pi-telegram/commit/c1b253aeb05604e3adc70bf8642011fea1113c2c)
- [`preset`](pi-extensions/preset) - Preset extension for Pi, vendored from [richardgill/pi-extensions/extensions/preset](https://github.com/richardgill/pi-extensions/tree/7e09e5371d8a7fa8d90adc91273503b68bcf6c61/extensions/preset) at [`7e09e53`](https://github.com/richardgill/pi-extensions/commit/7e09e5371d8a7fa8d90adc91273503b68bcf6c61)
- [`pi-inline-skills`](pi-extensions/pi-inline-skills) - Inline `$skill` autocomplete for Pi, vendored from [tifandotme/pi-extensions/packages/pi-inline-skills](https://github.com/tifandotme/pi-extensions/tree/b58f061992941a10b7f4a731915b512401b422bf/packages/pi-inline-skills) at [`b58f061`](https://github.com/tifandotme/pi-extensions/commit/b58f061992941a10b7f4a731915b512401b422bf)


## Inspiration

Inspired by https://github.com/mitsuhiko/agent-stuff. I want to gather interesting skills, prompts, commands, etc.

- [web-browser skill](https://github.com/mitsuhiko/agent-stuff/blob/main/skills/web-browser/SKILL.md): Is apparently better than playwright MCP at browser interactions. Want to try it out. [permalink](https://github.com/mitsuhiko/agent-stuff/blob/063815263cb1031acfa73e12c86f01281dfac5e2/skills/web-browser/SKILL.md)
- [anthropics/skills/frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md): According to Theo from T3gg, he uses this with a prompt that asks for up to 5 unique designs when creating a new design. Something to try. [permalink](https://github.com/anthropics/skills/blob/a5bcdd7e58cdff48566bf876f0a72a2008dcefbc/skills/frontend-design/SKILL.md)
- [mattpocock's skills](https://github.com/mattpocock/skills/) Matt Pocock has a lot of pretty useful and insightful skills.
- [badlogic/pi-skills](https://github.com/badlogic/pi-skills) from the creator of Pi
