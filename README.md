# grammar-burning

**Gramáticas en formación: un método prospectivo para sistemas agénticos y generación epistémicamente condicionada.**

Este repositorio conserva la línea experimental de *grammar burning*: descubrir reglas semánticas mediante contraejemplos reales, convertirlas en invariantes falsables, atacarlas con mutantes y sólo después discutir su promoción a una gramática maestra.

> Estado actual: `v0.6-pre` (semantic attestation). `G v0.1.1` permanece congelado y no se modifica desde este repositorio.

## Ciclo experimental

```text
observación
→ contraejemplo
→ invariante candidato
→ mutante
→ validador
→ transferencia entre agentes
→ nuevo contraejemplo
→ refinamiento
→ promoción
```

## Genealogía A–E

| Etapa | Dominio / prueba | Hallazgo principal |
|---|---|---|
| A | Attendance | integridad ≠ provenance; tests verdes ≠ production verification; atomicidad |
| B | Equipment Loan | recurrencia de provenance/atomicidad; SUT y persistencia pueden satisfacerse |
| C | Room Reservation, Claude vs Codex | transferencia; aparecen completitud contractual y reachability |
| D | Maintenance CLI | X-05/R-02 transfieren; aparece grounding de evidencia |
| E | Evidence-only sealed corpus | grounding estructural transfiere; aparece semantic attestation |
| v0.6-pre | Burn sobre outputs reales de E | execution-record authority + attestation profile + test invocation identity |

## Principios que sobrevivieron al burning

- `byte_integrity != provenance_truth != behavioral_verification`
- `IMPLEMENTED != REACHABLE != TEST_AUTHORED != EXECUTED != PASSED != VERIFIED`
- un claim `VERIFIED` debe quedar ligado al SUT exacto y a resultados materializados;
- las obligaciones externas no pueden desaparecer del grafo silenciosamente;
- una transición guardada cuya validez depende de un estado leído requiere frontera atómica/serializable;
- un `evidence kind` no tiene autoridad por su nombre: necesita attestation semántica verificable;
- todo símbolo normativo debe **pagar renta semántica**. Si no altera aceptación/rechazo, debe ser anotación o desaparecer.

## Estructura

- `experiments/attendance-v0.1/` y `attendance-v0.2/`: origen de invariantes P/X/R.
- `experiments-cross-case-v0.3/`: consolidación Attendance + Equipment Loan.
- `evaluations/`: resultados de transferencia y mutation burning de Cases C, D y E.
- `grammar/`: snapshots experimentales `v0.4-pre` → `v0.6-pre`, validadores y mutation suites.
- `public-bundles/`: material público usado en los experimentos de transferencia.
- `ops/`: instrucciones reproducibles de ejecución local, incluido discovery-first.
- `specimens/SHA256SUMS.md`: identidad de ZIPs congelados. Los binarios grandes no se versionan aquí.
- `archive/grammar-burning-research-snapshot-v0.6.zip`: snapshot completo del estado de investigación integrado.

## Estado de promoción

`v0.6-pre` deja como maduros para discusión de promoción: P-01M, X-01, X-02, X-03, X-05, X-02G, X-06, R-01, R-02 y R-04.

X-08, X-09, X-07R y T-01 pasan el burning interno de `v0.6-pre`, pero aún requieren transferencia agent-facing antes de promoverse.

## Regla de frontera

Este repo es laboratorio experimental. No implica que cada candidato de aquí pertenezca automáticamente al master graph. La promoción exige genealogía experimental, contraejemplo, falsación, controles legítimos y transferencia.
