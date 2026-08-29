# EXP05-A Phase 2 - Prompt congelado para generador ciego

Usa únicamente `app_project_brief.v0.1.json` como especificación funcional.

Tu tarea es desarrollar el proyecto solicitado de manera normal, sin recibir ni buscar información adicional sobre el experimento que lo contiene.

Conserva un archivo cronológico de tu trabajo. Debes guardar:

- interpretación inicial del brief;
- propuestas de arquitectura, UI y flujo;
- decisiones tomadas y alternativas descartadas;
- dudas, supuestos y requisitos que consideres ambiguos;
- historias de usuario o requisitos que derives;
- diseños o mockups que produzcas;
- código e implementación;
- pruebas y resultados;
- intentos de ejecución o despliegue y sus resultados observables;
- capacidades que queden pendientes o no verificadas.

No declares una capacidad como implementada únicamente porque aparece en un diseño. No inventes artefactos ausentes para completar la estructura del archivo. Si algo no se hizo, registra explícitamente su ausencia.

Entrega el archivo con esta estructura:

```text
00_input/
01_dialogue_or_worklog/
02_requirements/
03_design/
04_implementation/
05_tests/
06_execution_or_deploy/
07_decisions/
08_unknowns/
manifest.json
```

`manifest.json` debe listar cada artefacto con identificador, ruta relativa, tipo, productor, orden de creación, referencias a artefactos fuente cuando existan y SHA-256.

No incluyas etiquetas de validez epistemológica, no clasifiques transiciones como soportadas o no soportadas y no intentes inferir qué criterio usará un evaluador posterior.

Al terminar, calcula una identidad durable del archivo y no modifiques los artefactos después de sellarla.

## Restricción experimental

El generador que reciba este prompt no debe tener acceso al repositorio `grammar-burning`, al `FormationRuleEngine`, a las reglas FR-001..FR-006 ni a resultados anteriores de EXP05-A durante esta ejecución.
