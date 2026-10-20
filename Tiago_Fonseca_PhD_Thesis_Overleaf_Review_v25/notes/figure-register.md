# Thesis Figure Register - TI-MARL Revision v16

## 2026-10-19 — Generic mechanism figure withdrawn from the review

Removed the Figure 3.3 inclusion, caption, label and introductory paragraph from Section 3.3.2 at the author's request. The editable vector source and standalone asset remain available for possible later use. The published review now retains only the actor–critic schematic; no reference to the removed label remains in the chapter.

## 2026-10-19 — Moderate reduction of Figure 3.3

Reduced the mechanism comparison from 1000 × 840 to 1000 × 720 by tightening vertical gaps and entity spacing. Retained the four rows, all explanations, colours, font sizes and vector format. The scientific content is unchanged. Editable source remains `figures/build_review_configurations.py`.

## 2026-10-19 — Compact actor–critic schematic

Redesigned Figure 3.2 at 1000 × 430 points instead of 1000 × 830, reducing its height by 48% at the same page width. Three aligned columns distinguish critic inputs and actor-learning signals, with a single shared local-execution strip. MATD3 shows the actor update from Q1 and explains the minimum target used for both critics. Target-network details remain in prose. The figure now precedes the individual method descriptions. Source remains `figures/build_review_configurations.py`; the Section 3.3.2 mechanism figure is unchanged.


## 2026-10-19 — Actor–critic comparison and generic representation mechanisms

Added `fig:ch3-actor-critics` in Section 3.3.1, comparing replay-based MADDPG and MATD3 with on-policy MAPPO. The schematic distinguishes one action-value critic, twin critics with a lower target estimate and delayed actor update, and a state-value critic supplying advantages to PPO. It separates centralised training from local execution and is attributed to the three original studies already present in the bibliography.

Replaced the rejected energy-specific changing-community figure in Section 3.3.2 with `fig:ch3-variable-configurations`, a generic four-row comparison of set aggregation, attention, graph message passing and typed modules. Generic entity identifiers and repeated colours make the processing and output association explicit; the set row correctly produces a pooled summary rather than individual commands. Removed the previous title and all household/battery imagery. Both vector PDFs are maintained by `figures/build_review_configurations.py` as `review-actor-critics.pdf` and `review-variable-configurations.pdf`.


## 2026-10-18 — Comparing architectures for changing community configurations

Added an original vector comparison in Section 3.3.2, labelled `fig:ch3-variable-configurations`. The same member A receives battery B3 while member B leaves with battery B2. Three parallel panels explain entity collections with sets/attention, graph relationships, and repeated typed modules; command recipients retain their resource identifiers. Dashed outlines identify additions and crossed elements identify departures. This is a conceptual illustration of the reviewed mechanisms, which can be combined, not an implemented controller or an empirical result. The source reuses the thesis equipment symbols and palette: `figures/build_review_configurations.py`; vector output: `figures/review-variable-configurations.pdf`.


## 2026-10-16 — Figure simplified at the author's request

Figure 3.1 now shows only author–year references in its right-hand column, aligned with the corresponding left-hand stages. Explanations of what each source contributes remain in the following prose paragraph. Restored “Counterfactual comparison” as the stage-5 name and aligned the term and conditional formulation in 3.1.3. The Booth attribution in the prose continues to concern disconfirming cases. Caption shortened to “Review stages and methodological sources.” The figure remains on PDF page 89 and the explanation on page 90. Recompiled the thesis and standalone vector export and visually verified their layout; no unresolved references/citations or new overflows. Section 3.2 onward unchanged. Working files: `../tmp/pdfs/ch31-figure-simplified-2026-10-16/`.

## 2026-10-16 — Precise methodological attribution and compact placement

