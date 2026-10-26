# POC-01 — Estimación de partidas con históricos vs. línea base manual

**Semana 4 · Proyecto Integrador · Grupo 1 · Constructora Andina S.A.C.**
Tendencia: BI y analítica operacional (anillo *Adoptar*).

> **Vigente:** [Hito I v1.2, §5](../../documentos/proyecto/Semana5_Hito_I_v1.2.md) y [protocolo independiente v1.2](revision-v1.2/DISENO_EXPERIMENTAL.md), **diseño no ejecutado** y pendiente de validación humana. El contenido siguiente describe el experimento histórico, no el nuevo comparador. No transferir sus resultados al protocolo v1.2.

## Pregunta

¿Usar los históricos de obras cerradas para estimar partidas de una obra nueva reduce el error de estimación frente a la estimación manual sin base integrada?

## Hipótesis

**H1 revisada (24/10/2026):** en el escenario sintético, el método por ratios de costo/unidad alcanza **MAPE promedio ≤15 %** y reducción relativa ≥30 % frente a un control simulado. No se exige que cada partida esté dentro de ±15 % ni se afirma significancia estadística. El tareo generado no se utiliza en el estimador actual.

## Alcance y exclusiones

- **Se prueba:** el método de estimación por ratios históricos (costo/unidad) y la mecánica de medición del error (MAPE), sobre datos sintéticos.
- **No se prueba:** desempeño real de negocio, integración con el ERP productivo, calidad de datos reales, adopción de usuarios.
- **Exclusión explícita:** no se conecta con producción ni con datos confidenciales.

## Datos

- Origen: **sintéticos**, generados por `src/synthetic_erp_data.py` con semilla fija `20261002`.
- Contenido en `datos/`: `obras.csv`, `catalogo_partidas.csv`, `metrados.csv`, `costos.csv`, `tareo.csv`, `obra_nueva.csv` y `obra_nueva_real.csv` (verdad de referencia, solo para evaluación).
- Volumen: 6 obras cerradas, 8 partidas de catálogo, 1 obra nueva (6 partidas).
- Limitación: no reproduce la variabilidad ni la calidad de datos de un ERP real.

## Métricas y umbrales (definidos antes de ejecutar)

| Métrica | Umbral de aceptación | Decisión |
|---|---|---|
| MAPE del método analítico | ≤ 15 % | Continuar |
| Reducción del error vs. base manual | ≥ 30 % | Continuar |
| MAPE del método analítico | > 30 % | Detener |

Los umbrales son **metas internas académicas**, no benchmarks de negocio. AACE 18R-97 no demuestra un umbral MAPE por partida para este caso. Reglas uniformes: continuar si se cumplen ambas metas; detener si MAPE analítico >30 %; modificar en cualquier otro caso. Si el MAPE del control es cero, la reducción relativa no se define: modificar el diseño, sin inventar un porcentaje. Un costo real cero produce error explícito, no un falso error de 0 %.

## Procedimiento (reproducible)

**Procedimiento histórico con escritura: no ejecutarlo sobre este repositorio para verificarlo.** Regenera `datos/*.csv` y `resultados/resultados.csv`; `verificar_poc.py` también los sobrescribe. El bloque se conserva como antecedente. Para comprobación actual de solo lectura y trabajo futuro aislado, consultar el [flujo seguro](../../documentos/mantenimiento/PREPARACION_SEMANA_06.md).

```bash
cd poc/POC-01-estimacion-historicos
python3 src/synthetic_erp_data.py    # genera datos/*.csv desde la raiz de la PoC
python3 src/experimento_bi.py        # calcula ratios, estima y evalúa
python3 pruebas/verificar_poc.py    # fixture sintética y comparación reproducible
python3 -m unittest discover -s pruebas -p "test_*.py"
```

Solo requiere Python 3 estándar (sin dependencias externas).

## Resultados

Semilla `20261002`, 6 partidas estimadas:

| Métrica | Valor |
|---|---|
| MAPE línea base manual | 20,19 % |
| MAPE método analítico | 11,31 % |
| Reducción del error | 43,98 % |
| ¿MAPE analítico ≤ 15 %? | SÍ |
| ¿Reducción ≥ 30 %? | SÍ |

Detalle por partida en `resultados/resultados.csv`.

## Limitaciones

- Resultados **simulados**: validan el método y las métricas, no el desempeño real.
- El modelo subestima obras más difíciles porque el ratio histórico promedia tipos de obra; se recomienda ajustar por tipo de obra en una segunda iteración.
- La línea base manual es una simulación con variabilidad asumida (σ = 25 %), declarada como supuesto.
- El control aplica ruido al costo real conocido; no es una estrategia de estimación que pueda usarse antes de conocer el real ni una medición humana.
- Una semilla, una obra nueva y seis partidas no demuestran generalización. No hay prueba de significancia, tablero, benchmark de carga ERP ni medición de adopción.
- CIM-01 e INS-02 superan 15 % de error individual; no ocultar esos resultados por cumplir el promedio.
- El CSV de resultados conserva ocho decimales de error desde v1.1 para evitar la diferencia de 0,01 puntos en la reducción al recomputarla desde valores redondeados.

## Decisión

**CONTINUAR solo la experimentación.** El escenario fijo cumple ambas metas descriptivas; no autoriza despliegue ni demuestra beneficio real. H2 y H3 están pendientes. Conservar umbrales al cambiar escenarios, medir sensibilidad y revisar sesgo. La decisión corresponde a **D-12** en el registro reconciliado del Hito I v1.1 (antes D-07 de S4). Los resultados originales de la entrega no se reescriben.

## Trazabilidad

- [Documento histórico S4](../../documentos/proyecto/Semana4_Proyecto_Integrador.md).
- [Corrección histórica v1.1](../../documentos/proyecto/Semana5_Hito_I_v1.1.md), sección 5; supuestos S-17/S-19.
- [Revisión vigente v1.2](../../documentos/proyecto/Semana5_Hito_I_v1.2.md), sección 5, y [nuevo diseño no ejecutado](revision-v1.2/DISENO_EXPERIMENTAL.md).
- Las fuentes históricas no verificadas no se emplean como prueba de los umbrales internos.
