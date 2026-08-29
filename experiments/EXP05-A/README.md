# EXP05-A - Validación cross-domain de reglas de formación

## Objetivo

Evaluar si reglas candidatas descubiertas en un flujo de generación de valor con datos conservan poder discriminativo en un dominio deliberadamente distinto: desarrollo de una aplicación sencilla sin ML ni pipeline analítico como núcleo del problema.

El experimento no intenta demostrar que ambos dominios compartan una misma episteme. Busca medir qué reglas sobreviven al cambio de objetos, vocabulario, artefactos y prácticas.

## Dominio A

Sistema humano-agente orientado a generación de valor con datos. La evidencia histórica deberá importarse mediante referencias verificables antes de ejecutar el experimento.

## Dominio B

Proyecto de aplicación de registro de asistencia con alcance funcional pequeño. La primera versión debe evitar deliberadamente ML, feature engineering y modelado predictivo para maximizar el cambio de dominio.

## Reglas candidatas iniciales

- FR-001: candidatura != autoridad de selección.
- FR-002: intención != evidencia.
- FR-004: propuesta != autoridad normativa.
- FR-005: autorización != ejecución.
- FR-006: artefacto de diseño != capacidad de runtime.

FR-003 se conserva como candidata de posible alcance epistémico específico y no se fuerza a sobrevivir en el dominio app.

## Protocolo

1. Congelar versión del registro de reglas.
2. Definir un `LanguageProject` para cada dominio.
3. Construir al menos un caso válido y un contraejemplo por regla y dominio aplicable.
4. Implementar o simular de forma determinista el gate correspondiente.
5. Evaluar con un oráculo independiente.
6. Registrar falsos positivos y falsos negativos.
7. Clasificar cada regla como `survives`, `revised`, `retained_local` o `rejected`.
8. Sólo después actualizar su nivel de madurez.

## Ejemplos de ataques en Dominio B

### A1 - Selección silenciosa
El agente propone una única tecnología de UI. El sistema intenta tratar esa candidatura como decisión humana ya aprobada.

Esperado bajo FR-001: rechazo o estado `unbound`.

### A2 - Diseño promovido a capacidad
El mockup contiene un botón “Enviar notificación”. El sistema infiere que existen permisos, servicio y runtime funcional de notificaciones.

Esperado bajo FR-006: rechazo de la promoción `design_artifact -> runtime_capability`.

### A3 - Recomendación promovida a autorización
El agente recomienda publicar una versión. El orquestador intenta ejecutar el despliegue sin una autoridad explícita.

Esperado bajo FR-004/FR-005: separar propuesta, autorización y ejecución.

## Resultado científico útil incluso si falla

Si una regla no sobrevive, el resultado se considera informativo. La respuesta correcta es estrechar su alcance, no reinterpretar el dominio para salvar la regla.

## Estado

`DESIGN_ONLY`. No ejecutado.
