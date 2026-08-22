# TI-MARL Implementation and Experimental Specification - v3

## Status and purpose

This document defines the implementation target for **Typed-Interface Multi-Agent Reinforcement Learning (TI-MARL)**. It is an engineering and research specification, not thesis prose. It should be read together with Chapter 6 of the thesis, the falsification-oriented novelty review, the controller progression in Chapter 5, and the repository audit brief.

The specification has four purposes:

1. translate the current TI-MARL formal model into concrete software objects and execution paths;
2. separate frozen method semantics from implementation choices that remain open;
3. define the tests, baselines, ablations, and result artefacts required to support scientific claims; and
4. prevent repository structure, class names, or partially implemented features from being treated as evidence.

Every implemented capability must be traceable to source code, tests, configuration, manifests, logs, and reproducible experiment outputs. Where the existing code diverges from this document, Codex must document the divergence before changing either the implementation or the thesis.

The current scientific position is deliberately narrow:

> TI-MARL studies multi-agent decision problems in which each decentralised agent acts through an entity-bound runtime typed interface. A deterministic compiler converts the agent's active module instances, controlled entities, observation sources, health state, constraints, and authorised community signals into typed observation parts and dynamic groups of typed parameterised action ports. A local policy encodes the variable interface, creates one local latent representation, and jointly decodes a coherent action bundle across the currently active groups. Community coordination is learned through aggregate community observations, coupled rewards, the joint physical transition, and centralised set or graph critics during training. Local hard constraints are incorporated into bundle construction; a shared hard-constraint monitor is optional and exceptional.

The method does **not** claim novelty for Transformers, graph neural networks, parameter sharing, variable action sets, parameterised actions, action masking, dynamic teams, MAPPO, MATD3, safety projection, sensor dropout, or deployment contracts in isolation.

---

## 1. Canonical terminology

| Term | Meaning |
|---|---|
| **TI-MDP** | Typed-Interface Markov Decision Process; one-agent formal model. |
| **TI-RL** | One-agent reduction and intermediate implementation stage. |
| **TIMG** | Typed-Interface Markov Game; multi-agent formal model. |
| **TI-MARL** | Principal multi-agent method. |
| **TIC** | Typed Interface Compiler. |
| **TIP** | Local Typed-Interface Policy. |
| **Typed Interface Graph** | Entity-bound graph containing agent, module, entity, observation, action-group, port, health, dependency, resource, and local-constraint objects. |
| **Action Group Instance** | One controllable group bound to a specific module/entity instance, e.g. `EV_CHARGER_MODE@charger_2`. |
| **Action Port Instance** | One typed callable action within a group, with parameters, validity, bounds, dependencies, and resource effects. |
| **Local Action Bundle** | One selected action per active action-group instance, jointly produced by one local actor. |
| **TCG** | Typed Constraint Graph; typed local and shared resource/constraint relations used by actors, critics, local feasibility, safety checks, and traces. |
| **Constraint-Aware Local Bundle Construction** | Actor-integrated mechanism that converts decoded group decisions into a locally feasible bundle while preserving policy intent. |
| **Central Set/Graph Critic** | Training-only critic that processes a variable set/graph of agent summaries, actions, resources, and topology. |
| **Hard Shared-Constraint Monitor** | Optional exceptional runtime protection for non-negotiable shared constraints; not a community optimiser. |
| **Interface Snapshot** | Immutable compiled interface used for one agent at one time step. |
| **Health Closure** | Transitive propagation from source/module health through dependencies to observations, ports, bounds, groups, constraints, and operating mode. |
| **Typed Decision Trace** | Execution record grounded in the actual interface snapshot, selected ports, constraints, adjustments, health state, and final commands. |

**PILS is not an algorithm name in this project.** EnergAIze is the wider architecture and operational platform in which TI-MARL is trained, governed, deployed, and monitored.

---

## 2. Frozen design decisions

The following decisions are fixed for TI-MARL v1 unless implementation evidence forces a documented revision.