Figure 3.1 now labels stage 5 “Critical comparison and disconfirming evidence”; its source column specifies Booth et al.'s disconfirming cases in qualitative evidence synthesis. This replaces the previous counterfactual title. Retained the other stage/source mappings and revised vertical spacing, preserving text sizes. The callout closes the first paragraph of 3.1 and the diagram fits on the same page (PDF 89, printed 45); methodological explanation starts on the next page. Checked the in-thesis rendering and standalone vector export. Source: `figures/review-protocol.tex`; export: `figures/review-protocol.pdf`.

## 2026-10-15 — Explain the source contribution at each review stage

Revised Figure 3.1 so that the right-hand column explains what is adapted from each source: search planning (Kitchenham and Charters), citation rounds (Wohlin), eligibility and staged screening, extraction forms and appraisal (Kitchenham and Charters), concept matrices (Webster and Watson), and disconfirming cases to challenge interpretations (Booth et al.). The author wants methodological citations attached to a clear borrowed procedure, not presented merely as author names.

Made “Counterfactual comparison” the prominent stage-5 title. Its description now identifies assessment of adopting an existing method through capabilities, assumptions and unresolved needs. Booth supplies the disconfirming-case rationale; the adoption comparison remains the thesis's analytical adaptation. Expanded row spacing for legibility and updated the caption. Both the native TikZ figure and its standalone PDF were checked, together with PDF pages 90–92.

## 2026-10-16 — Review stages aligned with subsection names

Renamed the first four Figure 3.1 stage titles to Search terms and sources; Eligibility criteria and study selection; Evidence extraction and appraisal; Comparative synthesis. The figure now belongs to the 3.1 methodological overview, with its caption mapping the stages to 3.1.1, 3.1.2 and 3.1.3. Counterfactual comparison and source attributions remain. Recompiled and visually checked the standalone vector export and the thesis placement.

## 2026-10-16 — Review protocol wording aligned with the executed search

Figure 3.1 retains its five stages and source attributions. Changed the Wohlin label to cited-work searching and simplified the counterfactual detail to assessing existing solutions. Adjusted the label length to preserve spacing below the column heading. Recompiled the standalone vector export and checked it alongside the final thesis placement on PDF page 90. Source: `figures/review-protocol.tex`; maintained export: `figures/review-protocol.pdf`.

## 2026-10-15 — Review protocol and methodological sources

Added the original editable vector figures/review-protocol.tex at fig:ch3-review-protocol in the introduction to 3.1. Five numbered stages show search, selection, extraction/appraisal, concept-based synthesis, and testing candidate gaps against existing alternatives. The sources are aligned with their respective procedures. Booth et al. support disconfirming cases; the counterfactual adoption comparison is the thesis's analytical use of alternatives, not attributed to Booth as a named search protocol. The diagram represents the prospective protocol and contains no invented screening counts.

The restrained sage/terracotta palette, numbered route and explicit labels remain readable in greyscale. The diagram appears on printed page 46, immediately after the method framing and before 3.1.1. figures/review-protocol-standalone.tex provides a reusable export wrapper; figures/review-protocol.pdf is the corresponding standalone PDF. Both the standalone rendering and the figure in the thesis were visually checked.

## 2026-10-14 — Representation illustration heading removed

Removed “One site, three resource records” from foundations-representations.pdf as requested. Centred the existing battery/charger icons above the three panels. The vector/set/graph examples, dimensions, caption and remaining labels are unchanged. Regenerated only this figure through build_foundations_extended.py.

## 2026-10-14 — Compact offline and hierarchy illustrations

Reworked foundations-offline.pdf from 800×235 to 800×152 points, retaining collection, fixed dataset, repeated learning and policy use in a single compact flow. Reworked foundations-hierarchy.pdf from 800×350 to 800×206 points. The same hourly signal branches to two site policies; local conditions distinguish a charging request from zero power, with local decisions every fifteen minutes. The concrete response example replaces the earlier large stacked hierarchy and separate timeline. Both original vector figures remain maintained by build_foundations_extended.py; captions were shortened alongside the exposition. Other figures are unchanged.

## 2026-10-14 — Neural and advanced foundations figures implemented

