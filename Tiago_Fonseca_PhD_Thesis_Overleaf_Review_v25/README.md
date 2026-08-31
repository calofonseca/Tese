# Tiago Fonseca — PhD Thesis LaTeX Project

This folder is an Overleaf-ready project for a doctoral thesis in the **Programa Doutoral em Engenharia Informática (PRODEI)** at the Faculdade de Engenharia da Universidade do Porto (FEUP).

## Quick start in Overleaf

1. Upload the project ZIP through **New Project → Upload Project**.
2. Select `main.tex` as the main document for the clean reading version, or `main-annotated.tex` for the evidence-management version.
3. Use **pdfLaTeX** as the compiler. Bibliography processing uses **Biber**.

## Template basis

The project follows the public FEUP dissertation format created by João Canas Ferreira and João Correia Lopes. The included `feupteses.sty` is a project-local working copy that preserves the relevant public interface and FEUP cover conventions. Before jury submission, compare it with the latest FEUP/PRODEI template and replace it where required.

The FEUP/U.PORTO logo in `figures/uporto-feup.png` was extracted from the candidate's 2024 TRP cover to preserve the existing FEUP visual identity.

## Current status

The project contains a **complete ten-chapter authorial working draft** from the front matter to the conclusions. The prose is written as one dissertation argument rather than as an AI planning response or a chapter blueprint. It remains scientifically incomplete where verified quantitative evidence, frozen software versions, detailed authorship, final figures, and deployment records are not yet available.

- Chapter 1 introduces the problem, RQs, objectives, contribution hierarchy, and thesis story.
- Chapter 2 contains the foundations and evidence-backed critical review, supported by four curated scoping reviews.
- Chapter 3 presents the architecture-first EnergAIze narrative: boundaries, common contracts, five functional planes, end-to-end flows, and architectural rationale with explicit requirement traceability.
- Chapter 4 presents the CityLearn-derived simulator through positioning, scenario and data contracts, environment and asset models, dynamic interfaces, validation, performance, and availability.
- Chapter 5 presents the cumulative progression of control and learning solutions. Results are placed close to the stage they validate, while the cross-method synthesis records what each stage solved and what remained.
- Chapter 6 presents **TI-MARL** as the principal algorithmic contribution. Versioned capability schemas and runtime health are compiled into entity-bound typed observations and dynamic action-group instances; local policies jointly decode coherent local action bundles, central set or graph critics support joint training, and runtime assurance protects exceptional hard constraints and failures.
- Chapter 7 presents the governed experiment and MARL policy-set lifecycle, including lineage, compatibility, promotion, packaging, edge deployment, monitoring, update, rollback, and recovery.
- Chapter 8 presents real-world validation and current REC/EV evidence with explicit evidence-level boundaries.
- Chapter 9 synthesises the findings and answers RQ1–RQ4.
- Chapter 10 provides the conclusions, final assessment of the central thesis, and future research.

The project provides two reading modes:

- `main.tex` builds the **clean authorial reading version**. Draft notes and incomplete evidence ledgers are hidden; missing figures remain as neutral spaces with their captions.
- `main-annotated.tex` builds the **annotated research version**. It retains draft notes, source requirements, experiment ledgers, and `[TBD]` markers for the remaining evidence audit.

The clean version is intended for reading the thesis argument and prose. The annotated version is the operational writing and evidence-management copy. Neither version invents results that have not been verified.

## Main narrative

The thesis does not present the earlier methods as failed attempts before TI-MARL. Each stage solves a concrete problem:

```text
feasible transparent control
→ explicit constraint-aware optimisation
→ model-free adaptation
→ decentralised multi-agent coordination
→ improved stability and data use
→ hierarchical local/community coordination
→ remaining non-composable interface and physics assumptions
→ TI-MARL
→ governed deployment and real-world validation
```

TI-MARL and EnergAIze play different roles. **TI-MARL is the principal algorithmic contribution. EnergAIze is the integrated research architecture and energy-domain reference implementation.** MATD3 is an important stage and possible learning backbone, not the overall unifying contribution.

## Important metadata to confirm

Edit `metadata.tex`:

- final title and subtitle;
- final supervisor and co-supervisor;
- submission month and year;
- jury members for jury/final versions.

The current project uses Prof. Luís Lino Ferreira and Prof. Armando Sousa. The final record must be confirmed before submission.

