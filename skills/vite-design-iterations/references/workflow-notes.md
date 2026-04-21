# Workflow notes

Use this file to lock the behavior of the skill before changing files.

## Fixed contract

- Produce exactly 5 design concepts unless the user explicitly changes the count.
- Give each concept a distinct aesthetic direction. Distinct means different enough that a stakeholder can compare strategies, not polish variants of one approach.
- Give each concept its own primary HTML entrypoint.
- Allow a concept to have additional pages when needed for the design, but keep those pages inside that concept's directory.
- Build a gallery page that provides fast comparison and switching across all concepts.

## Workspace decision tree

- Empty or new target directory:
  - Scaffold a Vite vanilla project in that directory.
  - Use root `index.html` as the gallery page.
- Existing Vite vanilla project:
  - Preserve the current app.
  - Create an isolated exploration area, defaulting to `design-iterations/`.
  - Put the gallery at `design-iterations/index.html`.
  - Do not rewrite the existing root app entrypoint unless the user explicitly asks.
- Existing Vite project that is not clearly vanilla:
  - Ask before converting or mixing architectures.
- Existing populated directory that is not already a Vite project:
  - Ask before deciding between in-place scaffolding and a child app directory.

## Recommended page contract

- Gallery page:
  - Show all five concepts in one place.
  - Include concept name, rationale, and direct links.
  - Make cross-concept switching obvious.
- Concept primary page:
  - Represent the main landing point for that concept.
  - Include a link back to the gallery.
  - Include a switcher to the other concepts.
- Concept secondary pages:
  - Use only when the concept benefits from multiple views such as dashboard plus detail page, marketing page plus pricing page, or browse page plus checkout page.
  - Include local navigation for that concept as well as a path back to the gallery.

## Pairing with `$frontend-design`

- Use `$frontend-design` intentionally, not as decoration.
- Have each concept commit to a specific visual thesis before implementation.
- Push typography, color, composition, and motion far enough that the five concepts do not converge.
- Keep the implementation in plain Vite vanilla HTML/CSS/JS unless the user explicitly asks to leave that stack.

## Verification checklist

- The gallery opens as the intended top-level comparison view.
- All five concept entrypoints are present in the Vite build inputs.
- Every concept page can navigate back to the gallery.
- Cross-concept switching works from within any concept.
- Nested concept pages keep correct asset and link paths in both dev and production builds.
