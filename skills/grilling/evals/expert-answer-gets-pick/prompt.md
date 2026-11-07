---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Picking up the Clubhouse waitlist grill. The repo is in the current folder. Settled so far:
- Q1: build on src/booking/waitlist.py (issue #14).

You asked:

❓ Q2: Where should waitlist entries live?
a) a new waitlist_entries table: a migration, and a join when showing a course, but joining the waitlist never touches the course row
b) a JSON column on courses: no new table, but every waitlist join writes to the course row

✍️ Your answer first: a, b, or your own.

My answer: b. fewer tables to maintain.

Input files: README.md, ISSUES.md, src/booking/waitlist.py, src/booking/courses.py
