# Open decisions

The canonical TI-MARL implementation target is defined in `TI_MARL_IMPLEMENTATION_SPEC_v3.md`. Frozen method decisions and unresolved choices are tracked in `notes/ti-marl/decision-log.md`. Older PILS- and JFAL-based documents are archived and do not define the current method.

## Metadata

- Confirm the final thesis title and subtitle.
- Confirm the final supervisor and co-supervisor record. The current project uses Luís Lino Ferreira and Armando Sousa.
- Confirm the submission date and jury composition.

## Canonical terminology

- Use **TI-MARL** for the principal algorithmic method.
- Use **TIMG** for the multi-agent formal model, **TI-MDP** for the one-agent formal model, and **TI-RL** for the one-agent reduction.
- Use **TIC**, **TIP**, **Action Group Instance**, **Action Port Instance**, **Local Action Bundle**, **Typed Interface Graph**, **TCG**, **Health Closure**, and **Typed Decision Trace** consistently.
- Do not reintroduce PILS or JFAL as algorithmic components.
- Confirm the final terminology against the paper and repository before submission.

## Research questions

- Audit the final wording against completed evidence.
- Confirm whether RQ3 supports both method development and systematic assessment, or should emphasise the latter.
- Preserve RQ2 as multi-dimensional scalability and RQ4 as governed coordinated policy-set lifecycle unless the final experiments cannot support them.

## Chapter 5: progressive solutions

- Freeze the exact five RBC levels and their information assumptions.
- Distinguish operational MILP from perfect-information/oracle variants.
- Decide the final role of PPO, SAC, TD3, MADDPG, and MATD3.
- Identify which learning enhancements are completed and which belong only in an appendix.
- For every stage, record the problem solved, evidence, conditions, remaining limitation, and relation to TI-MARL.

## Chapter 6: TI-MARL

- Freeze the reference backbone: TI-MAPPO, TI-MATD3, or both.
- Freeze the Typed Interface Graph schema and relation vocabulary.
- Select the local graph/set encoder and dynamic grouped-action decoder.
- Select the local hard-feasibility construction and verify that it preserves policy intent.
- Define the central set/graph critic inputs, pooling/message-passing structure, and treatment of variable populations.
- Freeze local and community reward decomposition and privileged-information boundaries.
- Define the hard shared-constraint monitor and show that it remains exceptional rather than performing normal community optimisation.
- Freeze health criticality, failure-scope, degradation, recovery, and admission rules.
- Define compatibility behaviour for new instances, held-out known-type compositions, and semantically unknown types.
- Complete structural baselines, health/reconfiguration tests, local bundle ablations, graph-critic comparisons, scalability tests, and typed-trace audits.

## EnergAIze and simulator

- Produce an as-built architecture audit from repositories and demonstrators.
- Confirm module names, boundaries, interfaces, flows, and implemented versus conceptual components.
- Preserve the distinction: Chapter 3 = blueprint; Chapter 7 = lifecycle machinery; Chapter 8 = deployed instance.
- Freeze the simulator release, upstream baseline, author contribution, test/audit results, and performance claims.

## Lifecycle and deployment

- Audit policy-set identity, compatibility metadata, staged deployment, mixed-version behaviour, coordination monitoring, rollback, disconnected-edge operation, and recovery.
- Separate documented design from implemented automation and empirically evaluated behaviour.
- Define the final system benchmarks and soak-test duration.

## Real-world validation

Classify every experiment as real-data simulation, target-hardware inference, hardware/software-in-the-loop, shadow mode, physical testbed, external-platform integration, limited direct operational control, or sustained operational control.

For each result, confirm the site, period, assets, policy, baseline, action authority, context, interventions, and limitations.

- Keep Chapter 8 divided into two independent demonstrator sections: OPEVA and DemFlex.
- For OPEVA, reconcile the D6.3 physical/integration record, the earlier nine-building benchmark, the four-building operational paper, and the later 17-installation manuscript campaign without pooling their results.
- Confirm the final OPEVA installation inventory, dates, control authority, policy versions, bounded actuations, and whether any reported period qualifies as sustained closed-loop operation.
- Obtain the authoritative DemFlex demonstrator brief, site and asset inventory, data lineage, controller and baseline, deployment record, action authority, duration, incidents, and verified results before completing its section.
- Confirm that the OPEVA D6.3 classified-deliverable citation and any adapted figures are permitted in the submitted/public thesis.

## Contributions and authorship

- Replace working contribution families with exact novelty and finding statements.
- Link each contribution to publications, artefacts, experiments, limitations, and candidate authorship.
- Use design records, CRediT statements, commits, reports, and supervision records together; do not use commit count alone.