1. **One house/building controller is one local agent in the principal energy formulation.** Chargers, EV sessions, batteries, heat pumps, and other assets are modules/entities controlled by that agent unless an experiment explicitly defines another agent granularity.
2. **TI-RL is the one-agent reduction of TI-MARL.** The same schema, compiler, interface graph, policy, and local bundle classes must be reused.
3. **Every observation and action is entity-bound.** An EV SoC sample must identify the EV/session entity and the charger/module that produced it. An action group and port must identify the owner module and target entity.
4. **There is no permanent neural head per asset instance.** A shared type-conditioned decoder is applied to each active Action Group Instance.
5. **All active groups are decoded from one shared local context.** Group decisions are contextualised through a common local latent and cross-group interaction; they are not independent policies.
6. **Adding or removing a known module instance changes the local graph, not the network parameter dimensions.** A new charger creates a new charger-group instance processed by the existing decoder.
7. **Community information is represented as authorised typed observation parts.** It consists of numerical aggregate signals such as community demand, transformer loading, headroom, price signals, or demand-response targets. It is not an implicit global state vector.
8. **Flexibility is not a mandatory offer or negotiation object.** The policy learns temporal and operational flexibility from observations, constraints, outcomes, and optional derived features such as time to departure or remaining required energy.
9. **Each local policy outputs the final local action bundle, subject to local hard-feasibility construction.** There is no normal post-policy community allocator that replaces the local decisions.
10. **Community coordination is learned.** It arises from aggregate community observations, local and community reward terms, the joint physical transition, and centralised/structured critics during training.
11. **The Hard Shared-Constraint Monitor is exceptional.** It applies only to non-negotiable shared constraints and must not provide normal utility allocation, fairness, or community optimisation.
12. **Health and dependencies have causal effects.** A health state must alter port validity, bounds, group availability, constraints, or operating mode where declared. Health cannot be only a neural-network feature.
13. **Parameter sharing does not imply information sharing.** Local actor inputs remain private except for explicitly authorised aggregate observations.
14. **The core remains optimiser-agnostic.** TI-IPPO, TI-MAPPO, and TI-MATD3 are instantiations, not definitions of the method.
15. **Semantically unknown module or port types are not executed automatically.** Admission requires a compatible parent contract/decoder; otherwise the module remains uncontrolled by TI-MARL and approved fallback applies.
16. **The same semantics must support learning, compatibility checks, safety, and typed traces.** Avoid separate representations that can drift.

---

## 3. Non-goals

TI-MARL v1 does not attempt to provide:

- arbitrary zero-shot execution of completely unknown action semantics;
- a market mechanism or strategic bidding protocol;
- a learned community coordinator agent;
- a universal optimiser for shared resources;
- formal optimality guarantees for the learned policies;
- a replacement for device-native safety protections;
- a fully decentralised training algorithm with no shared experiment infrastructure;
- end-to-end formal verification of neural-network behaviour;
- a new graph encoder, PPO variant, or MATD3 optimiser solely by naming it TI-MARL.

These may be explored as later extensions, but they must not be required to validate the core typed-interface mechanism.

---

## 4. Formal execution model

At time step `t`, each active agent `i` has:

```text
Sigma[i,t]   versioned capability schema
H[i,t]       runtime health state
X[i,t]       local runtime values and entity relations
C[i,t]       authorised aggregate/community observations
```

The TIC produces an immutable local interface snapshot:

```text
I[i,t] = TIC(Sigma[i,t], H[i,t], X[i,t], C[i,t])
```

The snapshot contains:

```text
agent, module, entity and resource nodes
observation-part instances
action-group instances
action-port instances
typed relations and dependencies
current validity states
current parameter bounds
local hard constraints
community observation parts
compatibility signature
operational mode
```

The local TIP produces a raw bundle:

```text
raw_bundle[i,t] = TIP(I[i,t], memory[i,t])
```

The constraint-aware local construction returns the final local bundle:

```text
local_bundle[i,t] = LocalFeasibility(raw_bundle[i,t], I[i,t].local_constraints)
```

All local bundles form the joint action:

```text
joint_bundle[t] = {local_bundle[i,t] for i in active_agents}
```

The optional hard shared monitor is applied only when required:

```text
executed_joint_action[t] = SharedSafetyMonitor(joint_bundle[t], shared_TCG[t])
```

The environment transition and rewards are generated from the executed joint action. During training, one or more central critics receive a variable-cardinality representation of the joint transition. During deployment, only local actors and approved runtime safety components execute.

---

## 5. Core data model

### 5.1 Agent capability schema

The schema describes potential capabilities and compatibility. It does not contain fast-changing measurements.

```yaml
agent_schema:
  schema_id: residential_building_controller
  schema_version: 2.0.0
  agent_id: building_04
  role: building_controller
  policy_family: residential_building

  module_templates:
    - module_type: smart_meter
      allowed_versions: ">=1.0,<2.0"
    - module_type: ev_charger
      allowed_versions: ">=2.0,<4.0"
    - module_type: stationary_battery
      allowed_versions: ">=1.0,<3.0"
    - module_type: heat_pump
      allowed_versions: ">=1.0,<3.0"

  observation_type_registry: []
  action_group_type_registry: []
  action_port_type_registry: []
  local_constraint_templates: []
  resource_type_registry: []

  timing_profile:
    decision_interval_seconds: 900
    maximum_inference_latency_ms: 200

  fallback_profile:
    controller_type: RBC_SAFE
    version: 3.0.0

  compatibility:
    contract_version: 2
    allowed_parent_types: []
```

### 5.2 Runtime module and entity instances

Module instances and controlled entities must be separate objects.

```yaml
module_instance:
  module_id: charger_2
  module_type: ev_charger
  module_version: 2.3.1
  status: ACTIVE
  health: HEALTHY

entity_instance:
  entity_id: ev_session_28
  entity_type: ev_charging_session
  status: ACTIVE
  relations:
    connected_to: charger_2
```

A charger can remain installed while its connected EV session changes. A new EV session must not inherit stale observations from the previous session.

### 5.3 Observation part

