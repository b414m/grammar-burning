# H01 - Generación epistémicamente condicionada

## Hipótesis principal

> Condicionar la generación sobre un estado epistémico exógeno al generador y sobre reglas de formación ejecutables reduce la tasa de transiciones semánticas no soportadas, evaluadas por un oráculo independiente de esas reglas, a un costo de capacidad generativa útil que es medible y menor que el beneficio, dentro de la clase de transiciones que las reglas alcanzan a expresar.

## Variables conceptuales

Sea:

- `G`: generador probabilístico base;
- `E`: estado epistémico exógeno al generador;
- `R`: conjunto versionado de reglas de formación ejecutables;
- `C(R)`: clase de transiciones que `R` puede representar;
- `O`: oráculo de evaluación independiente de `R`;
- `T_u`: transición semántica no soportada;
- `U`: medida de capacidad generativa útil.

La condición experimental central compara:

```text
G
```

contra:

```text
G | E, R
```

sobre una misma distribución de tareas.

## Resultado primario

Dentro de `C(R)`:

```text
Rate(T_u | G, E, R) < Rate(T_u | G)
```

El resultado no puede explicarse únicamente por abstención indiscriminada ni por degradación sustancial de utilidad.

## Subhipótesis

### H1.1 - Estado epistémico
Agregar un estado epistémico exógeno reduce transiciones no soportadas frente al generador base.

### H1.2 - Reglas ejecutables
Agregar `R` sobre `E` produce una reducción adicional frente a usar `E` sin enforcement.

### H1.3 - No trivialidad por abstención
La reducción de errores no se explica solamente por un aumento de respuestas vacías, negativas o de abstención.

### H1.4 - Costo medible
La pérdida de utilidad generativa puede cuantificarse y se mantiene bajo un umbral predefinido o presenta una frontera de Pareto favorable frente a la reducción de errores.

### H1.5 - Cobertura explícita
Los beneficios se reportan separando eficacia de cobertura. No se extrapola el resultado a clases de error que `R` no puede representar.

## Condiciones experimentales mínimas

- `A`: LLM base.
- `B`: LLM + retrieval/contexto, cuando aplique.
- `C`: LLM + estado epistémico estructurado, sin reglas ejecutables.
- `D`: LLM + estado epistémico estructurado + reglas ejecutables.

## Métricas candidatas

- **UTR**: Unsupported Transition Rate.
- **EUTR**: Expressible Unsupported Transition Rate.
- **RC**: Rule Coverage.
- **FRR**: False Rejection Rate.
- **URR**: Useful Response Rate.
- **AAR**: Appropriate Abstention Rate.
- **UCS**: Unsupported Claim Severity.

Las definiciones operacionales de estas métricas deberán congelarse antes de observar resultados finales.

## Independencia del oráculo

`O` no puede ser la misma implementación usada para imponer `R`. El protocolo debe registrar identidad, versión y provenance del oráculo y debe permitir auditoría de desacuerdos.

## Falsadores relevantes

La hipótesis se debilita o rechaza si ocurre alguno de los siguientes casos dentro del alcance declarado:

1. `E + R` no reduce EUTR frente al baseline.
2. La reducción desaparece bajo evaluación independiente.
3. La mejora proviene casi totalmente de abstención indiscriminada.
4. La pérdida de utilidad supera el beneficio definido antes del experimento.
5. La regla genera una tasa elevada de falsos rechazos de transiciones válidas.

## No-afirmaciones

Esta hipótesis no afirma que:

- todas las alucinaciones sean transiciones semánticas expresables;
- una gramática pueda garantizar verdad factual;
- las reglas descubiertas sean universales;
- un estado epistémico correcto pueda compensar evidencia de origen incorrecta;
- restringir más siempre produzca mejores sistemas.
