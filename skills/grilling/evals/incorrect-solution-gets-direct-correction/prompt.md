---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Continuing a grill of a Python/PostgreSQL search endpoint. The only decision we're checking is query construction. The search term is arbitrary text entered by an anonymous website visitor.

My plan is:
query = "SELECT * FROM courses WHERE title = '" + search_term + "'"
cursor.execute(query)

I think this is safe because the database will reject bad SQL. Can we treat that as settled?
