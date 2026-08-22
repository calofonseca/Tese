# Authorial Style Guide for the Thesis — v11

## 1. Lead with the scientific subject

A paragraph should normally begin with the system, method, problem, result, or evidence.

Prefer:

> MATD3 reduced critic overestimation under the evaluated REC configuration.

Avoid:

> This section explains why MATD3 was considered.

One short orientation paragraph is sufficient at the start of a chapter. Repeated reminders of the chapter's purpose should be removed.

## 2. State the contribution before its boundary

Prefer:

> The lifecycle architecture governs coordinated policy sets through explicit lineage, compatibility, promotion, deployment, monitoring, and rollback.

Then delimit it:

> The current implementation retains target-specific adapters and selected manual transitions.

Avoid opening with:

> The contribution is not the invention of MLOps...

## 3. Keep planning outside dissertation prose

Writer instructions, missing evidence, repository checks, figure sources, and experiment prompts belong in:

- `\draftnote{...}`;
- `draftonly` blocks;
- the annotated PDF;
- project notes or evidence matrices.

They must not appear in the clean prose as:

- `the final result should...`;
- `this table will be populated...`;
- `the final chapter must...`;
- `values remain to be confirmed...`.

## 4. Use present tense for methods and argument

Use the present tense for the architecture, formalism, protocol, and interpretation:

> TI-MARL represents the active interface through typed observation parts and action ports.

Use past tense for completed experiments:

> The controller reduced the measured peak by ...

Use future tense only for genuine future research, not for unfinished writing.

## 5. Explain intuitively before formalising

Introduce the problem through a recurring energy example, then define the formal object.

```text
EV charger gains V2G capability
→ observations and callable actions change together
→ fixed action layout becomes insufficient
→ typed-interface formalisation
```

Examples clarify the concept; they do not replace definitions or evidence.

## 6. Preserve stable terminology

Use the same term for the same object throughout the thesis:

- agent;
- asset;
- controller;
- policy;
- policy set;
- interface;
- scenario;
- environment;
- deployment target;
- Scalability;
- Deployability;
- Safety;
- Robustness.

Do not create synonyms merely to vary the prose.

## 7. Keep evidence next to the claim

A contribution paragraph should identify:

1. the problem;
2. the method or artefact;
3. the evidence;
4. the conditions under which the result holds;
5. the remaining boundary.

Avoid a long method chapter followed by a detached global results chapter.

## 8. Use negative framing selectively

`does not`, `rather than`, and `not automatically` are useful when they create a real conceptual boundary. They should not become a habitual opening pattern.

Prefer a positive statement where possible:

> Real-world validation provides combined evidence about interfaces, data quality, runtime resources, fallback, and lifecycle behaviour.

Instead of:

> The main contribution of real-world validation is not a single percentage.

## 9. Vary rhythm without sacrificing precision

Use parallel lists for:

- definitions;
- protocol steps;
- taxonomies;
- lifecycle states;
- evaluation metrics.

Use connected prose for causal explanation and interpretation. Avoid making every paragraph a symmetric list of three or four items.

## 10. Separate evidence levels explicitly

Always distinguish:

- simulation with synthetic data;
- simulation with real data;
- digital replica or replay;
- target-hardware inference;
- hardware/software-in-the-loop;
- shadow operation;
- limited field control;
- sustained closed-loop operation.

The evidence level is part of the claim, not an implementation footnote.

## 11. Maintain the cumulative research story

For each pre-TI-MARL stage:

```text
problem encountered
→ solution introduced
→ evidence obtained
→ problem solved
→ conditions of the solution
→ assumption that remained
```

TI-MARL emerges from the non-composition of the remaining assumptions. Earlier methods retain their scientific value as baselines, mechanisms, empirical contributions, teachers, fallbacks, or components.

## 12. Reserve direct answer format for Chapter 9

An explicit structure such as:

```text
Research question
Answer
Evidence
Boundary
```

is appropriate in the synthesis chapter. Earlier chapters should present the investigation directly rather than sounding as though they answer an examiner after every section.

## 13. Apply the section-granularity rule

- A numbered section carries a distinct claim, method, or evidence block.
- A numbered subsection normally sustains one to two pages.
- One or two short paragraphs become an unnumbered paragraph heading or merge with a related subsection.
- The hierarchy follows the thesis argument, not the repository structure.

## 14. Keep clean and annotated builds separate

- `main.tex`: authorial reading version.
- `main-annotated.tex`: evidence prompts and production notes.

The clean version should never expose a writer instruction, empty result ledger, orange draft note, or literal `[TBD]` marker.
