---
name: council
description: Get review or feedback from a council of Claude and GPT models. Pass "high" for the high council. Use only when the user explicitly invokes this skill.
argument-hint: "[high] [request]"
disable-model-invocation: true
---

# Council

Finish the work before convening: fix known issues, address outstanding PR
comments, and run the relevant checks. Skip this for code the user plans to
replace.

## Members

Each cell is the member's reasoning effort; `-` means it does not sit on that
council. Convene the high council only when the user asks for it. If the user
names members, use those.

| Member | Council | High council |
| --- | --- | --- |
| Opus 5.5 (`opus`) | high | high |
| GPT-6.1 Sol (`gpt-6.1-sol`) | high | high |
| GPT-6 Astra (`gpt-6-astra`) | medium | high |
| Fable 5.1 (`fable`) | - | high |

Run Claude members as fresh subagents with the member's model and effort. Do
not fork: a fork ignores the model override. Run GPT members with Codex in the
background:

```bash
codex exec -m <model> -c model_reasoning_effort=<effort> -s read-only \
  --ephemeral --ignore-user-config -o <output-file> - < <request-file>
```

Start every member at once. If a member cannot run, report it instead of
substituting another model.

## Review

Give each member the request and the context it needs, and keep its work
read-only. Summarize the useful findings, disagreements, and recommended next
steps. For a code review, ask each member for a score out of 10; if one gives no
score, write `no score` rather than inventing one.

A full pass by every member is one round. If you agree with the findings, make
the changes and convene a fresh council for the next round, until the members
are satisfied or the remaining findings are ones you've declined.

Members can be wrong. Decline findings you disagree with, say why, and give the
reason to the next round so the finding isn't raised again just to be declined
again. Reviewers will suggest improvements beyond the task, especially in later
rounds. Decline those rather than expanding the work.

If the work ends in a pull request, add the scores to its description (edit it,
don't comment); otherwise put them in the final reply:

```markdown
## Council review

| Member | Round 1 | Round 2 |
| --- | --- | --- |
| Opus 5.5 | 7/10 | 9/10 |
| GPT-6.1 Sol | 8/10 | 10/10 |
```
