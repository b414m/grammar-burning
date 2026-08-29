# H02: descubrimiento de reglas de formación

Estado: METHOD HYPOTHESIS v0.1

## Hipótesis

Un archivo machine-readable producido por una práctica humano-agente puede utilizarse para reconstruir reglas de formación operacionalizables cuando las regularidades candidatas se someten a contraejemplos, implementación ejecutable, evaluación adversarial y pruebas de transferencia entre dominios.

## No se afirma

- que toda regularidad observada sea una regla de formación;
- que las reglas descubiertas sean universales o ahistóricas;
- que una taxonomía de dominios equivalga a una gramática;
- que la supervivencia en un solo dominio establezca generalidad;
- que la implementación de una regla demuestre su corrección normativa.

## Criterio mínimo de promoción

Una regularidad candidata R sólo puede avanzar de observación a regla operacional si existe al menos un x tal que R(x) produzca una consecuencia verificable distinta de no intervenir.

En forma abreviada:

```text
if rule forbids_or_redirects_nothing:
    not yet a formation rule
```

## Niveles de madurez

- R0 OBSERVATION: regularidad percibida en el archivo.
- R1 CANDIDATE: formulación explícita con alcance tentativo.
- R2 OPERATIONAL: expresada como gate, contrato o verificador ejecutable.
- R3 ADVERSARIAL: sobrevivió contraejemplos diseñados para violarla.
- R4 CROSS_DOMAIN: conserva poder discriminante en al menos un dominio diferente.
- R5 PROMOTED: evidencia acumulada suficiente para tratarla provisionalmente como parte de una gramática operacional.

La promoción sigue siendo revisable.

## Prueba inicial

EXP05-A compara reglas observadas en Data Value / DVL con un flujo de desarrollo de aplicación deliberadamente no centrado en ML. El resultado esperado no es que todas sobrevivan. Las reglas que fallen son evidencia sobre el límite de alcance del estrato descubierto.

## Criterio de falsación fuerte

H02 se debilita si las reglas candidatas sólo pueden formularse después de conocer el dominio de destino, si pierden toda capacidad de rechazo fuera del caso que las originó, o si el procedimiento de promoción acepta reglas tan abstractas que cualquier transición resulta compatible con ellas.
