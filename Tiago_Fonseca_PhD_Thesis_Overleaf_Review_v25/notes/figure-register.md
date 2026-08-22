# Thesis Figure Register - TI-MARL Revision v16

This register accompanies the visible `\plannedfigure` placeholders in the LaTeX source. It is a production plan, not a claim that the underlying evidence already exists.

## Global rules

- Prefer vector PDF/SVG/TikZ for conceptual diagrams and architecture figures; use raster images only for evidential photographs or screenshots.
- Every figure must be introduced and interpreted in the text before or immediately after it appears. A figure should support a claim or reduce conceptual load; decorative stock imagery is excluded.
- Data plots must be generated from archived machine-readable results by a versioned script. Record software version, hardware, scenario, seeds/repetitions, aggregation, uncertainty, and exclusions.
- Use stable terminology across all figures: agent, asset, controller, policy, policy set, scenario, interface, observation part, action port, target, deployment, fallback.
- Site photographs and UI screenshots require permission, anonymisation, and a clear evidential purpose. A dashboard screenshot must not replace the underlying quantitative result.
- Captions should state what is shown and the evidence boundary. Source/adaptation/permission information belongs in the caption or a source note where required.
- Keep fonts readable at final A4 size (normally at least 8--9 pt), avoid colour-only encoding, and ensure print/greyscale legibility.

## Planned figures

| Label | Chapter | Visual type | Intended claim/purpose | Required source or status |
|---|---:|---|---|---|
| fig:intro-rec-as-cps | 1 | Conceptual CPS/domain diagram | REC as physical assets + agents + local/community objectives | Final EnergAIze terminology |
| fig:ch2-reconfiguration-taxonomy | 2 | Taxonomy diagram | Six distinct forms of dynamicity/reconfiguration | Scoping reviews A--C |
| fig:ch2-evidence-ladder | 2 | Evidence ladder | Simulation-to-operation evidence levels | Review protocols A--D |
| fig:energaize-overview | 3 | Component-centred framework diagram | EnergAIze as a whole: repeatable building instance, Percepta, predictors, Algorithms/FSA, fail-safe execution, external platforms, assets, simulation, and REC coordination | Redrawn in TikZ from Manuscript V3 and OPEVA D6.3; final attribution/permission check |
| fig:sim-architecture | 4 | System architecture | CityLearn v3 as a complete multi-community REC environment with buildings, assets, local sharing, demand response, events, controllers, and KPIs | Included from the simulator manuscript source bundle; vector PDF |
| fig:sim-high-frequency | 4 | Multi-resolution data plot | Identical annual energy can expose materially different peaks at 1 h, 15 min, and 15 s | Included from the archived deterministic trace-replay evidence; vector PDF |
| fig:sim-deferrable-cycle | 4 | Service timeline/profile | Deferrable control shifts a complete cycle inside a valid start window without erasing its deadline | Included from the simulator manuscript source bundle; vector PDF |
| fig:sim-rec-settlement | 4 | Multi-panel accounting result | Local energy sharing changes community and participant outcomes even for the same physical trajectory | Included from the archived annual settlement example; vector PDF |
| fig:sim-dynamic-topology / fig:sim-topology-timeline | 4 | Event/result timeline | Member and asset changes propagate to the active entity set and controller contract | Included from the archived dynamic-topology example; vector PDF |
| fig:sim-robustness-channels | 4 | Control-loop event plot | Observation, forecast, action, and equipment failures act on distinct channels and remain auditable | Included from the archived robustness example; vector PDF |
| fig:control-progression | 5 | Cumulative progression | Problems solved and assumptions remaining at each stage | Method/claim/evidence ledger |
| fig:control-common-protocol | 5 | Experiment protocol | Fair information, budget, seed, KPI, and statistics rules | Frozen protocol |
| fig:maddpg-matd3-comparison | 5 | Algorithm + metric schematic | Standard change and thesis-specific comparison | Frozen code/results |
| fig:hierarchical-control-architecture | 5 | Two-level control diagram | Community coordinator and local workers | As-built hierarchy |
| fig:control-comparative-results | 5 | Multi-panel data plot | Control, learning, service, and resource results | Verified seed-level table |
| fig:lifecycle-entity-model | 7 | Entity/provenance model | Run-policy-policy set-package-deployment lineage | Domain/database models |
| fig:lifecycle-state-machine | 7 | Lifecycle state machine | Validation, promotion, staging, activation, rollback | Implemented states/transitions |
| fig:lifecycle-four-planes | 7 | Layered architecture | Experiment, governance, deployment, assurance planes | As-built architecture |
| fig:lifecycle-deployment-sequence | 7 | Deployment sequence | Coordinated staged policy-set rollout/rollback | Protocol and logs |
| fig:lifecycle-monitor-recovery | 7 | Monitoring/recovery loop | Infrastructure, data, control, safety, coordination signals | Telemetry/event schema |
| fig:validation-evidence-levels | 8 | Evidence ladder with cases | OPEVA and DemFlex evidence classified independently | Audited demonstrator records |
| fig:operational-contexts-topology | 8 | OPEVA site and integration topology | Three sites, physical assets, partner platforms, EnergAIze path, action authority | OPEVA D6.3, as-built sites, partner permissions |
| fig:operational-runtime-timeline | 8 | OPEVA operational timeline | Actions, states, data incidents, intervention, updates | Aligned OPEVA timestamp logs |
| fig:realworld-results | 8 | Print-ready comparative plots | OPEVA and DemFlex results separated by evidence level | Final audited demonstrator results |
| fig:sim-to-operation-gap-map | 8 | Cross-demonstrator assumption/evidence map | What changed from simulator to OPEVA and DemFlex operation | Incident/integration logs |
| fig:rq-evidence-map | 9 | RQ-finding traceability | Direct/supporting evidence and boundaries | Final claim-evidence matrix |
| fig:requirement-tradeoff-map | 9 | Trade-off/causal map | Interactions among four requirements | Cross-chapter findings |
| fig:thesis-contribution-stack | 10 | Synthesis diagram | Cumulative contributions and RQ answers | Final contribution list |

