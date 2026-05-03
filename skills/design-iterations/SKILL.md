---
name: design-iterations
description: Design and implement multiple distinct web application concepts.
---

# Design Iterations Skill

Build 5 distinct concepts each exploring a clear and intentional aesthetic direction. 

## When to Use

Use this skill when the user wants to:

- Explore multiple design directions before committing to one.
- View mockups of different alternatives

## Inputs to Gather (or Assume)

- Purpose & audience: What problem does this UI solve? Who uses it?
- Brand/voice: Any reference brands, tone, or visual inspiration?
- Technical constraints: Framework, library, CSS strategy, accessibility, performance
- Content constraints: Required copy, assets, data, features

## Design Thinking (Required)

For **each** concept, commit to a **single, bold aesthetic direction**. Name it and execute it consistently. Examples:
- Brutalist / raw / utilitarian
- Editorial / magazine / typographic
- Luxury / refined / minimal
- Retro‑futuristic / cyber / neon
- Art‑deco / geometric / ornamental
- Handcrafted / organic / textured

**Avoid generic AI aesthetics.** No “default” fonts, color schemes, or stock layouts.

Before writing code, define the system:
1. **Visual direction** — one sentence that describes the vibe
2. **Differentiator** — what should be memorable about this UI?
3. **Typography system** — display + body fonts, scale, weight, casing
4. **Color system** — dominant, accent, neutral; define as CSS variables
5. **Layout strategy** — grid rhythm, spacing scale, hierarchy plan
6. **Motion strategy** — 1–2 meaningful interaction moments

## Implementation

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

- Create a new empty directory where you will scaffold a vite `vanilla` project.
- Each concept must have its own primary HTML entrypoint
- Add secondary pages inside of that concept's directory.

### Design comparison gallery

- Use a gallery as the main comparison surface.
    - For each concept, include:
        - concept name
        - one-sentence rationale
        - link to the main page
        - links to any extra pages for that concept
    - Each concept must link back to the gallery.
    - The gallery must provide fast comparison and switching across all five concepts.

### Vite HTML routing

- Treat HTML files as first-class source files. Do not tuck the gallery into `public/`.
- Rely on Vite's direct HTML routing in development.
- Any HTML file under the Vite root is directly routable in development.
- Nested pages should work directly, for example `concepts/concept-01/index.html` at `/concepts/concept-01/`.
- Use Vite's `vanilla` template unless the user explicitly asks for something else.
- When scaffolding a fresh project, use `.` with `--no-interactive`.
- Do not introduce a custom `root`, router, or framework unless the user asks.
- Do not add build config unless the user explicitly asks for production output.
- Keep assets and CSS simple and local to the pages using them.

## Verification

- Confirm the gallery opens as the comparison view.
- Confirm all concepts load in local development.
- Confirm every concept page can navigate back to the gallery.
- Confirm cross-concept switching works.

## Notes

- Optimize for concept speed, not production hardening.
- Avoid React, Vue, routing libraries, or build-specific complexity unless the user explicitly asks for them.