Added foundations-neural.pdf and redesigned foundations-offline.pdf, foundations-hierarchy.pdf, foundations-representations.pdf, foundations-attention.pdf and foundations-modular.pdf. All six are original vector illustrations in a consistent terracotta/sage palette, generated by figures/build_foundations_extended.py. The legacy build_foundations_diagrams.py entry point delegates its advanced figures to that builder to avoid restoring superseded artwork. The existing resources, RL interaction and CTDE illustrations remain unchanged.

The neural figure distinguishes three measured features, four learned hidden components and one output. Offline separates collection, fixed archive, repeated learning and later use. Hierarchy shows coordinator/site decisions and their time scales. Representations compare vector positions, entity sets and relations using battery B and chargers C1/C2, then introduce C3. Attention shows queries/keys/values and a post-normalisation Transformer block with residual paths. Modular decoding reuses the same charger parameters for separate charger outputs and a different decoder for the appliance action. Figures are integrated with the running examples; conceptual attributions appear in captions where appropriate.

## CTDE illustration implemented, 14 October 2026

Added original vector figures/foundations-ctde.pdf, generated by figures/build_foundations_ctde.py, at fig:ch2-ctde in 2.3.2. Two panels reuse the same site and actor symbols. Joint observations/actions reach a centralised critic during training; dashed arrows show policy updates. In execution, local inputs reach the actors and produce charging powers. Warm terracotta/sage palette follows Figure 2.4. Based on Lowe et al. (2017), attributed in the caption. Supersedes the pending CTDE proposal below. Restored concise prose to avoid repeating the figure.

## Section 2.3 organisation table revised; figure proposal pending, 13 October 2026

Reworked tab:ch2-learning-organisation into three dimensions: learning information, action selection and policy parameters, with REC interpretations. The author requested text first and any image proposals in the final response. No new artwork was created; a diagram contrasting joint learning information with local execution could clarify CTDE in a later approved visual pass.

## Reward-objective table removed, 13 October 2026

Removed Table 2.3 Roles and notation in specifying and evaluating a learning objective, including its introducing sentence and tab:ch2-objective-concepts label, at the author's request. No other source references used that label. All figure artwork remains unchanged; later tables renumber through LaTeX.

## Figure 2.4 — compact editorial redesign, 13 October 2026

Rebuilt figures/foundations-rl-cycle.pdf with figures/build_foundations_rl_cycle.py as an original vector diagram. Warm terracotta and sage accents, cream/mist circular emblems, serif entity names and restrained sans-serif labels replace the earlier blue/green rectangular boxes. Two labelled directional channels show action going to the environment and next state plus reward returning to the agent. The fully observable MDP meaning and r_t-after-a_t convention are preserved, with the existing Sutton and Barto caption attribution. Artwork is 740 × 235 points and is placed at 86% text width, reducing its printed height by about 26% relative to the previous figure. Other figures are unchanged.

## Information-source table removed, 13 October 2026

Removed the former Table 2.2 describing information sources at the author's request. The retained availability/health/dependency/degraded-operation table is now Table 2.2. All artwork and figure captions remain unchanged; compilation updates later table numbering and page references automatically.

## Foundations flexibility figures — updated 13 October 2026

Figure 2.1 remains the community pyramid with its yellow review reminder. Figure 2.2 is the attributed FlexOffer illustration, now placed immediately after its introduction and before the equations, at 90% text width; its artwork is unchanged. Figure 2.3 shows fixed, shiftable, and elastic asset operation. Added a stationary battery beside EV charging and a variable-speed heat pump in the elastic group, retaining the established native vector symbols, palette, and illustrated grouping. Only `resources()` in `figures/build_foundations_diagrams.py` was regenerated. The two new information/operational tables replace prose enumerations; the rejected cyber-physical figure remains removed.

## Foundations figure order, 12 October 2026 — author review

The revised explanation introduces FlexOffer before classifying resources. Its illustration is now Figure 2.1; the resource/flexibility comparison is Figure 2.2 and is called out before the device examples. Existing labels, captions, attribution, and vector artwork are unchanged.

