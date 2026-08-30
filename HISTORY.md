# Experimental history

## v0.1 — first Attendance burn
P/X/R families, provenance ambiguity, exact-SUT gap, reachability gaps, persistence-boundary gap.

## v0.2 — executed Attendance witnesses
R-04 deterministic close/edit race (20/20); X-03 negative persistence control; evidence-state vocabulary.

## v0.3 — cross-case consolidation
Attendance + Equipment Loan. P-01 and R-04 recur across domains; X-01/X-03/R-01 shown satisfiable. First typed evidence relation vocabulary and mutation suite.

## v0.4-pre — materialization, contract completeness, reachability
Case C exposed entities that resolved but did not materialize and required capabilities that could disappear. P-01M, R-02 and experimental X-05 introduced.

## v0.5-pre / r1 — evidence grounding and dead-symbol removal
Case D exposed ungrounded witness tokens. Structured evidence bindings introduced. Dead normative fields (`witnesses`, `witness_bindings`, `required_witnesses`, `reachability_witnesses`) removed/prohibited in r1.

## Case E / evaluation v0.6
Both agents independently transferred structural grounding. Adversarial mutations showed that a structurally grounded `kind` could still lie about semantics.

## v0.6-pre — semantic attestation
External pinned execution records, case-specific semantic attestation profiles and test invocation selectors close the known semantic-laundering escapes. Two real controls ACCEPT; 22 distinct mutant operators rejected against both outputs (44/44 applications).

## Case E v0.6 transfer gate — prepared
A final agent-facing bundle reuses the same sealed Case E corpus and exposes `v0.6-pre` semantic attestation. The public stimulus preserves 11/11 sealed hashes, has canonical ZIP paths, contains no reference graph/mutants/prior outputs, and was preflighted against two private controls (`valid=true`, 0 errors). This gate tests whether Claude Code and Codex can independently author X-08/X-09/X-07R/T-01 rather than merely consume a migrated projection.
