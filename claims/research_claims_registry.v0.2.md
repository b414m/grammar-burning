# Research Claims Registry v0.2

Este registro conserva v0.1 y actualiza únicamente el estado evidencial después de EXP05-A fase 1.

| ID | Afirmación | Estado actual | Evidencia / límite |
|---|---|---|---|
| C01 | Es posible reconstruir reglas de formación a partir de archivos machine-readable producidos por sistemas humano-agente. | HYPOTHESIS | Aún falta demostrar el ciclo de descubrimiento desde archivo real, no sólo implementar reglas ya propuestas. |
| C02 | Algunas reglas de formación sobreviven cambios de dominio. | PRELIMINARY_PROBE | EXP05-A fase 1 mostró transferencia sintética para FR-A y FR-C, pero sin archivo real ni oráculo independiente. No permite claim cross-domain. |
| C03 | Un estado epistémico exógeno reduce transiciones semánticas no soportadas frente al generador base. | NOT_TESTED | Requiere EXP05-B A vs C con oráculo independiente. |
| C04 | Reglas de formación ejecutables aportan reducción adicional sobre el estado epistémico sin enforcement. | NOT_TESTED | Requiere EXP05-B C vs D. |
| C05 | La reducción no se explica únicamente por abstención indiscriminada. | NOT_TESTED | Requiere métricas de utilidad, abstención y falsos rechazos. |
| C06 | El costo en capacidad generativa útil es menor que el beneficio dentro de la clase de transiciones representables. | NOT_TESTED | Debe congelarse una función o criterio de utilidad/beneficio antes de resultados. |
| C07 | `candidatura != selección` tiene alcance mayor que un único flujo de datos. | PRELIMINARY_PROBE | El mismo gate discriminó fixtures de data_value y app_development. Fase 2 debe usar archivo real y oráculo independiente. |
| C08 | `autorización != ejecución` conserva poder discriminativo en múltiples dominios agénticos. | PRELIMINARY_PROBE | Transferencia sintética observada en fase 1; R4 no autorizado. |
| C09 | “Arqueología prospectiva” describe un método técnico útil y no sólo una metáfora. | METHODOLOGICAL_PROPOSAL | Ya existen protocolo, reglas ejecutables, CI y artifacts, pero falta demostrar el ciclo completo archivo -> descubrimiento -> regla -> falsación -> uso. |
| C10 | El método constituye una contribución original respecto al estado del arte. | UNESTABLISHED | Revisión sistemática/comparativa aún pendiente. |
| C11 | La taxonomía concreta de `claim_ceiling` puede ser dependiente del dominio aunque la regla abstracta de no-promoción sea más general. | OBSERVATION | EXP05-A fase 1 produjo `REPRESENTATION_GAP` en APP-B1; debe investigarse con una representación de claims explícitamente parametrizable. |

## Convención de estados

- `HYPOTHESIS`: afirmación falsable formulada, sin evidencia suficiente.
- `NOT_TESTED`: experimento pendiente.
- `PRELIMINARY_PROBE`: evidencia de implementación o fixtures que orienta el diseño, pero no autoriza la afirmación científica correspondiente.
- `OBSERVATION`: hecho reproducible del sistema o experimento con alcance explícitamente limitado.
- `CANDIDATE`: evidencia parcial que requiere validación adicional.
- `SUPPORTED`: evidencia reproducible suficiente para el alcance declarado.
- `REFUTED`: evidencia contradice la afirmación dentro del alcance declarado.
- `METHODOLOGICAL_PROPOSAL`: definición/procedimiento propuesto que todavía debe demostrar utilidad y poder discriminativo.
- `UNESTABLISHED`: no debe formularse como contribución demostrada.

## Regla

Un claim sólo puede cambiar de estado mediante una nueva referencia de evidencia durable. El texto narrativo del paper no tiene autoridad para promocionarlo.
