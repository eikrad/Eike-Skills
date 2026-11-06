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
a) a new waitlist_entries table
b) a JSON column on courses

➡️ a, because booking a spot locks the course row (SELECT ... FOR UPDATE in courses.py), so a JSON column on that row would make every waitlist join wait on the same lock as bookings. Best case for b: no new table, and no join when showing a course.

My answer: nah, b. JSON column.

Input files: README.md, ISSUES.md, src/booking/waitlist.py, src/booking/courses.py
