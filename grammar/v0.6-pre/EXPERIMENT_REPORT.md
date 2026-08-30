# Grammar burning v0.6-pre — semantic attestation

## Scope

`v0.6-pre` continues the frozen A–E evidence line without modifying `G v0.1.1` and without re-running application/test workloads. It attacks the Case E distinction:

```text
structurally grounded evidence != semantically attested evidence
```

The source specimens are the actual Claude Code and Codex Case E evidence graphs that independently passed `v0.5-pre-r1`.

## Candidate rules under burn

- **X-08 — evidence_kind_requires_semantic_attestation**: an evidence kind has no authority merely because a binding names it. The kind resolves to an external attestation specification whose predicates are evaluated against the authoritative materialized result.
- **X-09 — execution_record_is_materialized_authority**: graph-local command, exit code, success semantics, SUT, test and result identity must agree with a pinned materialized execution record.
- **X-07R — success_semantics_must_be_attested**: typed success metadata cannot be invented in the graph; it must agree with authoritative execution metadata.
- **T-01 — test_invocation_identity**: logical tests sharing one source file are distinguished by a machine-checkable invocation selector matched against the authoritative command.

## Universal rule vs case-specific semantics

The grammar does **not** hardcode that concurrency means `successes == 1` or persistence means `fresh_process == true`.

Instead:

```text
universal grammar
    requires semantic attestation
             |
             v
external semantic_attestation_profile
    defines predicates for this verification context
             |
             v
materialized result bytes
```

For Case E, the external profile defines concrete predicates over the sealed JSON logs. This keeps the grammar general while making each normative evidence kind mechanically meaningful.

## Authoritative execution records

`execution_records.json` is treated as a verifier input, not as graph-authored prose. The Case E profile pins it to:

```text
673761a36484bd6d8ad5298533ed62db85b842f6115cdc83abe1b67aaa20e4d1
```

Every supporting execution must declare `execution_record_id`. The validator checks equality/identity for:

- command;
- exit code;
- typed success semantics;
- SUT path + SHA-256;
- test source path + SHA-256;
- result path + SHA-256.

## Test invocation identity

Each logical test now has an `invocation_selector`, e.g.:

```json
{"kind":"command_arg_equals","index":2,"value":"concurrency"}
```

An `EXECUTES` edge is valid semantically only when the authoritative command satisfies the selector. Therefore adding a graph-local edge from the concurrency execution to `TEST-FULL` no longer launders test identity merely because both logical tests live in `test_suite.py`.

## Control migration

The actual Case E outputs were migrated structurally only:

1. add `execution_record_id` to each execution by matching its already-materialized command to the sealed execution records;
2. add an invocation selector to each logical test using the already-materialized command selector.

No tests were re-run, no result bytes changed, no SUT bytes changed, and no semantic claims were added.

Results:

```text
Claude control  -> ACCEPT (0 errors)
Codex control   -> ACCEPT (0 errors)
```

## Mutation burn

The suite contains **22 distinct mutant operators**. It includes the 9 structural attacks already killed by `v0.5-pre-r1`, the 8 semantic survivors discovered in Case E, and 5 additional authority/identity attacks.

Across both real outputs:

```text
Claude: 22 / 22 mutants REJECTED
Codex : 22 / 22 mutants REJECTED

44 / 44 actual-output mutant applications rejected
2 / 2 legitimate controls accepted
```

The former Case E survivors now die for the intended reasons:

- FULL cannot become R-04 evidence because selector `full` is not authorized for `concurrency_witness` and the result predicates fail.
- FULL cannot become X-03 evidence because the persistence predicates fail.
- FULL cannot become R-01 conformance evidence because the conformance predicates fail.
- `/bin/true` contradicts the authoritative execution record.
- invented assertion counts contradict authoritative success semantics.
- a concurrency binding cannot cite `full.log` because binding result identity must equal the authoritative result.
- a concurrency execution cannot `EXECUTES TEST-FULL` because its selector does not match the authoritative command.
- mutating `execution_records.json` breaks its pinned SHA-256 and its contents contradict the graph.

Additional mutants killed:

- missing `execution_record_id`;
- swapping a concurrency execution to the FULL record;
- missing test invocation selector;
- laundering the concurrency selector to `full`;
- introducing an evidence kind with no attestation specification.

## Result

`v0.6-pre` closes the known Case E semantic-laundering attacks while accepting both independently produced Case E evidence structures after a provenance-preserving structural migration.

This does **not** prove the semantic-attestation grammar universal. In particular, X-08/X-09/X-07R/T-01 have been burned against real outputs but have not yet been independently authored by Claude Code and Codex from the public specification. They therefore remain experimental rather than promoted.

## Root-of-trust boundary

The evidence graph cannot prove the trustworthiness of its own validator, grammar, contract or semantic-attestation profile. Those are verifier configuration and require an external trust anchor (release hash, signed package, policy distribution, etc.). This is a boundary, not a graph field to recursively self-certify.
