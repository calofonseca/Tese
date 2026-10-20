# Tiago Fonseca — PhD Thesis LaTeX Project

This folder is an Overleaf-ready project for a doctoral thesis in the **Programa Doutoral em Engenharia Informática (PRODEI)** at the Faculdade de Engenharia da Universidade do Porto (FEUP).

## Quick start in Overleaf

1. Upload the project ZIP through **New Project → Upload Project**.
2. Select `main.tex` as the main document.
3. Use **pdfLaTeX** as the compiler. Bibliography processing uses **Biber**.

## Template basis

The project follows the public FEUP dissertation format created by João Canas Ferreira and João Correia Lopes. The included `feupteses.sty` is a project-local working copy that preserves the relevant public interface and FEUP cover conventions. Before jury submission, compare it with the latest FEUP/PRODEI template and replace it where required.

The FEUP/U.PORTO logo in `figures/uporto-feup.png` was extracted from the candidate's 2024 TRP cover to preserve the existing FEUP visual identity.

## Current status

**20 October 2026 — publications as SC9:** the author requested the publication count as the ninth entry in Scientific Contributions, with a front-matter reference, instead of a separate Professional Contributions subsection. Section 1.4 again has three subsections. Repository names in 1.4.2 use bibliography citations without additional direct hyperlinks. This supersedes the preceding subsection arrangement recorded below.

**20 October 2026 — contribution titles and publications:** SC4--SC8 have shorter, direct titles. A separate Professional Contributions subsection reports the current thesis-linked set of two journal articles and three conference papers, with the CityLearn v3 preprint identified separately. The front-matter list now includes Percepta, and the published conference status and metadata of EnergAIze and the real-world REC control paper have been verified and corrected.

**20 October 2026 — concise contribution revision:** Section 1.4 now introduces its three subsections. Eight concise scientific contributions include the review and gap analysis as SC1; the previous seven become SC2--SC8. Five software/data contributions identify CityLearn v3, CityLearn UI, datasets, controller software and operational services, with links to the scientific contributions. The first explicit appendix reference is now in Chapter 3, so Simulation Studies of Community Energy Management is Appendix A and Reproducibility and Supplementary Material is Appendix B. This supersedes the historical appendix order and contribution numbering below.

**20 October 2026 — appendix order by first mention:** Reproducibility and Supplementary Material is Appendix A, first referenced in Section 1.4.2. Simulation Studies of Community Energy Management is Appendix B, first referenced in Chapter 3. This order supersedes the earlier appendix letters in the historical entries below.

**20 October 2026 — pagination of Chapters 1–3:** reviewed the rendered pages, reduced large gaps around figures, balanced section openings, and kept vulnerable paragraph endings together. The current PDF has **341 pages**. Chapters 1, 2, and 3 occupy printed pages **1–14, 15–44, and 45–86**; Chapter 4 starts on p. 87. Scientific wording, font sizes, margins, and citations are preserved. The reading PDF and parent-folder two-level index have been updated; pagination figures in the earlier editorial entries below describe their respective builds.

**20 October 2026 — contribution argument and MARL rationale:** Sections 1.1.1, 1.4.1, 3.2.3, and 3.7 now implement the accepted gap-to-contribution revision. SC1–SC7 retain their identifiers, titles, and order; their scientific objects and cumulative roles are more explicit. The working comparison matrix is in `notes/contribution-structure-plan-2026-10-17.txt`. That build contained 345 pages.

**20 October 2026 — terminology completion:** the final focused pass covers Chapters 1–3, the shared glossary, and clickable acronym links. Section 2.5 now explains offline dataset coverage, linked to the methods in Section 3.4.1. That build contained 345 pages; Chapters 1, 2, and 3 started on printed pages 1, 15, and 47. The two-level index in the parent folder gives the current pagination; page counts in the historical editorial account below refer to earlier compilations.

The project contains a **ten-chapter authorial working draft** from the front matter to the conclusions. Chapter 3 has been written through its final discussion: Section 3.1 is approved; Sections 3.2–3.7 are available for author review. The dissertation remains scientifically incomplete where verified quantitative evidence, frozen software versions, detailed authorship, final figures, and deployment records are not yet available.

