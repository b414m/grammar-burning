# Research Claims Registry v0.1

Este archivo evita que el artículo trate hipótesis, resultados y antecedentes como si tuvieran el mismo estatus.

| ID | Afirmación | Estado actual | Evidencia requerida |
|---|---|---|---|
| C01 | Es posible reconstruir reglas de formación a partir de archivos machine-readable producidos por sistemas humano-agente. | HYPOTHESIS | Casos reproducibles de descubrimiento + provenance + contraejemplos. |
| C02 | Algunas reglas de formación sobreviven cambios de dominio. | NOT_TESTED | EXP05-A u otro experimento cross-domain. |
| C03 | Un estado epistémico exógeno reduce transiciones semánticas no soportadas frente al generador base. | NOT_TESTED | EXP05-B, comparación A vs C con oráculo independiente. |
| C04 | Reglas de formación ejecutables aportan reducción adicional sobre el estado epistémico sin enforcement. | NOT_TESTED | EXP05-B, comparación C vs D. |
| C05 | La reducción no se explica únicamente por abstención indiscriminada. | NOT_TESTED | Métricas de abstención, utilidad y falsos rechazos. |
| C06 | El costo en capacidad generativa útil es menor que el beneficio dentro de la clase de transiciones representables. | NOT_TESTED | Función/criterio de utilidad y beneficio congelado antes de resultados. |
| C07 | `candidatura != selección` es una regla de formación con alcance mayor que un único flujo de datos. | CANDIDATE | Importar evidencia de origen y probar en dominio app. |
| C08 | `autorización != ejecución` conserva poder discriminativo en múltiples dominios agentic. | CANDIDATE | Evidencia cross-domain y oráculo independiente. |
| C09 | “Arqueología prospectiva” describe un método técnico útil y no sólo una metáfora. | METHODOLOGICAL_PROPOSAL | Mostrar que cada concepto se materializa en protocolo, artefactos, reglas y experimentos reproducibles. |
| C10 | El método constituye una contribución original respecto al estado del arte. | UNESTABLISHED | Revisión sistemática/comparativa de literatura antes de claim de novedad. |

## Convención de estados

- `HYPOTHESIS`: afirmación falsable formulada, sin evidencia suficiente.
- `NOT_TESTED`: diseño disponible, experimento pendiente.
- `CANDIDATE`: evidencia parcial o de otro contexto, requiere validación local.
- `SUPPORTED`: evidencia reproducible suficiente para el alcance declarado.
- `REFUTED`: evidencia contradice la afirmación dentro del alcance declarado.
- `METHODOLOGICAL_PROPOSAL`: definición/procedimiento propuesto, debe demostrar utilidad y poder discriminativo.
- `UNESTABLISHED`: no debe formularse como contribución demostrada.

## Regla

El texto del artículo debe usar verbos compatibles con el estado del claim. Por ejemplo, `NOT_TESTED` se formula como “hipotetizamos” o “evaluaremos”, no como “demostramos”.
