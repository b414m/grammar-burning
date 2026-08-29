# Grammar Discovery Protocol v0.1

## Propósito

Definir un procedimiento reproducible para proponer, operacionalizar, atacar y promover reglas de formación a partir de un archivo de práctica humano-agente.

Este protocolo no presupone que las reglas descubiertas sean universales ni que constituyan por sí mismas una episteme. Su función es separar observaciones, hipótesis de regularidad, decisiones normativas y evidencia experimental.

## Unidad de análisis

La unidad mínima es una **transición semántica** entre dos estados o posiciones discursivas. Ejemplos:

- propuesta -> selección;
- evidencia descriptiva -> afirmación predictiva;
- autorización -> ejecución;
- artefacto de diseño -> capacidad de runtime.

La transición debe poder representarse de forma suficientemente explícita para que un verificador determine si cumple o viola una regla candidata.

## Ciclo de descubrimiento

```text
archivo observado
      ↓
tensión o regularidad recurrente
      ↓
regla de formación candidata
      ↓
contraejemplo explícito
      ↓
operacionalización como gate/contrato
      ↓
prueba adversarial
      ↓
validación entre dominios
      ↓
promover / revisar / rechazar
```

## Requisitos mínimos de una regla candidata

Toda regla FR-x debe declarar:

- `statement`: formulación breve y falsable;
- `scope`: clase de transiciones a la que pretende aplicar;
- `forbids_or_requires`: qué transición prohíbe, restringe o exige;
- `observed_from`: artefactos o experimentos que motivaron la regla;
- `counterexample`: caso que debería ser rechazado si la regla es válida;
- `operationalization`: gate, contrato, esquema o verificador ejecutable;
- `oracle`: procedimiento de evaluación independiente de la implementación de la regla;
- `known_limits`: qué no afirma la regla;
- `maturity`: nivel de madurez R0-R5.

Una formulación que no prohíbe, restringe o exige ninguna transición concreta no se considera todavía una regla de formación operacional.

## Niveles de madurez

### R0 - Observación
Aparece una tensión o regularidad, pero todavía no existe una regla falsable.

### R1 - Regla candidata
Existe formulación falsable, alcance provisional y al menos un contraejemplo.

### R2 - Operacionalizada
La regla tiene representación ejecutable como gate, contrato o verificador.

### R3 - Adversarialmente probada
Existe al menos un ataque explícito diseñado para romper la regla y se documenta el resultado.

### R4 - Validada entre dominios
La regla conserva poder discriminativo fuera del dominio donde fue descubierta. Un fallo en otro dominio reduce su alcance en lugar de forzar su universalidad.

### R5 - Regla promovida de gramática
Existe evidencia suficiente para tratarla como regla estable dentro de un alcance declarado y versionado. R5 no significa universal ni eterna.

## Separación descriptivo / normativo

Descubrir una regularidad no autoriza automáticamente imponerla.

```text
regularidad observada
        ≠
regla normativamente adoptada
```

Toda promoción a una restricción activa debe registrar quién o qué proceso tuvo autoridad para adoptarla y con qué justificación.

## Oráculo independiente

Una regla no puede validarse únicamente preguntando a su propia implementación si fue satisfecha. La evaluación debe depender de un oráculo independiente, por ejemplo:

- anotación humana experta con protocolo explícito;
- dataset gold construido por separado;
- reglas de referencia independientes;
- adjudicación entre múltiples jueces con resolución documentada.

El oráculo puede equivocarse. Por ello también debe tener provenance y versionado.

## Prueba entre dominios

La validación entre dominios no busca demostrar que dos dominios comparten una episteme. Busca medir qué reglas sobreviven al cambio de objetos, vocabulario y prácticas.

Una regla que falla fuera de su dominio de origen puede seguir siendo válida como regla local.

## Criterio de promoción

Una regla no asciende de nivel por consenso retórico. Debe cumplir la evidencia mínima del nivel correspondiente y conservar trazabilidad hacia artefactos concretos.

## Criterio de rechazo

Una regla puede ser:

- `rejected`: contradicha dentro de su alcance declarado;
- `revised`: el alcance o formulación se estrecha;
- `superseded`: una regla posterior explica mejor los mismos casos;
- `retained_local`: falla cross-domain pero se conserva como regla específica de dominio.

## Principio de archivo

El proyecto debe producir suficiente evidencia machine-readable para que un tercero pueda reconstruir por qué una regla fue propuesta, implementada, atacada y promovida sin depender de la memoria de una conversación.
