# Codex Brief — Implementation, Evidence, and Authorship Audit for the PhD Thesis

## Purpose

This project contains a complete authorial working draft of Tiago Fonseca's PhD thesis. The scientific story and chapter structure are already defined. The next task is **not to redesign the thesis or rewrite its prose**. The next task is to connect the thesis to the implementation, experiments, repositories, publications, and real-world records that support it.

Codex should use its access to the relevant repositories and development history to build an auditable account of:

- what was designed;
- what was implemented;
- what was tested;
- what was evaluated quantitatively;
- what was deployed or demonstrated;
- what was published or released;
- what remains incomplete;
- what Tiago contributed directly and what was collaborative.

Do not infer evidence from a class name, README claim, issue title, or planned architecture alone. Verify functionality through source code, tests, configurations, experiment outputs, logs, deployment records, releases, papers, or other concrete artefacts.

---

## Thesis structure that the audit must preserve

The thesis follows this cumulative argument:

```text
Problem and Research Questions
        ↓
Foundations, literature, and residual gaps
        ↓
Global EnergAIze architecture
        ↓
Simulator and experimental foundation
        ↓
Progressive control and learning solutions
        ↓
TI-MARL as the principal algorithmic contribution
        ↓
Lifecycle, orchestration, and edge deployment
        ↓
Integrated and real-world validation
        ↓
Answers to the Research Questions and discussion
        ↓
Conclusions
```

Relevant technical chapters:

- **Chapter 3:** EnergAIze architecture and common operational contracts.
- **Chapter 4:** simulator, datasets, scenarios, interfaces, validation, performance, and open-source artefacts.
- **Chapter 5:** progressive control and learning solutions, including RBCs, MILP, PPO, SAC, TD3, MADDPG, MATD3, behaviour cloning, replay, offline RL, distillation, and hierarchy.
- **Chapter 6:** TI-MARL, the principal algorithmic contribution.
- **Chapter 7:** experiment and MARL policy-set lifecycle, orchestration, and distributed edge deployment.
- **Chapter 8:** integrated and real-world evidence.
- **Chapter 9:** synthesis and answers to RQ1–RQ4.

### Canonical terminology

- **TI-MARL** is the canonical name of the principal algorithmic method. **PILS has been abandoned as an algorithm name.**
- **TIMG** is the formal multi-agent model; **TI-RL** is the one-agent reduction and implementation stage; **TIP**, **TIC**, the entity-bound interface graph, **TCG**, local bundle construction, central set/graph critics, the optional hard shared monitor, and runtime assurance are defined in `TI_MARL_IMPLEMENTATION_SPEC_v3.md`.
- Read `TI_MARL_IMPLEMENTATION_SPEC_v3.md` in full before auditing or implementing Chapter 6. It supersedes older TI-MARL/PILS planning notes.
- **MATD3 is important but is not automatically the main thesis contribution.** Standard MATD3 is prior work. TI-MATD3 and TI-MAPPO are candidate learning backbones whose exact role must be supported by implementation and evidence.
- **EnergAIze** is the integrated research architecture and energy-domain reference implementation, not the entire scientific thesis.
- **MorphTag Arena is not part of the main thesis narrative.** Do not reintroduce it unless a later decision explicitly uses it as supplementary mechanism evidence.

---

## Research Questions to support

### RQ1 — Scalability of Heterogeneous Multi-Agent Control
Under which conditions can MARL-based control maintain acceptable control performance and resource use as the number and diversity of participating agents and controlled assets increase and their availability changes?

### RQ2 — Deployability of Learned Controllers
How can evaluated MARL controllers be brought into use in real installations with manageable integration effort and maintained there with reproducible behaviour?

### RQ3 — Physical and Operational Safety
How can physical, electrical, and service constraints be represented, enforced, and assessed throughout MARL training and real-world control?

### RQ4 — Robustness to Real-World Disturbances
How can MARL-based control maintain acceptable service, degrade in a controlled manner, and recover when data, communication, equipment, or operating conditions depart from nominal assumptions?

---