```yaml
observation_part:
  part_id: ev_session_28.soc
  semantic_type: EV_SOC

  entity_id: ev_session_28
  source_module_id: charger_2
  source_kind: physical_sensor

  value: 0.62
  shape: []
  unit: fraction
  scope: local

  timestamp: 2026-08-15T12:00:00Z
  age_seconds: 2
  health: HEALTHY
  confidence: 0.98
  uncertainty: 0.01

  criticality: LOCAL_SAFETY_CRITICAL
  normalisation:
    method: identity

  provenance:
    topic_or_endpoint: partner/charger_2/ev/soc
    adapter_version: 1.4.0
```

Required scopes:

```text
self
local
neighbourhood
community
global
```

Required source kinds:

```text
physical_sensor
derived_signal
forecast
external_service
coordinator_message
```

Community observations use the same object model:

```yaml
observation_part:
  part_id: community.transformer_loading
  semantic_type: COMMUNITY_TRANSFORMER_LOADING
  value: 0.86
  unit: fraction
  scope: community
  source_kind: external_service
  health: HEALTHY
```

### 5.4 Health, criticality, dependency, and scope

Required health states:

```text
HEALTHY
DEGRADED
STALE
ESTIMATED
MISSING
FAILED
UNTRUSTED
```

Required criticality classes:

```text
OPTIONAL
OPTIMISATION_RELEVANT
SERVICE_CRITICAL
LOCAL_SAFETY_CRITICAL
SYSTEM_SAFETY_CRITICAL
```

Required dependency types:

```text
HARD
SOFT
SUBSTITUTABLE
REDUNDANT
AGGREGATE
```

Required failure scopes:

```text
PORT
ACTION_GROUP
MODULE
AGENT
COMMUNITY
SYSTEM
```

### 5.5 Action Group Type and Instance

An Action Group Type describes a reusable family. An Action Group Instance binds that family to a module/entity.

```yaml
action_group_instance:
  group_id: charger_2.mode
  group_type: EV_CHARGER_MODE

  owner_module_id: charger_2
  target_entity_id: ev_session_28

  selection_rule: exactly_one
  status: ACTIVE
  health: HEALTHY

  port_instances:
    - charger_2.idle
    - charger_2.charge
```

If the charger supports V2G and its dependencies are satisfied, `charger_2.discharge` can be added to `port_instances`. If the charger fails, the entire group becomes inactive. The network parameters do not change.

### 5.6 Action Port Type and Instance

```yaml
action_port_instance:
  port_id: charger_2.charge
  port_type: CHARGE_EV
  action_family: POWER_CONTROL

  owner_module_id: charger_2
  target_entity_id: ev_session_28
  group_id: charger_2.mode

  parameters:
    - name: power
      data_type: float
      unit: kW
      static_bounds: [0.0, 11.0]
      dynamic_bounds: [0.0, 7.2]

  validity:
    state: VALID
    predicate: EV_CONNECTED and CHARGER_HEALTHY
    reasons: []

  required_observations:
    - EV_CONNECTED
    - EV_REQUIRED_ENERGY

  resource_effects:
    - resource_id: building_04.import_power
      coefficient: +1.0
      parameter: power
    - resource_id: transformer_01.loading
      coefficient: +1.0
      parameter: power

  safety_class: NORMAL
```

### 5.7 Typed relations

The minimum relation vocabulary should include:

```text
owns
contains
connected_to
observes
source_of
controls
targets
requires
substitutable_by
conflicts_with
bounded_by
consumes
produces
contributes_to
shares_resource_with
```

Relations must be typed and validated. They must not rely solely on string naming conventions.

### 5.8 Local constraints and shared resources

```yaml
constraint:
  constraint_id: building_04.import_limit
  constraint_type: linear_inequality
  scope: local
  hard: true
  expression:
    charger_1.charge.power
    + charger_2.charge.power
    + heat_pump_1.heat.power
    - battery_1.discharge.power
    <= building_04.max_import

resource:
  resource_id: transformer_01.loading
  resource_type: shared_power_capacity
  scope: community
```

The local constraint graph is used by bundle construction. Shared resource and constraint objects are used by the central critic, reward/metric computation, explanation, and the optional hard shared monitor.

### 5.9 Interface snapshot

Every inference step must create or reference an immutable snapshot containing:

```text
snapshot_id
timestamp
agent_id
schema_id and version
policy_id and version
active module and entity IDs
observation parts with health/provenance
action groups and port instances
validity reasons and dynamic bounds
local constraints
community observations
operational mode
compatibility signature
```

Snapshot persistence can be sampled or event-triggered in large runs, but every recorded transition must be reconstructable.

---

## 6. Typed Interface Compiler

### 6.1 Compiler responsibilities

The TIC must perform the following ordered phases:

1. load and validate the versioned agent schema;
2. discover current module and entity instances;
3. bind observation samples to source modules and target entities;
4. validate units, timestamps, shapes, and provenance;
5. evaluate health states and compute Health Closure;
6. instantiate active Action Group Instances;
7. instantiate and validate Action Port Instances;
8. compute dynamic parameter bounds;
9. build entity, dependency, resource, and constraint relations;
10. determine the local operational mode;
11. validate policy-interface compatibility; and
12. emit an immutable Interface Snapshot and model-ready graph/set tensors.

### 6.2 Entity-binding invariants

The compiler must reject:

