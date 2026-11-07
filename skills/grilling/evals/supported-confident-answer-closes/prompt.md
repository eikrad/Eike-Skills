---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Continuing our grill on a public booking endpoint. The last question was whether a client retries a timed-out booking with the same idempotency key or a new key. The strongest objection to reusing a key was accidentally treating a changed request as the old booking.

My answer: Definitely reuse the same key for the same logical booking. We already agreed to store the request hash and reject reuse with a different body. The supplied integration-test result confirms that concurrent identical retries create one booking, while the changed-body case returns a conflict. That addresses the objection; I accept retaining keys for the agreed seven days.

The only remaining release decision is whether a failed final retry should show the user a support link or an in-app retry button. Ask that next.
