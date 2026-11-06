---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

We're mid-grill on the Clubhouse waitlist plan (booking app for a tennis club). Here's where we are.

Plan: add a waitlist to course bookings. When a course is full people queue, and when someone cancels the next person gets the spot.

Settled so far:
- Q1: build on the existing src/booking/waitlist.py from issue #14 rather than start fresh.
- Q2: persist entries in a new waitlist_entries table.
- Q3: a freed spot is offered to the next person with a 2-hour window to confirm, then it moves on.
- Q4: offers go out by email through the existing notification module.

Still open in my notes: whether members go ahead of guests in the queue. That's the last one. Next question.
