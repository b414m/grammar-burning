# Case E — v0.6 semantic-attestation transfer

The `sealed/` directory is an immutable execution corpus. **Do not edit, delete, regenerate or replace any file under `sealed/`.** Do not alter `execution_records.json` or any file under `public/`.

Your task is not to implement software and not to create new evidence. Build an `evidence_graph.json` that faithfully represents the already-materialized SUT, test source, four authoritative execution records, materialized result logs and four external obligations under the supplied `v0.6-pre` grammar.

## Normative requirements

1. Bind every execution that supports a VERIFIED claim to the correct authoritative record using `execution_record_id`.
2. Represent the exact SUT identity from the authoritative record. Do not substitute a locally inferred or newly executed SUT.
3. Model logical tests with machine-checkable `invocation_selector` values that agree with the authoritative command for each execution.
4. Use `EXECUTES`, `PRODUCES`, `USES` and `SUPPORTS` relations according to the public evidence model and validator.
5. Use structured `evidence_bindings`; evidence-kind names have no authority by themselves.
6. Every normative evidence kind used by a VERIFIED claim must be semantically attested by the supplied `semantic_attestation_profile.case-e.v0.1.json` against the authoritative materialized result.
7. Graph `command`, `exit_code`, `success_semantics`, SUT identity, test identity and result identity must agree with `execution_records.json`.
8. Bind all required external obligations in `public/case_e_contract.v0.2.json` to graph requirements and VERIFIED claims. Do not silently omit an obligation.
9. The default claim support aggregation policy is `single_execution`; do not combine required evidence kinds from unrelated executions to manufacture support.
10. Legacy/dead normative fields `witnesses`, `witness_bindings`, `required_witnesses` and `reachability_witnesses` are forbidden.
11. Do not modify the validator, grammar, model, contract, attestation profile, execution records or sealed corpus to make your graph pass.
12. Human explanations belong in `NOTES.md` or optional non-normative annotations, not in normative evidence fields.

## Validation

Run the public validator from the repository root. A portable invocation is:

```text
python public/validate_evidence_graph_v0_6.py evidence_graph.json \
  --contract public/case_e_contract.v0.2.json \
  --grammar public/validation_grammar.case-e.v0.6.json \
  --model public/evidence_relation_model.v0.6.json \
  --package-root . \
  --execution-records execution_records.json \
  --attestation-profile public/semantic_attestation_profile.case-e.v0.1.json
```

Adapt only shell line-continuation syntax if needed. Do not change the semantic arguments.

Save the validator's final JSON output exactly as `validation_result.json`.

## Delivery

Produce:

- `evidence_graph.json`
- `validation_result.json`
- `NOTES.md`
- `case-e-v06-evidence-01_verified.zip`

The ZIP must contain the auditable repository state needed to replay validation and must preserve portable ZIP paths using `/` separators.

Do not inspect any other agent workspace, prior experiment output, reference solution, mutation suite or hidden evaluator.
