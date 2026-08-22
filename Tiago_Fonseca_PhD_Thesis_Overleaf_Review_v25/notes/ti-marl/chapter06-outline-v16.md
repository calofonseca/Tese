# Chapter 6 Outline - TI-MARL v16

## Narrative flow

```text
Chapter 5 capabilities and remaining fixed-interface assumption
        ↓
Closest prior approaches and the residual typed-interface problem
        ↓
TI-MDP / TI-RL and TIMG / TI-MARL formalisation
        ↓
TI-MARL architecture at a glance
        ↓
Entity-bound runtime interface compilation
        ↓
One local typed policy per agent, with dynamic group instances
        ↓
Local coherent action-bundle construction
        ↓
Joint training through central set/graph critics
        ↓
Learned community coordination under decentralised execution
        ↓
Typed constraints, exceptional safety monitoring, and health-aware degradation
        ↓
Compatibility, typed traces, experiments, results, and RQ contribution
```

## Structure

### Unnumbered chapter introduction

Connects the solutions established in Chapter 5 to the remaining fixed-interface assumption. Introduces a building with multiple chargers as the running example.

### 6.1 Scientific Positioning and Problem Formulation

- Closest approaches and residual problem
- Typed-Interface Decision Processes
  - TI-MDP and TI-RL
  - TIMG and TI-MARL
  - Local Action Bundle and joint transition
  - Optional exceptional hard shared-constraint monitor

### 6.2 TI-MARL Architecture at a Glance

Presents the complete architecture in one figure and separates decentralised runtime actors from the training-only central critic.

### 6.3 Entity-Bound Runtime Typed Interfaces

- Schemas, entities, and dynamic module instances
- Typed observation parts and aggregate community context
- Dynamic Action Group Instances and typed parameterised Action Ports
- Health-aware causal compilation and Health Closure

### 6.4 Local Typed-Interface Policies

- Local information boundaries and parameter sharing
- Typed graph/set encoding and one local latent
- Contextual embeddings for all active groups
- Shared type-conditioned group/port decoding
- Constraint-aware Local Action Bundle construction

### 6.5 Multi-Agent Learning and Community Coordination

- Joint training and decentralised execution
- Central set and graph critics
- TI-IPPO, TI-MAPPO, and TI-MATD3
- Community observations, local/community rewards, and learned coordination

### 6.6 Typed Constraints, Safety, and Runtime Robustness

- Typed Constraint Graph
- Exceptional hard shared-constraint monitoring
- Runtime assurance and degraded modes

### 6.7 Compatibility and Typed Explainability

- Interface snapshots and admission checks
- Execution-level typed decision traces
- Formal and operational properties

### 6.8 Experimental Methodology and Baselines

- Chapter 5 references and structural baselines
- Reconfiguration, health, coordination, scale, and ablation protocol

### 6.9 Results and Comparative Analysis

- Nominal performance
- Multiple assets and held-out compositions
- Health-aware robustness and local safety
- Multi-agent coordination and shared constraints
- Scalability and runtime cost
- Ablations, explainability, and boundary conditions

### 6.10 Discussion, Generality, and RQs

Positions the method against RQ1-RQ3 and separates general typed-interface claims from energy-specific evidence.

### 6.11 Chapter Summary

Closes the cumulative Chapter 5 -> Chapter 6 argument.

## Running example

The same building example is reused throughout:

```text
Building agent A
  main meter
  charger_1 -> EV session 17
  charger_2 -> EV session 28
  battery_1
  heat_pump_1

Authorised community observations
  community net demand
  transformer loading/headroom
  peak state
  PV surplus or coordination signal
```

The example shows:

- entity-bound EV observations;
- addition of `charger_3` without network resizing;
- shared dynamic decoding across charger instances;
- one coherent action bundle across all local assets;
- local house/phase feasibility;
- central graph-critic training;
- shared hard-limit intervention only when necessary;
- charger failure, stale SoC, main-meter failure, and recovery;
- typed compatibility and execution traces.
