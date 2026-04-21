# Vite multi-page notes

These notes capture the Vite details that matter for this skill. They are based on the official Vite docs reviewed on April 20, 2026:

- https://vite.dev/guide/
- https://vite.dev/guide/build#multi-page-app
- https://vite.dev/guide/features.html
- https://vite.dev/guide/assets.html

## Entry model

- `index.html` is source code and the application entrypoint in Vite. It is not a static file that belongs in `public/`.
- HTML files are first-class entrypoints. In development, any HTML file under the Vite root is directly routable by path.
- Nested pages work naturally in dev:
  - `<root>/index.html` -> `/`
  - `<root>/about.html` -> `/about.html`
  - `<root>/concepts/concept-01/index.html` -> `/concepts/concept-01/`

## Scaffolding facts

- Use Vite's native `vanilla` template for this skill unless the user says otherwise.
- You can scaffold directly into the current directory by using `.` as the project name.
- Vite supports a `--no-interactive` flag for prompt-free setup.
- Vite currently documents a Node requirement of `20.19+` or `22.12+`. Respect the local environment before scaffolding.

## Build requirements for multi-page apps

- Dev routing is not enough for production builds. For build output, include every generated HTML entry in `build.rolldownOptions.input`.
- Use resolved file paths, not relative strings.
- For HTML entries, Vite ignores the object key name and uses the resolved file path when generating the built HTML output. The folder structure should therefore be designed intentionally.

Example pattern:

```js
import { resolve } from 'node:path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rolldownOptions: {
      input: {
        gallery: resolve(import.meta.dirname, 'index.html'),
        concept01: resolve(import.meta.dirname, 'concepts/concept-01/index.html'),
        concept02: resolve(import.meta.dirname, 'concepts/concept-02/index.html'),
      },
    },
  },
})
```

## Root caveat

- If the project sets a custom Vite `root`, remember that `import.meta.dirname` still points at the folder containing `vite.config.*`.
- When resolving HTML build inputs for a custom-root project, include the `root` directory in the resolved paths instead of assuming the config file location is the served root.

## Asset and path handling

- Prefer imported assets over `public/` assets. Imported assets participate in the module graph and build rewriting.
- If you must use `public/`, reference those files with root-absolute paths such as `/icon.png`, not `public/icon.png`.
- Vite automatically processes asset URLs referenced from supported HTML elements such as `<script type="module" src>`, `<link href>`, and `<img src>`.
- Nested concept pages are where asset-path mistakes usually happen. Favor module imports, colocated CSS, and deliberate relative links.

## Base-path guidance

- Do not change `base` by default.
- If the site must be portable under an unknown nested path, a relative base such as `"./"` or `""` is allowed.
- Relative base relies on `import.meta` support. Do not switch to it casually inside an existing project with established deployment assumptions.
