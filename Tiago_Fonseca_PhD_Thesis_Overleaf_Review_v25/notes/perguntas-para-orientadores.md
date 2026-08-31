# Reunião com os orientadores

## Estrutura atual da tese

### Elementos iniciais

- Declaration of Honour
- Declaration on the Use of Generative Artificial Intelligence
- Statement on Co-Authored Work
- Acknowledgements
- Abstract
- Resumo
- Publications and Research Outputs Arising from the Thesis
- List of Acronyms
- Glossary

### 1. Introduction

- 1.1 Context and Motivation
  - 1.1.1 Distributed and Dynamically Reconfigurable Cyber-Physical Systems
  - 1.1.2 Renewable Energy Communities as Representative Cyber-Physical Systems
  - 1.1.3 MARL for Mixed Cooperative--Competitive Decentralised Control
- 1.2 Requirements for MARL in Real-World CPS
- 1.3 Thesis Proposition, Research Questions, and Scope
  - 1.3.1 Thesis Proposition
  - 1.3.2 Research Questions
  - 1.3.3 Research Objectives
  - 1.3.4 Scope and Assumptions
- 1.4 Research Contributions and Outcomes
  - 1.4.1 Scientific Contributions
  - 1.4.2 System, Software, and Open-Source Contributions
  - 1.4.3 Societal and Environmental Relevance
- 1.5 Research Path and Thesis Organisation

### 2. Real-World Multi-Agent Control in Cyber-Physical Systems: Foundations, State of the Art, and Research Gaps

- 2.1 Literature Scope and Evidence Approach
  - 2.1.1 Scope and Sources
  - 2.1.2 Evidence Synthesis and Limitations
- 2.2 Distributed, Heterogeneous, and Dynamically Reconfigurable Cyber-Physical Systems
  - 2.2.1 Distributed Control and Operational Constraints
  - 2.2.2 Heterogeneous Agents, Assets, and Interfaces
  - 2.2.3 Dynamic Populations, Capabilities, and Reconfiguration
- 2.3 Renewable Energy Communities as Representative CPSs
  - 2.3.1 Participants, Assets, and Heterogeneity
  - 2.3.2 Flexibility, Temporal Coupling, and Dynamic Availability
  - 2.3.3 Individual and Community Objectives and Physical Constraints
- 2.4 Control Approaches for Distributed Energy Systems and Related CPS
  - 2.4.1 Explicit Control: Rules, Optimisation, and Predictive Control
  - 2.4.2 Reinforcement Learning and Multi-Agent Control
  - 2.4.3 Structured, Federated, Transfer, Hybrid, and Hierarchical Approaches
  - 2.4.4 When MARL Adds Value across CPS Domains
- 2.5 Foundations of Reinforcement Learning and MARL Used in This Thesis
  - 2.5.1 Sequential Decision-Making and Partial Observability
  - 2.5.2 Reinforcement Learning and Actor--Critic Methods
  - 2.5.3 Markov Games, MARL, and CTDE
  - 2.5.4 MARL Challenges Relevant to This Thesis
- 2.6 Simulation and Levels of Real-World Evidence
- 2.7 Critical Analysis of the State of the Art
  - 2.7.1 RQ1: Dynamic and Heterogeneous Multi-Agent Control
  - 2.7.2 RQ2: Multi-Dimensional Scalability of Learning and Coordination
  - 2.7.3 RQ3: Safe and Robust Operation
  - 2.7.4 RQ4: Governed and Deployable MARL Lifecycle
- 2.8 Adjacent Challenges and Scope Boundaries
  - 2.8.1 Supporting Requirements and Evaluation Conditions
  - 2.8.2 Important Challenges Beyond the Central Scope
- 2.9 Synthesis of Residual Gaps and Thesis Requirements
- 2.10 Chapter Summary

### 3. EnergAIze: An Integrated Framework for Intelligent Energy Management

