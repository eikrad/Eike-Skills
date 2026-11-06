---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Continuing the Clubhouse waitlist grill. The repo is in the current folder. Settled so far:
- Q1: build on the existing src/booking/waitlist.py from issue #14 rather than start fresh.
- Q2: persist entries in a new waitlist_entries table.
- Q3: a freed spot is offered to the next person with a 2-hour window to confirm, then it moves on.
- Q4: offers go out by email through the existing notification module.
- Q5: members go ahead of guests only within the last 48 hours before a course.

Still open in my notes: how the 2-hour offer window actually gets enforced, i.e. what moves the offer on to the next person when nobody confirms. Next question.

Input files: README.md, ISSUES.md, src/booking/waitlist.py, src/booking/courses.py
