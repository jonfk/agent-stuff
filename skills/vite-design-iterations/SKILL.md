---
name: vite-design-iterations
description: Create exactly five distinct web-application design iterations in a local Vite vanilla project using Vite's native multi-page HTML model. Use when Codex needs to explore multiple frontend directions for a website or web app, create separate HTML entrypoints for each concept, or build a local gallery for comparing and switching between concepts. Designed to be used with $frontend-design.
---

# Vite Design Iterations

Build a five-concept local design exploration workspace in Vite vanilla, not a production app. Optimize for fast concept development in the dev server.

## Workflow

### 1. Classify the target workspace

- Empty or new directory: scaffold a Vite `vanilla` project there.
- Existing Vite vanilla project: add a `design-iterations/` sandbox and leave the current app alone.
- Anything else: stop and ask. Do not guess.

### 2. Pair explicitly with `$frontend-design`

- Use `$frontend-design` to push the visual quality and differentiation of each concept.
- Generate five concepts that are clearly different in mood, typography, layout, color, and motion.
- Name each concept with a distinct design direction before implementation.
- Keep each concept visually distinct, not a polished variant of the same idea.

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
- Each concept must have its own primary HTML entrypoint.
- Add secondary pages only when a concept benefits from multiple views, and keep them inside that concept's directory.

### 4. Build a real comparison gallery

- Use the gallery as the main comparison surface.
- For each concept, include:
  - concept name
  - one-sentence rationale
  - link to the main page
  - links to any extra pages for that concept
- Every concept page must link back to the gallery and include a concept switcher.
- The gallery must provide fast comparison and switching across all five concepts.

### 5. Use Vite's native HTML routing

- Treat HTML files as first-class source files. Do not tuck the gallery into `public/`.
- Rely on Vite's direct HTML routing in development.
- Any HTML file under the Vite root is directly routable in development.
- Nested pages should work directly, for example `concepts/concept-01/index.html` at `/concepts/concept-01/`.
- Use Vite's `vanilla` template unless the user explicitly asks for something else.
- When scaffolding a fresh project, use `.` with `--no-interactive`.
- Do not introduce a custom `root`, router, or framework unless the user asks.
- Do not add build config unless the user explicitly asks for production output.
- Keep assets and CSS simple and local to the pages using them.

## Concrete Defaults

- Default to Vite's `vanilla` template.
- Default to scaffolding in the target directory only when it is empty or new.
- Default sandbox name in an existing Vite vanilla project: `design-iterations/`.
- Default concept directory names: `concept-01` through `concept-05`.
- Default gallery title: a concise project name plus "Design Gallery".
- Keep the iteration count fixed at five unless the user explicitly changes it.

## Verification

- Confirm the gallery opens as the comparison view.
- Confirm all five concepts load in local development.
- Confirm every concept page can navigate back to the gallery.
- Confirm cross-concept switching works.

## Notes

- Keep the work non-destructive when the target already contains a real application.
- Optimize for concept speed, not production hardening.
- Avoid React, Vue, routing libraries, or build-specific complexity unless the user explicitly asks for them.
