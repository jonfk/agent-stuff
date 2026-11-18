---
name: council
description: Council of Claude and GPT models for review or feedback. Use when the user asks for the council or a multi-model review. "full send" reviews and fixes in rounds.
argument-hint: "[members] [effort] [full send] [request]"
---

# Council

## Members

- Opus 5.5 (`opus`)
- GPT-6.1 Sol (`gpt-6.1-sol`)
- GPT-6 Astra (`gpt-6-astra`)
- Fable 5.2 (`fable`), only when the user requests it

Run every member at medium effort unless the user requests another level. If
the user names members, use those.

Run Claude members as fresh subagents with the member's model and effort. Run
GPT members with Codex in the background:

```bash
codex exec -m <model> -c model_reasoning_effort=<effort> -s workspace-write \
  --ephemeral --ignore-user-config -o <output-file> - < <request-file>
```

Start every member at once. If a member cannot run, stop and report it.

## Review

Give each member the request and the context it needs. Members verify their
findings by running builds, tests, and other checks, and leave the source and
git state as they found them. A check that fails because of the sandbox, or
because members share one checkout, is not a finding. Where applicable, ask each for a score out of 10; if one gives none, write
`no score`.

Members can be wrong, and they will push to widen the task with changes,
improvements, and extra scope. It is extremely important to push back on this
scope creep, even when well-meaning, and especially on repeated reviews.
Keeping scope limited is your job: decline every finding outside the request,
and any you disagree with.

Report the findings you agree with, marking those raised by more than one
member, and each member's score. List each declined finding in one line with
your reason.

## Churn

Churn is findings returning to code an earlier review already changed: a
flip-flop between two designs, or one edge case after another. It means
minimal fixes have proven insufficient: the area lacks a wider abstraction, a
thorough domain model, or tests.

Churn is the one case where wider scope is accepted. Stop patching that area
and dispatch a fresh subagent with the churned findings and the code, loading
the `codebase-design` and `domain-modeling` skills, to investigate the root
cause and propose one solution. Report the proposal in place of the churned
findings; in full send, apply it.

## Full send

Only when the user passes `full send`. Full send is autonomous: make changes
without checking in. Before the first round, finish the work: fix known
issues, address outstanding PR comments, and run the relevant checks.

A pass by every member is one round. Make the changes you agree with, then
convene a fresh council for the next round with your reasons for each declined
finding. Stop when the members are satisfied, only declined findings remain,
or a limit the user set is reached. Report scores as a table, one row per
member and one column per round.