## Build modes

The project has two entry points:

```text
main.tex            clean authorial reading version
main-annotated.tex  research annotations and evidence prompts visible
```

For a jury or final FEUP build, change the `feupteses` option in the selected entry point:

```tex
\usepackage{feupteses}                  % working cover
% \usepackage[juri]{feupteses}          % jury version
% \usepackage[final]{feupteses}         % final electronic version
% \usepackage[final,onpaper]{feupteses} % printed final version
```

## Folder structure

- `main.tex`: clean authorial document entry point.
- `main-annotated.tex`: annotated working entry point.
- `metadata.tex`: title, author, degree, supervisors, date, and PDF metadata.
- `frontmatter/`: declarations, abstracts, output map, and glossary.
- `chapters/`: one file per chapter.
- `bibliography/`: BibLaTeX database.
- `figures/`: logos, diagrams, plots, and photographs.
- `appendices/`: supplementary reproducibility material.
- `notes/`: writing rules, review evidence, and open decisions not included in the clean PDF.

## Writing conventions

The thesis is drafted in clear formal British English:

- state the scientific object, method, result, or evidence before explaining structure;
- use a concrete example when an abstract concept first appears;
- explain why a concept matters before adding technical detail;
- maintain one line of argument across chapters;
- repeat stable technical terms rather than inventing synonyms;
- distinguish simulation, hardware/runtime, testbed, shadow, and operational evidence;
- state what a method solved, under which conditions, and what remained;
- present contributions affirmatively and place boundaries in scope or limitations paragraphs;
- keep editorial instructions and missing-result prompts out of clean dissertation prose;
- limit claims to what the sources and experiments support.

See `notes/writing-style.md`.

## Structural granularity rule

The outline follows a claim-oriented hierarchy:

- a numbered second-level section must carry a distinct idea, claim, evidence block, or argumentative movement and must have enough content to justify the break;
- a numbered third-level subsection should normally support about one to two pages of final text, including method, evidence, figure, table, or discussion;
- a topic that remains only one or two short paragraphs is kept as an unnumbered paragraph heading or merged with a related subsection;
- central thesis objects and concise chapter summaries are deliberate exceptions.

This rule must be applied again after verified results replace the current placeholders.

## Bibliography and compilation

The project uses BibLaTeX with Biber and an author-year style. Verify every reference against the publisher or official source.

Clean build:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Annotated build:

```bash
pdflatex main-annotated.tex
biber main-annotated
pdflatex main-annotated.tex
pdflatex main-annotated.tex
```

## Codex implementation and evidence audit

Before further thesis rewriting, use `CODEX_AUDIT_BRIEF.md` as the task brief for a repository-aware Codex audit. The brief instructs Codex to inspect the as-built implementation, experiments, deployments, releases, and authorship evidence; populate the master evidence matrix; identify missing experiments; and propose thesis patches without silently rewriting or overclaiming.

The initial CSV schema is in `notes/audits/master-evidence-matrix-template.csv`. Codex should place its first-pass outputs under `notes/audits/` and should not modify the clean thesis prose until the audit has been reviewed by the author. For TI-MARL implementation and Chapter 6 evidence production, `TI_MARL_IMPLEMENTATION_SPEC_v3.md` is the canonical technical brief; it includes the as-built architecture map, mandatory baseline matrix, five Chapter 6 result blocks, figure-generation inputs, acceptance criteria, and reformulation triggers.

## Before submission

1. Freeze the as-built EnergAIze architecture.
2. Create the master method/claim/evidence/authorship matrix.
3. Verify every numerical result, scenario, baseline, seed, and evidence level.
4. Complete or remove unsupported TI-MARL, lifecycle, and field claims.
5. Replace contribution families with final quantitative finding statements.
6. Confirm publications and CRediT-style author contributions.
7. Repeat the Chapter 2 searches through institutional databases and archive screening decisions.
8. Verify bibliography metadata and software/data releases.
9. Replace every neutral figure space with a verified figure or remove the reference.
10. Validate the final FEUP/PRODEI template and metadata.

## Planned figures

The annotated PDF contains orange planning boxes with the required source and evidential role of each figure. The clean PDF shows only neutral figure spaces and captions, keeping production instructions out of the reading flow. The complete production requirements are in `notes/figure-register.md`; visual conventions are in `notes/visual-style-guide.md`.
