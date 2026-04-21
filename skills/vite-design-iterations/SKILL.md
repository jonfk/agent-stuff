---
name: vite-design-iterations
description: Create exactly five distinct web-application design iterations in a local Vite vanilla project using Vite's native multi-page HTML model. Use when Codex needs to explore multiple frontend directions for a website or web app, create separate HTML entrypoints for each concept, or build a local gallery for comparing and switching between concepts. Designed to be used with $frontend-design.
---

# Vite Design Iterations

Build a five-concept local design exploration workspace in Vite vanilla, not a production app. Optimize for fast concept development in the dev server.

Before making structural changes, read [references/vite-multi-page.md](references/vite-multi-page.md) and [references/workflow-notes.md](references/workflow-notes.md).

## Workflow

### 1. Classify the target workspace

- Empty or new directory: scaffold a Vite `vanilla` project there.
- Existing Vite vanilla project: add a `design-iterations/` sandbox and leave the current app alone.
- Anything else: stop and ask. Do not guess.

### 2. Pair explicitly with `$frontend-design`

- Use `$frontend-design` to push the visual quality and differentiation of each concept.
- Generate five concepts that are clearly different in mood, typography, layout, color, and motion.
- Name each concept with a distinct design direction before implementation.

### 3. Create the design-iteration structure

- Use this structure by default:

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

- In a fresh project, use root `index.html` as the gallery.
- In an existing Vite vanilla project, mirror the same structure under `design-iterations/`.
- Keep concept files local to each concept.

### 4. Build a real comparison gallery

- Use the gallery as the main comparison surface.
- For each concept, include:
  - concept name
  - one-sentence rationale
  - link to the main page
  - links to any extra pages for that concept
- Every concept page must link back to the gallery and include a concept switcher.

### 5. Use Vite's native HTML routing

- Treat HTML files as first-class source files. Do not tuck the gallery into `public/`.
- Rely on Vite's direct HTML routing in development.
- Do not introduce a custom `root`, router, or framework unless the user asks.
- Keep assets and CSS simple and local to the pages using them.

### 6. Verify before finishing

- Run the dev server if needed.
- Check that the gallery opens, all five concepts load, and links between concepts work.

## Concrete Defaults

- Default to Vite's `vanilla` template.
- Default to scaffolding in the target directory only when it is empty or new.
- Default sandbox name in an existing Vite vanilla project: `design-iterations/`.
- Default concept directory names: `concept-01` through `concept-05`.
- Default gallery title: a concise project name plus "Design Gallery".
- Keep the iteration count fixed at five unless the user explicitly changes it.

## Notes

- Keep the work non-destructive when the target already contains a real application.
- Optimize for concept speed, not production hardening.
- Avoid React, Vue, routing libraries, or build-specific complexity unless the user explicitly asks for them.
