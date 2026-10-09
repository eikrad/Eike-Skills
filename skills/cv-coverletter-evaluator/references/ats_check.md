# ATS gate

A hygiene gate: its one job is to confirm the documents survive being opened and parsed. Report **Pass / Pass with notes / Fail** plus at most three lines. Every ATS recommendation also passes the Human Test.

## Fail — the only ATS items that may be Critical

- Text stored as an image, or a scanned/non-text PDF. Test: select and copy text from the PDF.
- A multi-column layout whose main column interleaves on extraction.
- Contact details only inside a header/footer graphic.
- A file format the employer's system cannot accept. Submit the rendered PDF (DOCX also works); LaTeX source is a working file.

**awesome-cv and similar LaTeX templates:** copy-paste the rendered PDF and confirm the text comes out clean and in order — glyphs can embed as paths, and sidebars or timelines can scramble extraction. If it fails, suggest a plainer template for this application.

## Pass with notes — [Polish] at most

**Section headings:** standard Danish or English names.

| English | Danish | Non-standard (note) |
|---|---|---|
| Experience / Work Experience | Erfaring / Erhvervserfaring | "Where I've been", "My journey" |
| Education | Uddannelse | "Schools" |
| Skills | Kompetencer / Færdigheder | "What I do well" |
| Certifications | Certifikater | "Wall of fame" |
| Languages | Sprog | — |
| Summary / Profile | Profil / Kort om mig | "About me" is fine |

**Dates:** one format throughout (`2022–Present`, `Jan 2020 – Dec 2022`, `jan. 2020 – dec. 2022`), with plain hyphens or en dashes.

**Glyphs:** decorative icons standing in for labels.

**Contact block:** full name, phone with +45, plain-text email, city, LinkedIn URL. A photo sits outside the parsing-critical area (top right is typical).

**Filename:** `Firstname_Lastname_CV_Company.pdf` pattern — underscores, plain ASCII (the repo's `Rades_CV_<Company>_<Language>.pdf` fits).

**Cover letter:** plain single-column body, address block at the top, all text as text.

## Vocabulary mirroring — budget of 5

With a posting, pick up to **5** central terms the posting uses for things the candidate has genuinely done and the CV describes in other words. Recommend rewording those five at most. Each item:

- describes experience the candidate actually has, at its true size;
- rewrites an existing line in place;
- reads naturally to a human and passes the Human Test;
- is **[Polish]** — unless the term is central to how the hiring manager thinks about the role, in which case it moves to Perspective A.

Every vocabulary item is a rewrite of a true line in the employer's words. When the candidate has not done the thing, the finding is "this posting may not fit" — keyword lists, skills clouds, hidden text and repeated terms stay out of the recommendations.
