# Thesis Visual and Reference Review - Working Draft v9

## Scope

This revision reviewed the complete working thesis for figure placement, visual planning, citation placement, bibliography consistency, and final PDF layout. Existing prose was retained where no change was necessary.

## Visual planning completed

- Added **35 visible figure placeholders** across Chapters 1-10.
- Each placeholder records:
  - the intended visual type;
  - the purpose of the figure;
  - the evidence, source material, screenshots, logs, or datasets required to produce it;
  - a stable LaTeX label and draft caption.
- Added a natural in-text cross-reference for every planned figure.
- Added a full figure register and a visual style guide under `notes/`.
- Added short running chapter headers to prevent long chapter titles from colliding with page numbers.

## Citation and bibliography review completed

- Bibliography records: **103**.
- Records currently cited in the thesis: **96**.
- Missing citation keys: **0**.
- Unused records intentionally retained for final review: **7**.
- Converted four arXiv-only records from `@article` to `@online` to match their current publication status and remove Biber data-model warnings.
- Strengthened citations around load-bearing claims in Chapters 1, 3, 5, 6, 7, 8, and 9.
- Checked that citations are normally placed immediately after the proposition they support rather than collected ambiguously at paragraph endings.
- Validated the BibLaTeX data model with Biber.

## Technical validation

- Compiled with pdfLaTeX and Biber.
- Final PDF: **236 A4 pages**.
- No undefined citations or cross-references.
- No LaTeX errors.
- No overfull boxes reported in the final compilation log.
- PDF is openable, unencrypted, text-based, and passed preflight.
- All pages were rendered at low resolution and reviewed through contact sheets; representative figure-heavy pages were also inspected at higher resolution.

## What remains

- Replace each orange planning box with a final vector diagram, result plot, approved screenshot, or documented photograph.
- Generate quantitative plots only from frozen, archived, machine-readable experiment outputs.
- Confirm final architecture diagrams against the as-built repositories and deployment records.
- Confirm permissions, anonymisation, and resolution for operational screenshots and photographs.
- Complete a final publisher-level audit of DOI, venue, year, author order, and preprint/published status.
- Decide whether the seven currently unused bibliography records remain useful.
- Re-run the final visual and citation audit after the quantitative results and final figures are inserted.
