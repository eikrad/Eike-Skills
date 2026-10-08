---
name: cv-coverletter-evaluator
description: "Human Test evaluation of a CV, cover letter or full application, delivered as a prioritized report. Use when the user wants an application reviewed, critiqued, scored or improved; asks whether it fits the Danish market or carries AI tells; or when job-application finishes step 7 (pre-send)."
---

# CV & Cover Letter Evaluator

The reader is a human being at a specific Danish company. Parsers, keyword coverage and formatting conventions count only as far as they serve that reader.

## The Human Test

Apply it to every recommendation: **after the change, would a human reader at this company understand the document better, believe it more, or want to meet this person more?**

- Passes → prioritize normally.
- Only a machine benefits → **[Polish]** at most, and say so in the item.
- Helps a parser at the human reader's expense → drop it.

Recommend only words the candidate would say out loud in an interview.

## Weighting

Governs the rating and the recommendation order.

| Lens | Weight | May produce Critical? |
|---|---|---|
| A — Hiring manager (comprehension & persuasion) | 40 % | Yes |
| B — Danish job market | 35 % | Yes |
| C — Language & AI-tells | 15 % | Only for errors a native reader would notice |
| ATS parsing gate | 10 % | Only if the document genuinely fails to parse |

**Catalog and argument:** the CV is the catalog; the cover letter is the argument for *this* role. Lenses A, B and the cross-cutting checks all judge against this split.

## Inputs

- **Documents (at least one):** CV and/or cover letter as `.pdf`, `.tex`, `.md`, `.txt`, pasted text or URL. With one document, evaluate it and name the missing one in the report.
- **Mixed paste:** segment by content — bullet-heavy reverse-chronological → CV; flowing paragraphs addressed to a person → cover letter; "We are looking for" / "Ansvarsområder" → job posting. Ask one focused question only when the split stays ambiguous.
- **Job posting (optional):** anchor the evaluation to it, reading it for **the company's own vocabulary and priorities**.
- **Missing context:** evaluate generically and note where role context would sharpen a finding.

**In the Awesome-eik repo** (files the user hands over directly take precedence):

| Input | Location |
|---|---|
| CV | `examples/Rades_CV_<Company>_<Language>.tex` (or compiled `.pdf`) on the current company branch |
| Cover letter | `examples/Rades_CoverLetter_<Company>_<Language>.tex` |
| Posting | `jobdescription.txt` |
| Formatting & content rules | `application_checklist.md` — each violation is a finding |
| Fixed wordings & Evidence floor | `.claude/skills/job-application/references/claim-wording.md` — each violation is an A finding |
| Facts | `candidate_profile_extended.md` — grep it; it is large |

`employment_history.tex` and `education.tex` are stable files the job-application skill keeps off company branches; recommend changes to them as **[Note]**.

## Workflow

Read every input before writing any finding. Run A, B and C as separate lenses — each catches what the others miss — and merge them only at step 8.

### 1. Read

Read all inputs. Record, per document, its language (Danish or English); from the posting, the sector (offentlig/privat) and company size.

**Done when:** every document is classified as CV, cover letter or posting, each has a language, and sector is set (or "unknown").

### 2. Colleague Test

Close the documents. From memory, write two plain sentences you would say to a colleague in the corridor: *what this person does, and why they might be right for this role.* Plain words, yours.

**Done when:** both sentences exist and share no distinctive phrase with the documents. A shared phrase means you read the document back — rewrite. If the sentences only come after re-reading, that is the **headline finding of the whole report**: the application is not legible to a human.

### 3. Perspective A — Hiring manager (40 %)

Read as a busy hiring manager **at this company**: 30 seconds for the cover letter, 60 for the CV, then decide interview / pass / maybe.

**Comprehension:**

