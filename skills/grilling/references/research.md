# Research behind the grilling rules

These rules come from the literature review for DemBot P9.17, a single-player 1:1 Socratic interview (DemAI-tech/dembot#511), ingested into Eike's second brain under `Sources/Research/` on 2026-11-06, and from the grill session that designed P9.17. The summaries below follow those source notes, including their caveats. Most of these studies concern political opinions or tasks with a correct answer, not plan or design decisions, so applying them to a grill is an inference.

## Ask without leading: preserve value choices and make expertise available

- **Jakesch, Bhat, Buschek, Zalmanson & Naaman (2023)**, "Co-Writing with Opinionated Language Models Affects Users' Views", *CHI '23*, doi:10.1145/3544548.3581196. N = 1,506 people wrote with an assistant slanted to one side. Both their writing and their later survey attitudes moved toward the model's side (d = 0.22 and d = 0.19). Most found the suggestions "balanced and reasonable", and only 10% of those whose view the model supported noticed the slant. The authors call this latent persuasion.
- **El-Sayed et al. (2024)**, "A Mechanism-Based Approach to Mitigating Harms from Persuasive Generative AI", arXiv:2404.15058 (Google DeepMind preprint, not peer-reviewed). Lists anchoring and defaults under "alteration of the choice environment", and sycophancy, flattery and mirroring of the user's views under the trust-and-rapport mechanisms of manipulation.
- **Enríquez, Pei & Pentland (2026)**, "Position: AI Should Facilitate Democratic Deliberation at Scale", *ICML 2026* (position paper). Its over-reliance safeguards include "multiple options rather than single recommendations that create anchoring effects" and making AI assistance optional, not the default. Its rule: "AI should inform and enable choices, not make them".

P9.17 settled this as "the participant writes first, the AI drafts only on request". For value choices, the grill normally hears the user's answer before offering a pick, and offers one only when asked. Technical judgement is different: a recommendation follows the user's direction, or comes directly when they don't know or ask for help. Recommendations are marked as the agent's view with their strongest material downside where one exists. Recording answers without praise is a design choice intended to reduce steering, not a demonstrated guarantee.

## Facts persuade: give those that cut each way together, with sources

- **Hackenburg et al. (2025)**, "The levers of political persuasion with conversational artificial intelligence", *Science* 390, eaea3884. N = 76,977, 19 models, 707 issues. Persuasion came mostly from post-training and prompting, not personalisation or scale. The most persuasive prompt was the "information" prompt, and information density explained 44% of the variance in persuasive effect. Where persuasiveness rose, factual accuracy fell. Conversation beat a static message by 41-52%.
- **Costello, Pennycook & Rand (2024)**, "Durably reducing conspiracy beliefs through dialogues with AI", *Science* 385, eadq1814. A three-round dialogue with counter-evidence tailored to the reasons a person had just given reduced belief by about 20%, and the effect held at two months. 99.2% of the sampled AI claims were rated true. Accurate sourcing did not limit the influence; it was the lever.
- **Lin et al. (2025)**, "Persuading voters using human-artificial intelligence dialogues", *Nature* 648, 394-401. AI advocacy dialogues moved candidate preference more than typical video ads, using relevant facts and evidence rather than psychological tricks, and not all of those facts were accurate.
- **Niemeyer, Veri, Dryzek & Bächtiger (2024)**, "How Deliberation Happens: Enabling Deliberative Reason", *APSR* 118(1). Across 19 forums, balanced information and presentations from different sides are named as the guard against one framing dominating.

Accurate facts can still influence a decision, and a citation makes a claim checkable rather than automatically correct. The practical rule is to present relevant competing evidence and uncertainty together, weighted by credibility and impact. This does not require equal airtime or a defence of a demonstrably incorrect option. Neither symmetry nor sourcing guarantees neutrality.

## Vary the probe rather than repeating justifications

- **Crawford & Ruscio (2021)**, "Asking People to Explain Complex Policies Does Not Increase Political Moderation", *Psychological Science* 32(4), 611-621, doi:10.1177/0956797620972367. Three preregistered replications (N = 1,054) of Fernbach et al. (2013). Explaining a policy mechanistically did lower people's self-rated understanding, but did not moderate their positions. What did replicate is the well-established finding that **providing justifications for prior beliefs strengthens those beliefs**. In Fernbach's original, listing reasons never moderated.

The grill varies its probes and avoids making the user repeat an already answered justification. A mechanism probe ("walk me through how that works") can expose gaps in understanding. A hard quota of one "why" per branch does not follow from these findings, nor do they show that every request for reasons entrenches a view.

## Perspective and counter-considerations, posed as questions

- **Goodin (2000)**, "Democratic Deliberation Within", *Philosophy & Public Affairs* 29(1), 81-109, and **Goodin & Niemeyer (2003)**, "When Does Deliberation Begin?", *Political Studies* 51(4), 627-649. Much of deliberation can happen within a person. In a citizens' jury, attitudes moved more in the information phase than in the discussion phase. The mechanism, imaginative rehearsal, weighing alternatives and role-taking, is known here only from secondary sources (Ralston 2010), and the jury is a single small case.
- **Cappella, Price & Nir (2002)**, "Argument Repertoire as a Reliable and Valid Measure of Opinion Quality", *Political Communication* 19(1), 73-93. Opinion quality includes both the reasons for one's own view and the reasons others with the opposite view might have.
- **Danry, Pataranutaporn, Mao & Maes (2023)**, "Don't Just Tell Me, Ask Me", *CHI '23*, doi:10.1145/3544548.3580672. N = 204. AI-framed questioning improved discernment of logically flawed statements more than no feedback, and more than causal explanations from an always-correct AI. The task has a right answer, and agency was not measured.

Perspective and counter-consideration questions are useful interview tools. Record material objections and the user's response or residual risk in the handoff. A known factual error should still be corrected directly; these studies do not imply that every correction must become a question.

## Probe unresolved risks; confidence alone decides neither scrutiny nor closure

- **Sharma et al. (2024)**, "Towards Understanding Sycophancy in Language Models", *ICLR 2024*, arXiv:2310.13548. Five assistants were consistently sycophantic across four tasks. Human preference data favours responses that match the user's views, sometimes over correct ones. The tasks are general assistant tasks, not dialogue about decisions.
- **Salvi, Horta Ribeiro, Gallotti & West (2025)**, "On the conversational persuasiveness of GPT-4", *Nature Human Behaviour* 9(8). With basic personal data, GPT-4 was more persuasive than humans 64.4% of the time. Tailoring to what the AI knows about the person raises influence. The setting was adversarial debate.

These findings motivate checking substantive counterarguments rather than agreeing by default. They do not establish that more confident users need harder challenges. The grill scales scrutiny by consequences, missing evidence and untested assumptions. A supported answer, explicit acceptance of a known residual risk, or a bounded experiment can close a branch. Uncertainty should be named and investigated when useful, not automatically treated as either failure or progress. The agent changes its assessment for a stated reason.

## Check back in the user's own words, with authorship visible

- **Birt, Scott, Cavers, Campbell & Walter (2016)**, "Member Checking: A Tool to Enhance Trustworthiness or Merely a Nod to Validation?", *Qualitative Health Research* 26(13), 1802-1811. Returning a summary for confirmation is weak validation. Synthesized Member Checking lets participants engage with and add to the interpretation, and what they add is itself data.
- Jakesch et al. (2023), above: people may not notice the slant of suggestions they accept. A visible record of agent additions and recommendations can help make authorship clearer, but is not a complete measure of influence.

An optional restatement can reveal misunderstandings when the user wants it. The default handoff records their choices and reasons, marks agent additions and choices following its recommendation, and flags material contradictions. An explicit stop or summary request ends questions immediately; it does not require a restatement or another confirmation. Member checking in qualitative research does not establish that mandatory restatement improves software planning.

## Workflow choices not established by the literature

The following adaptations support software and project decisions. They are practitioner choices, not findings established by the sources above.

- **Technical questions normally get advice after the user's direction.** Software decisions mix technical constraints with values. The agent explains constraints and recommends an approach while leaving priorities to the user; uncertainty or a request for help permits advice immediately. This preserves access to expertise without claiming to eliminate anchoring.
- **Reversibility and bounded completion.** Scrutiny follows actual consequences: deployment, migration cost, consumers and commitments, not a fixed list of "one-way" objects. Cheap decisions close on an answer; important ones may close on a reasoned answer, explicit acceptance of residual risk, or an experiment with a success criterion. Completion concerns material decisions within the user's scope, with deferred items recorded honestly. Bounded research, reuse of findings, optional check-back and a project handoff with observable acceptance criteria are workflow heuristics, not experimentally validated rules.

## Observed in the P9.17 grill session

- One question per turn kept answers fast. With a recommendation attached, Eike still picked against it at least four times (Q6, Q7, Q9, Q14). But the agreeing answers may have been anchored, and Jakesch suggests nobody would have noticed.
- Facts looked up mid-grill reshaped later questions: an existing issue turned "how do we build X?" into "is the existing issue the anchor?".
- Several of the best decisions were Eike's own variants, not any of the listed options.
- A closing summary table, checked before acting, caught misunderstandings.
