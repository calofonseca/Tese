# Source and Provenance Notes

## Candidate source

The first drafting basis is the 2024 Doctoral Thesis Research Plan (TRP):

- working title and subtitle;
- author and programme;
- initial problem framing around distributed mixed cooperative--competitive CPS;
- smart energy management as the case-study domain;
- preliminary focus on scalability, deployability, safety/security, and robustness;
- preliminary edge-deployment and training/runtime architecture.

The thesis draft does not silently preserve every TRP decision. The TRP describes planned work and contains terminology that has since been refined. In particular:

- `Safety` and `Security` are now separated;
- EnergAIze is positioned as an integrated energy-domain research platform;
- the thesis includes a substantial simulator contribution and lifecycle-orchestration contribution;
- the final co-supervisor must be confirmed;
- the final RQs and contribution claims remain subject to evidence audit.

## External literature

References included in Chapter 1 were selected from official legislation, primary publication pages, established books, and peer-reviewed surveys. Full critical review and gap claims belong to Chapter 2 and require a documented evidence matrix rather than a small convenience sample.

## OPEVA and Chapter 8 demonstrator context

The August 2026 Chapter 3/8 revision used two author-supplied sources:

- `Manuscript V3.docx`, an unpublished working manuscript describing the OPEVA demonstrator, its 17-installation real-data simulation campaign, 18-month/15-minute dataset, EnergAIze architecture, controller comparisons, and performance/equity analysis;
- `OPEVA - D6.3 - Presentation of all final demonstrators_V1.0.pdf`, the approved 22 April 2026 OPEVA deliverable, especially Section 3.8, Demo 9 --- Flexible Charging Scheduler.

The sources serve different purposes. D6.3 supports the Demo 9 sites, installed charging equipment, partner platforms, protocols, components, implementation status, and scenario-level evidence boundaries. The manuscript supports the later 17-installation experimental framing and current performance/equity campaign. D6.3 also reports an earlier nine-building benchmark with a different dataset and time resolution. The two campaigns must remain separate in Chapter 8.

The four-building real-world REC study is part of the OPEVA evidence and remains cited through `fonseca2025realworldrec`. DemFlex is a separate demonstrator and requires its own authoritative context before site, asset, controller, or result claims are added.

## EnergAIze Chapter 3 narrative decision

Chapter 3 is organised around the concrete EnergAIze framework rather than generic architectural planes or lifecycle flows. The entry point is the complete building-level framework shown in `Manuscript V3.docx`: Algorithms/FSA, Percepta and the Data Provider, the Fail-Safe Supervisor, prediction, PulseCharge, the local data record, external platforms, and physical assets. CityLearn/EVLearn and the experiment/policy lifecycle are retained as supporting development capabilities. The main TikZ figure is a thesis-specific redraw of the manuscript and OPEVA D6.3 architecture and therefore requires a final attribution and permission check.

## CityLearn v3 Chapter 4 source and narrative decision

The August 2026 Chapter 4 rewrite used the simulator paper and its internal evidence bundle in `/home/tiago/dev/Simulator` as its principal technical source:

- `citylearn_paper_overleaf/main.tex` and the compiled manuscript figures;
- `docs/paper/simulator_paper_context_pack.md` for implementation lineage and contribution scope;
- `docs/paper/simulator_paper_benchmark_results.md` and the final manuscript tables for measured validation and computational evidence.

The thesis chapter does not reproduce the paper verbatim, but it now follows the paper's strongest methodological ordering where this improves readability. It is organised around one causal argument: realistic REC conditions must remain traceable from scenario declaration to controller-visible input, requested action, applied action, and reported physical/service outcome. The long environment survey in the previous draft was condensed into a role-based positioning section, while the architecture section now contains the developed simulator capabilities in a coherent sequence: scenario and time contracts, electrical and flexibility assets, local services, topology and health events, multiple communities, and controller interfaces.

Following the 21 August 2026 structural review, Chapter 4 uses seven top-level movements: research contribution; problem, requirements, and positioning; architecture and REC modelling capabilities; canonical annual datasets; evaluation protocol and scorecard; verification and current evidence; and contribution boundaries. The inherited-environment gap was merged into the requirements section, the iterative-development and public-release accounts were combined, and the controller-lifecycle subsection was rewritten around development, pre-deployment qualification, and post-deployment replay. The datasets deliberately follow the simulator capabilities, so that the reader first understands what the environment represents and only then how the canonical suite exercises it. The main text defines a layered controller scorecard; the broader KPI catalogue is retained in Appendix~A.4.

Following author feedback, the chapter now opens with a dedicated account of why the simulator changed from supporting infrastructure into a research contribution. It distinguishes the intended scope of CityLearn v2/EVLearn from the combined requirements introduced by the thesis, explains the cross-cutting implementation burden behind apparently individual features, and connects simulator, algorithm, and demonstrator development as an iterative research process.

The simulator is also treated as an explicit component of the controller-to-deployment pipeline. It does not deploy a policy to the edge; it supplies the versioned environment, scenario, data, event, interface, reward, constraint, baseline, and evaluation contracts used for experiment reconstruction, validation, promotion, packaging compatibility, incident replay, and revalidation. Chapter 4 now maps that role to RQ1--RQ4 and to the four cross-cutting requirements of scalability, deployability, safety, and robustness; Chapter 7 contains the reciprocal lifecycle bridge.

The thesis uses *CityLearn v3* as the scientific name for the simulator generation documented in the associated manuscript. Its public installable distribution is the SoftCPS REC Simulator (`softcpsrecsimulator`), which retains the `citylearn` import path. The public SoftCPS repository is a research fork; it must not be described as replacing or constituting a release of the separate upstream CityLearn repository. Public-release facts were checked on 20 August 2026: PyPI version 1.7.0, MIT licence, and source/wheel distributions. The statement that release prompted exchanges with researchers at multiple universities is author-supplied qualitative dissemination evidence and is deliberately not presented as a quantified adoption or independent-validation claim.

Quantitative test counts, performance measurements, and application examples are attributed to the evaluated manuscript evidence bundle. They must be regenerated or explicitly tied to the final archived simulator release if the implementation changes before thesis submission. The six reused vector figures are author-produced manuscript artefacts; their final caption wording and publication/attribution status should be checked when the simulator paper is submitted or published.

## AI-assisted drafting

The initial structure and prose were prepared with generative-AI assistance under the author's direction. The candidate must review every paragraph, verify every citation, replace provisional claims, and ensure that the final wording reflects the research accurately.