- **Jargon audit:** list every acronym, tool, internal project name, methodology or job title this hiring manager would not decode in one second. Foreign, sector-specific and internal-ladder titles count ("Senior Referent" or "Fachbereichsleiter" mean nothing in a Danish org chart); translate them to what the role actually was.
- **So-what test:** ask of each bullet "and what changed because of that?" A task with no outcome fails.
- **Ownership test:** can the reader tell the candidate did it? A bullet describing a system ("Agents: systems that plan a task …") leaves open whether the candidate built, used or read about it. Rewrite to open on a verb with the candidate as subject ("built", "measured", "led"). Added after a reader caught such bullets on the general CV (2026-10-07) that had passed the other tests.
- **Repo-inventory test:** strip every tool, model and library name from a bullet. If a list of components remains instead of a problem and a result, the bullet inventories a repository. A technical reader can decode every term and still not know what was built or why it mattered. Rewrite led by the problem; assume the reader skips repo links (some repos are private).
- **Vocabulary mirroring:** where true experience is described in words the company does not use, recommend the same true claim in *their* words — translation for a human reader, claim unchanged.
- **Domain translation:** when changing field, sector or country, the bridge must be explicit and the pivot motivated in one clear sentence.

**Persuasion:**

- Does the opening sentence pull the reader on, or could it describe anyone?
- Within 5 seconds of the CV, are role and level clear?
- What does this person bring that the next applicant lacks?
- Which claims sound inflated or unverifiable?
- Which two questions would you ask in the interview? Basic clarifications of *what he actually did* signal a comprehension problem, not an interview hook.
- Would you want to meet this person? One honest sentence.

**Done when:** every CV bullet and every letter paragraph has been through the so-what, ownership and repo-inventory tests, failures quoted with a rewrite; the jargon list is complete; the two interview questions are written; 6–10 findings.

### 4. Perspective B — Danish job market (35 %)

Read `references/danish_market.md` now and apply every section of it — language fit, the ansøgning, the CV, tone, sector, opportunity check.

**Done when:** each section of that file has yielded a finding or an explicit pass; 6–10 findings.

### 5. Perspective C — Language & AI-tells (15 %)

Read `references/ai_tells.md` now and apply it: mechanics, second-language tells, then the AI-tell count per document.

**Done when:** every spelling or grammar error is quoted with its correction (including spelling variants such as on-premise/on-premises), contact details, phone format and date format are compared between CV and letter and each mismatch is quoted, each document carries an AI-tell count and its tier from the file, and 4–8 findings quote the text.

### 6. Cross-cutting checks

**Consistency CV ↔ cover letter**

- Dates, titles and employer names match exactly.
- Every letter claim has a CV entry behind it ("led a team of 8" → the CV shows it).
- Tone and register match.
- The letter argues *why this role* from the most relevant CV items. A project restated at paragraph length (stack, test counts, repo tour) is a catalog dump; proof fits in one clause.
- Count the proofs in the letter's offer section: a semicolon list of three past systems is three proofs. More than two is a finding.

**Claims & evidence check (Awesome-eik repo)** — judged against the source of truth, since a document can read well and still be wrong or leave out its best material.

- **Claims:** for each quantified, ownership or qualifier claim ("built", "operate", "production", "daily", "validated", "checked against the source"), grep `candidate_profile_extended.md` and `claim-wording.md`. Unsupported → A finding, "remove or verify". Contradicts `claim-wording.md` → Critical (A).
- **Evidence left on the table:** name the three strongest posting-relevant facts in the profile (user counts, before/after results, employer-anchored outcomes; start from the Evidence floor in `claim-wording.md`). Each one the CV omits → A finding with a rewrite. Test counts and repo sizes are inventory, not outcomes.
- **Shape claims:** before writing that the letter "has" an element (availability, personal paragraph, call to action), quote the sentence that shows it. No quote → it is missing.

**Red flags & quantification**

- **Gaps:** each gap over 4 months; if the letter leaves it unaddressed, recommend a one-line framing.
- **Frequent moves:** several jobs under 12 months each — worth pre-empting.
- **Quantification:** per role, count bullets carrying a number (people, %, currency, time, scale); target 1–2 per role, flag roles at zero. Numbers make a claim checkable for the human reader, so these are A findings.
- **Vague verbs:** "responsible for", "involved in", "helped with", "assisted in" → "led", "shipped", "owned", "delivered", "reduced X by Y%".

**Done when:** each of the three subsections has findings or "No issues identified", and every quantified, ownership and qualifier claim has been grepped, covering each Employment, Mentoring and Volunteer bullet ("trained", "led", "managed" count as ownership claims); a claim without a profile hit is quoted as "remove or verify".

### 7. ATS gate (last)

A hygiene gate: it confirms the documents parse, nothing more. Read `references/ats_check.md` and apply its fail conditions, pass-with-notes conditions and vocabulary budget.