| fig:ti-reduction-and-game | 6 | Formal reduction diagram | TI-RL one-agent reduction versus TI-MARL joint learning and decentralised execution | Frozen formal notation and actor/critic implementation |
| fig:timarl-architecture | 6 | Layered architecture diagram | Local entity-bound interfaces and actors, joint transition, exceptional shared monitor, and training-only critic | Implemented architecture and frozen terminology |
| fig:timarl-multiple-chargers | 6 | Entity-bound typed graph | Multiple chargers, connected EV sessions, shared decoders, and runtime module admission | Final schema/object identifiers and executable scenario |
| fig:timarl-interface-anatomy | 6 | Paired annotated object cards | Concrete fields and dependency relation of one EV observation and one action port | Frozen schema fields and source adapters |
| fig:timarl-health-closure | 6 | Dependency/state diagram | Failure scope, health propagation, group removal, bound contraction, safe isolation, and recovery | Implemented health rules and fallbacks |
| fig:timarl-local-encoder | 6 | Neural architecture diagram | Typed graph encoding, one local latent, contextual group embeddings, and shared dynamic decoder | Final encoder, group mixer, and tensor shapes |
| fig:timarl-graph-critic | 6 | CTDE graph diagram | Local actors and training-only central set/graph critics over variable agents and shared resources | Final TI-MAPPO/TI-MATD3 critic implementation |
| fig:timarl-typed-constraint-graph | 6 | Typed resource/constraint graph | Local charger/battery/heat-pump limits and shared transformer constraint | Scenario contract and constraint builder |
| fig:timarl-decision-trace | 6 | Auditable decision trace | Interface snapshot, observations, valid/invalid ports, group actions, feasibility adjustment, shared intervention, and final commands | Runtime trace schema and one archived episode |
| fig:timarl-experimental-design | 6 | Experiment matrix | Nominal, reconfiguration, health, coordination, scalability, ablation, and boundary tests | Frozen run manifest and baseline matrix |
| fig:timarl-results-summary | 6 | Multi-panel result plot | Comparative control, held-out composition, health, shared coordination, runtime cost, and ablations | Verified seed-level outputs and plotting scripts |

## Final pre-submission checks

- Replace every visible placeholder with a final figure or delete it if the surrounding text is already clearer without it.
- Confirm that all figure labels are referenced in the prose and that the caption matches the final image rather than the planning description.
- Verify permissions and attribution for adapted figures, partner/site photographs, and external screenshots.
- Regenerate all result figures from the final archived data and rerun the PDF visual inspection after replacement.