## Foundations, 12 October 2026 — seven active vector figures

New Chapter 2 uses seven conceptual figures: resource flexibility, FlexOffer, fixed-dataset learning, hierarchy, vector/set/graph representations, attention, and modular action decoding. `figures/build_foundations_diagrams.py` generates six original vector PDFs using the established equipment pictograms and blue/green/gold palette. `build_foundations_flexoffer.py` supplies the adapted FlexOffer; its caption attributes Fonseca et al. (2022). Labels, callouts and captions are integrated. These figures explain concepts and contain no measured performance. The old combined-chapter figure plan is superseded for these sections. Chapter 3 uses four comparative tables, including the final four-RQ counterfactual comparison.

The new chapter split shifts the former Chapters 3–9 to 4–10. Historical entries below retain their date-specific numbering; source filenames and figure labels are unchanged.

## Chapter 1 research map removed, 11 October 2026 — author decision

Removed the research map and its callout from the final introduction section at the author’s explicit request. Neither the research map nor the earlier graphical abstract appears in the thesis. Source assets remain available but unused. This supersedes the active-use status recorded below.

## Chapter 1 research map, 11 October 2026 — author-selected replacement

The merged final section of Chapter 1 uses `figures/introduction-research-map.tex`, an editable TikZ map of the investigation and Chapters 2–9. Chapter references update automatically. The main arrows indicate chapter order; a dashed return from operational studies to the experimental environment indicates how experience informs development. Small line illustrations distinguish research, architecture, simulation, comparison, learning, installations, and synthesis. The chart icon is schematic and encodes no empirical results. The existing `fig:intro-graphical-abstract` label is retained to preserve references. Earlier graphical-abstract assets remain unchanged and unused; no front-matter abstract was added.

## Household-sharing figure removed, 11 October 2026 — author decision

Removed `fig:intro-energy-sharing` from Chapter 1 at the author's explicit request, together with its textual callout and caption. The existing files under `figures/introduction-energy-sharing*` and their builder are retained as unused assets. The graphical overview remains and is renumbered automatically. This supersedes the active-use status recorded below on 9 October.

This register accompanies the visible `\plannedfigure` placeholders in the LaTeX source. It is a production plan, not a claim that the underlying evidence already exists.

## Figure 1.1 final artwork, 9 October 2026

- `fig:intro-energy-sharing` now uses a finished vector illustration in `figures/introduction-energy-sharing.pdf`, generated by `figures/build_introduction_energy.py`. The two household boundaries identify the ownership of the stationary battery and the EV charger, with both household connections meeting a shared local electricity network.
- Arrows identify possible uses of a midday solar surplus: storage behind the producing household's connection and charging at the neighbouring household. They are illustrative energy-use paths, not measurements or dedicated peer-to-peer cables. The second household retains rooftop PV, consistent with the surrounding example.
- The figure uses embedded sans-serif fonts, the established blue/green/terracotta pictorial palette, uniform equipment outlines, and labels readable at the thesis text width. Direction, position and labels preserve meaning in greyscale. The main caption and short list-of-figures entry were updated to match the drawing. The Chapter 1 graphical abstract is a separate figure and is unchanged.

## Global rules

- Prefer vector PDF/SVG/TikZ for new conceptual diagrams and architecture figures. Preserve and reuse author-selected source figures when requested; Chapter 3 explicitly uses the original raster diagrams supplied by the author.
- Every figure must be introduced and interpreted in the text before or immediately after it appears. A figure should support a claim or reduce conceptual load; decorative stock imagery is excluded.
- Data plots must be generated from archived machine-readable results by a versioned script. Record software version, hardware, scenario, seeds/repetitions, aggregation, uncertainty, and exclusions.
- Use stable terminology across all figures: agent, asset, controller, policy, policy set, scenario, interface, observation part, action port, target, deployment, fallback.
- Site photographs and UI screenshots require permission, anonymisation, and a clear evidential purpose. A dashboard screenshot must not replace the underlying quantitative result.
- Captions should state what is shown and the evidence boundary. Source/adaptation/permission information belongs in the caption or a source note where required.
- Keep fonts readable at final A4 size (normally at least 8--9 pt), avoid colour-only encoding, and ensure print/greyscale legibility.

