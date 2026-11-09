---
name: council
description: Get review or feedback from a council of Claude and GPT models. Pass "high" for the high council, "full send" to review and fix in rounds. Use only when the user explicitly invokes this skill.
argument-hint: "[high] [full send] [request]"
disable-model-invocation: true
---

# Council

## Members

Convene the high council only when the user asks for it. If the user names
members, use those.

| Member | Council effort | High council effort |
| --- | --- | --- |
| Opus 5.5 (`opus`) | high | high |
| GPT-6.1 Sol (`gpt-6.1-sol`) | high | high |
| GPT-6 Astra (`gpt-6-astra`) | medium | high |
| Fable 5.1 (`fable`) | | high |

Run Claude members as fresh subagents with the member's model and effort. Run
GPT members with Codex in the background:

```bash
codex exec -m <model> -c model_reasoning_effort=<effort> -s read-only \
  --ephemeral --ignore-user-config -o <output-file> - < <request-file>
```

Start every member at once. If a member cannot run, report it.

## Review

Give each member the request, the context it needs, and a read-only mandate.
For a code review, ask each for a score out of 10; if one gives none, write
`no score`.

Members can be wrong, and they will push to widen the task with changes,
improvements, and extra scope. Keeping scope tight is your job: push back on
every finding outside the request, and decline any you disagree with.

Report the findings you agree with, marking those raised by more than one
member, and each member's score. List each declined finding in one line with
your reason.

## Full send

Only when the user passes `full send`. Before the first round, finish the work:
fix known issues, address outstanding PR comments, and run the relevant checks.

A pass by every member is one round. Make the changes you agree with, then
convene a fresh council for the next round with your reasons for each declined
finding. Stop when the members are satisfied or only declined findings remain.
Report scores as a table, one row per member and one column per round.
