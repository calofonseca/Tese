# Thesis Structure and Granularity Audit - v10

This audit records the structural revision requested after the v9 visual/reference review. The rule applied throughout the thesis is that numbered headings must correspond to substantive argumentative units rather than to every named implementation detail.

## Applied rule

- A numbered second-level section must carry a distinct idea, claim, evidence block, or argumentative movement and must have enough substance to justify the break.
- A numbered third-level subsection should normally support approximately one to two pages of final text, including its method, evidence, figure, table, or discussion.
- A topic consisting of only one or two short paragraphs is represented as an unnumbered paragraph heading or merged with a related subsection.
- Central thesis objects can remain visible as intentional exceptions.

## Structural change by chapter

| Chapter source | v9 sections | v10 sections | v9 subsections | v10 subsections | v10 paragraph headings |
|---|---:|---:|---:|---:|---:|
| chapter01-introduction.tex | 6 | 6 | 23 | 16 | 22 |
| chapter02-foundations.tex | 10 | 10 | 46 | 26 | 49 |
| chapter03-energAIze-architecture.tex | 8 | 6 | 31 | 3 | 27 |
| chapter04-simulator.tex | 12 | 8 | 18 | 0 | 21 |
| chapter05-algorithms.tex | 11 | 8 | 16 | 0 | 31 |
| chapter06-ti-marl.tex | 13 | 6 | 16 | 0 | 34 |
| chapter07-lifecycle-deployment.tex | 11 | 7 | 11 | 0 | 15 |
| chapter08-real-world-validation.tex | 9 | 4 | 6 | 0 | 11 |
| chapter09-discussion.tex | 12 | 9 | 11 | 0 | 36 |
| chapter10-conclusions.tex | 7 | 6 | 8 | 0 | 17 |

## Principal decisions

- Chapter 1 keeps the four real-world properties visible, but merges the interdependency discussion into the surrounding section and joins scientific positioning, the research problem, and the thesis proposition into one substantial subsection.
- Chapter 2 now opens with **Review Design and Evidence Base**. The review objectives remain visible, while search, selection, extraction, synthesis, and limitations are consolidated. Foundations, REC properties, controller families, and environment families are grouped into larger evidence-bearing subsections.
- Chapter 3 keeps an architecture-first opening, expands the functional module discussion around five planes, and replaces one numbered subsection per requirement with **Architectural Rationale and Requirement Traceability**. The mapping is explicitly described as traceability rather than proof.
- Chapter 4 is compressed from a feature-by-feature outline into eight claim-oriented sections. Small asset, event, and validation topics are retained as paragraph-level units inside broader sections.
- Chapter 5 places result expectations and ablations close to the method stage they validate. Full seed tables, sweeps, and secondary results remain assigned to the appendix, while the unified comparison and solved-problem ledger stay in the main chapter.
- Chapters 6-10 were also audited. Short implementation or future-work subsections were collapsed into paragraph-level units, while the core scientific objects and RQ answers remain visible.

## Reassessment rule

The hierarchy must be checked again when verified results replace the current TBDs. A paragraph may become a numbered subsection if it gains a complete method-and-evidence block. Conversely, any planned subsection that remains short in the final version should stay merged.