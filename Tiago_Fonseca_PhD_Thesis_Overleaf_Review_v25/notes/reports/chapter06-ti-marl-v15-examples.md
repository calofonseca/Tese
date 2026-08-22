# TI-MARL Chapter 6 Revision v15

This revision strengthens the explanatory path of Chapter 6 without changing the thesis-wide argument.

## Main changes

- The unnumbered opening now states explicitly what the progressive methods in Chapter 5 solved and isolates the remaining fixed-interface assumption.
- Section 6.1.2 now formalises both the one-agent Typed-Interface MDP/TI-RL reduction and the multi-agent Typed-Interface Markov Game/TI-MARL method.
- Section 6.2 is now `TI-MARL Architecture`, with an architecture-at-a-glance subsection followed by a substantial running example.
- The running example follows two building agents from a versioned capability schema to:
  - compiled observation parts;
  - grouped parameterised action ports;
  - a local action-bundle intent;
  - a shared transformer conflict;
  - a utility-aware joint allocation;
  - health-induced action-port contraction.
- Concrete tables now show the anatomy and semantics of schemas, observations, ports, resource couplings, and execution traces.
- The local-policy section reuses the same example to explain common latent context, multiple action-group heads, authorised community observations, and the distinction between policy context and authoritative constraints.
- The constraint section includes explicit local and shared equations for the running example.
- The explainability section includes an illustrative trace grounded in compiler predicates, policy outputs, constraints, and allocation results.
- Two new figure placeholders were added:
  - the complete running contract-to-action example;
  - the anatomy of a typed observation part and typed action port.

## Writing principles

The revision uses final-style authorial prose. The running example is explicitly illustrative rather than presented as empirical evidence. Method definitions are stated positively, while uncertainty and implementation decisions remain in annotated-only notes.
