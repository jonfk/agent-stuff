# Workflow notes

## Fixed contract

- Produce exactly 5 design concepts unless the user explicitly changes the count.
- Give each concept a distinct aesthetic direction, not a polished variant of the same idea.
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
- Anything else:
  - Ask before changing structure.

## Recommended page contract

- Gallery page: show all five concepts with names, rationale, and direct links.
- Concept primary page: include a link back to the gallery and a switcher to the other concepts.
- Concept secondary pages: add them only when the concept benefits from multiple views.

## Pairing with `$frontend-design`

- Use `$frontend-design` intentionally, not as decoration.
- Have each concept commit to a specific visual thesis before implementation.
- Push typography, color, composition, and motion far enough that the five concepts do not converge.
- Keep the implementation in plain Vite vanilla HTML/CSS/JS.

## Verification checklist

- The gallery opens as the comparison view.
- All five concepts load in local development.
- Every concept page can navigate back to the gallery.
- Cross-concept switching works.
