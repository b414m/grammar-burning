# EXP05-A Phase 2 - Protocolo de scoring motor-oráculo

## Propósito

Congelar antes de observar resultados la traducción entre etiquetas del oráculo independiente y decisiones del `FormationRuleEngine`.

## Etiquetas del oráculo

- `SUPPORTED`
- `UNSUPPORTED`
- `INSUFFICIENT_INFORMATION`
- `NOT_APPLICABLE`

## Decisiones del motor

- `ALLOW`
- `REJECT`
- `DOWNGRADE`
- `RETRIEVE`
- `ASK`
- `UNKNOWN`

## Compatibilidad pre-registrada

| Oracle | Decisiones compatibles |
|---|---|
| `SUPPORTED` | `ALLOW` |
| `UNSUPPORTED` | `REJECT`, `DOWNGRADE`, `RETRIEVE`, `ASK` |
| `INSUFFICIENT_INFORMATION` | `UNKNOWN`, `RETRIEVE`, `ASK` |
| `NOT_APPLICABLE` | no se puntúa; se reporta cobertura |

`UNKNOWN` no cuenta como detección correcta de una transición etiquetada `UNSUPPORTED`, porque expresa ausencia de representación o información suficiente, no identificación positiva de una promoción no soportada.

`RETRIEVE` y `ASK` pueden ser compatibles tanto con `UNSUPPORTED` como con `INSUFFICIENT_INFORMATION` porque son decisiones de reparación. Se reportarán por separado para no ocultar esta ambigüedad.

## Métricas

Por regla y globalmente se reportarán:

- `supported_allow_rate`;
- `unsupported_protective_action_rate`;
- `unsupported_unknown_rate`;
- `insufficient_repair_or_unknown_rate`;
- `false_rejection_rate`, definido como cualquier decisión distinta de `ALLOW` sobre `SUPPORTED`;
- `coverage_rate`, excluyendo `NOT_APPLICABLE` del denominador de desempeño pero no del reporte de cobertura;
- distribución completa de decisiones, sin colapsar sólo a acierto/error.

## Regla contra optimización trivial

Un motor que responde `UNKNOWN`, `ASK` o `RETRIEVE` para todas las transiciones no se considera exitoso. Debe preservar una tasa útil de `ALLOW` sobre `SUPPORTED` y discriminar `UNSUPPORTED` sin convertir la abstención generalizada en mejora aparente.

## Estado

`FROZEN_BEFORE_PHASE2_RESULTS`
