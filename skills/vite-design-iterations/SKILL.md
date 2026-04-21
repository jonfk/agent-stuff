---
name: vite-design-iterations
description: Create exactly five distinct web-application design iterations inside a Vite vanilla project using Vite's native multi-page HTML model. Use when Codex needs to explore multiple frontend directions for a website or web app, create separate HTML entrypoints for each concept, build an index gallery for comparing and switching between concepts, or set up a design-iteration workspace in a new or existing Vite vanilla project. Designed to be used in conjunction with $frontend-design.
---

# Vite Design Iterations

Build a five-concept design exploration workspace in Vite vanilla, not a single final design. Keep each concept independently browsable, easy to compare, and compatible with Vite's native multi-page HTML workflow.

Before making structural changes, read [references/vite-multi-page.md](references/vite-multi-page.md) and [references/workflow-notes.md](references/workflow-notes.md).

## Workflow

### 1. Classify the target workspace

- Treat the target as one of four cases:
  - Empty directory or new directory: scaffold a Vite vanilla project there.
  - Existing Vite vanilla project: preserve the current app and create an isolated design sandbox inside the project.
  - Existing Vite project that is not clearly vanilla: stop and ask before converting its structure.
  - Existing non-Vite populated directory: stop and ask before choosing in-place scaffolding versus a child app.
- Detect "existing Vite vanilla project" conservatively. Confirm `vite` is present and the project appears HTML/CSS/JS-first rather than framework-first.
- Do not replace the current root app entrypoints in an existing project unless the user explicitly asks for that.

### 2. Pair explicitly with `$frontend-design`

- Use `$frontend-design` to push the visual quality and differentiation of each concept.
- Generate five concepts that are meaningfully different in mood, typography, layout, color, and motion. Do not produce minor variants of one theme.
- Name each concept with a memorable design direction before implementation.
- If `$frontend-design` is unavailable in the environment, state that briefly and continue using the same design standards.

### 3. Create the design-iteration structure

- The output contract is fixed:
  - Exactly 5 concepts.
  - Each concept has its own primary HTML entrypoint.
  - A concept may include additional pages when the design needs them.
  - The gallery must make it easy to compare and switch across all concepts.
- Preferred structure:

```text
index.html
concepts/
  concept-01/
    index.html
    main.js
    styles.css
  concept-02/
    index.html
  concept-03/
    index.html
  concept-04/
    index.html
  concept-05/
    index.html
```

- In a fresh project, use root `index.html` as the gallery entrypoint.
- In an existing Vite vanilla project, place the gallery and concept pages in an isolated sandbox such as `design-iterations/` and leave the existing app flow intact.
- Keep concept-local files close to the corresponding HTML entrypoint. Share code only for deliberate common utilities or tokens.

### 4. Build a real comparison gallery

- The gallery page is not a placeholder. It is the comparison surface for the five designs.
- Include, at minimum, for each concept:
  - Concept name.
  - One-sentence design rationale.
  - Link to the primary page.
  - Links to any secondary pages for that concept.
- Every concept page must include:
  - A clear link back to the gallery.
  - A switcher to jump to the other four concepts.
  - Local navigation when that concept spans multiple pages.
- Keep navigation paths compatible with both the Vite dev server and production build output.

### 5. Implement with Vite's native multi-page model

- Treat HTML files as first-class source files. Do not tuck the gallery into `public/`.
- In dev, rely on Vite's direct HTML routing for nested entrypoints.
- In build, add every generated HTML entrypoint to `build.rolldownOptions.input`.
- If the project uses a custom `root`, resolve input paths relative to that root. See [references/vite-multi-page.md](references/vite-multi-page.md) for the exact caveat.
- Prefer imported assets and CSS over `public/` assets unless file-name stability or source-free references are required.

### 6. Verify before finishing

- Run dependency install only when needed for the current package manager.
- Run a production build after generating the concepts.
- Check that:
  - The gallery loads.
  - All five concept entrypoints build successfully.
  - Cross-concept links and back-to-gallery links work.
  - Secondary concept pages build and route correctly.
  - Asset paths are valid from nested HTML pages.

## Concrete Defaults

- Default to Vite's `vanilla` template.
- Default to scaffolding in the target directory only when it is empty or new.
- Default sandbox name inside an existing Vite vanilla project: `design-iterations/`.
- Default concept directory names: `concept-01` through `concept-05`.
- Default gallery title: a concise project name plus "Design Gallery".
- Keep the iteration count fixed at five unless the user explicitly changes it.

## Notes

- Keep the work non-destructive when the target already contains a real application.
- Use opinionated structure only where it helps consistency. Preserve existing naming and package-manager conventions when working inside an existing project.
- Avoid adding React, Vue, routing libraries, or component frameworks unless the user explicitly asks to leave Vite vanilla.
