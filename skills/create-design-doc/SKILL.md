---
name: create-design-doc
description: Help write, refine, or review technical design docs, RFCs, architecture proposals, technical plans, and decision notes. Use for point-in-time technical proposals optimized for clear reasoning, trade-off analysis, and expert review.
disable-model-invocation: true
---
# Design Docs

Use this skill when writing, reviewing, or improving a technical design doc.

A design doc is a point-in-time proposal made before implementation. Its purpose is to help competent reviewers decide whether the proposed design is a good trade-off for the problem being solved.

It is not primarily system documentation, a complete implementation manual, or a living source of truth. If the design changes materially after approval, write a follow-up design doc or decision note.

## Core principles

### Make the doc convincing

A good design doc should lay out the argument for a proposal.

It should answer the questions a thoughtful reviewer would naturally ask:

- What problem are we solving?
- Why does it matter?
- What are we proposing?
- Why this approach?
- What alternatives were considered?
- What trade-offs are we accepting?
- What risks or unknowns remain?

Do not merely describe the desired system. Explain why the design makes sense.

### Scale the doc to the decision

The length and detail of the doc should be proportional to:

- Importance of the decision.
- Complexity of the problem.
- Ambiguity in the requirements or solution.
- Number of stakeholders.
- Cost of being wrong.
- Difficulty of changing the decision later.

A simple change may only need a paragraph. A complex architectural decision may need a full document.

Do not write a long doc by default.

### Spend detail where mistakes are expensive

Do not distribute detail evenly.

Give more attention to decisions that are:

- Expensive to reverse.
- Architecturally significant.
- Cross-system or cross-team.
- User-visible.
- Operationally risky.
- Likely to affect future work.
- Based on non-obvious trade-offs.

Give less attention to choices that are obvious, local, easy to change, or better handled in code review.

### Use the three-layer onion

Structure the argument in layers:

1. Problem, goals, non-goals, and requirements.
2. Functional design: what behavior or capability the system provides.
3. Technical design: how the system provides it.

Each layer should justify the next.

If the problem is unclear, technical details are premature.  
If the functional design does not satisfy the goals, implementation details do not matter.  
If the technical design does not support the functional design, the proposal is weak.

### Make tradeoffs clear

Do not pretend the proposal is perfect.

A strong design doc is honest about:

- What the design optimizes for.
- What it makes worse.
- What risks it introduces.
- Which assumptions matter.
- Which alternatives were rejected and why.

The goal is not to prove perfection. The goal is to show that the proposal is a reasonable and well-considered trade-off.

## Workflow

First determine whether the user wants a new doc, outline, review, rewrite, shorter decision note, or questions to resolve before writing.

If key context is missing, ask concise clarifying questions. If the user wants a draft anyway, state reasonable assumptions and continue.

Calibrate the output size before drafting: paragraph note, short design doc, or full design doc.

## Minimal structure

Use this structure as a starting point, not as a mandatory template.

### Summary

Briefly state:

- The problem.
- The proposed solution.
- The most important trade-off.
- The expected outcome.

A reader should understand the shape of the proposal from this section alone.

### Problem

Explain the current situation and why it is insufficient.

Include only the context needed to understand the decision.

### Goals and non-goals

State what the design should and should not accomplish.

Non-goals should rule out plausible adjacent work, not obvious irrelevancies.

### Requirements or decision criteria

List the criteria that matter for choosing a design.

Examples:

- Functional behavior.
- Performance.
- Reliability.
- Compatibility.
- Migration constraints.
- Operational burden.
- Developer experience.
- Cost or complexity.

Only include criteria that affect the decision.

### Proposed design

Describe the design at the level needed to evaluate it.

Focus on stable and important aspects:

- Main components.
- Responsibilities.
- Interfaces.
- Data flow.
- State transitions.
- Key dependencies.
- Failure modes.
- Hard-to-change choices.

Avoid volatile implementation details unless they are essential to the decision.

### Alternatives considered

Describe the serious alternatives.

For each alternative, explain:

- Why it was plausible.
- Why it was rejected.
- What trade-off the proposed design makes instead.

This is one of the most important sections.

### Trade-offs, risks, and open questions

Be explicit about costs, risks, and uncertainty.

Include unresolved questions only when they matter to approving or implementing the design.

### Implementation or rollout plan

Include this only when it helps evaluate feasibility.

For small changes, a sentence may be enough. For larger changes, include sequencing, migration, rollback, or ownership details as needed.

## Status

Use simple statuses:

- Draft: being written, discussed, or reviewed.
- Approved: accepted as the point-in-time decision.

Do not silently rewrite approved history. If the decision changes materially, write a follow-up.

## Style guidance

Write for competent reviewers with limited attention.

Prefer:

- Direct language.
- Clear reasoning.
- Concrete examples.
- Explicit trade-offs.
- Short sections.
- Diagrams when they compress understanding.

Avoid:

- Boilerplate sections.
- Unnecessary implementation detail.
- Exhaustive history of every idea considered.
- Vague goals.
- Hiding uncertainty.
- Treating the template as mandatory.

## Review guidance

When reviewing a design doc, evaluate the argument layer by layer:

1. Is the problem real and worth solving?
2. Are the goals and non-goals right?
3. Do the requirements capture what matters?
4. Does the functional design satisfy the requirements?
5. Does the technical design support the functional design?
6. Were serious alternatives considered?
7. Are the trade-offs and risks acceptable?
8. Is the level of detail appropriate for the cost of being wrong?

A good review improves the decision. It is not a search for template compliance.
