---
name: feature-workflow
description: >
  TDD feature workflow from idea to committed, tested code. Use when the user wants to build or
  start a feature, asks what's next on the roadmap, or mentions TDD or /tdd.
---

# Feature Workflow

idea → scan → requirements → branch → phased plan → tracer bullets → PR

## 1. What to Build

Roadmap file (`ROADMAP.md`, `TODO.md`, `docs/roadmap.md`) → show the next uncompleted item.
User described it → use that. Neither → ask.

Done when the user has confirmed one concrete item.

## 2. Scan

Read the code before planning anything.

**Conventions** — `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `CONVENTIONS.md`, `CONTRIBUTING.md`, README architecture sections. Extract naming, folders, test framework, import style, linting. Conventions are law.

**Affected modules** — read every file this feature touches. Note public interfaces at risk, shared utilities, and established patterns (errors, data fetching, test structure). Pick up the codebase's domain language — tests get named in it.

**Baseline** — run the full suite. A red baseline stops the workflow: report it and get it green before anything else.

Done when you have reported conventions, affected modules, and a green baseline.

## 3. Requirements

Ask in one message, everything at once, skipping what the scan already answered:

- **Scope** — does / doesn't do, acceptance criteria, non-goals
- **Seams** — the public boundaries this feature exposes. Name each one. Tests live at seams and nowhere else; that is what keeps the suite from sprawling into every edge case.
- **Data** — input/output shapes with example values, API contracts, existing structures touched
- **Edges** — invalid input, failure modes, races, retry/fallback
- **Integration** — interface changes, new dependencies
- **Constraints** — latency/memory/platform, auth/permissions/sanitisation

Done when every seam is confirmed by the user and every acceptance criterion is answered.

## 4. Branch

Propose `feature/<short-kebab-description>`, then create it from the up-to-date base branch.

## 5. Phased Plan

Distinct phases, real file paths from the scan, one risk tag each:

- `isolated` — new code, nothing else depends on it
- `shared` — touches logic other modules use
- `public` — changes a public interface or shared state

```
Phase N: <title> [isolated|shared|public]
  Seam: <the seam its tests drive>
  Files: <paths>
  Depends on: <phases/modules>
  Commit: "feat(<scope>): <description>"
```

Done when the user has approved the plan.

## 6. Tracer Bullets — per phase

Each test is a tracer bullet: one vertical slice through one seam to green, then aim the next one by what this one revealed. Write tests one at a time, never a batch up front.

**Red** — one test at one seam. Name it as a capability in domain language ("user can checkout with valid cart"). Drive it through the public interface and assert only behaviour observable at the seam. Write expected values as literal examples, so the test fails when the logic is wrong. Run it and show it failing for the right reason.

**Green** — write only the code this test demands, in project conventions. Run it and show it passing.

**Refactor** — clarity, naming, duplication, with the suite green after each change. `public` phases: check every caller and confirm interface compatibility.

Repeat Red → Green → Refactor until the phase's seam covers its acceptance criteria.

**Commit** — stage the phase's files and commit with its planned message. Prefixes: `feat` `fix` `refactor` `test` `chore`. `shared` and `public` phases also get a body: why this approach, alternatives considered, known gaps.

**Report** — `✅ Phase N done — <what changed>. Remaining: X, Y, Z.`

Done when the full suite is green and the phase is one commit. One phase = one commit, so the history stays bisectable.

## 7. Wrap-Up

```bash
git diff <base>... --unified=0 | grep -E '^\+.*(TODO|FIXME|HACK|XXX)'
git log <base>..HEAD --oneline
```

Resolve each new TODO or track it deliberately. Draft the PR: what & why, key decisions, phases, testing, known gaps. Show the next roadmap item.

Done when every new TODO is resolved or tracked and the PR draft is in front of the user.