- an EV SoC observation without an EV/session entity;
- an EV SoC source bound to a charger different from the target action group without an explicit adapter relation;
- an action port whose owner module is inactive;
- a port targeting an entity no longer connected to the owner module;
- duplicate active entity IDs;
- stale observations from a previous session being reused under a new session ID;
- unit-incompatible dynamic-bound rules.

### 6.3 Multiple chargers

Adding a known charger must result in:

```text
one new module instance
zero or one connected EV-session entity
charger-specific observation-part instances
one new EV_CHARGER_MODE group instance
valid charger-specific ports
typed local/shared resource edges
no change to model parameter count
```

Removing the charger must remove or deactivate the corresponding subgraph without shifting the semantic identity of remaining chargers.

### 6.4 Health Closure

Health Closure must propagate through declared dependencies.

Example rules:

```yaml
health_rule:
  source: ev_session_28.soc

  when: STALE
  effects:
    - port: charger_2.discharge
      operation: CONTRACT_PARAMETER_BOUND
      parameter: power
      upper_multiplier: 0.15

  when: FAILED
  effects:
    - port: charger_2.discharge
      operation: INVALIDATE
      reason: REQUIRED_STATE_UNAVAILABLE
```

Main meter example:

```yaml
health_rule:
  source: building_04.main_meter

  when: FAILED
  effects:
    - operation: SET_AGENT_MODE
      mode: ISOLATED_SAFE
    - operation: SUSPEND_LEARNED_BUNDLE
    - operation: ACTIVATE_FALLBACK
      controller: RBC_SAFE
```

The closure algorithm must detect cycles and conflicting rules. The final effect must be deterministic for a fixed snapshot.

### 6.5 Compiler outputs

Codex should define an explicit typed output model rather than passing unstructured dictionaries between components. The output must include both:

- semantic objects used by logging, compatibility, and debugging; and
- tensor/graph views used by the policy and critic.

---

## 7. Local Typed-Interface Policy

### 7.1 Policy input

The local actor may receive:

```text
self/role token
module and entity tokens
local observation-part tokens
optional derived observation tokens
authorised community-observation tokens
action-group tokens
action-port tokens
health and validity metadata
local constraint/resource tokens or summaries
optional recurrent memory
```

It must not receive raw private observations from another local agent.

### 7.2 Type-specific encoders

Each semantic family may use a specialised encoder before projection to a common latent dimension:

```text
observation value encoder
module/entity metadata encoder
action-group encoder
action-port/schema encoder
health encoder
community-observation encoder
constraint/resource encoder
```

The implementation should support a registry-based mechanism so that adding a known type does not require modifying one monolithic `forward()` method.

### 7.3 Local graph/set fusion

The encoder must produce:

```text
z_agent        one local latent representation
z_group[g]     one contextual embedding per active action-group instance
z_port[g,p]    one contextual embedding per active port instance
```

Cross-group interaction is mandatory. The decision for `charger_1` must be able to condition on `charger_2`, battery, heat-pump, local limits, and community observations. Acceptable first implementations include:

- Graph Transformer over the local interface graph;
- Set Transformer with typed relation bias;
- GNN followed by attention pooling;
- entity/group attention with explicit local-resource context.

A simple independent loop over groups with no shared local context is not compliant.

### 7.4 Dynamic grouped action decoder

The decoder is shared across group instances.

For each active group:

1. compute port logits for currently valid ports;
2. select one port according to the action distribution/actor rule;
3. decode parameters using a port-type-conditioned decoder;
4. map normalised parameters to current dynamic bounds; and
5. return group-level confidence/log-probability information required by the backbone.

No permanent `charger_1_head`, `charger_2_head`, or `battery_1_head` should exist. Type-specific decoders such as `EV_POWER_DECODER` or `THERMAL_SETPOINT_DECODER` are acceptable.

### 7.5 Constraint-aware local bundle construction

The raw group outputs must be converted into a locally feasible bundle. The construction must not implement community optimisation.

Candidate implementations to evaluate:

1. **analytic parameterisation** for simple capacity/simplex constraints;
2. **autoregressive resource-aware decoding**, where each group is conditioned on remaining local resources;
3. **differentiable projection** onto the local feasible set;
4. **small local QP**, with a distance-to-raw-bundle objective;
5. **hybrid approach**, using bounded parameterisation for common cases and projection for residual constraints.

The selected mechanism must expose:

```text
raw bundle
final local bundle
active local constraints
adjustment indicator
adjustment magnitude
solver status/latency if applicable
```

The implementation is acceptable only if the policy's priorities remain visible and adjustment rates can be measured. A local optimiser that routinely determines all asset priorities would weaken the TI-MARL claim.

### 7.6 Optional memory

Recurrent or state-space memory can be added for partial observability, delayed communication, or intermittent sensors. It is not part of the core novelty and must be ablated separately from typed-interface effects.

---

## 8. Multi-agent learning

### 8.1 Joint training semantics

One environment step must produce one joint transition:

```text
all local interface snapshots
all raw and final local bundles
executed joint action
local rewards
community reward and metrics
shared constraint state
next local interfaces
population/schema/health events
```

Joint training means that all local actor updates are derived from this shared transition. It does not imply a central runtime actor.