## Chapter 4: daily dataset interpretation, final pass, 1 October 2026

- New `fig:sim-dataset-daily` uses `simulator-portugal-daily.pdf`: two seasonal columns, each pairing mean demand/PV power above residential/service vehicle presence. Shared axes, the established blue/green/purple palette, and solid/dashed lines support comparison and greyscale reading. It extends the existing monthly seasonal view without replacing the original architecture or archived mechanism figures.
- `build_simulator_daily.py` is the editable plotting source. Aggregated quarter-hour profiles, time/season conventions, and source hashes accompany the PDF. The plotted quantities are unchanged scenario inputs and scheduled presence, not controller results. Both the standalone figure and final thesis page are inspected before delivery.

## Chapter 4: original preprint architecture restored, 1 October 2026

- The author's selected `simulator-environment-architecture.pdf` is active again, reproduced unchanged from the CityLearn v3 preprint's architecture asset. This supersedes the revised-vector selection below; that alternative and its builder remain available but unused.
- The seven chapter figures now accompany their explanatory sections: architecture, temporal resolution, complete appliance cycles, local settlement, changing resources, failure channels, and dataset seasonality. Their labels and source assets are preserved. The caption for the architecture credits the simulator paper.

## Chapter 4: simulator and dataset figures, 1 October 2026

- Historical alternative (now unused): `simulator-environment-architecture-revised.pdf` is a vector view generated by `build_simulator_figures.py`. Houses, resource icons, local controller interfaces, common simulation time, and local/combined evaluation follow Chapter 3's pictorial palette and shared controller symbol. Observations and actions remain separately labelled. The original manuscript architecture remains preserved.
- `simulator-portugal-seasonal.pdf` shows monthly daily-average non-shiftable demand and PV for both years, with line style distinguishing year and markers/colour distinguishing the signals. `simulator-portugal-member-energy.pdf` shows 2024 member-level demand/production, with shape distinguishing residences/services and a labelled equality reference. `simulator-portugal-services.pdf` shows session targets and appliance start-window slack, with boxplot definitions in its caption.
- Descriptive plots use the archived Portugal input series and descriptive CSV tables; hashes are in `simulator-dataset-figure-sources.json`. They show constructed input conditions, not controller performance. Existing timestep, cycle, settlement, topology, and failure figures retain their original archived evidence.

## Chapter 3: community and runtime readability, 30 September 2026

- Figure 3.2 now uses `energaize-community-deployment-revised.png`. The updated image enlarges the component names and observation/action labels, retaining the master's figure's community server, local controllers, and equipment illustrations. The original PNG remains available. The caption identifies this as an adaptation.
- Figure 3.3 now uses `energaize-runtime-revised.pdf`. Its editable source, `build_energaize_runtime.py`, draws the text, groups, connections, and controller in vector form, reusing five pictograms from the preserved original in `runtime-icons/`. The controller symbol matches the development/deployment views. The forecasting group explicitly contains Predictor and Flexon; Percepta has separate observation, proposed-action, validation, and equipment paths. The independently confirmed Supervisor has limiting and RBC-fallback responsibilities; Watchdog monitoring is a distinct dashed path. Repeated building instances occupy one compact row.
- Both views preserve the pictorial palette and portrait page orientation. Supersedes the earlier status below describing the community and runtime originals as unchanged in the active manuscript. The standalone runtime PDF is suitable for reuse in slides.

## Chapter 3 narrative and infrastructure figures, 30 September 2026

