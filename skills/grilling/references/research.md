# Research behind the grilling rules

These rules come from the literature review for the P9.17 single-player session (2026-11-06) and from what worked in that session's grill. Each section names the rule in `SKILL.md`, what the source found, and how the rule follows from it.

## Vary the probe; ask "why" at most once per branch

- **Fernbach, Rogers, Fox & Sloman (2013)**, *Psychological Science*: asking people to explain how a policy works moderated their positions, but asking them to list reasons for their position did not.
- **Crawford & Ruscio (2021)**, *Psychological Science*: three preregistered close replications found no moderation from explanation either.

So the "explain it" probe moves people less than expected, and the "justify it" probe doesn't move them at all. A repeated "why" mostly has the user rehearse their case. The grill mixes in consequence, perspective and counter-consideration probes, which put something new in front of the user rather than asking them to repeat what they hold.

## Put counter-considerations as questions

- **Danry, Pataranutaporn, Mao & Maes (2023)**, *CHI*: an AI that framed its explanation as a question ("if X, would Y follow?") improved people's accuracy at judging the logic of arguments more than an AI that stated the explanation outright.

## Push against the lean; hold positions under pushback

- **Sharma et al. (2024)**, *ICLR*, "Towards Understanding Sycophancy in Language Models": RLHF-trained assistants tailor answers to the user's stated views, give up correct answers when challenged, and human preference data rewards this.

Without a counterweight, the grill drifts toward the user's view. Aiming the probe against the lean, closing a branch on its answered counter-consideration rather than on the user's confidence, and changing position only for a named reason are that counterweight.

## Recommend only on fact-shaped questions

- **Jakesch, Bhat, Buschek, Zalmanson & Naaman (2023)**, *CHI*, "Co-Writing with Opinionated Language Models Affects Users' Views": people who wrote with a model slanted toward one side shifted both their essays and their later survey answers toward that side, mostly without noticing.

A recommendation on a value question puts the model's slant into the user's decision. P9.17 resolved this as "the participant writes first, the AI drafts only on request". The grill keeps recommendations where they save time without carrying values (fact-shaped questions) and asks for the user's answer first everywhere else.

## Balance when raising an objection

When the grill raises an argument against an option, it also names the strongest argument for it. A one-sided objection steers as surely as a one-sided recommendation.

## Check back in the user's own words

- **Birt, Scott, Cavers, Campbell & Walter (2016)**, *Qualitative Health Research*, "Member Checking: A Tool to Enhance Trustworthiness or Merely a Nod to Validation?": handing participants a summary to approve yields little. Asking them to engage with a synthesis and add to it yields more.

So the check-back starts with the user's restatement, and the table is built from it.

## Observed in the P9.17 session

- One question per turn, with options and a recommendation, kept answers fast. Eike picked against the recommendation at least four times (Q6, Q7, Q9, Q14), so a recommendation doesn't prevent disagreement, but it may still have anchored the answers that agreed with it.
- Facts looked up mid-grill reshaped later questions: an existing issue turned "how do we build X?" into "is the existing issue the anchor?".
- Several of the best decisions were Eike's own variants rather than any of the listed options.
- A closing summary table, checked before acting, caught misunderstandings.