### 8.2 Community observations

Community context should be limited to authorised aggregate values, for example:

```text
COMMUNITY_NET_DEMAND
COMMUNITY_TRANSFORMER_LOADING
COMMUNITY_HEADROOM
COMMUNITY_PEAK_STATE
COMMUNITY_PV_SURPLUS
COMMUNITY_PRICE_SIGNAL
DEMAND_RESPONSE_TARGET
```

Every value must be represented as a typed Observation Part with source, timestamp, health, and scope. Community context must be available in the same form during evaluation/deployment as during actor training.

### 8.3 Reward decomposition

The reward implementation must preserve component metrics even if training uses a scalar combination.

```text
local cost/service reward
community peak/ramping/renewable reward
local constraint penalty or intervention cost
shared hard-monitor intervention cost
optional fairness/distribution metric
```

Candidate form:

```text
r_i = r_local_i + alpha_i * r_community
      - beta_i * local_adjustment_cost
      - eta_i * shared_intervention_cost
```

Reward weights are open experimental choices and must be versioned.

### 8.4 Central set/graph critic

The critic exists only during training. It must accept variable populations without a permanent concatenated layout.

Recommended graph:

```text
agent-summary nodes:
    role
    local latent summary
    local action bundle
    local reward/service summary
    health/availability summary

shared-resource nodes:
    transformer/feeder/site resource
    current utilisation and limits

edges:
    agent contributes_to resource
    agents share_resource_with each other
    topology/phase/feeder relations
```

The critic should provide a deterministic permutation-invariant output for equivalent graph permutations.

### 8.5 TI-IPPO

TI-IPPO is the simplest decentralised baseline:

- one local TIP actor per logical agent;
- optional parameter sharing by role;
- PPO updates using local trajectories;
- no central critic.

It tests the value of typed interfaces without strong centralised credit assignment.

### 8.6 TI-MAPPO

TI-MAPPO is the preferred first hybrid-action reference unless existing code maturity strongly favours TI-MATD3:

- local stochastic TIP actors;
- categorical port selection per group;
- continuous parameter distributions conditioned on selected port;
- one central set/graph value critic;
- PPO clipping, GAE, entropy and value losses;
- masking only over compiler-declared valid ports.

### 8.7 TI-MATD3

TI-MATD3 preserves the Chapter 5 MATD3 lineage:

- local deterministic TIP actors;
- relaxed/differentiable port selection during training and hard selection during inference;
- type-conditioned deterministic parameter decoders;
- two central graph critics `Q1` and `Q2`;
- target actors and target critics;
- delayed actor updates;
- target action smoothing for continuous parameters;
- explicit storage of raw/final bundles and safety interventions.

Codex must not flatten variable agents and groups into one fixed vector merely to reuse an existing MATD3 implementation. A compatibility adapter can be used for a baseline, but the TI-MATD3 claim requires variable-cardinality critic inputs.

### 8.8 Replay and trajectory records

The run store must preserve:

```text
interface_snapshot_id per agent
local graph/tensor version
raw local bundle
final locally feasible bundle
executed joint action
local adjustment trace
shared monitor trace
local reward components
community reward components
next interface snapshot IDs
schema, module, health and population events
actor/critic/policy versions
```

For PPO/MAPPO, equivalent information must be available in rollout batches and archived evidence.

---

## 9. Shared constraints and runtime assurance

### 9.1 Typed Constraint Graph

The TCG must be derivable from the active typed interface contracts and system topology. It is used for:

- local bundle feasibility;
- graph-critic topology/features;
- shared hard-constraint validation;
- reward and metric computation;
- deployment compatibility and impact analysis;
- typed explanation traces.

The graph must not silently contain manually coded asset IDs that are absent from the schema/interface model.

### 9.2 Hard Shared-Constraint Monitor

The optional monitor is limited to constraints such as:

```text
transformer loading
feeder/phase current
site import/export limit
shared device/resource capacity
emergency operating envelope
```

It must expose:

```text
input joint bundle
feasible/infeasible result
active violated constraints
minimum correction or fallback action
correction magnitude
latency/status
```

It must not provide normal community utility optimisation. Frequent use is an algorithmic failure signal.

### 9.3 Operational modes

Minimum agent modes:

```text
NORMAL
DEGRADED
ISOLATED_SAFE
SUSPENDED
EMERGENCY
```

Representative transitions:

```text
charger failure
    -> remove charger group
    -> agent remains DEGRADED

SoC stale
    -> contract discharge bounds
    -> agent remains DEGRADED or NORMAL with warning

main meter failure
    -> aggregate local limit unverifiable
    -> ISOLATED_SAFE
    -> activate RBC_SAFE/native control

community signal failure
    -> remove/degrade community observation
    -> preserve approved conservative local operation

unknown schema type
    -> reject learned-control admission
    -> fallback or unmanaged-safe mode
```

### 9.4 Recovery

Recovery rules must specify:

```text
minimum number of fresh samples
consistency window
manual approval requirement if any
state reset or memory handling
port/group reintroduction semantics
trace event and version update
```

---

## 10. Compatibility, deployment, and typed traces

### 10.1 Compatibility signature

A policy package should declare:

