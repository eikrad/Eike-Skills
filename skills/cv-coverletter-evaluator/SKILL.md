name: cv-coverletter-evaluator
description: "Evaluate a CV and/or cover letter from three weighted perspectives — hiring manager (can a human at this company understand it?), Danish job-market expert, language/AI-tells reviewer — with ATS treated only as a parsing gate, never an optimization target. Delivers a structured Markdown report with pros, cons, prioritized recommendations, a success-potential rating, and a brainstorming kickoff. Trigger when the user asks to review, critique, evaluate, score, or improve a CV, resume, cover letter, or full application — or shares one and asks 'is this any good?', 'fit for the Danish market?', 'any AI tells?'"
CV & Cover Letter Evaluator
The stakes are real: a good evaluation can change an outcome. Take the work seriously.
The document is written for a human being at a specific Danish company. Everything else — parsers,
keyword coverage, formatting conventions — serves that reader or it does not matter.
Weighting (governs the rating and the recommendation order)
Lens
Weight
May produce Critical?
A — Hiring manager (comprehension & persuasion)
40 %
Yes
B — Danish job market
35 %
Yes
C — Language & AI-tells
15 %
Only for errors a native reader would notice
ATS parsing gate
10 %
Only if the document genuinely fails to parse
The Human Test (hard rule)
Every single recommendation must pass this: would a human reader at this company understand the document
better, believe it more, or want to meet this person more, after the change?
Passes → prioritize normally.
Only a machine benefits → maximum priority [Polish], and say so explicitly in the item.
Makes the document worse for a human but better for a parser → do not recommend it at all.
Never recommend adding a word the candidate would not say out loud in an interview.
Integration with job-application skill
Default trigger: Run automatically after job-application step 7 (pre-send checklist), unless the user explicitly skips review.
When running in the Awesome-eik repo:
Find CV source at examples/Rades_CV_<Company>_<Language>.tex (or compiled .pdf) on the current company branch
Find cover letter at examples/Rades_CoverLetter_<Company>_<Language>.tex
Use jobdescription.txt as the job posting
Use application_checklist.md as the formatting and content rules reference — flag violations
If the user provides files or pasted text directly, use those instead.
Inputs
Required (at least one): CV and/or cover letter — as files (.pdf, .tex, .md, .txt), pasted text, or a URL. If only one document is provided, evaluate what's there and note what's missing.
If the user pastes a mixed blob, segment by content: bullet-heavy reverse-chronological → CV; flowing paragraphs addressed to a person → cover letter; "We are looking for" / "Ansvarsområder" → job posting. Ask one focused question only if genuinely ambiguous.
Optional: Job posting (file, pasted text, or jobdescription.txt). If present, anchor the evaluation to it — and use it primarily to learn the company's own vocabulary and priorities, not to build a keyword list.
Workflow
Read everything before writing anything.
Read all inputs. Detect language per document (Danish or English). Note sector (offentlig/privat) and company size from the posting.
Run Perspective A, then B, then C — independently. Do not blend findings until synthesis.
Run cross-cutting checks.
Run the ATS gate last, as a pass/fail hygiene check only.
Apply the Human Test to every candidate recommendation; drop or demote failures.
Synthesize into the report.
Save or present the report (see Output below).
1. Three perspectives
Run each independently. The value is that different lenses catch different things.
Perspective A — Hiring manager (weight 40 %)
Read as a busy hiring manager at this specific company: 30 seconds for the cover letter, 60 for the CV, then decide interview / pass / maybe.
Start with the Colleague Test — do this before anything else, and do it from memory:
Close the documents. Write two plain sentences you would say to a colleague in the corridor: what this
person does, and why they might be right for this role. No jargon, no borrowed phrasing from the CV.
If you cannot write those two sentences without going back to the document, that is the headline
finding of the entire report — the application is not legible to a human.
Put those two sentences verbatim in the report. They show the candidate what actually landed.
Then check comprehension in detail:
Jargon & acronym audit: list every acronym, tool, internal project name, methodology, or job title that
a hiring manager at this company would not decode in one second. Each one is a finding. Titles from
another country, sector, or company's internal ladder count — "Senior Referent" or "Fachbereichsleiter"
means nothing in a Danish org chart; translate to what the role actually was.
The so-what test: for each bullet, ask "and what changed because of that?" A bullet that names a task
but not an outcome fails. Quote the failing bullets.
Vocabulary mirroring (human version): where the candidate's true experience is described in words the
target company does not use, recommend saying the same true thing in their words. This is translation
for a human reader, not keyword insertion — the underlying claim must be unchanged and still true.
Domain translation: if changing field, sector, or country, is the bridge made explicit? A reader will
not build it for you. Is the pivot motivated in one clear sentence?
Then judge persuasion:
Does the opening sentence make me want to keep reading, or could it have been written about anyone?
In the first 5 seconds of the CV, can I tell what this person does and what level they're at?
Is there a clear value proposition — what does this person bring that the next applicant doesn't?
Are claims credible, or inflated? Is anything unverifiable-sounding?
What two questions would I want to ask in an interview? (If they are basic clarifications about what he
actually did, the document has a comprehension problem, not an interview hook.)
Would I want to meet this person? Why or why not — in one honest sentence.
Write 6–10 specific bullet findings.
Perspective B — Danish job-market expert (weight 35 %)
Judge the application as a Danish recruiter or leader would, not as a US career blog would.
Reality check first: in Denmark the ansøgning is read by a person, usually early and usually
carefully — often before the CV. Many employers, especially SMEs and the public sector, use light
recruitment systems (HR-ON, Emply/Talentech) or plain email; aggressive US-style keyword filtering is the
exception, not the rule. Never trade human readability for parser coverage in this market.
Language fit (highest-signal item in this section):
Posting in Danish → apply in Danish. Applying in English to a Danish-language posting is a major negative
signal unless the posting invites English. Flag it as Critical.
If Danish is not fluent: state the level factually and concretely ("Dansk på B1, i gang med Modul 4"),
never hide or inflate it. Silence reads worse than an honest level.
Non-EU candidates: one short factual line on right to work. EU/EEA: no mention needed.
The ansøgning (cover letter):
Max 1 page, roughly 2,500–3,000 characters. Flag bloat hard.
Expected shape: hook / why this company → fagligt (what you can do, with evidence) → personligt
(who you are as a colleague) → close with availability and an invitation to talk.
The personligt paragraph is expected and is read seriously — flag if missing, and flag if it is generic
("I am a team player who loves challenges").
Salutation: "Kære [Navn]" when known; "Kære rekrutteringsansvarlig" if not. Sign-off: "Med venlig hilsen".
Danish workplaces are on first-name, du-form terms — no German-style formality or title stacking.
Closing conventions: start date / notice period ("Jeg kan tiltræde den 1. [måned]" or the opsigelsesvarsel)
and a call to action ("Jeg står gerne til rådighed for en uddybende samtale").
Contact person: Danish postings almost always name one and invite a call. If the candidate has not
called, note it as a concrete opportunity — and if they have, the letter should reference it.
The CV:
1–2 pages. Structure: kort profil (3–5 lines) → erfaring (reverse chronological) → uddannelse →
kompetencer → sprog (with CEFR levels) → IT → fritidsinteresser. Flag missing or out-of-order sections.
Photo and date of birth are still common in DK, unlike US/UK. Note presence/absence neutrally, never as an error.
Fritidsinteresser and frivilligt arbejde are not filler in Denmark — foreningsliv and volunteering read
as genuine personality and reliability signals. Flag if absent or reduced to a bare word list.
Referencer: "Referencer oplyses gerne på forespørgsel" is standard; listing names is not expected.
Gaps: parental leave (barsel), study, and deliberate breaks are read pragmatically. Name them plainly
rather than concealing them.
Tone calibration:
Flat hierarchy, directness, understatement. The candidate presents as a future colleague, not a superstar.
Flag American-style superlatives ("world-class", "rockstar", "passionate game-changer", "proven track
record of excellence") — in DK they reduce credibility rather than raise it.
Slightly understated confidence backed by concrete evidence beats loud confidence. Collaboration and
initiative ("jeg tog fat", "vi fik") land better than lone-hero framing.
Sector: offentlig (kommune/region/stat) → more formal, addresses the posting's kvalifikationskrav
fairly directly, frames impact on citizens/society, expects structure. Privat → shorter, business
outcomes, more room for personality.
Opportunity check: if the fit is weak through the formal channel, note whether an uopfordret ansøgning
or a network/LinkedIn route would materially raise the odds — a large share of Danish positions are filled
that way.
Write 6–10 specific bullet findings.
Perspective C — Language & AI-tells (weight 15 %)
Mechanics: spelling errors (quote the wrong word + correction), grammar, punctuation, capitalization (Danish capitalizes nouns far less than German — a frequent German-speaker error), date/number formatting consistency (DK: 01.03.2024 or 1. marts 2024; comma as decimal separator).
Danish-as-a-second-language tells: German or English sentence structure carried into Danish, false
friends, verb-second violations, over-long subordinate clauses. Flag these separately from AI-tells — they
have a different fix.
AI-tells — flag concentration, not isolated cases:
Em dashes used stylistically and repeatedly (— like this —)
"Not just X, but Y" rhetorical patterns; tricolons
Words/phrases: "leverage", "navigate", "ensure", "passionate", "delve", "robust", "comprehensive", "tapestry", "bridge the gap", "synergy", "in today's fast-paced world"
Generic openers: "I am writing to express my interest in…"
Overly perfect parallel bullet structures
Hedge + abstract claim combinations: "various", "numerous", "a range of" instead of specifics
Write 4–8 findings with quoted text where applicable.
2. Cross-cutting checks
Consistency: CV ↔ Cover letter
Dates, titles, and employer names match exactly
Cover letter claims are backed by CV entries ("led a team of 8" → CV reflects it)
Tone and register match
Cover letter curates the most relevant CV experiences and explains why this role — the CV is the catalog, the cover letter is the argument
Red flags & quantification
Employment gaps: note any gap > 4 months. If the cover letter doesn't address it, recommend a one-line framing.
Frequent moves: multiple jobs each < 12 months — worth pre-empting.
Quantification: for each role, count bullets with a number (people, %, currency, time, scale). Goal: at least 1–2 per role. Flag roles with zero. Numbers serve the human reader — they make a claim checkable — so this is an A-weighted finding, not a formatting one.
Vague verbs: "responsible for", "involved in", "helped with", "assisted in" — suggest stronger replacements ("led", "shipped", "owned", "delivered", "reduced X by Y%").
3. ATS gate (run last, weight 10 %)
This is a hygiene gate, not an optimization target. Its only job is to confirm the document survives
being opened and parsed. Report it as Pass / Pass with notes / Fail plus at most three lines.
Fail conditions (these — and only these — may be Critical):
Text stored as an image, or a scanned/non-text PDF
A multi-column layout where the main content column would be interleaved on extraction
Contact details only inside a header/footer graphic
A file format the employer's system cannot accept
Pass-with-notes conditions (maximum priority [Polish]):
Non-standard section headings — Danish or English standard names are fine ("Erfaring"/"Experience", "Uddannelse"/"Education", "Kompetencer"/"Skills")
Inconsistent date formats
Decorative icons or glyphs standing in for labels
Vocabulary coverage — budget for this gate only:
If a job posting was provided, identify at most three central terms the posting uses for things the
candidate has genuinely done, and that the CV currently describes in different words. Recommend rewording
those, and only those. This budget limits what this gate may contribute — it is not a cap on the
report's total recommendations, which are never truncated. Each such item must:
describe experience the candidate actually has — never invent or stretch;
be phrased as a rewrite of an existing line, not an addition;
read naturally to a human and pass the Human Test;
be marked [Polish] unless the term is also central to how the hiring manager thinks about the role, in
which case it belongs in Perspective A instead.
Never recommend a keyword list, a skills-cloud, white text, keyword density, or repeating a term to
raise a match rate. If the candidate has not done the thing, the answer is "this posting may not fit", not
"add the word".
4. Report
Produce one Markdown report with exactly this structure. If a section has nothing to flag, write "No issues identified." — do not drop the heading.
Code
Priority rules (mandatory)
Critical is reserved for items from Perspective A or B, or a genuine ATS parse failure. Nothing else.
Tag every recommendation with its source lens (A/B/C/ATS) so the balance is visible at a glance.
If more than a quarter of the recommendations carry the ATS tag, the evaluation has drifted — re-check
each against the Human Test and demote or drop.
Harvest recommendations from the whole report, not only a shortlist. Never truncate the list to a
fixed-length shortlist unless the user asks for one. The three-item budget in the ATS gate limits that
gate's own contribution and nothing else — it never justifies shortening this list.
If an item cannot be implemented honestly (missing evidence), still list it and say "skip unless X is true."
Output
In the Awesome-eik repo: save report as examples/evaluation_<Company>_<YYYY-MM-DD>.md on the current branch. Print the path.
Otherwise: render the full report inline in chat.
Either way: lead the conversational response with the Colleague Test result, the headline finding and the success-potential rating in 2–3 sentences, then point to the file or note the report is below.
Rules
Write to the candidate in second person ("you"), not about them.
Be direct and specific. "Bullet 3 in role 2 has no number" is useful. "Add more numbers" is not.
Quote actual text when flagging something — vague feedback can't be acted on.
Don't rewrite the entire CV unless asked. Evaluation first; rewrites are a separate request.
Don't moralize about AI use — flag concentration of tells, not isolated cases.
Don't refuse to evaluate due to missing context — evaluate generically and note where role context would help.
When the user asks to implement recommendations, implement the full recommendations list (skip only items marked impossible without inventing experience). After implementing, re-run the Colleague Test on the edited document. If the two sentences are now harder to write than before, the edits made it worse for a human — revert the offending changes and report which ones.