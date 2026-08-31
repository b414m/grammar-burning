# Grounded Synthesis — research incubator

**Status:** INCUBATOR / OUTSIDE `G` / NO PROMOTED INVARIANTS.

This line starts from a question that is upstream from the current Evidence Grammar:

> Given a requirement, constraints, and a bounded snapshot of available knowledge, how can an agent arrive at a technical decision whose rationale is traceable, contestable, and eventually testable?

The current grammar-burning line primarily answers a later question:

> Given an artifact, executions, results, and obligations, when may a claim be admitted as verified?

Grounded Synthesis must not collapse these two questions.

## Provisional pipeline

```text
REQUIREMENT
    +
CONSTRAINTS
    +
KNOWLEDGE SNAPSHOT
        ↓
CANDIDATE ALTERNATIVES
        ↓
DECISION
        ↓
RATIONALE / ASSUMPTIONS
        ↓
ARTIFACT
        ↓
EVIDENCE COMPILER
        ↓
ADMISSIBLE CLAIMS
```

## Research boundary

The following labels are only namespaces for observations, not invariants:

- `K-*` — knowledge/source phenomena
- `D-*` — decision/alternative phenomena
- `A-*` — assumption phenomena
- `C-*` — constraint/applicability phenomena

A candidate rule may enter the normal grammar-burning lifecycle only after a concrete counterexample demonstrates why the distinction matters.

## Initial experimental target

Do **not** begin with “the corpus of all human knowledge”. Use a small, frozen knowledge packet and one technical decision with several plausible alternatives.

A suitable first experiment should provide:

1. one explicit requirement;
2. a few explicit constraints;
3. a bounded, versioned knowledge packet;
4. at least three technically plausible alternatives;
5. one decision to be defended;
6. enough source material to construct both legitimate and adversarial rationales.

The first objective is not to reward the “best” decision. It is to discover when a rationale appears grounded while actually losing source support, applicability, temporal validity, assumptions, or relevant alternatives.

## Candidate attack directions, not rules

Examples of phenomena to try to falsify:

```text
source exists
    !=
source supports the claim

source supports claim
    !=
claim applies under current constraints

plausible option
    !=
justified choice among alternatives

assumption
    !=
observation

historically valid source
    !=
currently adequate knowledge snapshot
```

These statements are hypotheses for experiment design. They are not yet grammar.

## Gate before activation

Grounded Synthesis becomes an active grammar-burning experiment only after the Case E v0.6 transfer gate is evaluated against independent Claude and Codex outputs.

Until then:

- no changes to `G`;
- no `K-*`, `D-*`, `A-*`, or `C-*` promotion;
- no attempt to merge knowledge reasoning into the current Evidence IR;
- no claim that the future system is already an “epistemic compiler”.

The existing Evidence Compiler remains a separately testable downstream component.