- Chapter 1 introduces the problem, RQs, objectives, contribution hierarchy, and thesis story.
- Chapter 2 establishes energy-resource and flexibility concepts, single-agent and multi-agent reinforcement learning, reward design, offline learning, hierarchy, and structured policy architectures. Seven conceptual vector figures support the explanation; energy balances and evaluation indicators remain in the simulator chapter. Local paragraph and float adjustments allow the chapter to finish on printed p. 44; the unnecessary forced break before offline RL has been removed.
- Chapter 3 defines a systematised review protocol, distinguishing energy-application searches from complementary thematic mechanism searches. Search term families and selection statuses are explained in Sections 3.1–3.2; `notes/research/ch03-review-records.txt` links the underlying records. Section 3.2 compares simulation-based community energy applications, real-world energy-control evidence, and remaining research gaps. The real-world account distinguishes hybrid tests, laboratories and operating installations; Section 3.2.3 develops the gaps from the comparison with simulation and consolidates the operational synthesis. Its selection records are in `notes/research/marl-comunidades-2026-10-17/`: 129 identified publications, 70 selected external publications (50 simulation applications, ten physical/operational studies, and ten supporting reviews/frameworks/benchmarks). The selection account is condensed into one paragraph, distinguishing 53 records without sufficient full-text assessment from six outside the external comparison or language scope; operational comparators remain identified in the evidence discussion. The full 50-study simulation comparison is now Table A.1 in the new first appendix, **Simulation Studies of Community Energy Management** (printed pp. 253–257). The existing supplementary material follows unchanged as Appendix B (from p. 259). Chapter 3 occupies 42 content pages (pp. 45–86); Chapter 4 starts on p. 87. Table pagination uses the available space before continuation pages without changing table content or typography. Its thematic conclusions focus on evidence and gaps, and the final Chapter Summary links the findings back to Sections 3.1–3.6 and RQ1–RQ4. The chapter has 12 comparison tables, including a compact RQ synthesis in Section 3.7 connecting the literature-based answers to the gaps pursued in the thesis. Section 3.4 develops offline and prior-guided learning, policy reuse and cohorts, adaptation, system integration, and controller lifecycle support. It cites 31 selected sources and uses two tables to distinguish reusable preparation from local work and simulation from operational evidence. The final editorial pass reduces Section 3.4 by approximately 22%, retaining all cited works and both tables. Its opening maps the four subsections, and nine unnumbered mini-headings organise the three methodological subsections. The four subsection openings now establish the operational context before introducing method groups or the comparative synthesis. Transitions distinguish data-based preparation, policy reuse, and operational integration. The compact evidence table groups studies into six approaches and identifies their evaluation settings in three columns, without repeating the preparation mechanisms of the preceding table. The expanded two-paragraph closing distinguishes preparation shared across installations from recurring calibration, integration, validation and update effort, retaining the combined effort/performance gap. It omits the former candidate-method pointer and next-section announcement. Its final source/selection record is in `notes/research/ch03-section34-final-2026-10-17/reading-record.md`; the earlier primary readings remain available. The compiled section occupies printed pages 62–70 in the 339-page PDF. The approved final editing pass reduces Section 3.3 by approximately 20%, retains all 36 cited works and the capability table, and now uses a single-sentence table lead-in. The section occupies printed pages 54–61. Section 3.3 now has three subsections: learning and coordination for many members, architectures for changing members and within-member assets, and comparative analysis. Transfer and operational reconfiguration evidence is integrated with the architectural mechanisms. Section 3.3.2 uses four unnumbered headings distinguishing entity representation, entity-to-action mapping and semantics, graph relationships, and modular reuse across resource types. The text explicitly acknowledges that these mechanisms overlap and can coexist. The actor–critic schematic is retained; the generic mechanisms figure and its introductory paragraph have been removed at the author's request. Table 3.5 restores the author-preferred five capability rows: entity-associated decisions, heterogeneous action meanings, changing tasks, modular reuse, and energy reconfiguration. A single sentence introduces the table. Its compact columns identify capabilities, methods with references, and evaluation settings without repeating method descriptions. The gap is explicitly bounded to the reviewed evidence and concerns joint REC membership and within-member equipment changes, with retained control distinguished from adaptation. The latest approved closing uses two paragraphs after Table 3.5: established capabilities and candidate methods, followed by the joint-change evaluation gap and its significance. UPDeT, Entity Gym/RogueNet, MOHITO, Shared Modular Policies, COIN and graph-based energy controllers are presented as candidates for later investigation. The table and both closing paragraphs now fit together on printed p. 61. The repeated joint-change example is removed from 3.3.2, and explanatory colons are avoided in the section prose. Teamwork, robot and physical charging examples are introduced in 3.3.2 before being summarised in 3.3.3. Every source cited in the synthesis is introduced earlier in the review. MOHITO, COIN, Entity Gym/RogueNet and UAS are explicit antecedents; marlenv is a brief software-interface precedent. Section 3.3 remains a literature review, comparing demonstrated capabilities and their evaluation scope before identifying the open question about joint membership and equipment changes; it does not introduce TI-MARL. Its follow-up reading record is `notes/research/ch03-antecedents-2026-10-19/reading-record.md`. Section 3.3.1 uses three unnumbered mini-headings and explicit transitions to distinguish actor–critic methods, shared learning and value factorisation, and the organisation of interactions. CTDE and algorithm names are introduced locally. The compact actor–critic figure precedes the individual method descriptions; COMA and HAPPO/HATRPO provide additional examples. The independent-PPO comparison was removed at the author's request. Its source record is in `notes/research/ch03-section33-2026-10-17/reading-record.txt`. Section 3.5 develops constraint representation, action protection and supervision, coordinated physical limits and service feasibility, and comparative questions. It directly cites 21 publications and retains two tables. The final editorial pass preserves every citation in the preceding version and reduces the source word count by approximately 24%. Eight unnumbered mini-headings distinguish learning criteria, predictive verification, output correction, continued admissibility, supervision, and coordinated service. The opening maps the four subsections, and the conclusion states the shared-limit/individual-service question immediately after the evidence table. No bibliography entries were added in this pass. Its source record is in `notes/research/ch03-section35-2026-10-17/reading-record.md`; the section occupies printed pages 70–77. Section 3.6 develops robust learning, fault handling, degraded service and recovery, followed by operational evidence and comparative questions. It retains all 20 cited publications and two comparison tables. The final editorial revision adds an explicit subsection map and eight unnumbered method/evidence headings, clarifies transitions, and reduces repetition by approximately 24%. The synthesis opens with the question of retained individual service and sustained coordinated recovery, distinguishing learning from fallback and intervention. No bibliography entries were added in this pass. Its reading record is `notes/research/ch03-section36-2026-10-17/reading-record.md`; the section occupies printed pages 77–84 (PDF pages 121–128). Section 3.7 remains a Chapter Summary without subsections or a method catalogue. Its developed paragraphs follow the progression from Sections 3.1–3.6 and give each of RQ1–RQ4 the same sequence: reviewed approaches, the answer supported by the literature, and the specific gap pursued in the thesis. A compact three-column table consolidates these relationships. Explicit references to Section 1.2 explain how the reviewed evidence grounds the research problem. The summary occupies printed pages 84–86. Earlier source readings remain recorded in `notes/source-notes.md`.
- Chapter 4 presents the integrated EnergAIze architecture: building and community control, runtime components, controller development, experiment orchestration, model packaging, deployment, and the return of operating records to development. The Job Orchestrator, Worker Agent, heterogeneous execution adapters, persistent job records, recovery, and inference services are developed here. Three author-selected source figures remain in use, and three pictorial vector diagrams explain controller development, orchestration infrastructure, and model loading. Controller development and experiment orchestration/deployment have separate major sections; the controller leads the runtime component account. The former Chapter 7 systems-evaluation protocol is removed at the author's request.
- Chapter 5 presents the CityLearn-derived simulator through positioning, scenario and data contracts, environment and asset models, dynamic interfaces, validation, performance, and availability.
- Chapter 6 presents the cumulative progression of control and learning solutions. Results are placed close to the stage they validate, while the cross-method synthesis records what each stage solved and what remained.
- Chapter 7 presents **TI-MARL** as the principal algorithmic contribution. Versioned capability schemas and runtime health are compiled into entity-bound typed observations and dynamic action-group instances; local policies jointly decode coherent local action bundles, central set or graph critics support joint training, and runtime assurance protects exceptional hard constraints and failures.
- Chapter 8 presents real-world validation and current REC/EV evidence with explicit evidence-level boundaries.
- Chapter 9 synthesises the findings and answers RQ1–RQ4.
- Chapter 10 provides the conclusions, final assessment of the central thesis, and future research.