**Done when:** the verdict is Pass / Pass with notes / Fail with at most three lines, plus at most 5 vocabulary-mirroring items.

### 8. Human Test and report

Run the Human Test on every candidate recommendation, then fill the report template below.

**Done when:** every heading in the template is present (empty ones read "No issues identified."); every finding from A, B, C and the cross-cutting checks appears in Recommendations; every recommendation carries a priority and a lens tag; the priority rules hold.

### 9. Deliver

- **In the Awesome-eik repo:** save to `examples/evaluation_<Company>_<YYYY-MM-DD>.md` on the current branch — exactly this name, so reports are findable across branches. Print the path.
- **Elsewhere:** render the full report in chat.

Open the chat reply with the Colleague Test result, the headline finding and the rating in 2–3 sentences, then point to the file or the report below.

**Done when:** the file exists at that path (or the report is in chat) and the reply opens with those three items.

## Report template

```
# CV & Cover Letter Evaluation — [Candidate Name] / [Target Role or "Generic"]

**Date:** YYYY-MM-DD
**Documents reviewed:** [list]
**Job posting:** [filename / "Not provided"]
**Languages detected:** [CV: DA/EN, Cover letter: DA/EN]
**Sector:** [offentlig / privat / unknown]

## The Colleague Test
The two plain sentences, verbatim, written from memory.
Then one line: did this work, or did the document have to be re-read?

## Executive summary
2–4 sentences. Lead with the headline finding.

## Success-potential rating
Strong / Solid / Mixed / Weak — one sentence justification.
Weighted: hiring manager 40 %, Danish market 35 %, language 15 %, ATS 10 %.
If a job posting was provided: fit score (e.g. "7/10") with reasoning.

## Pros — what's working
4–8 specific bullets.

## Cons — what's holding it back
4–8 specific bullets.

## Perspective A — Hiring manager (40 %)
6–10 bullets. Include the jargon/acronym list and the two interview questions.

## Perspective B — Danish job market (35 %)
6–10 bullets.

## Perspective C — Language & AI-tells (15 %)
4–8 bullets with quoted text.

## Cross-cutting checks
### Consistency CV ↔ Cover letter
### Claims & evidence check
### Red flags & quantification

## ATS gate
Pass / Pass with notes / Fail — plus at most three lines, and the vocabulary-mirroring items if any.

## Recommendations — complete and prioritized
Every actionable fix from Cons, Perspectives A–C and Cross-cutting checks.

Format each item as:
`N. **[Critical|Important|Polish]** (A/B/C/ATS) …` — what to change, why, concrete rewrite where possible.
Observational items (no edit) are marked **[Note]**.

Order: Critical → Important → Polish → Note; within a priority, A → B → C → ATS.

## Brainstorming kickoff
3–5 open questions that surface material the candidate has not yet put on the page.
End by inviting the user to pick one or two to dig into next.
```

### Priority rules

- **Critical** comes only from Perspective A or B, or a genuine ATS parse failure.
- Tag every recommendation with its lens (A/B/C/ATS) so the balance shows at a glance.
- ATS-tagged items stay at or below a quarter of the list; above that, the evaluation has drifted — re-run the Human Test on each and demote or drop.
- The list is complete: harvest it from the whole report, and shorten it to a "top N" only when the user asks for a shortlist.
- An item that needs evidence the candidate may lack stays on the list as "skip unless X is true."

## Voice

- Address the candidate as "you", including the Colleague Test and "would I meet you?".
- Every finding is specific and quotes the text it flags: located and actionable, like "Bullet 3 in role 2 has no number".
- AI use itself is neutral; the finding is a concentration of tells.
- The evaluation is the deliverable; a full rewrite is a separate request.

## Implementing recommendations

When the user asks to implement:

1. Implement the **full** list, skipping only items marked impossible without inventing experience.
2. Place [Polish] and ATS items in bullets or skills lines; the CV profile and the letter's opening stay reserved for A and B material.
3. Ask the user about items that need their decision before committing.
4. **Re-run the Colleague Test** on the edited documents. If the two sentences are harder to write than before, the edits hurt the human reader — revert the offending changes and name them.
5. Append a dated section to the report with the implementation status and the re-run Colleague Test, so the next review sees what changed.

**Done when:** every list item is implemented, skipped with a reason, or answered by the user, and the dated section is in the report.