The building flow, community view, and complete runtime diagram retain the author's original images. Three editable vector companions use the established palette and illustrated computing/equipment symbols. `figures/build_energaize_lifecycle.py` generates their standalone PDFs. The original master's simulation figure remains preserved, while its position in the chapter now holds a dedicated learning/evaluation view.

The three vector views now share one controller symbol and one model-bundle symbol. Development identifies installation records (1), community configuration (2), prepared scenarios (3), training (4), evaluation (5), and the exported bundle (6). The orchestration view expands an experiment containing the simulator and controller, identifying training/evaluation as stages 4/5. Deployment starts with the same bundle (6), then continues through the catalogue (7), operator selection (8), and backend loading (9). The controller is visible inside the inference service. These shared objects connect the figures without adding another overview; the surrounding prose maps the controller back to the original runtime diagram's EnergAIze Algorithm block. Community and experiment configuration remain generic, with the runtime input/output description exported in the model contract.

| Label | Chapter | Visual type | Purpose | Status |
|---|---:|---|---|---|
| fig:energaize-development | 3 | Pictorial development flow | Records/configuration, simulated interaction, policy learning, fixed-policy evaluation, and selected bundle | `energaize-controller-development.pdf`, editable vector |
| fig:energaize-orchestration | 3 | Computing deployment view | Host boundaries, separate worker/experiment containers, local and remote execution, shared job interface | `energaize-orchestration.pdf`, editable vector; placement checked against compose definitions |
| fig:energaize-deployment | 3 | Pictorial deployment and runtime flow | Model bundle, operator selection, inference, Percepta, and action supervision | `energaize-model-deployment.pdf`, editable vector |

## Planned figures

Chapter 2 update, 8 October 2026: `fig:ch2-flexoffer` is the completed Figure 2.1, generated by `figures/build_foundations_flexoffer.py` as `foundations-flexoffer.pdf`. It is a vector adaptation of Figure 1 in Fonseca et al. (2022), DOI 10.3390/en15238875, with original explanatory example values. It shows independent start-time choice and energy bounds per interval, including a selected schedule. Colours match the blue/green/gold thesis palette; hatching and line style preserve greyscale meaning. The reconfiguration figure is unchanged and is automatically numbered Figure 2.2.