The project maintains one thesis version, with `main.tex` as its sole entry point and `main.pdf` as the reading output. The ten-chapter structure integrates orchestration and deployment into Chapter 4; the retired standalone systems-evaluation source is no longer included. Existing source filenames for the later chapters are retained. Working notes remain in the sources and in `notes/`; Chapter 3 contains its completed discussion and chapter closure; the author removed the protocol-status note. Missing figures retain neutral spaces with their captions.

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
→ real-world validation within the architecture established in Chapter 4
```

TI-MARL and EnergAIze play different roles. **TI-MARL is the principal algorithmic contribution. EnergAIze is the integrated research architecture and energy-domain reference implementation.** MATD3 is an important stage and possible learning backbone, not the overall unifying contribution.

## Important metadata to confirm

The title is **Multi-Agent Reinforcement Learning Control of Renewable Energy Communities**, with no subtitle, as confirmed by the author following the supervisors' meeting (recorded 2026-09-10).

Confirm the remaining fields in `metadata.tex`:

- final supervisor and co-supervisor;
- submission month and year;
- jury members for jury/final versions.

The author is **Tiago Carlos Caló Fonseca**. The project uses **Luís Miguel Moreira Lino Ferreira, PhD** as supervisor and **Armando Jorge Sousa, PhD** as co-supervisor, following the author's preferred form of address.

The document's title page follows the centred layout of the [FEUP LaTeX template](https://www.overleaf.com/latex/templates/feup-dissertation-format/qrsrxjjwzrzf), linked from [Correia Lopes's FEUP page](https://pages.up.pt/~up230756/doku.php/teach/feupteses) and checked on 2026-09-10. The author appears below the title. FEUP also provides separate graphical cover templates through its [doctoral draft documents page](https://sigarra.up.pt/feup/en/WEB_BASE.GERA_PAGINA?P_pagina=258292).

## Main document and cover options

The sole entry point is:

```text
main.tex
```

For a jury or final FEUP cover, change the `feupteses` option in `main.tex`:

```tex
\usepackage{feupteses}                  % working cover
% \usepackage[juri]{feupteses}          % jury version
% \usepackage[final]{feupteses}         % final electronic version
% \usepackage[final,onpaper]{feupteses} % printed final version
```

## Folder structure

- `main.tex`: sole thesis entry point.
- `metadata.tex`: title, author, degree, supervisors, date, and PDF metadata.
- `frontmatter/`: declarations, a separate Funding section, acknowledgements, abstracts, output map, and glossary.
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

Build:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

## Codex implementation and evidence audit

Before further thesis rewriting, use `CODEX_AUDIT_BRIEF.md` as the task brief for a repository-aware Codex audit. The brief instructs Codex to inspect the as-built implementation, experiments, deployments, releases, and authorship evidence; populate the master evidence matrix; identify missing experiments; and propose thesis patches without silently rewriting or overclaiming.

The initial CSV schema is in `notes/audits/master-evidence-matrix-template.csv`. Codex should place its first-pass outputs under `notes/audits/` and should not modify the clean thesis prose until the audit has been reviewed by the author. For TI-MARL implementation and Chapter 7 evidence production, `TI_MARL_IMPLEMENTATION_SPEC_v3.md` is the canonical technical brief; it includes the as-built architecture map, mandatory baseline matrix, five TI-MARL result blocks, figure-generation inputs, acceptance criteria, and reformulation triggers.

## Before submission

1. Freeze the as-built EnergAIze architecture.
2. Create the master method/claim/evidence/authorship matrix.
3. Verify every numerical result, scenario, baseline, seed, and evidence level.
4. Complete or remove unsupported TI-MARL, lifecycle, and field claims.
5. Replace contribution families with final quantitative finding statements.
6. Confirm publications and CRediT-style author contributions.
7. Update the Chapter 3 literature search before submission, verify the final versions of cited preprints, and archive any additional selection decisions.
8. Verify bibliography metadata and software/data releases.
9. Replace every neutral figure space with a verified figure or remove the reference.
10. Validate the final FEUP/PRODEI template and metadata.

## Planned figures

Chapter 2 uses finished figures and tables. Chapter 3 currently includes its eligibility table; evidence tables will be developed with each literature-review section. Later chapters retain some neutral figure spaces and captions while their evidence and artwork are being prepared. Production instructions remain in the source and in `notes/figure-register.md`; visual conventions are in `notes/visual-style-guide.md`.
