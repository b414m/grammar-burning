# EXP05-A Phase 2 - Brief de generación ciega del archivo app

## Propósito

Producir un archivo de desarrollo de aplicación que pueda ser evaluado posteriormente por el `FormationRuleEngine` sin haber sido diseñado para satisfacer sus reglas.

El generador de este archivo no debe recibir:

- el registro de Formation Rules;
- el código del motor;
- los resultados de EXP05-A fase 1;
- las etiquetas esperadas del oráculo;
- ejemplos de ataques construidos alrededor de FR-001..FR-006.

Puede recibir únicamente el brief funcional congelado `app_project_brief.v0.1.json` y las instrucciones generales de conservar artefactos y decisiones del proceso.

## Regla de independencia

La independencia aquí significa independencia informacional respecto del motor, no independencia organizacional absoluta. El generador puede ser humano o agente, pero la sesión de generación debe quedar aislada de las reglas bajo prueba.

Si el generador conoce las Formation Rules, el archivo resultante se clasifica como `CONTAMINATED_FOR_CROSS_DOMAIN_VALIDATION` y sólo puede utilizarse como piloto.

## Instrucción para el generador

Desarrolla una aplicación pequeña de registro de asistencia a partir del brief adjunto. Trabaja como lo harías normalmente. Conserva las decisiones y artefactos que produzcas durante el proceso, incluyendo propuestas descartadas, dudas, supuestos, cambios de requisito, artefactos de diseño, implementación, pruebas y cualquier intento de ejecución o despliegue.

No clasifiques los artefactos en términos de reglas epistemológicas ni intentes anticipar qué será considerado válido o inválido por un evaluador posterior.

## Archivo mínimo de salida

La ejecución debe producir un directorio durable con:

```text
00_input/
01_dialogue_or_worklog/
02_requirements/
03_design/
04_implementation/
05_tests/
06_execution_or_deploy/
07_decisions/
08_unknowns/
manifest.json
```

No todos los directorios tienen que contener artefactos. La ausencia debe quedar registrada en `manifest.json`, no rellenada artificialmente.

## Manifest mínimo

Cada artefacto debe registrar:

- `artifact_id`;
- `relative_path`;
- `artifact_type`;
- `producer`;
- `created_order`;
- `sha256`;
- `source_artifact_refs` cuando existan;
- `notes` opcionales.

El manifest no debe contener etiquetas `SUPPORTED/UNSUPPORTED` ni referencias a Formation Rules.

## Congelamiento

Una vez finalizada la generación:

1. calcular hashes de todos los artefactos;
2. congelar el commit o bundle del archivo;
3. generar `archive_identity.json` con commit/hash raíz;
4. sólo entonces permitir acceso al motor y al protocolo de adjudicación.

## Estado

`READY_FOR_BLIND_GENERATION`
