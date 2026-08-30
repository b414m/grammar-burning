# Case E v0.6 — final transfer gate

## Objective

Test whether Claude Code and Codex can independently author semantic-attested evidence under `v0.6-pre`, using the same immutable Case E execution corpus.

This is not a software-development experiment. The only new variable is the public grammar/evidence contract.

## Public stimulus

Artifact: `case-e-public-bundle-v0.3.zip`

SHA-256:

`5e9075ac5e0b6cad094f908fd77b8e1b5d6bf6ed0a8c6afa435308ef059027fe`

Properties checked before release:

- 11/11 sealed corpus hashes preserved from Case E.
- 0 ZIP entries using Windows `\\` separators.
- no reference evidence graph included.
- no mutation fixtures included.
- no previous Claude/Codex output included.
- the supplied v0.6 validator accepts both private reference controls against exactly this bundle (`valid=true`, `0 errors`).

## Experimental isolation

Create two clean directories from the same ZIP:

- `case-e-v06/claude`
- `case-e-v06/codex`

Verify the bundle SHA-256 before extraction. Initialize Git independently in each directory and commit the extracted public bundle as the baseline.

Agents must not inspect each other's workspace or any prior experiment output.

## Agent-facing task

Both agents receive the exact same external prompt. The detailed normative specification lives in `README.md` and `case_e_agent_instruction.md` inside the bundle.

Expected agent output ZIP:

`case-e-v06-evidence-01_verified.zip`

## Evaluation after return

1. Freeze both ZIPs and compute SHA-256.
2. Replay the public v0.6 validator independently.
3. Verify public/sealed inputs remain byte-identical.
4. Check archive portability/canonical paths separately from evidence semantics.
5. Apply the 22 hidden v0.6 mutant operators to each actual output.
6. Compare authoring strategies and error trajectories.
7. Promotion gate:
   - both legitimate outputs ACCEPT;
   - hidden mutants continue to REJECT;
   - no new semantic-laundering escape is found.

If the gate holds, begin drafting `G v0.1.2 candidate`. If it does not, freeze the new counterexample and refine before promotion.
