# Revised Working Draft Reading Guide

## Purpose

This version is written from the title page to the final conclusion so that the thesis can be read as one connected argument. It is deliberately more complete than the verified evidence. Draft notes, `[TBD]` tables, and conditional statements identify the places that require an experiment, repository audit, publication check, or authorship decision.

## First reading: the story

Read once without correcting individual sentences:

1. Does Chapter 1 promise the thesis you want to defend?
2. Does Chapter 2 derive precise residual gaps without pretending prior work does not exist?
3. Does Chapter 3 describe the EnergAIze architecture that was actually built?
4. Does Chapter 4 state the simulator contribution relative to CityLearn and other environments?
5. Does Chapter 5 show a cumulative research progression in which each method solves a problem?
6. Does Chapter 5 lead naturally to TI-MARL rather than presenting TI-MARL as one more algorithm?
7. Does Chapter 6 contain the principal algorithmic novelty and a fair evaluation plan?
8. Does Chapter 7 describe implemented lifecycle behaviour rather than desired functionality?
9. Does Chapter 8 classify every real-world result honestly?
10. Do Chapters 9 and 10 conclude only what Chapters 4--8 can support?

## Status labels

- **Supported working prose:** grounded in current sources or artefacts, but still editable.
- **Provisional result:** a value or conclusion exists but needs exact scenario and baseline verification.
- **Planned evidence:** an implemented mechanism exists but the common experiment or ablation is incomplete.
- **Research direction:** method or experiment is still being developed.
- **Remove if unsupported:** a claim must not remain unless the audit produces evidence.

## MATD3 decision

Standard MATD3 is prior work. The thesis can still make an important MATD3-related contribution through:

1. a rigorous new domain and real-world evaluation;
2. material, named method modifications supported by ablations; or
3. reproducible integration as the selected backbone within TI-MARL and EnergAIze.

The thesis should not claim `we introduce MATD3`. It may claim a MATD3-based method or control stack once the modifications and evidence are identified.

## Immediate audit matrix

Create one row per method or artefact with:

- name and version;
- baseline, solution stage, backbone, enhancement, or contribution;
- problem addressed and what was solved;
- remaining assumption;
- RQ and chapter;
- source repository/commit;
- dataset/scenario;
- observations/actions/reward;
- runs and seeds;
- metrics and strongest result;
- negative/boundary result;
- real-world evidence level;
- paper/output and author contribution;
- missing evidence;
- keep / merge / appendix / remove decision.

## Current chapter roles

- Chapter 3 = architecture and common operational contracts.
- Chapter 4 = simulator contribution and evidence.
- Chapter 5 = progressive control and learning solutions; solved-problem ledger; requirements for TI-MARL.
- Chapter 6 = TI-MARL, the principal algorithmic contribution.
- Chapter 7 = policy-set lifecycle and deployment systems contribution.
- Chapter 8 = integrated real-world evidence.
- Chapter 9 = cross-cutting RQ answers and validity.
- Chapter 10 = concise conclusion and future research.


## Structural hierarchy check

When final evidence is inserted, re-audit every heading:

- keep a numbered second-level section only when it sustains a distinct claim or evidence block;
- keep a numbered third-level subsection only when it has enough substance for roughly one to two pages;
- merge or demote short two-paragraph topics;
- allow exceptions only for central thesis objects, RQ answers, and concise chapter summaries.