- 3.1 Architectural View I: A Supervised Energy Decision
- 3.2 Architectural View II: A Distributed Renewable Energy Community
- 3.3 Architectural View III: Functional Components and Interfaces
  - 3.3.1 Percepta and the Data Provider
  - 3.3.2 Prediction, PulseCharge, and User Flexibility
  - 3.3.3 Algorithms, Inference, and the Fail-Safe Supervisor
- 3.4 Controller Development and Runtime Operation
  - 3.4.1 CityLearn, EVLearn, and Experimental Development
  - 3.4.2 Runtime Topologies and Deployment Boundary
- 3.5 Architectural Rationale and Thesis Map
- 3.6 Chapter Summary

### 4. CityLearn v3: A Simulation and Evaluation Environment for Renewable Energy Communities

- 4.1 The Simulator as an Experimental Research Contribution
  - 4.1.1 Research Instrument and Public Software
  - 4.1.2 CityLearn v3 Across the Controller Lifecycle
- 4.2 Problem Definition, Requirements, and Positioning
  - 4.2.1 Limitations of the Inherited Environment and Required Experimental Contract
  - 4.2.2 Lineage and Position within Existing Environments
- 4.3 CityLearn v3 Architecture and REC Modelling Capabilities
  - 4.3.1 System Architecture and the Scenario-to-Evidence Path
  - 4.3.2 Scenario, Time, Unit, and Data Contracts
  - 4.3.3 Stationary Storage and Electrical-Service Limits
  - 4.3.4 Electric Vehicles and Chargers
  - 4.3.5 Deferrable Appliances
  - 4.3.6 Local Energy Sharing and Settlement
  - 4.3.7 Changing Community Members and Assets
  - 4.3.8 Controlled Data and Equipment Failures
  - 4.3.9 Demand-Response Services
  - 4.3.10 Multiple Communities
  - 4.3.11 Controller Interfaces and Applied-Action Traceability
- 4.4 Datasets Developed to Evaluate REC Controllers
  - 4.4.1 Common Temporal, Provenance, and Accounting Contract
  - 4.4.2 Composition and the Separation of Infrastructure from Mobility
  - 4.4.3 Experimental Ladder and Matched Scenario Variants
  - 4.4.4 Validation Protocol and Annual Baseline Execution
- 4.5 Evaluation Protocol and Controller Scorecard
  - 4.5.1 Reference Controllers and Fair Comparisons
  - 4.5.2 Core Scorecard and Result Exports
- 4.6 Chapter Synthesis

### 5. Control and Learning Methods for Renewable Energy Communities

- 5.1 Research Progression
- 5.2 Common Control Problem and Experimental Protocol
  - 5.2.1 REC Control Formulation
  - 5.2.2 Information and Comparison Surfaces
  - 5.2.3 Dataset Ladder and Experimental Funnel
  - 5.2.4 Training Budgets, Repetition, and Statistical Reading
- 5.3 Engineering the Control--Learning Interface
  - 5.3.1 From Simulator State to Policy Input
  - 5.3.2 Action Semantics and the Executed Transition
  - 5.3.3 Reward Lineage
  - 5.3.4 Replay, Demonstrations, and Rare Events
  - 5.3.5 Optimisation, Checkpoints, and Export Continuity
- 5.4 Level I: Transparent and Constraint-Aware Controllers
  - 5.4.1 Business-as-Usual and the Rule-Based Ladder
  - 5.4.2 MILP Reference Problems
  - 5.4.3 Evidence Produced at Level I
- 5.5 Level II: Adaptive Building Control
  - 5.5.1 Strict Local Learning Contract
  - 5.5.2 Proximal Policy Optimisation
  - 5.5.3 Twin Delayed Deep Deterministic Policy Gradient
  - 5.5.4 Residual Control, Service Protection, and Local Safety
  - 5.5.5 Entity-Structured PPO
- 5.6 Level III: Decentralised Multi-Agent Control
  - 5.6.1 Centralised Training and Decentralised Execution
  - 5.6.2 MADDPG and the Original EnergAIze Formulation
  - 5.6.3 MATD3
  - 5.6.4 Alternative MARL Comparators
  - 5.6.5 Entity-Structured MATD3
  - 5.6.6 Evidence Produced at Level III
