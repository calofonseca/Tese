# Thesis Writing Style

## Voice and readability

- Write in formal, direct English.
- Prefer a clear sentence over an impressive-sounding sentence.
- Introduce a concrete example when an abstract concept first appears.
- Explain why a concept matters before adding technical detail.
- Keep paragraphs connected: the last idea of one paragraph should prepare the next.

## Terminology

Use one stable term for each recurring concept.

- `cyber-physical system` / `CPS`
- `renewable energy community` / `REC`
- `agent`, `asset`, `controller`, and `policy` are distinct
- `scalability`, `deployability`, `safety`, and `robustness` retain the definitions in Chapter 1
- `security` is not a synonym for `safety`
- `transferability` is not a synonym for `deployability`
- `real-world operation` must identify the actual evidence level
- `EnergAIze` is the integrated research platform and energy-domain reference implementation, not the thesis itself

Avoid inventing synonyms merely to create variety. Repeating the correct technical term is preferable to changing its meaning.

## Claims and evidence

- Put evidence near the claim it supports.
- Distinguish measured findings from expected or potential impact.
- Distinguish real data in simulation from physical deployment.
- State the evaluated scale and remaining bottleneck instead of writing only that a method is scalable.
- Avoid `few works`, `the literature lacks`, or `state of the art` without a defined corpus or strong supporting sources.
- Report negative or inconclusive results when they affect the thesis argument.

## Chapter flow

Each technical chapter should normally contain:

1. the specific problem and claim;
2. related work needed locally;
3. method or artefact;
4. experimental design;
5. results;
6. local discussion and limitations;
7. contribution to the research questions;
8. transition to the next chapter.

## Examples

Examples should make the argument easier to follow, not serve as substitutes for definitions. Prefer recurring examples from EV charging and energy communities so the reader does not have to learn a new domain in every section. Use examples from robotics, transport, or industrial CPS only when they clarify the generality of a property.

## Cumulative research story

The thesis should not read as a catalogue of algorithms and should not describe every pre-TI-MARL method as a failed attempt. For every stage, use the same narrative unit:

1. problem encountered;
2. solution introduced;
3. evidence and result;
4. what was solved;
5. conditions under which it was solved;
6. remaining assumption or new problem revealed.

TI-MARL is then introduced as the integration and generalisation of selected solutions whose assumptions did not automatically compose under reconfiguration. The same requirements that motivate TI-MARL become its evaluation criteria.

## Principal roles

- **TI-MARL**: principal algorithmic contribution.
- **MATD3**: important method, empirical contribution, and possible TI-MARL backbone; not the overall unifying contribution.
- **EnergAIze**: integrated research architecture and energy-domain reference implementation.
- **Chapter 5 methods**: solutions, evidence, teachers, fallbacks, backbones, or mechanisms; not a flat list of equal contributions.

## Preferred explanatory pattern

Prefer:

> MATD3 reduced the observed critic overestimation and seed variability under the evaluated REC scenarios, while retaining a fixed agent interface.

Avoid:

> MATD3 solved instability.

Every solved-problem statement should include the scope and the remaining boundary.

## Section hierarchy and minimum substance

The numbered hierarchy must follow the substance of the argument rather than the number of implementation details available.

- A numbered `\section` (for example, 4.3) must carry a distinct idea, claim, evidence block, or argumentative movement. It should be long enough to justify a visible break, or contain enough substantial subsections to do so.
- A numbered `\subsection` (for example, 4.3.1) should normally sustain approximately one to two pages of final thesis text, including the method, evidence, figure, table, or discussion associated with that point.
- A topic that currently consists of only one or two short paragraphs should normally become an unnumbered `\paragraph{...}` inside a broader section, or be merged with a closely related subsection.
- Exceptions are allowed for central thesis objects whose visibility is important, such as an individual research question or a concise thesis statement. The exception should be intentional rather than caused by premature fragmentation.
- Do not create a numbered subsection merely because a software module, algorithm class, metric, or future experiment has a name. Use the hierarchy to reveal the thesis argument, not the repository tree.
- Reassess the hierarchy after verified results are inserted. A topic may grow into a subsection if it acquires a full method and evidence block; a planned subsection should be collapsed if the final evidence remains short.


## Authorial voice and final-prose rules

- State the scientific object, method, result, or evidence before explaining the chapter structure. The first sentence of a paragraph should normally begin with the subject matter, not `This chapter`, `This section`, `The purpose`, or `The thesis`.
- Use chapter-level metadiscourse once at the opening and, where useful, once in the summary. Remove repeated reminders of what the chapter does.
- Present contributions affirmatively. Replace `The contribution is not X; it is Y` with a direct statement of Y, while retaining the relevant boundary in a later scope or limitations paragraph.
- Keep editorial instructions, missing-result prompts, and repository-audit tasks inside `\draftnote{...}` or `draftonly`; they must not appear as dissertation prose.
- Use `should` and `must` for genuine scientific, physical, or methodological requirements, not for instructions to the future writer.
- Reduce repeated constructions such as `rather than`, `not only`, `does not automatically`, `This distinction is important`, and symmetrical `first/second/third` lists when a direct causal statement is clearer.
- Vary sentence and paragraph rhythm. Parallel lists are useful for definitions and protocols but should not become the default form of every argument.
- Put claim boundaries after the positive contribution or result, not before it. The text should sound careful without sounding apologetic.
- In provisional chapters, describe the evaluation protocol in the present tense and keep unverified quantitative claims in draft annotations. Once results are frozen, replace the protocol-only wording with measured findings.
- Chapter 9 may use an explicit `Research question / Answer / Evidence / Boundary` structure because its purpose is synthesis. Earlier chapters should present the investigation directly.
