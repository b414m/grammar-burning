# EXP05-A Phase 1 - Resultado del probe sintético cross-domain

## Estado

`IMPLEMENTATION_PROBE_ONLY`

Este resultado no constituye validación científica cross-domain ni permite promover reglas a R4. La fase utilizó fixtures sintéticos y un oráculo de fixtures definido por el mismo equipo de investigación.

## Ejecución de referencia

- repositorio ejecutor: `b414m/data-value-compiler`
- rama: `eli-formation-rule-engine-v0.1`
- commit: `a25c8d794183f61832f4600fff4fc63ffa7f2f9e`
- GitHub Actions run: `33279508594`
- tests: `13 passed`
- artifact: `exp05a-phase1-synthetic-probe`
- artifact id: `9722550029`
- artifact digest: `sha256:87c83e605958a1ee5b98d21f37a175797441a8fd6dfb293e0927eed8d88f42be`

## Resultado observado

Todos los casos coincidieron con las etiquetas del oráculo de fixtures.

| Regla ejecutable | Dominios del probe | Resultado fase 1 |
|---|---|---|
| `FR-A-PROPOSAL-SELECTION-AUTHORITY` | data_value, app_development | `SYNTHETIC_TRANSFER_OBSERVED` |
| `FR-B-EVIDENCE-CLAIM-CEILING` | data_value, app_development | `REPRESENTATION_GAP` |
| `FR-C-AUTHORIZATION-EXECUTION` | data_value, app_development | `SYNTHETIC_TRANSFER_OBSERVED` |

La señal más informativa es FR-B: el motor actual representa una jerarquía `descriptive/diagnostic/predictive/causal/prescriptive`, pero no puede trasladarla sin modificación a afirmaciones de assurance de software. El caso `APP-B1` produjo `UNKNOWN` con `claim_class_or_ceiling_unknown`.

Esto evita una conclusión artificial de universalidad. La regla abstracta “evidence class cannot silently promote claim class” puede seguir siendo candidata, pero su taxonomía concreta de claims es actualmente dependiente del dominio.

## Lo que sí permite afirmar esta fase

1. El mismo código de FR-A discrimina fixtures válidos e inválidos en dos vocabularios de proyecto sin modificación de la regla.
2. El mismo código de FR-C discrimina autorización, aceptación de proveedor y ejecución en ambos dominios sintéticos.
3. El diseño fail-closed expone una insuficiencia representacional en FR-B en lugar de reinterpretar automáticamente una clase de afirmación desconocida.
4. El pipeline produce un artefacto machine-readable reproducible desde CI.

## Lo que no permite afirmar

- que FR-A o FR-C sean reglas cross-domain R4;
- que FR-B sea falsa o universal;
- que el desarrollo de apps constituya una episteme separada;
- que exista todavía un oráculo independiente;
- que el método general de Grammar esté validado.

## Siguiente condición experimental

La fase 2 debe introducir un archivo real de desarrollo de aplicación generado sin adaptar retrospectivamente los casos a las reglas, y un protocolo de adjudicación independiente del `FormationRuleEngine`.
