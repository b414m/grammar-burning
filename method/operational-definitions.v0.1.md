# Definiciones operacionales v0.1

Estado: FROZEN FOR METHOD MILESTONE v0.1

Estas definiciones fijan el vocabulario mínimo del programa experimental. No se presentan como ontología universal ni como descripción exhaustiva de una episteme.

## LanguageProject

Unidad analítica que agrupa objetos, actores, enunciados, acciones, condiciones de validez, relaciones de autoridad, transiciones y artefactos dentro de una práctica situada.

Su función es permitir comparar usos y condiciones de validez sin asumir de antemano fronteras disciplinares.

## EpistemicState

Estado exógeno al generador que registra, como mínimo, la evidencia disponible, su procedencia, el techo de afirmación admisible, autoridades vigentes, incertidumbres y restricciones aplicables en un momento t.

Un EpistemicState no es la memoria interna del modelo ni una autoevaluación generada por el mismo agente.

## SemanticMove

Propuesta tipada de transformación discursiva o decisional. Ejemplos: observación -> predicción, propuesta -> selección, autorización -> ejecución.

La unidad de evaluación no es necesariamente el token ni la frase superficial, sino el cambio de posición semántica que el enunciado intenta efectuar.

## FormationRule

Restricción verificable sobre una clase de SemanticMove dadas ciertas condiciones del EpistemicState.

Una FormationRule candidata debe:
1. declarar qué transición regula;
2. declarar sus precondiciones;
3. producir una consecuencia observable cuando la transición no está soportada;
4. admitir al menos un contraejemplo que pueda violarla;
5. registrar procedencia y nivel de madurez.

Una regla que no pueda prohibir, degradar o desviar ninguna transición no se considera operacionalizada.

## FormationRuleEngine

Mecanismo determinista que recibe EpistemicState, SemanticMove y FormationRule(s), y devuelve una decisión de transición. El vocabulario inicial de decisiones es:

- ALLOW
- REJECT
- DOWNGRADE
- RETRIEVE
- ASK
- UNKNOWN

La decisión del motor no establece por sí sola verdad factual. Establece admisibilidad bajo las reglas y el estado suministrados.

## Unsupported Semantic Transition

SemanticMove cuya promoción no está suficientemente soportada por el EpistemicState según un criterio de evaluación independiente del generador. En los experimentos principales, el ground truth de esta categoría no debe provenir únicamente de las mismas reglas que condicionan la generación.

## Rule Coverage

Proporción de la clase de transiciones evaluadas que puede representarse con el lenguaje de reglas disponible. Eficacia dentro de cobertura y amplitud de cobertura se reportan separadamente.

## Useful Generative Capacity

Capacidad del generador para producir respuestas relevantes, informativas y accionables dentro de la tarea, medida independientemente de la simple ausencia de violaciones. La abstención total no cuenta como éxito.
