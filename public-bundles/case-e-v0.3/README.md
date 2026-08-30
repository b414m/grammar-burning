# Case E v0.6 transfer gate

This is the **final agent-facing transfer test** for the current grammar-burning line.

The software, test source, execution records and result artifacts are already materialized and sealed. Your task is **evidence modeling only**: construct an `evidence_graph.json` that truthfully satisfies the supplied external contract under `v0.6-pre` semantic attestation.

Start with `case_e_agent_instruction.md`.

## Immutable inputs

Do not modify:

- `sealed/**`
- `sealed_manifest.json`
- `execution_records.json`
- `public/**`

The public validator treats `execution_records.json` and the semantic-attestation profile as verifier inputs. The evidence graph does not get to rewrite execution history.

## Intended outputs

Create only the requested agent outputs at repository root:

- `evidence_graph.json`
- `validation_result.json`
- `NOTES.md`
- `case-e-v06-evidence-01_verified.zip`

The bundle intentionally contains **no reference evidence graph and no hidden mutation fixtures**.
