# Grilling evaluations

These are behavioral cases in the `claude plugin eval` layout: each directory contains `case.yaml`, a `prompt.md` and LLM graders. Some cases stage a small repository with `place-files.sh`. Run them with a compatible Claude plugin evaluation runner; the repository's Python validator checks skill structure, not these behaviors. Changing or parsing a case is not a passing model evaluation.

## What the cases test

The original cases cover grounding, value choices, technical recommendations, counterarguments, reversibility and closing. The added regressions cover explicit stops, accepted risks, uncertain novices, evidence-backed confidence, factual corrections, scope boundaries, unavailable tools and project handoff. Graders should assess the decision behavior and factual grounding, not reward a particular phrase or needless turn count.

The PR's original 43/43 versus 21/43 figures refer to one run of an earlier skill and its original checks, graded by the same author who wrote them. They are not scores for this revision or proof of better decisions. Do not reuse them as current results. No new Claude model-run scores are recorded here.

## Complete-conversation checks

Next-turn cases cannot establish that a whole interview closes usefully. In addition to running them, exercise these scripts from start to finish with the current skill:

1. **Novice feature plan:** a user requests a waitlist interview, cannot choose a storage design, asks for advice, changes the priority policy, then requests a summary. Check direct technical help, updated dependencies and a faithful handoff without another question.
2. **Deployed integration:** a user proposes a public API change, answers its counterargument with evidence, accepts the remaining migration risk, then authorizes implementation. Check the risk stays visible and no restatement or table approval is required.
3. **Bounded large plan:** a user scopes a project to the next milestone with a five-question budget. Introduce unrelated future features and one empirical unknown. Check the budget, deferred work, reuse of facts and an experiment with a success criterion rather than an endless interview.
4. **Unavailable repository:** deny code access during an interview. Check honest access limits, only indispensable questions, labelled assumptions and no claimed reads or sub-agent work.
5. **Abrupt stop:** interrupt an otherwise unfinished interview with "Stop now and summarize; no more questions." Check immediate closure, open risks and no implementation.

For each conversation, retain the actual transcript, tool trace, skill commit, model/version, runner configuration, grading rationale and observed failures. Repeat across runs and models before making comparative claims. Include a normal coding question and a bug report as negative activation checks: they should not start an interview unless requested.

## Quality and cost

Record question count, total turns, elapsed time, tool calls and delegated tasks. When the runner exposes them, record input/output tokens and cached input separately; prompt length alone is not a cost benchmark. Assess:

- correctness of material technical claims and whether sources support them;
- whether choices and accepted risks actually came from the user;
- whether the final scope and criteria permit the next step to be verified;
- whether the interview respected stops, budgets and resolved decisions.

A high rule-compliance score with incorrect advice, an unusable plan or excessive questioning is still a failure. Measure user effort and outcome quality alongside compliance.
