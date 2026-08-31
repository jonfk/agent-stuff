---
name: git-create-commit
description: Create a git commit for the intended current changes. Use when the user asks the agent to make, create, or run a commit.
---

# Create a Git Commit

Inspect the current changes and understand both their intent and implementation. Review several previous commits and use them as examples of the repository's conventions for scopes, wording, capitalization, and body style.

Create the requested commit using a Conventional Commits subject. Make the subject, body, and overall message length proportional to the importance and complexity of the change. A simple change may need only a subject. A significant or critical change should include a body that explains the intent and why the change matters, rather than merely repeating the diff.

Stage only the changes that belong to the user's requested or completed work, preserving unrelated changes in the working tree. Create the commit, then report its commit hash and final message.
