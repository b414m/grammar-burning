# EXP05-B - Generación epistémicamente condicionada

## Objetivo

Probar H01 mediante un experimento controlado que separe el efecto de contexto adicional del efecto de restricciones semántico-epistémicas ejecutables.

## Condiciones

### A - Generador base
El modelo recibe la tarea y responde sin estado epistémico estructurado ni reglas de formación.

### B - Generador + contexto/retrieval
El modelo recibe evidencia contextual adicional cuando la tarea lo requiera, pero no existe enforcement de reglas de formación.

### C - Generador + estado epistémico exógeno
El modelo recibe un estado estructurado que declara evidencia, provenance, clase de afirmación admisible, autoridad y estado de incertidumbre. No existe enforcement externo de reglas.

### D - Generador + estado epistémico + reglas ejecutables
Además de `E`, las transiciones propuestas son evaluadas por reglas versionadas antes de convertirse en salida aceptada o cambio de estado.

## Principio de independencia

El generador no puede ser la autoridad exclusiva que construye o valida `E`. El evaluador final tampoco puede ser la misma implementación usada para imponer las reglas.

## Unidad de evaluación

La unidad primaria no será el token, sino el **movimiento semántico tipado**. Ejemplos:

```text
DescriptiveClaim
PredictiveClaim
CausalClaim
Recommendation
Authorization
ExecutionReport
Abstention
```

La representación exacta debe congelarse antes del benchmark.

## Dataset de prueba

El conjunto debe incluir, como mínimo:

- casos válidos que las reglas deben permitir;
- ataques diseñados para inducir promoción semántica no soportada;
- casos fuera de cobertura para medir límites;
- casos donde abstenerse sea correcto;
- casos donde abstenerse sea un falso rechazo.

Los ejemplos de evaluación no deben reutilizar sin control los mismos casos empleados para diseñar las reglas.

## Métricas

Se reportarán por separado:

- EUTR, errores dentro de la clase expresable;
- RC, cobertura de reglas;
- FRR, rechazos incorrectos;
- URR, utilidad de la respuesta;
- AAR, abstención apropiada;
- tasa total de abstención;
- severidad de transiciones no soportadas.

No se reducirá el resultado a una sola cifra antes de estudiar el trade-off error-utilidad.

## Análisis

El análisis principal comparará A, B, C y D. También se estudiará una frontera de Pareto entre reducción de transiciones no soportadas y pérdida de capacidad generativa útil.

## Controles negativos

- Regla irrelevante para la transición evaluada.
- Estado epistémico incompleto marcado como `UNKNOWN`.
- Regla deliberadamente demasiado estricta para verificar que FRR detecta sobre-restricción.

## Criterio anti-trivialidad

Una condición que logre cero errores respondiendo siempre `UNKNOWN` o absteniéndose no se considerará superior si destruye la utilidad generativa.

## Estado

`DESIGN_ONLY`. No ejecutado.
