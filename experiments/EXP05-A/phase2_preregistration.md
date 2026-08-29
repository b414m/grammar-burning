# EXP05-A Phase 2 - Pre-registro de validación con archivo real de desarrollo de app

## Objetivo

Evaluar si las reglas candidatas conservan poder discriminativo cuando se aplican a un archivo real producido durante el desarrollo de una aplicación sencilla sin ML como núcleo funcional.

La fase 2 no puede reutilizar como evidencia los fixtures sintéticos de fase 1. Aquellos sirven únicamente para verificar la implementación del motor.

## Dominio B congelado

Proyecto de aplicación de registro de asistencia con alcance reducido. El objetivo es generar un archivo de trabajo suficientemente completo para observar propuestas, decisiones, requisitos, artefactos de diseño, autorizaciones y ejecuciones sin introducir deliberadamente un pipeline de ML.

## Reglas candidatas bajo evaluación

1. `FR-001 / FR-A`: candidatura o propuesta no equivale a selección autorizada.
2. `FR-003 / FR-B`: una clase de evidencia no puede promover silenciosamente una clase de afirmación que exige mayor soporte.
3. `FR-005 / FR-C`: autorización no equivale a ejecución.
4. `FR-006`: artefacto de diseño no equivale a capacidad de runtime. Esta regla todavía requiere una implementación ejecutable separada y no se considera probada por FR-C.

## Separación de roles

La fase debe distinguir al menos:

- `generator`: agente o equipo que produce los artefactos del proyecto app;
- `formation_rule_engine`: implementación que evalúa transiciones tipadas;
- `oracle`: adjudicador independiente de la implementación de las reglas;
- `researcher`: integra resultados sin modificar etiquetas post-hoc.

El mismo output del `FormationRuleEngine` no puede ser usado como ground truth.

## Archivo mínimo requerido

El proyecto app deberá producir, con referencias durables:

- intención/requisito inicial;
- propuestas del agente;
- decisiones explícitas del humano cuando existan;
- user stories o requisitos funcionales;
- prototipo o diseño de interfaz;
- contratos de permisos/capacidades requeridas;
- implementación o ausencia explícita de implementación;
- solicitudes de ejecución/deploy;
- autorizaciones de ejecución;
- evidencia observable de aceptación o rechazo por el proveedor/runtime;
- registro de incertidumbres y datos ausentes.

## Unidad experimental

La unidad no será el documento completo sino una `SemanticTransitionCandidate` extraída del archivo:

```text
source artifact/state
  + proposed semantic move
  + target artifact/state
  + provenance
  + timestamp/order
```

Cada candidata será etiquetada por el oráculo como:

- `SUPPORTED`
- `UNSUPPORTED`
- `INSUFFICIENT_INFORMATION`
- `NOT_APPLICABLE`

antes de comparar contra el motor.

## Métricas pre-registradas

- cobertura de reglas sobre transiciones etiquetadas;
- tasa de detección de transiciones `UNSUPPORTED`;
- falsos rechazos sobre transiciones `SUPPORTED`;
- tasa de `UNKNOWN` apropiados sobre `INSUFFICIENT_INFORMATION`;
- gaps de representación por regla;
- acuerdo motor-oráculo, reportado por regla y no sólo agregado.

## Criterio de promoción a R4

Una regla no se promueve a R4 por aparecer en dos dominios. Como mínimo debe:

1. tener una representación ejecutable congelada antes de adjudicar resultados;
2. poseer ejemplos positivos y contraejemplos naturales en el archivo real;
3. ser evaluada por un oráculo independiente;
4. mostrar poder discriminativo sin una tasa de falsos rechazos que vuelva trivial el gate;
5. no depender de redefinir post-hoc los objetos del dominio para preservar la regla.

La decisión final permitida por regla será una de:

- `PROMOTE_R4`
- `REVISE_AND_RETEST`
- `RETAIN_LOCAL`
- `REJECT`
- `INSUFFICIENT_EVIDENCE`

## Regla anti-rescate

Si una regla falla, no se modificará la interpretación del caso después de observar el output del motor para hacerla encajar. Toda modificación de la regla o de su taxonomía crea una nueva versión y exige un nuevo experimento.

## Estado

`PREREGISTERED_NOT_RUN`
