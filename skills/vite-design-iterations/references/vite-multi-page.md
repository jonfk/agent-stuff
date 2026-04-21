# Vite multi-page notes

These notes capture the Vite details that matter for this skill. They are based on the official Vite docs reviewed on April 20, 2026:

- https://vite.dev/guide/
- https://vite.dev/guide/build#multi-page-app
- https://vite.dev/guide/features.html
- https://vite.dev/guide/assets.html

## Use these rules

- `index.html` is source code and the application entrypoint in Vite. It is not a static file that belongs in `public/`.
- Any HTML file under the Vite root is directly routable in development.
- Nested pages work naturally in dev:
  - `<root>/index.html` -> `/`
  - `<root>/concepts/concept-01/index.html` -> `/concepts/concept-01/`
- Use Vite's `vanilla` template unless the user says otherwise.
- You can scaffold into the current directory with `.` and `--no-interactive`.
- Prefer local CSS and local assets over `public/` for this skill.

## Keep it simple

- Do not add build config unless the user explicitly asks for production output.
- Do not add a custom Vite `root` unless there is a strong reason.
- Do not move the gallery into `public/`.
