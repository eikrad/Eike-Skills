---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

We're grilling a one-off, local CSV-to-JSON converter, not a service. Agreed scope:
- Read one UTF-8 CSV file and write one JSON array.
- Preserve the input row order.
- Require id and title columns; fail before writing output if either is absent.
- Report a malformed input row with its line number and leave any existing output unchanged.
- Acceptance checks: a two-row valid sample produces two ordered objects; a missing title header and a malformed row both exit nonzero without overwriting output.
- No hosting, accounts, database, analytics, scheduling, or future product roadmap.

Those are all the choices needed for this task. End the grill and give me the implementation handoff now. Do not start a new discussion of other features.
