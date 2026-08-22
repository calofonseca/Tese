# TI-MARL Thesis and Implementation Revision - v16

## Scope

This revision replaces the previous negotiation/allocation interpretation of TI-MARL with the final decentralised local-agent design agreed for the thesis.

The principal energy formulation now uses one building controller per agent. Chargers, EV sessions, batteries, heat pumps, and other devices are module/entity instances inside that agent. Every observation and action is entity-bound. A known module instance can enter or leave at runtime without changing the neural-network parameter dimensions.

## Scientific architecture

The revised method contains:

1. TI-MDP and TI-RL as the one-agent formal model and reduction;
2. TIMG and TI-MARL as the multi-agent formal model and method;
3. a Typed Interface Compiler producing an entity-bound typed interface graph;
4. one local Typed-Interface Policy per agent;
5. one local latent representation and contextual embeddings for all active Action Group Instances;
6. a shared type-conditioned decoder rather than a permanent head per asset instance;
7. one coherent Local Action Bundle per agent;
8. local hard-feasibility construction that preserves policy intent;
9. aggregate community observations and local/community rewards;
10. training-only central set/graph critics under CTDE;
11. a Typed Constraint Graph shared across learning, local feasibility, safety, compatibility, and tracing;
12. exceptional hard shared-constraint monitoring rather than normal central allocation;
13. health-aware causal interface recompilation and scoped degraded modes;
14. entity-bound compatibility and typed decision traces.

## Removed concepts

The following are not part of the TI-MARL core:

- offer phase;
- mandatory flexibility envelope;
- community coordinator agent;
- community allocation intent;
- Joint Feasibility and Allocation Layer;
- normal post-policy community optimisation;
- Coordination Bids;
- permanent neural heads for individual asset instances.

Flexibility is learned from observations such as SoC, target SoC, departure time, state, forecasts, constraints, outcomes, and optional derived features. Community coordination is learned through aggregate observation parts, coupled rewards, the joint transition, and central critics during training.

## Chapter 6

`chapters/chapter06-ti-marl.tex` was rewritten as authorial thesis prose. It now contains:

- local related work and scientific positioning;
- formal TI-MDP/TI-RL and TIMG/TI-MARL definitions;
- a complete architecture figure;
- a multiple-charger running example;
- explicit observation and action-port tables;
- health-aware compilation examples;
- local typed graph encoding and dynamic grouped-action decoding;
- local bundle feasibility equations;
- set/graph critic and CTDE explanation;
- typed constraints, runtime assurance, compatibility, and explanation traces;
- full experimental methodology and result sections;
- figure placeholders tied to concrete implementation evidence.

The compiled Chapter 6 occupies 26 pages in the full thesis.

## Codex specification

`TI_MARL_IMPLEMENTATION_SPEC_v3.md` is the canonical implementation and experimental brief. It includes frozen decisions, non-goals, data schemas, pseudocode, model interfaces, implementation phases, baselines, ablations, experiments, metrics, evidence gates, kill tests, required artefacts, and unresolved decisions.

Older implementation specifications and historical JFAL/PILS documents have been moved to `notes/archive/` and must not be used as the current design.

## Global thesis alignment

The abstract, introduction, EnergAIze architecture, Chapter 5 transition, discussion, conclusions, glossary, appendix, README, Codex audit brief, open-decision log, and figure register were aligned with the revised TI-MARL architecture.

## Validation

- Clean thesis compiled with pdfLaTeX and Biber.
- Annotated thesis compiled with pdfLaTeX and Biber.
- No undefined citations or references.
- No LaTeX errors.
- No overfull boxes in the clean or annotated build.
- Clean thesis: 240 A4 pages.
- Annotated thesis: 242 A4 pages.
- Isolated Chapter 6: 26 A4 pages.
- Implementation specification converted to a separate PDF.

Quantitative result sections remain intentionally unfilled until the repository and experiment audit produces verified evidence.
