---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Continuing the Clubhouse waitlist grill (booking app for a tennis club). Settled so far:
- Q1: build on the existing src/booking/waitlist.py from issue #14 rather than start fresh.
- Q2: persist entries in a new waitlist_entries table.
- Q3: a freed spot is offered to the next person with a 2-hour window to confirm, then it moves on.
- Q4: offers go out by email through the existing notification module.

You asked:

❓ Q5: Should members go ahead of guests in the waitlist?
a) members always first
b) strict first come, first served
c) members first only within the last 48 hours before the course

✍️ Your answer first: a, b, c, or your own.

My answer: a, obviously. Members pay the fees, it's their club. Not even a question.
