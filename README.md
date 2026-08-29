# grammar-burning

# Gramáticas en formación
## Un método de arqueología prospectiva para sistemas agénticos y generación epistémicamente condicionada

`grammar-burning` es un laboratorio de investigación para estudiar cómo reconstruir reglas de formación a partir del archivo producido por sistemas humano-agente y cómo reutilizar reglas suficientemente sustentadas como restricciones ejecutables durante generación posterior.

El repositorio no parte de la existencia de una gramática universal. Las reglas se consideran hipótesis revisables y deben ganar madurez mediante evidencia, contraejemplos, operacionalización, pruebas adversariales y validación entre dominios.

## Tesis de trabajo

Una gramática operacional no se define como un catálogo de términos, sino como un conjunto de restricciones sobre transformaciones posibles dentro de proyectos del lenguaje. Una regla candidata sólo adquiere valor metodológico cuando puede distinguir al menos una transición admisible de una inadmisible y existe un procedimiento independiente para evaluar esa distinción.

## Hipótesis experimental principal

> Condicionar la generación sobre un estado epistémico exógeno al generador y sobre reglas de formación ejecutables reduce la tasa de transiciones semánticas no soportadas, evaluadas por un oráculo independiente de esas reglas, a un costo de capacidad generativa útil que es medible y menor que el beneficio, dentro de la clase de transiciones que las reglas alcanzan a expresar.

## Líneas de trabajo

- **Descubrimiento de reglas de formación**: archivo -> regularidad -> regla candidata -> contraejemplo -> gate/contrato -> ataque -> prueba entre dominios.
- **Generación epistémicamente condicionada**: generador probabilístico + estado epistémico exógeno + reglas ejecutables + oráculo independiente.
- **Arqueología prospectiva**: hacer que el sistema deje un archivo machine-readable de decisiones, evidencias, autoridades, transiciones y rechazos mientras la práctica todavía se está formando.

## Estructura inicial

```text
paper/                 borrador del artículo en español
method/                protocolo de descubrimiento
formation-rules/       registro versionado de reglas candidatas
schema/                 contratos conceptuales machine-readable
hypotheses/             hipótesis falsables
experiments/            diseños y resultados experimentales
claims/                 registro de afirmaciones y su estado
```

## Regla editorial del proyecto

Una afirmación filosóficamente sugerente no se trata como contribución técnica hasta que podamos responder:

1. ¿Qué transición prohíbe o restringe?
2. ¿Qué artefactos la sustentan?
3. ¿Qué contraejemplo podría falsarla?
4. ¿Cómo se evalúa sin usar la propia regla como juez?

## Estado

Trabajo exploratorio. Las definiciones, nombres y niveles de madurez son provisionales. El repositorio separará explícitamente evidencia observada, inferencias, decisiones normativas y resultados experimentales.
