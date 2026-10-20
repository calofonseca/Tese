# TI-MARL Decision Log

## Implemented scope used in the thesis, 8 October 2026

The implementation account in Chapter 6 supersedes the candidate design choices below. The supported learners are TI-PPO and TI-MAPPO, with a shared local typed actor and, for TI-MAPPO, a mean-pooled central set critic. The local analytic projector acts within a member. A graph critic, TI-MATD3 and a cross-member hard corrector are not part of the claimed implementation. The actor-only bundle defines the method-specific handoff; complete production serving is not certified by the current generic path. The focused suite passed 139 tests; see `verification-2026-10-08.json` and its log for the tested state. Annual comparative control results remain outstanding.

## Historical v16 design record

## Frozen decisions

1. One building controller is one local agent in the principal energy formulation.
2. Chargers, EV sessions, batteries, heat pumps, and other controlled elements are entity/module instances inside that agent.
3. Observations and actions are entity-bound through explicit identifiers and typed relations.
4. A known new asset instance changes the local interface graph, not the network parameter dimensions.
5. There is no permanent neural head per asset instance; one shared type-conditioned decoder processes active Action Group Instances.
6. All active groups are contextualised by one local latent and cross-group interaction before the Local Action Bundle is decoded.
7. Community data enter as authorised aggregate typed observation parts; no community coordinator agent is required by the core method.
8. Flexibility is learned from state, timing, constraints, rewards, and optional derived observations; there is no mandatory offer/negotiation phase.
9. Community coordination is learned through aggregate observations, coupled rewards, the joint transition, and central set/graph critics during training.
10. Execution is decentralised; actor inputs do not contain raw private observations from other agents.
11. Local non-negotiable constraints are incorporated into bundle construction. The shared hard-constraint monitor is exceptional and does not optimise normal community behaviour.
12. Health and dependencies causally recompile the interface, affecting observations, ports, bounds, groups, constraints, or operating mode.
13. TI-RL is the one-agent reduction; TI-MARL is the principal multi-agent method.
14. TI-MARL is optimiser-agnostic. TI-IPPO, TI-MAPPO, and TI-MATD3 are candidate instantiations.
15. The same typed semantics support learning, compatibility, runtime safety, and decision traces.

## Open implementation decisions

- Reference learning backbone and order of implementation.
- Graph/set encoder, edge types, aggregation, and recurrent memory.
- Dynamic group decoding method for discrete ports plus continuous parameters.
- Local feasible-bundle construction: analytic parameterisation, autoregressive decoder, differentiable projection, local QP, or a justified combination.
- Central critic graph: node/edge features, privileged information, value/Q formulation, and variable-population batching.
- Reward decomposition and coefficients for local service, local cost, community performance, local constraint intervention, and shared intervention.
- Parameter-sharing families and role-specific adapters.
- Unknown-type compatibility and admission hierarchy.
- Health thresholds, recovery hysteresis, safe isolation, and fallbacks.
- Shared hard-constraint monitor and minimum-correction policy.
- Final scale, baselines, ablations, and statistical protocol.

## Evidence gates

- A fixed padded/masked baseline must not match TI-MARL across the key reconfiguration tests without material cost or loss of generalisation.
- Known-type instance addition/removal must require no network resizing.
- Observations from one charger/session must never be associated with another charger/session.
- Health failures must cause the declared scoped changes and recover according to the contract.
- Local feasibility adjustment must be measurable and must not perform the high-level control task on behalf of the actor.
- Shared safety intervention must be rare under nominal validated operation.
- The central critic must accept changing agent populations without rebuilding its parameter layout.
- Typed traces must be complete and generated from the actual runtime objects and transformations.
