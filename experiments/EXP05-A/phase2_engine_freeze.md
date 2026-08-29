# EXP05-A Phase 2 - Freeze del motor antes del archivo real

## Propósito

Este artefacto congela la representación ejecutable que deberá evaluarse contra el archivo real de desarrollo de app. Su función es impedir que las reglas se modifiquen después de observar los casos adjudicados.

## Implementación congelada

- repositorio: `b414m/data-value-compiler`
- rama: `eli-formation-rule-engine-v0.2`
- paquete: `dvl/v041`
- commit: `5bb4be8aff73809109436b4ad6782f1bffc649d6`
- workflow: `DVL v0.4.1 Formation Rule Engine`
- run: `33279658845`
- resultado CI: `success`
- tests: `15 passed`

## Reglas ejecutables incluidas

- `FR-001-PROPOSAL-SELECTION-AUTHORITY`
- `FR-002-INTENT-EVIDENCE-SEPARATION`
- `FR-003-EVIDENCE-CLAIM-CEILING`
- `FR-004-PROPOSAL-NORMATIVE-AUTHORITY`
- `FR-005-AUTHORIZATION-EXECUTION`
- `FR-006-DESIGN-RUNTIME-CAPABILITY`

## Cambio metodológicamente importante respecto a v0.4

La jerarquía concreta de claims deja de ser tratada como parte universal del motor. `FR-003` requiere ahora una taxonomía declarada e inyectada. El motor incluye únicamente `epistemic_v01` como taxonomía conocida de referencia.

No se ha inventado una taxonomía de assurance de software para hacer encajar el caso app. Si una transición usa una taxonomía no registrada, el resultado correcto es `UNKNOWN`.

Esto separa:

```text
formation rule
    !=
domain claim taxonomy
```

Asimismo, FR-006 exige hechos observables `implementation_present` y `runtime_verified`; un mockup no puede crear esos hechos por sí mismo.

## Regla de congelamiento

Cualquier cambio posterior en semántica, taxonomías, precedencia de decisiones o precondiciones genera una nueva versión del motor y no puede utilizarse para reinterpretar retrospectivamente los resultados de EXP05-A fase 2.

## Estado

`ENGINE_FROZEN_FOR_PHASE2`
