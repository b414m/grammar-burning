# Promotion readiness after v0.6-pre

## Mature enough for `G v0.1.2 candidate` discussion

These rules now have cross-case recurrence and/or cross-agent transfer evidence:

- P-01M — typed, resolvable, materialized provenance
- X-01 — verification binds to exact SUT
- X-02 — evidence states are distinct
- X-03 — persistence requires a boundary witness
- R-01 — production conformance is mechanical
- R-02 — required capability is production-reachable
- R-04 — guarded transitions require an atomic/serialized boundary
- X-05 — required external obligations have coverage
- X-02G — epistemic evidence is structurally grounded
- X-06 — support bundles are SUT-coherent

`X-07` (typed/checkable success semantics) also has transfer evidence in Case E, but `v0.6-pre` reveals that typing alone is insufficient; promotion should use the refined X-07R semantics rather than freeze the weaker wording.

## Hold outside G pending transfer

- X-08 — evidence kind requires semantic attestation
- X-09 — materialized execution record is authority
- X-07R — success semantics must be attested
- T-01 — test invocation identity

These four now survive mutation burning, but Claude/Codex have not yet been asked to author them independently from a public v0.6 specification.

## Profile candidate, not universal core

- P-01P — canonical portable archive projection (`/` ZIP paths). Recurrent in Codex D/E, but best treated as a packaging profile rather than a universal evidence-grammar rule.

## Recommendation

Do not create another application domain. If one final transfer gate is desired before drafting `G v0.1.2 candidate`, reuse Case E and ask both agents to **upgrade their own frozen graph** to the public v0.6 semantic-attestation contract. That is a schema/evidence transfer experiment, not a new software project.