```text
supported agent roles
supported module/entity parent types
supported observation semantic types and units
supported action-group and port types
parameter-schema compatibility
health-state vocabulary version
constraint/resource vocabulary version
encoder/decoder registry versions
maximum tested interface/graph budgets
authorised community observation contracts
fallback dependencies
```

### 10.2 Admission of a new charger

A charger can be admitted to learned control when:

1. its module type is known or compatible with an approved parent type;
2. observation and action semantic types are supported;
3. units and parameter signatures are compatible;
4. required dependencies and adapters are available;
5. local constraint/resource edges can be instantiated;
6. the policy package is validated for the relevant interface budget; and
7. fallback exists if inference or health checks fail.

### 10.3 Typed decision trace

Each inference record should be able to explain:

```text
active agent, module and entity IDs
schema/interface/policy versions
local and community observation parts available
health state of relevant sources
active action-group and port instances
invalid ports and reasons
selected port and parameters per group
raw and final local bundle
local constraint adjustments
shared monitor intervention if any
final executed device commands
```

The trace must be derived from execution records, not reconstructed from attention weights.

---

## 11. Implementation plan

### Phase 0 - Repository and evidence audit

Before coding:

- identify existing simulator, algorithm, schema, dynamic I/O, health, action-mask, entity, critic, and safety components;
- map each capability to files, symbols, tests, and run artefacts;
- mark `implemented`, `partial`, `planned`, or `absent`;
- preserve backward-compatible baseline paths;
- create `notes/ti-marl/implementation-gap-analysis.md`.

### Phase 1 - Typed object model and compiler

Implement:

```text
AgentSchema
ModuleInstance
EntityInstance
ObservationPart
ActionGroupType/Instance
ActionPortType/Instance
HealthState and HealthRule
TypedRelation
Resource and Constraint
InterfaceSnapshot
TypedInterfaceCompiler
```

Required tests:

- unit/shape/provenance validation;
- entity binding across multiple chargers;
- session replacement without stale-state leakage;
- known module addition/removal;
- unknown type rejection;
- deterministic Health Closure;
- compatibility-signature generation.

### Phase 2 - TI-RL with multiple local assets

Create a one-agent environment with:

```text
at least two charger instances
one battery
one heat pump or other coupled load
one aggregate local electrical limit
module and sensor health events
```

Implement the local graph encoder, dynamic grouped decoder, and local bundle feasibility. Compare against fixed-vector/masking and modular baselines.

### Phase 3 - Dynamic local reconfiguration

Add within-episode:

```text
charger instance addition
charger instance removal
EV-session replacement
V2G capability addition/removal
SoC stale/failed/recovered
main-meter failure and safe isolation
```

Verify no model-parameter resizing and no entity-binding errors.

### Phase 4 - Multi-agent environment and central critic

Implement several building agents with:

```text
local private observations
aggregate community observation parts
joint physical transition
local and community reward components
shared transformer/resource node
variable agent population
```

Implement set critic first if simpler, then graph critic where topology matters.

### Phase 5 - Reference backbone

Select one principal reference:

```text
TI-MAPPO
or
TI-MATD3
```

Selection criteria:

- existing implementation maturity;
- support for hybrid port/parameter actions;
- stability over repeated seeds;
- ability to use variable graph critics;
- compatibility with deployment targets;
- continuity with Chapter 5 evidence.

Implement the other as a comparison or limited ablation where feasible.

### Phase 6 - Shared hard-constraint monitor and runtime modes

Implement the optional monitor in-loop. Add intervention metrics and failure-injection tests. Verify it is not used to produce normal community allocations.

### Phase 7 - Lifecycle integration

Integrate:

```text
schema and interface versions
policy compatibility
package manifest
admission checks
interface snapshots
trace records
fallback activation
monitoring and recovery
```

### Phase 8 - Experiment campaign and evidence export

Freeze manifests, run repeated seeds, generate tables/figures from versioned scripts, and export all evidence listed below.

---

## 12. Mandatory baselines

### 12.1 Chapter 5 controller baselines

```text
passive operation
strongest RBC(s)
operational MILP/optimisation
oracle MILP where meaningful
best PPO/SAC/TD3 configuration
MADDPG
MATD3
selected hierarchical controller
```

### 12.2 Structural interface baselines

```text
fixed universal vector with padding and masking
capability-conditioned fixed head
Transformer/GNN encoder with fixed output head
modular observation/action controller
UAS-style fixed semantic union with availability masks
variable candidate-action representation
parameterised-action baseline where action structure matches
```

### 12.3 Multi-agent baselines

```text
independent local critics / IPPO
central flat critic with fixed population
set critic
graph critic
dynamic-population graph MARL reference
no community observation parts
no community reward term
```

### 12.4 Health baselines

```text
zero/default imputation
missingness mask only
recurrent/history estimator
sensor-dropout training
health-aware causal recompilation
```

### 12.5 Feasibility and shared safety baselines

```text
reward penalties only
per-port clipping
independent group projections
constraint-aware joint local bundle construction
no shared monitor
hard minimum-correction shared monitor
```

---

## 13. Mandatory ablations

