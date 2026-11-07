---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

End our waitlist grill with a compact handoff for the developer. No more interview questions and no implementation in this turn.

Agreed:
- Goal: reduce the admin's manual work when a course spot opens.
- Build on the existing waitlist module; persist a FIFO queue.
- Offer the freed place to the next queued person by email.
- The offer expires after two hours; expiry offers the place to the next person.
- Accepting a valid offer books one place and removes that person from the queue.
- Non-goals: member priority, SMS, operational dashboard.
- Dependency: the existing email sender must be callable by the expiry worker.
- Agreed checks: queue order survives a restart; a cancellation sends one offer to the queue head; an expired offer advances once; accepting the same offer twice never creates two bookings.
- Next verification step: run a small expiry-and-acceptance integration check against the existing booking module.
- Open risk: the behavior after a bounced email is deferred to the next release, as I explicitly accepted.

Use these requirements. If you add an acceptance check that we haven't agreed, label it as proposed.
