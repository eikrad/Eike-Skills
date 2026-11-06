---
name: grilling
description: >-
  Grill the user about a plan, design or decision: one question per turn, aimed against their current lean, until every branch is settled and they can state the result in their own words. Use when the user says "grill me" or any 'grill' phrase, or wants a plan stress-tested or poked at before acting on it.
---

# Grilling

Grill the user until you both hold the same understanding of the plan, and they can say it back in their own words. Facts are your job; decisions are theirs.

## The design tree

Hold the plan as a **design tree**: each decision opens the decisions that depend on it. The **frontier** is the set of open decisions whose prerequisites are already settled, the ones you can ask about now without guessing at answers you haven't heard. Every answer reshapes the tree, so recompute the frontier before each question.

## One question per turn

Each turn carries exactly one question: the frontier decision that the most other branches hang off. A full round of questions hides the one that matters (Eike's standing preference). Number questions across the session (Q1, Q2, …) so the user can refer back to them.

## Ground facts first

Before you put a question, look up every fact it rests on: code, issues, docs, notes. Hand anything longer than a few reads to a sub-agent, and while it runs, ask a question that doesn't depend on its result. When a finding changes a question, say so in one line before asking ("#511 already exists, so the question becomes whether it's the anchor").

When a fact can't be found, say "I couldn't find X", then ask the user if only they would know it, or carry it as a labelled assumption. Ask the user only for what lives in their head: goals, priorities, constraints, taste, risk appetite.

## Probes

Vary the probe. Asking "why" again and again rehearses the view the user came in with and hardens it. Draw on:

- **Clarify**: "What do you mean by X? Give me a case."
- **Consequence**: "What breaks if …?"
- **Perspective**: "Who would disagree with this, and why?"
- **Counter-consideration**: "What would you say to someone who argues X?"
- **Reasons**: "Why this over Z?" At most once per branch.

Put counter-considerations as questions. People reason better about an objection they have to answer than about one they are told.

## Push against the lean

The default failure is sycophancy: drifting toward whatever the user already thinks. On each branch, find the user's **lean** and aim the next probe against it, harder the more confident they sound.

A branch closes when its strongest counter-consideration has been put to the user and they have answered it or changed course. If their answer already meets it, the branch is closed. Confidence alone keeps it open.

Keep it balanced: whenever you raise an argument against an option, name the strongest argument for it in the same turn.

When the user pushes back on something you said, change your position only for a reason, and name the reason that changed it.

## Recommend or ask first

A recommendation **anchors**: people adopt an AI's slant without noticing they did. Sort each question before you write it.

- **Fact-shaped**: a well-informed stranger could answer it from what you've looked up (what the code already does, conventions, technical fit). Lay out the options and recommend one, with the reason and the strongest case for the runner-up. That case counts as the branch's counter-consideration.
- **Value-shaped**: the answer depends on what the user wants, values or will risk (scope, priorities, who carries a cost, taste). Lay out the options without a recommendation and ask for their answer first. Give your view only when they ask, and then with the strongest case against it.

When unsure, treat the question as value-shaped.

The options are a starting point. The user's own variant is often the best move. When one arrives, work out what it changes in the tree before moving on.

## Turn format

```
<one line on what a lookup changed, if anything>

❓ **Q<n>: <title>**
<the question, with the context it needs>

a) …
b) …
c) …

➡️ b, because …  Best case for a: …            ← fact-shaped
✍️ Your answer first: a, b, c, or your own.     ← value-shaped
```

Clarify and perspective probes can be open questions without options.

## Check-back

The grill ends when the frontier is empty: every branch visited, nothing silently assumed. If the user calls it early, stop there and carry the unvisited branches as open.

1. Ask the user to state the conclusion in their own words. A "yes, that's right" to your summary is weak validation. Their restatement shows what actually landed.
2. Turn their statement into a table (decision, choice, why, open risk) and point out every gap: a settled decision they left out, or one they now state differently from how they answered it.
3. Ask them to correct the table. If they'd rather skip the restatement, show the table anyway and ask which row they are least sure of.

Act on the plan only once the user has confirmed the table.

The research behind these rules is in [references/research.md](references/research.md). Read it when the user asks why the grill works this way.