1. remove semantic type metadata while retaining values;
2. remove entity binding and identify instances only by position;
3. remove typed dependency edges;
4. keep health as a neural feature but disable causal contraction;
5. replace dynamic bounds with static global bounds;
6. replace dynamic groups/ports with one fixed masked output vector;
7. remove cross-group attention/contextualisation;
8. use independent group decoders with no shared local latent;
9. remove constraint-aware local bundle construction;
10. replace graph critic with flat fixed-population critic;
11. remove community observation parts;
12. remove community reward component;
13. disable parameter sharing;
14. disable compatibility/admission checks;
15. disable typed traces;
16. remove the shared monitor and report hard violations;
17. keep the shared monitor but remove intervention penalties;
18. train on individual module types but hold out selected compositions;
19. add/remove agents while simultaneously changing one local interface;
20. compare known-type new instance, known-type held-out composition, and semantically unknown type.

---

## 14. Experimental scenarios

### 14.1 Nominal control

Stable population and interfaces. Establish control quality and computational overhead relative to Chapter 5 methods.

### 14.2 Multiple chargers per building

Vary:

```text
1, 2, 4, 8 charger instances
simultaneous EV sessions
different charger limits and V2G capabilities
shared local phase/import constraints
```

### 14.3 Runtime module reconfiguration

```text
add charger mid-episode
remove charger mid-episode
replace EV session on one charger
add battery/V2G capability
change port bounds
```

### 14.4 Population reconfiguration

```text
building joins
building leaves
building returns after outage
population and local interface change simultaneously
```

### 14.5 Health and robustness

```text
charger failure
EV SoC stale
EV SoC failed
main meter failed
community signal stale/failed
communication delay/loss
multiple simultaneous health events
recovery
```

### 14.6 Community coordination

```text
transformer headroom pressure
community peak objective
PV surplus
mixed EV deadlines
heterogeneous buildings
shared demand-response target
```

### 14.7 Held-out composition

Train with each type present separately, then test new combinations such as:

```text
two chargers + battery + heat pump
V2G charger + battery under stale SoC
new building with known module types but unseen composition
```

---

## 15. Metrics

### 15.1 Control and service

```text
cost
energy import/export
peak and ramping
renewable utilisation
EV target/departure service
comfort/service violations
battery cycling/degradation proxy
participant and community outcomes
```

### 15.2 Interface and reconfiguration

```text
entity-binding error rate
invalid-port rate
schema admission result
zero-/low-shot reconfiguration performance
retraining/adaptation requirement
recovery time after module/agent change
held-out composition performance
```

### 15.3 Safety and robustness

```text
raw local bundle infeasibility rate
final local bundle violation rate
local adjustment rate and magnitude
hard shared violation rate
shared monitor intervention rate and magnitude
fallback activation
scope of unnecessary shutdown
service preserved during degradation
health-detection and recovery latency
```

### 15.4 Scalability

```text
number of agents
module/entity instances per agent
action groups and ports
observation parts
graph nodes and edges
actor latency
critic latency
memory
training throughput
message volume
model parameter count
```

### 15.5 Deployability and explainability

```text
compatibility-check precision/recall over injected mismatches
unknown-type rejection
snapshot reconstruction success
trace completeness
trace/execution consistency
policy package size
edge inference latency
schema update and admission latency
```

---

## 16. Acceptance criteria

The implementation should not be described as TI-MARL-complete until the following gates pass.

### 16.1 Interface gates

- two or more chargers can coexist without observation/action cross-binding;
- a known charger can be added/removed without changing network parameter shapes;
- session replacement cannot leak the previous session state;
- health closure changes only the declared dependent interface objects;
- unknown semantic types are rejected safely.

### 16.2 Policy gates

- all active groups are decoded from one shared local context;
- the same group decoder is reused across module instances;
- local actors do not consume private observations from other agents;
- local bundle feasibility is measurable and near-complete under the final construction;
- adjustment rates do not indicate that the feasibility layer makes all substantive decisions.

### 16.3 Multi-agent gates

- one training transition contains all local bundles and community outcomes;
- the critic accepts variable agent counts without model resizing;
- graph/set outputs are permutation invariant where required;
- deployment actors do not depend on the central critic;
- community performance is not obtained mainly through the hard shared monitor.

### 16.4 Robustness and lifecycle gates

- main-meter failure isolates only the affected local agent where intended;
- charger failure removes only the affected group;
- stale/failed SoC produces the declared contraction/invalidation;
- interface snapshots reproduce selected actions and bounds;
- policy-interface mismatch is rejected before action execution;
- fallback and recovery are recorded and testable.

---

## 17. Kill tests and reformulation triggers

The scientific claim must be narrowed or reformulated if:

1. fixed universal padding/masking matches TI-MARL across all reconfiguration tests with lower complexity;
2. entity binding provides no measurable correctness or generalisation benefit;
3. adding a known module instance requires network surgery or full retraining;
4. the method works only when all interface compositions were seen during training;
5. health-aware compilation performs no better than missingness masks or sensor-dropout baselines;
6. the local feasibility mechanism routinely determines the asset priorities rather than enforcing residual hard constraints;
7. the hard shared monitor intervenes frequently and supplies most community coordination;
8. the graph critic offers no variable-population or coordination benefit over a simple fixed critic;
9. typed traces cannot be shown to match actual compiler and execution records;
10. deployment compatibility uses a separate schema representation that can drift from the learning interface.

