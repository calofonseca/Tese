# Chapter 6 TI-MARL Revision — v14

## Purpose

This revision restructures Chapter 6 so that it reads as a doctoral-thesis contribution rather than as a design discussion or implementation brief. The chapter now introduces the scientific position and formal problem before presenting the complete architecture, explains each component through generic definitions and energy examples, and reserves a full section for comparative results.

## Revised narrative

```text
Accumulated Chapter 5 findings
        ↓
Closest prior approaches and residual problem
        ↓
TI-MDP / TI-RL and TIMG / TI-MARL formulation
        ↓
Complete TI-MARL architecture
        ↓
Runtime contracts and interface compilation
        ↓
Local typed policies and multi-agent learning
        ↓
Typed constraint coordination and runtime assurance
        ↓
Learning, compatibility, and traces
        ↓
Experimental methodology and structural baselines
        ↓
Results compared with Chapter 5 and closest alternatives
        ↓
Discussion, generality, RQ contribution, and limits
```

## Final Chapter 6 structure

```text
6.1 Scientific Positioning and Problem Formulation
    6.1.1 Closest Approaches and the Residual Problem
    6.1.2 Typed-Interface Decision Processes

6.2 TI-MARL Architecture at a Glance

6.3 Runtime Contracts and Typed Interface Compilation
    6.3.1 Capability Schema, Runtime State, and Interface Snapshot
    6.3.2 Typed Observation Parts and Grouped Action Ports
    6.3.3 Health-Aware Causal Compilation

6.4 Local Typed-Interface Policies and Multi-Agent Learning
    6.4.1 Local Information Boundaries and Parameter Sharing
    6.4.2 Typed Policy Architecture and Local Action Bundles
    6.4.3 Learning Backbones and Centralised Critics

6.5 Typed Constraint Coordination and Runtime Assurance
    6.5.1 Typed Resource Couplings and the Constraint Graph
    6.5.2 Joint Feasibility and Allocation
    6.5.3 Runtime Assurance

6.6 Learning, Compatibility, and Decision Traces
    6.6.1 Learning through Coordinated Execution
    6.6.2 Formal Properties and Compatibility
    6.6.3 Decision Traces and Interface-Level Explainability

6.7 Experimental Methodology and Baselines
    6.7.1 Comparison Design and Reference Methods
    6.7.2 Reconfiguration Scenarios, Ablations, and Metrics

6.8 Results and Comparative Analysis
    6.8.1 Nominal Performance and Comparison with Chapter 5
    6.8.2 Reconfiguration and Held-Out Interface Compositions
    6.8.3 Health-Aware Robustness, Safety, and Joint Coordination
    6.8.4 Scalability and Runtime Cost
    6.8.5 Ablations and Boundary Conditions

6.9 Discussion, Generality, and Contribution to the Research Questions

6.10 Chapter Summary
```

## Main changes

- Removed the old numbered introductory section. The chapter now opens with a short unnumbered bridge from Chapter 5.
- Added a focused local state of the art with direct primary references and a table identifying the residual problem rather than claiming that individual components are new.
- Moved TI-MDP/TI-RL and TIMG/TI-MARL into the formal problem formulation before the architecture.
- Placed the complete architecture immediately after the formalisation, using a real TikZ figure rather than a planning placeholder.
- Expanded the architecture explanation into contracts/compiler, local policy/learning, coordination/assurance, and evidence/compatibility blocks.
- Preserved generic terminology while using recurring energy examples to make the definitions concrete.
- Added structural baselines derived from the novelty review and strong Chapter 5 controller configurations.
- Replaced a standalone evaluation-plan ending with a full Results and Comparative Analysis section.
- Kept claims conditional on future verified experiments and retained detailed missing-evidence instructions only in the annotated build.

## Evidence discipline

The chapter does not claim novelty for variable action spaces, parameterised actions, action masking, dynamic populations, sensor dropout, QP/shielding, fairness, parameter sharing, Transformers, or deployment contracts in isolation. The candidate contribution is the formal and operational coupling of:

```text
runtime typed contract
→ causal health-aware interface compilation
→ typed observations and grouped parameterised action ports
→ local policy over the current interface
→ typed resource couplings and joint allocation
→ compatibility, degraded operation, and execution trace
```

## Technical validation

- Clean thesis compiled with pdfLaTeX and Biber.
- Annotated thesis compiled with pdfLaTeX and Biber.
- No LaTeX errors.
- No undefined citations or cross-references.
- No overfull boxes in either full build.
- Clean and annotated PDFs contain 236 A4 pages.
- Standalone Chapter 6 contains 26 pages including its local references.
- The architecture figure appears immediately after Section 6.2.
