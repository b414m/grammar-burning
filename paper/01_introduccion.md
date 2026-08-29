# Introducción v0.1

## 1. Problema

Los modelos generativos producen lenguaje mediante mecanismos probabilísticos capaces de mantener coherencia local y resolver tareas abiertas. Sin embargo, la fluidez del lenguaje no garantiza que una transición entre afirmaciones sea válida dentro del proyecto técnico donde ocurre. Un sistema puede disponer de datos correctos y aun así transformar una observación descriptiva en una conclusión causal no soportada; puede recibir una preferencia humana y convertirla en evidencia; puede recomendar una acción y tratar la recomendación como autorización; o puede confundir un artefacto de diseño con una capacidad ya implementada.

Estos errores comparten una estructura: el sistema atraviesa una frontera semántica sin satisfacer las condiciones que vuelven admisible esa transición.

El problema se vuelve más difícil en arquitecturas agénticas porque el lenguaje ya no es únicamente una salida para lectura humana. Puede actuar como interfaz entre agentes, contratos, herramientas y decisiones de ejecución. Por ello, una promoción semántica no soportada puede convertirse en un cambio material del estado del sistema.

## 2. Del significado como uso a las condiciones de formación

Una primera intuición proviene de la filosofía tardía de Wittgenstein: el significado de una expresión depende de su uso dentro de una práctica. Términos aparentemente idénticos pueden adquirir condiciones distintas de aplicación en proyectos técnicos diferentes. Por ejemplo, “el modelo está listo” puede referirse a desempeño de validación, aptitud para despliegue, disponibilidad del pipeline o aceptación de producto, dependiendo del juego de lenguaje en que aparece.

Esta intuición no basta para responder qué limita esos usos. La perspectiva arqueológica asociada con Foucault desplaza la pregunta hacia las regularidades que permiten que ciertos objetos, enunciados, posiciones de autoridad y condiciones de verdad puedan aparecer dentro de una formación discursiva. El interés de este trabajo no es equiparar directamente una arquitectura de software con una episteme histórica, sino tomar en serio una consecuencia metodológica: las reglas relevantes no deberían deducirse de una taxonomía de disciplinas, sino reconstruirse desde el archivo de prácticas y transiciones observables.

## 3. Arqueología prospectiva

La arqueología tradicional trabaja retrospectivamente sobre un archivo ya sedimentado. Los sistemas agénticos ofrecen una posibilidad distinta: cada ejecución puede dejar artefactos machine-readable que registren intención, evidencia, provenance, autoridad, contratos, decisiones, rechazos y cambios de estado. Si esos artefactos se diseñan deliberadamente para preservar las condiciones de cada transición, el sistema comienza a producir un archivo de su propia práctica mientras ésta todavía se está formando.

Llamamos provisionalmente **arqueología prospectiva** al procedimiento de usar ese archivo vivo para proponer reglas de formación, convertirlas en restricciones ejecutables y volver a observar sus efectos sobre la práctica futura.

La expresión no pretende resolver por decreto el problema filosófico de observar una episteme desde el presente. Su función es operacional: nombrar un ciclo en el que las regularidades candidatas permanecen falsables, versionadas y sujetas a revisión.

## 4. Regla de formación operacional

En este trabajo, una regla de formación no se acepta por su elegancia conceptual. Debe distinguir transiciones.

```text
si una regla no prohíbe,
restringe o exige nada observable,
todavía no es una regla operacional
```

Ejemplos de reglas candidatas son:

```text
candidatura != selección
intención != evidencia
propuesta != autoridad
clase de evidencia != promoción automática de claim
autorización != ejecución
```

Cada regla debe declarar su alcance, un contraejemplo, una representación ejecutable y un mecanismo de evaluación independiente.

## 5. De la arqueología a la inferencia

Una vez que una regla alcanza suficiente madurez surge una segunda pregunta: ¿puede utilizarse no sólo para describir o auditar el sistema, sino para condicionar la generación futura?

Proponemos separar al generador probabilístico de un **estado epistémico exógeno** que represente, según el dominio, evidencia disponible, provenance, autoridad, clase de afirmación admisible e incertidumbre. Las reglas de formación operan entonces sobre movimientos semánticos propuestos antes de que éstos se acepten como nuevos estados o salidas del sistema.

La hipótesis no sostiene que este mecanismo elimine las alucinaciones en general. Su alcance es más estrecho: dentro de la clase de transiciones representables por las reglas, la combinación de estado epistémico exógeno y enforcement ejecutable debería reducir transiciones no soportadas sin destruir proporcionalmente la capacidad generativa útil.

## 6. Contribuciones previstas

El trabajo separa tres contribuciones que deberán validarse de manera independiente:

1. un protocolo para descubrir y madurar reglas de formación a partir de archivos humano-agente;
2. una arquitectura de generación condicionada por estado epistémico exógeno y reglas ejecutables;
3. un protocolo experimental que mida reducción de transiciones no soportadas, cobertura, falsos rechazos, abstención y utilidad.

Las contribuciones se consideran hipótesis de investigación mientras no exista evidencia experimental suficiente. El objetivo del proyecto es permitir que el alcance final sea determinado por los resultados, no por la amplitud de la formulación inicial.
