---
name: to-patch-md
description: use when working with a fork, updating a fork from upstream, resolving merge conflicts, or reimplementing fork behavior on clean upstream.
---

<what-to-do>
Use this skill when working with a forked project.

Create or update a `PATCH.md` file to document changes from upstream, guide future maintenance, and preserve the intent and design of fork-specific behavior.

When creating or updating `PATCH.md`, follow the format in [PATCH-FORMAT.md](./PATCH-FORMAT.md)

Treat `PATCH.md` as the maintenance guide for intentional differences between the fork and upstream.

Use it according to the task:

- When writing or updating `PATCH.md`, document each logical fork patch’s purpose, behavior, design, reimplementation notes, and verification.
- When updating from upstream or resolving merge conflicts, use `PATCH.md` to decide which fork behaviors and invariants must be preserved.
- When reimplementing fork changes on clean upstream, use `PATCH.md` as the behavioral specification and adapt the change to upstream’s current architecture.

Prefer current upstream architecture when applying, adapting, or reimplementing fork behavior.

After modifying code, update `PATCH.md` when the patch behavior, design, verification, or status has changed.
</what-to-do>

<supporting-info>
`PATCH.md` is not a changelog, raw diff summary, or replay script. It is a lightweight behavioral and architectural guide for fork-specific changes.

The goal is to preserve enough intent that fork-specific behavior can be maintained, adapted, or reimplemented even if upstream has reorganized the code.

Good `PATCH.md` entries describe stable concepts such as:

- purpose
- user-visible or developer-visible behavior
- subsystem responsibilities
- lifecycle stages
- data flow
- APIs or configuration semantics
- invariants
- verification steps

Avoid brittle references such as:

- line numbers
- narrow file paths
- local variable names
- temporary helper names
- incidental implementation details
</supporting-info>