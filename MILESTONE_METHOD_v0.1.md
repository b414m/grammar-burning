# METHOD MILESTONE v0.1

Estado del repositorio en este hito:

- METHOD: FROZEN v0.1
- OPERATIONAL DEFINITIONS: FROZEN v0.1
- HYPOTHESES: FROZEN v0.1 for initial experiments
- EXPERIMENT DESIGNS: OPEN TO EXECUTION DETAILS, not to post-hoc hypothesis rewriting
- RESULTS: OPEN
- CONCLUSIONS: OPEN
- ORIGINALITY CLAIM: UNESTABLISHED pending systematic state-of-the-art review

## Título de trabajo

**Gramáticas en formación: un método de arqueología prospectiva para sistemas agénticos y generación epistémicamente condicionada**

## Tesis mínima defendible

El proyecto investiga un método para reconstruir reglas de formación a partir del archivo machine-readable producido durante prácticas humano-agente, operacionalizarlas como restricciones ejecutables y evaluar su capacidad para discriminar y condicionar transiciones semánticas.

## Hipótesis experimental central

Condicionar la generación sobre un estado epistémico exógeno al generador y sobre reglas de formación ejecutables reduce la tasa de transiciones semánticas no soportadas, evaluadas por un oráculo independiente de esas reglas, a un costo de capacidad generativa útil medible y menor que el beneficio, dentro de la clase de transiciones que las reglas alcanzan a expresar.

## Disciplina de evidencia

El artículo debe crecer en el orden:

```text
experiment
  -> artifact
  -> result
  -> allowed claim
  -> paper
```

No se permite promocionar una hipótesis a conclusión mediante edición narrativa sin artefactos experimentales que la soporten.

## Próximo frente experimental

El siguiente trabajo se traslada al compilador para implementar un núcleo mínimo formado por:

```text
EpistemicState
+ SemanticMove
+ FormationRule
-> FormationRuleEngine
-> ALLOW | REJECT | DOWNGRADE | RETRIEVE | ASK | UNKNOWN
```

La implementación debe vivir en una línea versionada nueva, sin reescribir retrospectivamente los experimentos congelados del compilador.
