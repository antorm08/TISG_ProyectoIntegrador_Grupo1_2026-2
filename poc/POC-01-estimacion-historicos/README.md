# POC-01 — Estimación de partidas con históricos vs. línea base manual

**Semana 4 · Proyecto Integrador · Grupo 1 · Constructora Andina S.A.C.**
Tendencia: BI y analítica operacional (anillo *Adoptar*).

## Pregunta

¿Usar los históricos de obras cerradas para estimar partidas de una obra nueva reduce el error de estimación frente a la estimación manual sin base integrada?

## Hipótesis

**H1 (valor):** si se integran los históricos de tareo, metrados y costos de obras cerradas en un modelo analítico y se usan para estimar las partidas de una obra nueva, entonces el desvío entre el costo estimado y el costo real se reduce a un máximo de **±15 %** (MAPE), frente a la línea base manual.

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

Los umbrales de exactitud se anclan en AACE International (2020) RP 18R-97.

## Procedimiento (reproducible)

```bash
cd poc/POC-01-estimacion-historicos
python3 src/synthetic_erp_data.py    # genera ../datos/*.csv
python3 src/experimento_bi.py        # calcula ratios, estima y evalúa
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

## Decisión

**CONTINUAR.** H1 queda respaldada en este experimento sintético: el método analítico cumple ambos umbrales. La siguiente iteración (ajuste por tipo de obra) y la validación con datos anonimizados quedan para semanas posteriores. La decisión se registra en `gestion/registros/` (D-07).

## Trazabilidad

- Documento Semana 4: `documentos/proyecto/Semana4_Proyecto_Integrador.md` (secciones 3, 4 y 5).
- Fuentes: AACE International (2020); Abdelalim et al. (2025); Elserougy et al. (2024).
