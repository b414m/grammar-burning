# EXP05-A Phase 2 - Freeze del paquete de transporte para generador ciego

## Propósito

Registrar exactamente qué material se expuso al generador ciego mediante el repositorio público `b414m/clau-workspace`.

El paquete público es una proyección de transporte del brief y prompt internos ya congelados. Se removieron metadatos de investigación que podían revelar al generador la existencia o identidad de reglas, motor o repositorios relacionados. No se modificó el contenido funcional de la aplicación solicitado al generador.

## Repositorio público

- repositorio: `b414m/clau-workspace`
- rama: `main`
- acceso esperado del generador: lectura solamente

## Archivos expuestos

### `README.md`

- propósito: orientar el inicio y la entrega por ZIP
- SHA-256: `c044ebdba5843542f001fccec8f4f039eafde7b3fb3cf153da84c0cd1e76184a`

### `app_project_brief.v0.1.json`

- derivado de `experiments/EXP05-A/app_project_brief.v0.1.json`
- se removieron únicamente campos de metadatos de investigación (`experiment` y `formation_rules_disclosed_to_generator`)
- las restricciones funcionales, intención, capacidades mínimas, non-goals, decisiones abiertas, acceptance focus y archive requirement se conservaron
- SHA-256: `483a85e2dfb7f9d3b280608ddfda1fb0710c20d75340bf70f28b107861ffd51d`

### `blind_generator_prompt.v0.1.md`

- derivado de `experiments/EXP05-A/blind_generator_prompt.v0.1.md`
- se removieron nombres que podían revelar contexto experimental oculto y se añadió instrucción operacional explícita de devolver un ZIP porque el generador no requiere permisos de escritura en GitHub
- mantiene el requisito de archivo cronológico, estructura durable, manifest con SHA-256 y prohibición de completar artificialmente ausencias
- SHA-256: `1de035a20f6a02f8177f2af5297fe7f3c98e13abaa7e6fd95e561ad295bc9124`

## Commits de materialización pública

- README: `5b13feacdc04c4cc87a8dd5b6d499889bf4a90c9`
- brief: `0ef29862ae3ab3b19621117077dcf7124990a426`
- prompt: `6f308488f05307c8a6bcbca6aeb6a1b5ab4b0f38`

El commit final del repositorio público después de materializar el paquete es `6f308488f05307c8a6bcbca6aeb6a1b5ab4b0f38`.

## Regla de contaminación

Durante la generación, el generador sólo debe consultar `clau-workspace`. Si accede deliberadamente a repositorios relacionados, reglas, resultados anteriores o información acerca del sistema evaluador, la corrida no podrá usarse como evidencia limpia de transferencia cross-domain y deberá clasificarse como piloto o contaminada.

## Estado

`BLIND_GENERATOR_TRANSPORT_FROZEN`