## First-pass rule: audit before editing

During the first pass:

1. **Do not rewrite the clean thesis prose.**
2. **Do not replace or delete thesis claims merely because evidence has not yet been found.** Mark them as unsupported or pending.
3. **Do not silently upgrade planned features into implemented features.**
4. **Do not silently downgrade implemented work because documentation is incomplete.** Locate the code, tests, configurations, logs, and history.
5. Produce the audit outputs listed below.
6. Apply any later audit-based patch to the existing sources included by `main.tex`, using the reviewed audit entries.

---

## Repository discovery and inventory

Identify every relevant repository, package, service, branch, release, submodule, and experiment store associated with:

- EnergAIze architecture;
- CityLearn/EVLearn/CityLearn-REC simulator work;
- data collection, validation, forecasting, and messaging;
- RBC levels;
- MILP/optimisation;
- PPO, SAC, TD3;
- MADDPG and MATD3;
- behaviour cloning and guided exploration;
- prioritised or event-aware replay;
- offline RL;
- distillation and transfer;
- hierarchical coordination;
- TI-MARL, typed interfaces, dynamic inputs/outputs, physics-informed mechanisms, interface health, fail-safe operation, and fallback;
- experiment backend, workers, UI, registries, manifests, packaging, inference, deployment, monitoring, rollback, and recovery;
- simulated assets, testbeds, demonstrators, and real-world integrations.

For each repository record:

- repository name and URL or local path;
- purpose;
- default and relevant branches;
- important tags/releases;
- main packages/services;
- test locations;
- experiment/configuration locations;
- result/log/checkpoint locations;
- deployment definitions;
- principal contributors where verifiable;
- connection to thesis chapters and RQs.

Create: `notes/audits/repository-inventory.md`.

---

## Master method–claim–evidence–authorship matrix

Create one row per method, variant, system component, dataset/scenario contribution, or real-world result in:

`notes/audits/master-method-claim-evidence-matrix.csv`

Use the template at `notes/audits/master-evidence-matrix-template.csv` and extend it where necessary.

At minimum include:

- stable ID;
- canonical name;
- category: baseline / progressive solution / principal method / simulator / lifecycle / deployment / dataset / auxiliary mechanism;
- thesis chapter and section;
- RQ(s);
- problem addressed;
- exact claimed novelty;
- prior-work component used;
- thesis-specific modification or integration;
- implementation repository, path, symbol, and relevant commit/tag;
- configuration or manifest;
- dataset and scenario;
- observation, action, reward, constraint, and information assumptions;
- baselines;
- number of runs/seeds;
- metrics;
- strongest verified result;
- negative or boundary result;
- evidence level;
- publication/output;
- Tiago's contribution;
- co-author/collaborator contribution;
- current status;
- missing evidence;
- recommended placement: main body / appendix / repository only / remove;
- confidence and notes.

### Evidence-status vocabulary

Use one or more of these exact statuses:

- `planned`
- `designed`
- `implemented`
- `unit-tested`
- `integration-tested`
- `benchmark-complete`
- `statistically-evaluated`
- `hardware-runtime-tested`
- `HIL-or-testbed`
- `shadow-or-advisory`
- `limited-field-control`
- `sustained-operational-control`
- `published`
- `open-source-released`
- `deprecated`
- `superseded`
- `evidence-not-found`

Every non-trivial result must point to a concrete artefact: result file, experiment ID, log, table, notebook, script output, paper table, deployment record, or reproducible command.

---

## Specific audit questions by contribution

### Chapter 4 — Simulator

Separate inherited capability from thesis contribution.

For each simulator feature determine:

- Was it inherited from CityLearn, EVLearn, another upstream branch, or developed in this thesis?
- Which code implements it?
- Which tests verify it?
- Which physics or KPI audit validates it?
- Which scenarios exercise it?
- Was it released upstream or in a separate repository?
- Who authored it?

Audit at least:

- time and unit semantics;
- measured versus normalised PV;
- high-frequency data access;
- EVs, chargers, V2G, batteries, deferrable loads;
- phase/electrical service constraints;
- settlement and community KPIs;
- entity observations and action tables;
- topology and availability events;
- demand-response and robustness events;
- multiple communities;
- reproducibility, golden scenarios, physics audits, and performance benchmarks.

### Chapter 5 — Progressive algorithms

For every controller identify the exact implementation and experimental role.

#### RBC 1–5

- Freeze the actual class names and conceptual levels.
- Identify which information each level receives.
- Identify which physical/service guarantees are deterministic.
- Locate the comparative results that show what each added information layer solves.
- Identify which RBC serves as teacher, fallback, or operational baseline.

#### MILP

- Identify the exact formulation, variables, objectives, constraints, solver, horizon, forecast assumptions, and whether each result is operational-information or perfect-information/oracle.
- Record solver time and scale limits.

#### PPO, SAC, TD3

- Identify whether each is asset-level, building-level, or community-level.
- Freeze observation/action/reward definitions and training budgets.
- Record the scientific question answered by each method.

#### MADDPG and MATD3

- Separate standard prior-work mechanics from thesis-specific code and modifications.
- Identify exact MATD3 changes, if any, beyond a standard implementation.
- Locate evidence for stability, overestimation, critic disagreement, seed variance, sample efficiency, performance, action behaviour, or computational cost.
- Determine whether MATD3 is a standalone contribution, an empirical contribution, a backbone for TI-MARL, or a combination of these.

#### Behaviour cloning, replay, offline RL, distillation, hierarchy

For each mechanism record:

- what problem it addressed;
- how it was implemented;
- which base controller it modified;
- which ablation isolates its effect;
- whether it improved training, final performance, safety, transfer, model size, or deployment;
- whether the mechanism was retained in TI-MARL or rejected based on evidence.

### Chapter 6 — TI-MARL

Use `TI_MARL_IMPLEMENTATION_SPEC_v3.md` as the canonical implementation brief.

Create a component map with three columns:

```text
implemented and evaluated
implemented but not fully evaluated
planned or conceptual
```

Audit at least:

- canonical TI-MARL/TI-RL/TIMG terminology and versioned contract model;
- formal TIMG objects;
- active-agent and schema representation;
- typed observation parts;
- typed action ports;
- dynamic input/output mechanisms;
- interface compiler;
- action-port parameter heads;
- learning backbone and alternatives;
- hierarchical context;
- expert/offline data mechanisms;
- physics-aware features, residuals, or constraints;
- feasible-action construction;
- action masks, projections, bounds, and safe contraction;
- interface-health signals;
- fallback/fail-safe modes;
- energy-domain controlled-change experiments;
- ablations;
- integrated reconfiguration scenarios;
- scalability, safety, robustness, and resource evidence.

Do not infer that TI-MARL “does everything” because components exist. Each claimed property needs a corresponding experiment and metric.

### Chapter 7 — Lifecycle and deployment

Distinguish the following carefully:

- experiment tracking vs reproducible experiment contract;
- checkpoint storage vs policy registry;
- policy registry vs policy-set registry;
- serialisation vs executable packaging;
- multiple-model serving vs coordinated policy-set deployment;
- infrastructure monitoring vs data/control/safety/coordination monitoring;
- manual replacement vs staged update;
- software rollback vs policy-set rollback;
- edge inference vs governed heterogeneous edge lifecycle.

For each lifecycle feature identify:

- implementation location;
- state/data model;
- API/UI path;
- tests;
- failure behaviour;
- manual steps;
- measured overhead or latency;
- evidence of use in a demonstrator.

Audit experiment manifests, workers, retries, cancellation, lineage, registry metadata, compatibility, promotion, packages, target profiles, deployment state, telemetry, mixed versions, offline/disconnected operation, rollback, restart, recovery, and soak tests.

### Chapter 8 — Real-world evidence

Classify every result using one exact evidence level:

- `real-data simulation`
- `target-hardware inference`
- `software-in-the-loop`
- `hardware-in-the-loop`
- `shadow/advisory operation`
- `physical testbed`
- `limited field control`
- `sustained operational closed-loop control`

