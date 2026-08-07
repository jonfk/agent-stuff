---
name: fix-with-subagents
description: Process a user-provided list of issues or findings sequentially with fresh, context-isolated sub-agents. Each sub-agent independently validates one finding, chooses and implements a worthwhile fix, verifies it, and commits only that fix. Use only when the user explicitly invokes this skill and supplies findings to fix.
disable-model-invocation: true
---

# Fix Findings with Sub-agents

Expect an ordered list of findings. If the user does not supply any findings, ask for them.

Process the findings in the order supplied. Handle exactly one finding at a time, and wait for its sub-agent to finish before starting the next.

For each finding:

1. Start a new sub-agent using the available mechanism for creating a fresh context that does not inherit the calling agent's conversation. If the available sub-agent implementation cannot guarantee that isolation, stop and explain the limitation to the user.
2. Give the sub-agent only:
   - the individual finding, verbatim, and any proposed solution included with it;
   - the workflow instructions below;
   - access to the current repository so it can inspect the relevant code and repository instructions independently.
3. Do not give it other findings, the calling agent's analysis, or reports from previous sub-agents.
4. Instruct the sub-agent to:
   - independently verify that the finding is accurate and worthwhile to fix;
   - re-evaluate any proposed solution rather than accepting it uncritically, or determine a solution if none was proposed;
   - make no changes and create no commit if the finding is invalid or not worthwhile, and report the reasoning instead;
   - if the finding is valid, explain the chosen solution, plan the implementation, implement it, run relevant verification or tests, and review the resulting diff;
   - proceed from proposal through implementation without waiting for approval unless the user requested an approval gate;
   - commit only its own changes, following the repository's commit conventions and the Conventional Commits convention; if those conventions conflict, report the conflict instead of guessing;
   - report its validity decision, reasoning, solution, changes, verification results, and commit hash, if any.
5. Review the sub-agent's result and confirm the reported commit, if any, before processing the next finding.

After all findings have been processed, summarize the outcome and commit, if any, for each finding.
