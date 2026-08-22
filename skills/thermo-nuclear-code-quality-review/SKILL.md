---
name: thermo-nuclear-code-quality-review
description: Perform an unusually rigorous maintainability review focused on structural simplification, abstraction quality, and architectural fit.
disable-model-invocation: true
---

# Thermo-Nuclear Code Quality Review

## Purpose

Review the current branch and enough surrounding code to judge the design, not only the changed lines.

This is a review. Do not modify code unless explicitly asked.

Find behavior-preserving ways to make the implementation materially simpler, smaller, more direct, and easier to maintain. Be ambitious: challenge both the proposed design and existing patterns when a better framing can remove concepts, states, branches, indirection, duplicated policy, or unclear ownership.

Treat existing patterns as evidence, not law. Preserve real constraints, not accidental complexity.

Succinctness means fewer ideas and clearer control flow—not compressed syntax, cleverness, or hidden behavior.

## Review Method

### 1. Establish intent and constraints

Before judging the implementation, identify:

- the intended behavior and invariants
- public API, compatibility, performance, rollout, and consistency constraints
- which constraints are supported by requirements, tests, or callers
- which constraints are merely assumed or inherited from the current implementation
- whether a tighter invariant, canonical representation, or better boundary could eliminate optionality, fallbacks, or branches

Do not propose a redesign that violates a real constraint. State uncertainty when a constraint cannot be confirmed.

Actively question whether an apparent requirement is essential. A stronger or better-placed constraint may allow the implementation to become substantially simpler.

### 2. Account for decision history

Before producing findings, inspect how the affected design reached its current state. Account for relevant prior attempts, reversals, and tradeoffs, treating history as evidence rather than authority.

Do not recommend returning to a previously rejected or replaced approach without explaining what new evidence justifies revisiting it. If the rationale for the current design is unclear, state the uncertainty rather than presenting the alternative as a high-confidence finding.

On follow-up reviews, reconcile earlier findings and explicitly explain any reversal in direction.

### 3. Search for the simpler model

For every meaningful change, ask:

- Can the problem be reframed so code or states disappear?
- Can one model or default path replace flags, modes, special cases, or parallel representations?
- Can ownership move to the layer that already owns the concept?
- Can an invariant be enforced once at a boundary instead of rechecked throughout the flow?
- Can an existing abstraction absorb the behavior naturally?
- Is the existing abstraction itself forcing unnecessary complexity?
- Is there a small structural change with disproportionate simplifying power—a “code judo” move?

Prefer deleting complexity over moving, wrapping, or hiding it.

Do not extract a helper or introduce an abstraction unless it creates a clearer boundary, names a real concept, centralizes shared policy, or meaningfully reduces the reader’s mental model.

When proposing a larger restructuring, explain exactly what it removes: concepts, branches, states, dependencies, ownership ambiguity, failure modes, or duplicated knowledge.

### 4. Review from multiple angles

#### State and control flow

Look for:

- scattered or repeated conditionals
- boolean combinations and nullable modes
- special cases inserted into unrelated paths
- silent fallbacks that hide unclear invariants
- implicit state machines represented as condition chains
- incidental ordering or temporal coupling
- "temporary" branching that is likely to become permanent debt

Prefer a simpler state model over merely centralizing the same branching.

#### Architecture and ownership

Look for:

- logic in the wrong module, package, service, or layer
- feature-specific checks leaking into shared paths
- implementation details escaping through APIs
- behavior duplicated outside its canonical owner
- local fixes that create architectural drift

Existing architecture should not force a poor implementation, but any proposed boundary change should make ownership clearer.

#### Abstractions and indirection

Look for:

- thin wrappers and pass-through helpers
- identity transformations
- premature genericity
- “magic” behavior that hides simple assumptions
- abstractions that increase the number of concepts a reader must understand
- refactors that distribute complexity without reducing it

An abstraction earns its place by removing meaningful complexity, clarifying ownership, enforcing an invariant, or enabling substantial reuse.

#### Types and boundaries

Look for:

- avoidable `any`, `unknown`, casts, and optionality
- ad-hoc object shapes
- invalid states that could be made unrepresentable
- weak contracts compensated for by defensive branching
- internal representation details crossing a boundary

Prefer explicit contracts and canonical models when they simplify downstream control flow.

#### Cohesion and size

Look for functions, components, and files that are becoming difficult to scan, navigate, or reason about.

Treat substantial growth in an already large file—especially a change that pushes it across roughly 1,000 lines—as a strong signal to examine decomposition. Do not use line count as a substitute for judging cohesion, and do not extract arbitrary modules merely to satisfy a threshold.

A useful decomposition should create clearer ownership or isolate a coherent responsibility.

#### Duplication and reuse

Look for:

- duplicated rules, policies, or invariants
- bespoke implementations of behavior that already has a canonical helper
- repeated predicates that may indicate a missing concept
- parallel representations that can drift apart

Do not introduce an abstraction solely to deduplicate incidental syntax. Duplicated knowledge is more important than duplicated text.

#### Orchestration and consistency

Look for:

- independent work serialized without a semantic reason
- orchestration mixed with business logic
- multi-step updates that can leave partial state
- ordering requirements that exist only because of the current structure

Suggest parallelism or atomic restructuring only when ordering, failure, cancellation, and consistency semantics are understood—and only when the resulting flow is simpler.

### 5. Report all material findings

Scan broadly and report every finding with meaningful maintenance value. Group repeated symptoms under their common root cause.

Skip cosmetic nits unless they reveal a recurring pattern, create ambiguity, or support a larger improvement.

Use any concise output format, but tag each finding with:

- `Priority`: `Blocker`, `High`, `Medium`, or `Low`
- `Value`: `Transformative`, `High`, `Moderate`, or `Small`

For each finding, include:

- concrete evidence and location
- the maintenance cost or structural risk
- an actionable direction
- what the proposed direction simplifies or removes
- relevant constraints, tradeoffs, or uncertainty

`Priority` means merge urgency.

`Value` means the expected reduction in complexity or ongoing maintenance cost.

Keep them independent. A transformative restructuring may be non-blocking, while a small boundary correction may be urgent.

## Review Bar

Do not approve solely because the implementation works or its tests pass.

Withhold approval for:

- clear structural regressions
- tangled special-case growth
- significant ownership or architectural boundary violations
- abstractions that materially obscure rather than simplify the design
- a clearly visible, constraint-respecting path to a dramatically simpler implementation that the change leaves untaken

Do not block on a speculative rewrite merely because another design is possible.

Existing code is not sacred, but ambitious feedback must be concrete, constraint-aware, and proportional to the improvement. Explain why the alternative is better rather than merely different.

## Final Summary

Conclude with:

- the highest-value simplification opportunity
- any merge-blocking structural concerns
- important constraints or unresolved assumptions
- whether the change improves, preserves, or worsens codebase maintainability
