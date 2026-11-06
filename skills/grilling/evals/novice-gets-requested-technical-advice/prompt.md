---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

We're grilling a waitlist implementation. The app uses PostgreSQL, the queue must survive restarts, entries need FIFO ordering, and the same user must not join the same course twice. There are no deployed waitlist consumers yet. You asked whether entries should go in a new table or in JSON on courses.

I don't know enough about databases to choose. Please explain the practical difference and tell me what you recommend. Don't make me guess first.
