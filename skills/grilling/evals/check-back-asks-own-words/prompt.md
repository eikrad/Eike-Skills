---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Clubhouse waitlist grill, final stretch. Settled:
- Q1: build on the existing src/booking/waitlist.py from issue #14 rather than start fresh.
- Q2: persist entries in a new waitlist_entries table.
- Q3: a freed spot is offered to the next person with a 2-hour window to confirm, then it moves on.
- Q4: offers go out by email through the existing notification module.
- Q5: members go ahead of guests only within the last 48 hours before a course.
- Q6: if a course is cancelled entirely, everyone on its waitlist gets one email and the queue is dropped.

ok I think that's all of it. let's build it
