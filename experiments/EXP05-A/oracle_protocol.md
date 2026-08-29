# EXP05-A Phase 2 - Protocolo de adjudicación independiente

## Objetivo

Etiquetar `SemanticTransitionCandidate` derivadas del archivo app antes de comparar cualquier resultado con el `FormationRuleEngine`.

## Restricción principal

El oráculo no puede ver:

- decisiones del motor para las transiciones que está etiquetando;
- razones emitidas por el motor;
- métricas agregadas de acuerdo;
- resultados de adjudicaciones anteriores que dependan del motor.

Sí puede ver el archivo congelado, su manifest, el brief funcional y las definiciones neutrales de los campos de la transición.

## Etiquetas

- `SUPPORTED`: los artefactos disponibles sostienen la transición propuesta.
- `UNSUPPORTED`: la transición afirma más de lo que los artefactos permiten sostener.
- `INSUFFICIENT_INFORMATION`: no hay información suficiente para decidir soporte o falta de soporte.
- `NOT_APPLICABLE`: la transición propuesta no describe adecuadamente la relación observada en el archivo.

## Procedimiento

1. Verificar la identidad congelada del archivo.
2. Recibir una lista de candidatas sin salida del motor.
3. Revisar los artefactos fuente y destino.
4. Asignar etiqueta, rationale, evidencia y confianza.
5. Sellar el archivo de adjudicación y calcular su hash.
6. Sólo después ejecutar el motor sobre las mismas candidatas.
7. Comparar por regla y por clase de etiqueta.

## Segunda adjudicación

Si dos oráculos están disponibles, se conserva cada adjudicación por separado. Los desacuerdos se resuelven mediante un tercer proceso de adjudicación que tampoco puede ver la salida del motor.

No se promedian etiquetas.

## Regla anti-fuga

Si el oráculo ve la salida del motor antes de sellar sus etiquetas, la corrida queda marcada `ORACLE_CONTAMINATED` y no puede sostener claims de validación independiente.

## Salida

La salida debe validar contra `oracle_adjudication.v0.1.schema.json` y contener una identidad durable del archivo evaluado.

## Estado

`FROZEN_FOR_PHASE2`