For each demonstrator record:

- site and partner;
- dates and duration;
- assets;
- hardware and software versions;
- active controller/policy set;
- baseline;
- decision frequency and number of decisions;
- action authority;
- outages and communication failures;
- manual interventions;
- fail-safe/fallback interventions;
- promotions, updates, and rollbacks;
- energy/service/runtime results;
- data-protection or publication constraints;
- source record and author contribution.

Do not combine a simulation result, a target-hardware test, and a field deployment into one claim.

---

## Authorship and provenance audit

Create `notes/audits/authorship-and-provenance.md`.

Use commits, pull requests, issues, design documents, publications, contribution statements, project deliverables, and supervisor confirmation where available. Do not use commit count alone as authorship evidence.

For each contribution state:

- Tiago's conceptual contribution;
- implementation contribution;
- experiment contribution;
- analysis contribution;
- writing/release contribution;
- collaborator contributions;
- evidence source;
- unresolved attribution questions.

A CRediT-style mapping may be used, but it must remain specific to the actual work.

---

## Missing-experiment and priority plan

Create `notes/audits/missing-experiments-and-priorities.md`.

Group gaps into:

1. **Evidence already exists but must be located or normalised.**
2. **A small rerun or export is needed.**
3. **A controlled comparison is missing.**
4. **A principal ablation is missing.**
5. **A real-world claim lacks an auditable record.**
6. **A claim should be reduced or removed.**

For every missing item estimate:

- thesis claim blocked;
- RQ affected;
- minimal experiment or evidence needed;
- expected runtime/resources;
- dependencies;
- priority: critical / high / medium / optional;
- whether it belongs in the main body, appendix, or repository.

Prioritise experiments that distinguish contributions, answer RQs, or prevent overclaiming. Do not prioritise exhaustive combinations that do not change the thesis conclusion.

---

## Figure and table evidence map

Create `notes/audits/figure-and-table-data-map.md`.

For every planned thesis figure/table identify:

- chapter and label;
- exact source code or data source;
- generation script or recommended script;
- required filters/aggregation;
- statistical representation;
- whether values are verified;
- whether sensitive or confidential information must be removed;
- current status.

Prefer generated figures from frozen result data. Architecture figures must reflect the as-built system. Screenshots and photographs must have a specific evidential purpose and appropriate permission.

---

## Final audit outputs

The first-pass audit is complete only when the following exist:

```text
notes/audits/repository-inventory.md
notes/audits/master-method-claim-evidence-matrix.csv
notes/audits/implementation-status-by-chapter.md
notes/audits/authorship-and-provenance.md
notes/audits/missing-experiments-and-priorities.md
notes/audits/figure-and-table-data-map.md
notes/audits/proposed-thesis-patches.md
```

`proposed-thesis-patches.md` should list, but not yet apply:

- exact thesis section;
- current claim or placeholder;
- verified replacement content;
- evidence source;
- confidence;
- whether author approval is required.

---

## Quality rules

1. Never invent a result, version, deployment, or author contribution.
2. Mark uncertainty explicitly.
3. Use stable repository paths, symbols, commits/tags, experiment IDs, and file names.
4. Distinguish a feature from evidence that the feature works.
5. Distinguish a benchmark result from an operational result.
6. Distinguish standard algorithm behaviour from thesis-specific modifications.
7. Distinguish implementation novelty from scientific novelty.
8. Preserve negative and boundary results.
9. Keep the thesis story cumulative: each stage solves a problem and reveals the next integration requirement.
10. Do not redesign the chapter structure unless an evidence contradiction makes the current structure untenable; report such contradictions instead.

---

## Suggested execution sequence

```text
1. Discover repositories and artefact stores
2. Build repository inventory
3. Populate master evidence matrix from code and papers
4. Attach tests, results, logs, and deployment records
5. Audit authorship and provenance
6. Identify missing evidence and minimal experiments
7. Map figures/tables to frozen data
8. Propose thesis patches
9. Obtain author review
10. Patch the thesis sources included by main.tex
```
