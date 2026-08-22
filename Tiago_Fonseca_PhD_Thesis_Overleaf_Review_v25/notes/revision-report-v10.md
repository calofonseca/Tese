# Thesis Structural Refinement Report - v10

## Scope

This revision implements the structural decisions made after reviewing v9. The ten-chapter macro-story is unchanged. The work focused on the internal hierarchy, the relation between Chapter 1 sections, the review-method opening of Chapter 2, the architectural rationale and module space in Chapter 3, the fragmentation of Chapter 4, and the placement of results in Chapter 5. The same granularity rule was then applied across Chapters 6-10.

## Main changes

1. **Chapter 1**
   - Retained explicit Scalability, Deployability, Safety, and Robustness subsections.
   - Converted the short interdependency subsection into a paragraph-level conclusion.
   - Reorganised the middle of the chapter into:
     - Research Problem, Thesis Proposition, and Scope;
     - Research Questions, Objectives, and Research Strategy.
   - Merged scientific positioning, the research problem, and the thesis proposition into one substantial subsection.
   - Consolidated objectives, strategy, and traceability.

2. **Chapter 2**
   - Renamed the opening to **Review Design and Evidence Base**.
   - Removed the redundant phrase “Scoping Review Questions and Scope”.
   - Consolidated short foundation, REC, controller-family, and environment subsections into larger evidence-bearing units.
   - Preserved the four critical residual-gap subsections and the evidence-to-RQ synthesis.

3. **Chapter 3**
   - Kept the architecture-first opening.
   - Combined system context and common abstractions where the previous headings were too small.
   - Expanded the architecture around five functional planes:
     - Data and Integration;
     - Simulation and Experimentation;
     - Control and Learning;
     - Lifecycle and Governance;
     - Edge Runtime and Assurance.
   - Added a stable description pattern: responsibility, inputs, outputs, persistent state, interactions, failure modes, and detailed evidence chapter.
   - Replaced the former one-subsection-per-word mapping with **Architectural Rationale and Requirement Traceability**:
     - cross-cutting design principles;
     - a requirement-to-responsibility table;
     - trade-offs, boundaries, and non-guarantees.

4. **Chapter 4**
   - Reduced fragmentation and grouped the content by scientific claim rather than by every individual simulator feature.
   - Consolidated assets, interfaces, events, and validation mechanisms under broader sections.
   - Preserved all existing material and figure placeholders.

5. **Chapter 5**
   - Kept the cumulative research progression.
   - Moved result expectations and decisive ablations next to the method stage they validate.
   - Retained the unified cross-method comparison and solved-problem ledger.
   - Made the appendix boundary explicit: the chapter contains sufficient evidence for each claim; exhaustive seeds, sweeps, per-asset tables, and secondary variants belong in the appendix and archive.

6. **Chapters 6-10**
   - Applied the same hierarchy rule.
   - Collapsed small implementation subsections and future-work headings into paragraph-level units.
   - Preserved the main scientific objects: TIMGs, TI-MARL, lifecycle governance, real-world evidence, RQ answers, and central-thesis assessment.

## Validation

- Compiled with pdfLaTeX and Biber.
- 96 bibliography keys processed by Biber.
- No undefined citations or cross-references in the final pass.
- No multiply defined labels.
- No LaTeX errors or overfull boxes in the final log.
- Final PDF: 222 A4 pages, text-based and unencrypted.

## Remaining caveat

The structural rule has been applied to the present working content. It must be re-applied after final quantitative results are inserted. Some paragraph-level topics may grow into subsections; some current sections may still be merged if their final evidence remains short.