- 5.7 Prior Knowledge and Data-Efficient Learning
  - 5.7.1 Rule-Guided Exploration and Residual Policies
  - 5.7.2 Behaviour Cloning and Demonstration Use
  - 5.7.3 Replay as a Reusable Knowledge Source
  - 5.7.4 Offline Pretraining and Policy Distillation
- 5.8 Level IV: Hierarchical Community Coordination
  - 5.8.1 Decision Decomposition
  - 5.8.2 Global and Member-Specific Coordination
  - 5.8.3 Causal Signal Path and Neutral Parity
  - 5.8.4 Hierarchical Comparison
- 5.9 Cross-Method Synthesis and Open Limitations
  - 5.9.1 Contribution to the Research Questions
  - 5.9.2 Open Limitations
- 5.10 Chapter Summary

### 6. TI-MARL: Typed-Interface Multi-Agent Reinforcement Learning for Reconfigurable Cyber-Physical Systems

- 6.1 Scientific Positioning and Problem Formulation
  - 6.1.1 Closest Approaches and the Residual Problem
  - 6.1.2 Typed-Interface Decision Processes
- 6.2 Implemented TI-MARL Architecture
- 6.3 Entity-Bound Runtime Typed Interfaces
  - 6.3.1 Schemas, Entities, and Dynamic Module Instances
  - 6.3.2 Typed Observation Parts and Community Context
  - 6.3.3 Dynamic Action Groups and Typed Parameterised Ports
  - 6.3.4 Health-Aware Causal Compilation
- 6.4 Local Typed-Interface Policies
  - 6.4.1 Local Information Boundaries and Parameter Sharing
  - 6.4.2 Hierarchical Typed Encoding and Local Latent State
  - 6.4.3 Dynamic Grouped Action Decoding
  - 6.4.4 Constraint-Aware Local Bundle Construction
- 6.5 Multi-Agent Learning and Community Coordination
  - 6.5.1 Joint Training and Decentralised Execution
  - 6.5.2 Local and Central Set Critics
  - 6.5.3 TI-PPO and TI-MAPPO
  - 6.5.4 Community Observations, Rewards, and Learned Coordination
  - 6.5.5 Training Stability and Time Resolution
  - 6.5.6 Reusing Prior Knowledge without Extending Runtime Authority
- 6.6 Typed Constraints, Safety, and Runtime Robustness
  - 6.6.1 Typed Constraint Relations
  - 6.6.2 Boundary of Shared-Constraint Enforcement
  - 6.6.3 Runtime Assurance and Degraded Modes
- 6.7 Compatibility and Typed Explainability
  - 6.7.1 Interface Snapshots and Admission
  - 6.7.2 Checkpoint, Export, and Actor-Only Handoff
  - 6.7.3 Execution-Level Decision Traces
  - 6.7.4 Formal and Operational Properties
- 6.8 Experimental Methodology and Baselines
  - 6.8.1 Comparison Design and Reference Methods
  - 6.8.2 Reconfiguration Scenarios, Ablations, and Metrics
  - 6.8.3 Temporal Split, Seeds, and Selection Gates
- 6.9 Results and Comparative Analysis
  - 6.9.1 Implemented and Verified Behaviour
  - 6.9.2 Multiple Assets, Reconfiguration, and Held-Out Compositions
  - 6.9.3 Health-Aware Robustness and Local Safety
  - 6.9.4 Multi-Agent Coordination and Shared Constraints
  - 6.9.5 Scalability and Runtime Cost
  - 6.9.6 Ablations, Explainability, and Boundary Conditions
- 6.10 Discussion, Generality, and Contribution to the Research Questions
- 6.11 Chapter Summary

### 7. EnergAIze Policy Lifecycle: Experiment Orchestration and Distributed Inference