| Label | Chapter | Visual type | Intended claim/purpose | Required source or status |
|---|---:|---|---|---|
| fig:intro-graphical-abstract | 1 | Graphical abstract | EnergAIze architecture frames experimental foundations and deployment/evaluation; central renewable energy community with one local agent per building, enlarged TI-MARL compiler/shared actor/local feasibility loop, and TI-MAPPO training over active agents | Provisional AI-generated vector TikZ in figures/introduction-graphical-abstract.tex; marked in yellow for later replacement at the author's request on 28 September 2026; replaces the two former introductory overview diagrams |
| fig:ch2-reconfiguration-vocabulary | 2 | Completed TikZ conceptual diagram, revised 2026-09-14 | State, availability, local composition, and agent population, with semantic-type extension distinguished; no ordered difficulty hierarchy | Chapter 2 critical synthesis and declared known-type scope |
| tab:ch2-evidence-levels | 2 | Completed comparison table, revised 2026-09-14 | Complementary simulation, hardware, testbed, shadow, and operational settings; real-data provenance is a separate attribute | Replaces the planned evidence ladder |
| fig:energaize-building-loop | 3 | Original master's dissertation Figure 6, restored 2026-09-29 | Data inputs form the State of the Environment; EnergAIze determines actions for flexible assets | `figures/energaize-information-actions.png`; original image copied without alteration at the author's request |
| fig:energaize-community | 3 | Adapted master's dissertation Figure 8, revised 2026-09-30 | Local building controllers receive shared information and act on heterogeneous equipment | `figures/energaize-community-deployment-revised.png`; larger labels and separate observation/action arrows; the source PNG is retained |
| fig:energaize-overview | 3 | Coded redraw of the author-supplied runtime image, revised 2026-09-30 | Percepta connects observations, supporting services, controller, independent action validation, monitoring, records, and installation interfaces | `figures/energaize-runtime-revised.pdf`; vector text and connections, reused pictograms, distinct Predictor/Flexon, shared controller symbol; portrait orientation; original PNG retained |
| fig:energaize-development | 3 | Illustrated controller-development architecture, revised 2026-09-30 | Installation records and configuration support training and fixed-policy evaluation, followed by model selection and export | `figures/energaize-controller-development.pdf`; original master's image remains preserved as `energaize-simulation-deployment.png` |
| fig:sim-architecture | 4 | System architecture | CityLearn v3 as a complete multi-community REC environment with buildings, assets, local sharing, demand response, events, controllers, and KPIs | `simulator-environment-architecture.pdf`; original preprint figure restored unchanged at the author's request |
| fig:sim-high-frequency | 4 | Multi-resolution data plot | Identical annual energy can expose materially different peaks at 1 h, 15 min, and 15 s | Included from the archived deterministic trace-replay evidence; vector PDF |
| fig:sim-deferrable-cycle | 4 | Service timeline/profile | Deferrable control shifts a complete cycle inside a valid start window without erasing its deadline | Included from the simulator manuscript source bundle; vector PDF |
| fig:sim-rec-settlement | 4 | Multi-panel accounting result | Local energy sharing changes community and participant outcomes even for the same physical trajectory | Included from the archived annual settlement example; vector PDF |
| fig:sim-dynamic-topology / fig:sim-topology-timeline | 4 | Event/result timeline | Member and asset changes propagate to the active entity set and controller contract | Included from the archived dynamic-topology example; vector PDF |
| fig:sim-robustness-channels | 4 | Control-loop event plot | Observation, forecast, action, and equipment failures act on distinct channels and remain auditable | Included from the archived robustness example; vector PDF |
| fig:sim-dataset-daily | 4 | Seasonal daily input and vehicle-presence profiles | Explain coincidence and mismatch between non-shiftable demand, PV, and residential/service charging availability | `simulator-portugal-daily.pdf`; archived Core-30 inputs, 2024 Monday-Friday local-time means, vector plot |
| fig:control-progression | 5 | Cumulative progression | Problems solved and assumptions remaining at each stage | Method/claim/evidence ledger |
| fig:control-common-protocol | 5 | Experiment protocol | Fair information, budget, seed, KPI, and statistics rules | Frozen protocol |
| fig:maddpg-matd3-comparison | 5 | Algorithm + metric schematic | Standard change and thesis-specific comparison | Frozen code/results |
| fig:hierarchical-control-architecture | 5 | Two-level control diagram | Community coordinator and local workers | As-built hierarchy |
| fig:control-comparative-results | 5 | Multi-panel data plot | Control, learning, service, and resource results | Verified seed-level table |
| fig:validation-evidence-levels | 7 | Evidence ladder with cases | OPEVA and DemFlex evidence classified independently | Audited demonstrator records |
| fig:operational-contexts-topology | 7 | OPEVA site and integration topology | Three sites, physical assets, partner platforms, EnergAIze path, action authority | OPEVA D6.3, as-built sites, partner permissions |
| fig:operational-runtime-timeline | 7 | OPEVA operational timeline | Actions, states, data incidents, intervention, updates | Aligned OPEVA timestamp logs |
| fig:realworld-results | 7 | Print-ready comparative plots | OPEVA and DemFlex results separated by evidence level | Final audited demonstrator results |
| fig:sim-to-operation-gap-map | 7 | Cross-demonstrator assumption/evidence map | What changed from simulator to OPEVA and DemFlex operation | Incident/integration logs |
| fig:rq-evidence-map | 8 | RQ-finding traceability | Direct/supporting evidence and boundaries | Final claim-evidence matrix |
| fig:requirement-tradeoff-map | 8 | Trade-off/causal map | Interactions among four requirements | Cross-chapter findings |
| fig:thesis-contribution-stack | 9 | Synthesis diagram | Cumulative contributions and RQ answers | Final contribution list |

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