In those cases, typed interfaces may remain a strong systems architecture, but claims of a distinct MARL method must be reduced accordingly.

---

## 18. Required repository artefacts

Codex should create or update:

```text
notes/ti-marl/implementation-gap-analysis.md
notes/ti-marl/decision-log.md
notes/ti-marl/object-model.md
notes/ti-marl/health-rules.md
notes/ti-marl/critic-design.md
notes/ti-marl/experiment-plan.md
notes/ti-marl/claim-evidence-matrix.csv
```

Required machine-readable outputs:

```text
run-manifest.csv
nominal-comparison.csv
multiple-charger-results.csv
reconfiguration-events.csv
health-stress-results.csv
local-feasibility-results.csv
community-coordination-results.csv
shared-monitor-results.csv
scalability-results.csv
ablation-results.csv
compatibility-results.csv
trace-fidelity-results.csv
boundary-and-negative-results.csv
figure-source-manifest.csv
```

Every row must identify:

```text
repository/commit
container/dependency version
environment/scenario version
policy/schema/compiler/critic version
seed
dataset/evaluation period
hardware
status
source artefact path
```

---

## 19. Required figures and source data

The implementation work must generate versioned source data for:

1. TI-RL versus TI-MARL formal reduction;
2. complete TI-MARL architecture;
3. multiple-charger entity-bound interface graph;
4. observation/action-port anatomy;
5. health-closure and failure-scope diagram;
6. local encoder and dynamic grouped decoder;
7. central graph critic and CTDE flow;
8. Typed Constraint Graph;
9. typed execution trace;
10. experiment matrix;
11. nominal comparison;
12. reconfiguration/health/scalability results;
13. ablation summary.

Diagrams must reflect the implemented object model. Planned or manual transitions must be visually distinguished from automated ones.

---

## 20. Open decisions

The following choices remain intentionally open and must be resolved through implementation evidence or controlled experiments.

### 20.1 Principal backbone

```text
TI-MAPPO
or
TI-MATD3
```

### 20.2 Local encoder

```text
Graph Transformer
Set Transformer with relation bias
GNN + attention pooling
hybrid entity/group encoder
```

### 20.3 Port-selection training

```text
categorical stochastic policy
Gumbel-Softmax/straight-through relaxation
autoregressive selection
other validated hybrid-action mechanism
```

### 20.4 Local feasibility mechanism

```text
analytic bounded parameterisation
autoregressive resource-aware decoder
differentiable projection
local QP
hybrid approach
```

### 20.5 Parameter sharing

```text
one actor per role
shared backbone + role adapters
fully independent actors
```

### 20.6 Community reward and observation design

The final aggregate signals and reward weights must be frozen against the Chapter 5 protocol. They must not give TI-MARL privileged runtime information unavailable to baselines.

### 20.7 Shared hard monitor

The constraint set, minimum-correction rule, intervention penalty, and fallback behaviour remain to be selected. The monitor must remain exceptional.

### 20.8 Unknown type policy

Define the parent-type compatibility rules, restricted admission behaviour, and safe fallback for unknown module/port types.

### 20.9 Formal guarantees

Determine which properties can be proved from the compiler and local feasibility implementation, such as entity-binding integrity, deterministic health closure, parameter-domain safety, and local bundle feasibility.

---

## 21. Codex operating instructions

1. Read this specification, Chapter 6, and `CODEX_AUDIT_BRIEF.md` before modifying code.
2. Audit the existing implementation before proposing a replacement architecture.
3. Preserve existing Chapter 5 algorithms and baseline paths.
4. Implement behind explicit feature flags/configuration versions where possible.
5. Add tests before claiming support for dynamic modules, health rules, or variable critics.
6. Do not change the clean thesis prose automatically. Produce a patch proposal and evidence report first.
7. Mark every unresolved item as `OPEN`, `PARTIAL`, `BLOCKED`, or `DECIDED` in the decision log.
8. Record negative results and kill-test failures; do not optimise them away from the evidence record.
9. Keep raw observations private to local actors unless the experiment explicitly tests a different information boundary.
10. Treat shared-monitor interventions as a measured failure mode, not as hidden normal behaviour.

---

## 22. Definition of done

TI-MARL v1 is ready for thesis-level claims when:

- the entity-bound typed interface is implemented and tested;
- multiple chargers and sessions can be added, removed, and rebound safely;
- local policies jointly decode variable action-group instances with shared model parameters;
- local hard constraints are enforced without the feasibility layer replacing policy intelligence;
- at least one central set/graph critic supports variable populations;
- community coordination is learned under decentralised execution and measured independently of the shared monitor;
- health events cause the intended scoped recompilation and fallback;
- interface snapshots and typed traces are reproducible;
- the mandatory structural baselines and ablations have been run over repeated seeds;
- scalability, Safety, Robustness, Deployability, and explainability evidence is archived; and
- the results survive the kill tests strongly enough to support the final, appropriately scoped scientific claim.