- 7.1 Deployment Problem and Lifecycle Contract
- 7.2 End-to-End EnergAIze Lifecycle Architecture
- 7.3 Experiment Orchestration on Heterogeneous Compute
  - 7.3.1 Job Orchestrator and Persistent Job State
  - 7.3.2 Common Worker Agent Contract
  - 7.3.3 Execution Target Profiles
- 7.4 Experiment Evidence and Operator Supervision
- 7.5 Policy Packaging and Distributed Inference
  - 7.5.1 Validated Bundle Contract
  - 7.5.2 energAIze Inference Runtime
  - 7.5.3 Inference Targets and Bundle Management
- 7.6 Monitoring, Failure Handling, and Recovery
- 7.7 Systems Evaluation, Availability, and Contribution to RQ4
- 7.8 Chapter Summary

### 8. EnergAIze in Operation: Real-World Deployment and Validation

- 8.1 Evidence Levels and Comparative Reading
- 8.2 OPEVA Demonstrator
  - 8.2.1 Control Problem and Physical Configuration
  - 8.2.2 EnergAIze Integration Path
  - 8.2.3 Scenarios and Validation Strategy
  - 8.2.4 Results and Demonstrated Boundary
- 8.3 DemFlex Demonstrator
- 8.4 Cross-Demonstrator Lessons and Simulation-to-Operation Differences
- 8.5 Contribution to the Research Questions and Chapter Summary

### 9. General Discussion and Answers to the Research Questions

- 9.1 What the Combined Evidence Establishes
- 9.2 Answer to RQ1: Dynamic and Heterogeneous Multi-Agent Control
- 9.3 Answer to RQ2: Multi-Dimensional Scalability of Learning and Coordination
- 9.4 Answer to RQ3: Safe and Robust Operation
- 9.5 Answer to RQ4: Governed and Deployable MARL Lifecycle
- 9.6 Interactions among the Four Requirements
- 9.7 Scientific Contributions, Generality, and Responsible Use
- 9.8 Limitations and Threats to Validity
- 9.9 Implications and Open Research Problems

### 10. Conclusions and Future Research

- 10.1 What the Research Established
- 10.2 Answers to the Research Questions
- 10.3 Principal Contributions
- 10.4 Assessment of the Central Proposition
- 10.5 Limits of the Conclusions
- 10.6 Future Research Directions
- 10.7 Closing Remarks

### Appendix A. Reproducibility and Supplementary Material

- A.1 Claim and Evidence Inventory
- A.2 Scenario and Environment Manifests
- A.3 Canonical Annual Dataset Contract
  - A.3.1 Calendar, Price Forecasts, and Settlement
  - A.3.2 Demand, PV, and Stationary Storage
  - A.3.3 Electrical Connections and Phase Allocation
  - A.3.4 EVs, Sessions, and Deferrable Services
  - A.3.5 Topology and Robustness Calendars
  - A.3.6 Matched Annual Baseline Scorecard
- A.4 Simulator Audits and Demonstrative Results
  - A.4.1 Software and Contract Verification
  - A.4.2 Selected Capability Demonstrations
  - A.4.3 Performance and Scalability Smoke Benchmarks
- A.5 Simulator KPI Catalogue
- A.6 Controller, TI-RL, and TI-MARL Configurations
  - A.6.1 Executable Controller Inventory
  - A.6.2 Observation, Action, and Training Record
  - A.6.3 TI-MARL Reproducibility Contract
  - A.6.4 Reward Profile Ledger
- A.7 Hyperparameters, Seeds, and Statistical Procedures
- A.8 Supplementary and Negative Results
- A.9 Lifecycle and Deployment Records
- A.10 Software, Data, and Archival Record

## Perguntas para discutir

### 1. Título da tese

O título e o subtítulo estão adequados ou devem ser simplificados?

Título atual:

Multi-Agent Reinforcement Learning Control of Distributed Mixed Cooperative--Competitive Real-World Cyber-Physical Systems

Subtítulo atual:

Case Studies in Smart Energy Management

Pontos a confirmar:

- O título principal está demasiado longo?
- A expressão Mixed Cooperative--Competitive é necessária no título?
- Real-World é defensável perante os diferentes níveis de evidência utilizados?
- O subtítulo representa suficientemente as Renewable Energy Communities, o carregamento de EVs e os demonstradores?

Decisão:

### 2. Estrutura global

A sequência dos dez capítulos conta a história da tese com a separação correta entre arquitetura, simulador, controladores, TI-MARL, ciclo de vida/deployment e demonstradores?

Pontos a confirmar:

- O equilíbrio de dimensão e detalhe entre os Capítulos 3--8 é adequado?
- O Capítulo 7 deve permanecer como contribuição autónoma de ciclo de vida e deployment?
- O Capítulo 8 deve manter OPEVA e DemFlex como demonstradores separados?
- O material de reprodutibilidade está corretamente concentrado no Appendix A?

Decisão:

### 3. Páginas depois da epígrafe

Deve manter-se, na versão digital e na versão para impressão, a página de copyright seguida por um verso em branco antes da Declaration of Honour?

Nota atual:

- A página que contém apenas “© Tiago Fonseca, 2026” é a página de copyright.
- A página seguinte fica vazia porque o documento usa composição twoside/openright e faz a Declaration começar numa página ímpar.
- A sequência é intencional, mas convém confirmar se a FEUP a pretende também no PDF exclusivamente digital.

Decisão:

### 4. Declaration of Honour

O modelo oficial da FEUP agora reproduzido na tese está correto na sua redação e apresentação gráfica?

Nota atual:

- A formulação anterior, redigida especificamente para a tese, foi substituída pelo texto indicado pela FEUP.
- O espaço para data e assinatura foi mantido em branco de acordo com o modelo fornecido.

Decisão:

### 5. Declaration on the Use of Generative Artificial Intelligence

A declaração atual é suficiente e está alinhada com as regras da FEUP/U.Porto para teses de doutoramento?

Pontos a confirmar:

- É necessário identificar explicitamente as ferramentas utilizadas?
- Devem ser indicadas separadamente as utilizações em organização, revisão linguística, escrita, programação e testes?
- É necessário declarar partes ou capítulos específicos?
- Deve ficar explícito que nenhuma fonte, resultado experimental, número ou conclusão científica foi aceite sem verificação?
- Existe uma formulação institucional obrigatória ou recomendada?

Nota atual:

O texto foi revisto como uma declaração final. A IA é descrita como parceira de investigação, escrita e desenvolvimento de software, mantendo-se explícitos os mecanismos de verificação, os limites do seu uso e a responsabilidade integral do autor. Falta apenas confirmar se a FEUP exige a identificação nominal de cada sistema e versão utilizados.

Decisão:

### 6. Statement on Co-Authored Work

Deve existir uma secção autónoma de coautoria, mesmo quando a Declaration of Honour já refere que o trabalho colaborativo é identificado?

Nota atual:

- A Declaration of Honour apenas declara responsabilidade e remete para a identificação das contribuições.
- O Statement on Co-Authored Work tem uma função diferente: documentar quais os trabalhos colaborativos utilizados e qual foi a contribuição de cada pessoa.
- A declaração identifica o autor como responsável pela conceção da arquitetura global do projeto, da qual nasceram componentes de suporte e spin-offs técnicos por ele propostos e formulados.
- A tabela foi reservada aos componentes e ferramentas usados diretamente na tese; as publicações permanecem na lista de resultados científicos e nas referências.
- A tabela identifica o componente, os coautores ou contribuidores, o papel do autor e a localização do material na tese.
- O parágrafo genérico sobre supervisão de estudantes foi removido. A participação de estudantes será indicada apenas quando estiver ligada a material efetivamente utilizado.

Pontos a confirmar:

- A FEUP exige uma declaração autónoma para teses que integram trabalho coautorado?
- É preferível uma tabela de contribuições, uma declaração por capítulo ou ambas?
- Deve usar-se a taxonomia CRediT?
- Qual o grau de detalhe necessário relativamente a orientadores, colegas, estudantes e parceiros industriais?

Decisão:
