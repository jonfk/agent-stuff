# preset

Pi extension for named presets that can set model, thinking level, tools, and per-preset system prompt instructions.

Part of [`pi-extensions`](../../README.md).

## Install with pi

```bash
pi install npm:@richardgill/pi-preset
```

or locally

```bash
pi install ~/code/pi-extensions/main/extensions/preset
```

## Configure

Create `preset.jsonc` in your pi agent config folder for global presets:

```jsonc
{
  "presets": {
    "plan": {
      "provider": "openai-codex",
      "model": "gpt-5.2-codex",
      "thinkingLevel": "high",
      "tools": ["read", "bash"],
      "instructions": "Planning mode. Do not edit files."
    },
    "implement": {
      "provider": "anthropic",
      "model": "claude-sonnet-4-5",
      "thinkingLevel": "high",
      "tools": ["read", "bash", "edit", "write"],
      "instructions": "Implementation mode. Make focused changes."
    }
  }
}
```

You can also define project-local presets in `./.pi/preset.jsonc` from the directory where
you start pi:

```jsonc
{
  "presets": {
    "review": {
      "provider": "openai-codex",
      "model": "gpt-5.2-codex",
      "thinkingLevel": "high",
      "tools": ["read", "bash"],
      "instructions": "Review this project. Do not edit files."
    }
  }
}
```

Project presets are merged over global presets. If a project preset has the same name as a
global preset, the project preset wins. Project-local config only supports `presets`; other
extension options should stay in the global agent config.

## Usage

```bash
pi --preset plan
```

- `/preset` opens the selector
- `/preset implement` activates a preset directly
- `ctrl+shift+u` cycles presets
