# PATCH format

The PATCH.md file lives at the root of the repo.
it documents the intentional differences between a fork and upstream.

Its purpose is to preserve the intent, behavior, and design constraints of fork-specific changes so they can be maintained, reapplied, or reimplemented when syncing with upstream.

```md
# PATCH.md

## Documentation Rules

- Document intent and behavior, not raw diffs.
- Prefer architectural descriptions over file paths, line numbers, or narrow code references.
- Describe stable concepts such as subsystems, data flow, lifecycle stages, APIs, configuration semantics, user-visible behavior, and invariants.
- Avoid details likely to become stale after upstream refactors.
- Group related changes into logical patches.
- Keep entries concise enough to review during an upstream merge.
- Include extra metadata only when it materially helps future maintenance.
- Use stable public names when helpful, but avoid incidental implementation details.

## Patches

### P001: {Patch name}

{1-3 sentences describing the feature or change}

#### Behavior

Describe what this fork does differently from upstream.

#### Design

Describe how the behavior fits into the system at an architectural level. Avoid brittle references to exact files, line numbers, or incidental implementation details.

#### Reimplementation

Explain how to recreate the behavior if the current patch no longer applies cleanly.

#### Verification

Describe how to confirm the behavior still works.
```