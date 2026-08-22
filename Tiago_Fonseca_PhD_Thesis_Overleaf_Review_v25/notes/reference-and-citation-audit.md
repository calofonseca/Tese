# Reference and Citation Audit - Working Draft v10

## Actions completed in this revision

- Rechecked citation integrity after the v10 structural consolidation and section merges; no citation key or cross-reference was lost.

- Verified that every citation key used in the chapter sources exists in `bibliography/references.bib`.
- Reviewed citation placement around the new architecture, algorithm, TI-MARL, lifecycle, and evidence-level claims. Citations are placed after the supported proposition and before sentence punctuation.
- Added first-use or load-bearing citations where the prose previously relied on Chapter 2 without identifying representative primary/system evidence.
- Added citations to the author's prior EnergAIze, EVLearn, and real-world REC work where the thesis describes inherited or previously published components.
- Added the canonical Prioritized Experience Replay citation at the point where prioritized/event-aware replay is introduced.
- Changed four arXiv-only records from `@article` to `@online` (`schulman2017ppo`, `ackermann2019matd3`, `levine2020offline`, and `rusu2015distillation`) so that Biber does not require a nonexistent journal title.
- Preserved citations already used appropriately in Chapters 1 and 2; they were not moved or multiplied without a textual reason.

## Citation-placement rules used

1. Cite a source at the first substantive use of an external method, dataset, environment, system, or factual result.
2. Put the citation after the claim it supports, normally before the final punctuation.
3. Use primary papers or official system documentation for specific capabilities and results; use reviews for taxonomy or field-level synthesis.
4. Cite the author's own prior publications when text describes previously published methods, software, or evidence, while keeping authorship attribution separate from scientific support.
5. Do not cite a whole paragraph with one source when different sentences depend on different evidence.
6. Results produced in this thesis should normally point to a numbered finding, table, figure, appendix, repository release, or archived experiment rather than an external citation alone.

## Current automated counts

- Bibliography records: **103**.
- Records cited in the current chapter/front-matter sources: **96**.
- Missing citation keys: **0**.
- Records currently unused and retained for final review: `ahmad2023microgrid`, `alichoi2020smartgrid`, `bakare2023demand`, `desomer2017reallife`, `mahela2022masgrid`, `skouras2020ev`, and `vazquezcanteli2020marlisa`.
- Biber data-model validation completed without warnings after the four arXiv record-type corrections.

## Remaining final audit

- Verify author names, title capitalization, venue, year, volume/issue, pages, DOI, and final publisher URL for every bibliography record.
- Replace preprint metadata with the final peer-reviewed version where one exists, while preserving arXiv identifiers only when useful.
- Repeat or audit the Chapter 2 searches through institutional databases and archive the final screening record.
- Confirm that every factual number in Chapters 4--8 points to the exact frozen result, site report, paper, or log from which it was taken.
- Add source/adaptation/permission statements to every non-original or jointly produced figure.
- Confirm publication status and candidate/co-author contributions before the front matter is frozen.
- Remove bibliography entries that remain unused after the final text and add no references merely to make the bibliography appear broader.
