# POC-01 — Protocolo independiente v1.2

UNMSM, FISI. Curso: Tendencias en Ingeniería de Software y Gestión. Grupo 1.
Semana 4 integrada en Hito I S5. Versión v1.2, 25/10/2026.

## 1. Pregunta, métodos y alcance

¿El costo unitario histórico ponderado por metrado (M1) reduce el error frente a
una tarifa histórica mediana por partida (B0), al estimar una obra sintética nueva?

B0 no es una estimación humana observada ni usa el costo real futuro. Es un
comparador simple razonable. La mediana resiste extremos sin ajustar parámetros
con el conjunto evaluado; puede superar a M1. No se presupone una victoria.

Para cada partida p, con históricos H_p de costo C_hp y cantidad Q_hp >0:

- B0_p = Q_presupuestada_p × mediana(C_hp / Q_hp).
- M1_p = Q_presupuestada_p × suma(C_hp) / suma(Q_hp).

Ambos usan exactamente los mismos registros válidos, moneda y unidad. El efecto
comparado es la regla de agregación, no adopción de BI, calidad empresarial o IA.
El alcance de la evaluación es costo/unidad, no productividad HH/unidad.

## 2. Contrato de separación y prevención de fuga

| Entrada | Uso permitido | Restricción |
|---|---|---|
| `../datos/obras.csv` | Seleccionar solo OB-C01–OB-C06, estado Cerrada, 2021–2026 | OB-N01 2027 se excluye de referencia |
| `../datos/costos.csv` | Costos de las obras cerradas seleccionadas | Ningún costo de obra evaluada |
| `../datos/metrados.csv` | Cantidad de referencia por obra/partida | Join uno a uno con costos; duplicados o unidades incompatibles invalidan |
| `../datos/obra_nueva.csv` | ID de partida y cantidad presupuestada de OB-N01 | No contiene real; la cantidad es una entrada ex ante supuesta |
| `../datos/catalogo_partidas.csv` | Solo ID, descripción y unidad | No entregar al predictor `costo_unitario_base` o parámetros generadores |
| `../datos/obra_nueva_real.csv` | Solo evaluación posterior a congelar predicciones | Prohibida en estimación, selección de reglas, umbrales o imputación |
| `../resultados/resultados.csv` | Antecedente histórico, no entrada de nuevos métodos | No usar control con real×ruido ni mezclar métricas |

Las rutas de la tabla son relativas a este directorio. El año 2027 es parte del
conjunto sintético, no una afirmación de trabajo real ejecutado en el futuro.

Flujo propuesto reproducible:

1. Registrar hashes de entradas, versión del protocolo y lista de obras/partidas.
2. Separar físicamente referencia, cantidades y verdad. Extraer solo columnas
   permitidas; validar unicidad `(obra_id, partida_id)`, cantidades/costos finitos
   y positivos y la unidad por partida. No mezclar monedas/tipologías sin declarar.
3. Calcular ambos métodos con la misma referencia. Mínimo dos observaciones
   históricas por partida. Si no alcanza, registrar faltante; no imputar desde real.
4. Guardar predicciones, IDs y hash **antes** de abrir la verdad. El predictor no
   debe recibir la ruta de la verdad ni consultar el catálogo de costos latentes.
5. Evaluar por join exacto de IDs: faltantes/duplicados/verdad no positiva invalidan
   el caso. Calcular sobre el mismo conjunto para ambos métodos y reportar cobertura.
6. Publicar todos los escenarios y las decisiones, incluso desfavorables.

Los CSV existentes ya fueron inspeccionados en revisiones anteriores. Este
rediseño elimina fuga en el algoritmo propuesto, pero **no convierte el conjunto
en un test ciego o confirmatorio**. Una validación futura confirmatoria requerirá
nuevas obras/semillas congeladas antes de evaluarlas y separación organizativa
del evaluador, si es viable. No se afirma que eso ya se haya realizado.

## 3. Métricas y reglas congeladas para futura ejecución

APE_p = 100 × abs(pred_p − real_p) / abs(real_p), solo real_p >0.
MAPE = suma(APE_p)/n, con todas las partidas previstas evaluables.
Reducción = 100 × (MAPE_B0 − MAPE_M1)/MAPE_B0. Baseline cero = ND.
Cobertura =100 × partidas con ≥2 referencias / partidas previstas.
Diagnóstico monetario: error absoluto por partida y suma, sin nueva meta universal.

Continuar investigación de M1 si cobertura=100 %, no hay fuga/invalidación,
MAPE_M1 ≤15 % y reducción ≥30 %. Detener la evaluación si hay fuga o datos inválidos;
no clasificar esos casos como éxito ni calcular promedios sobre sobrevivientes.
Con datos válidos, detener esa variante si MAPE_M1 >30 %. En los demás casos,
modificar/investigar. Si B0 es perfecto, reducción relativa ND y no se acredita
mejora; conservar M1 solo por otro criterio futuro explícito, no por esta hipótesis.

Los límites 15/30/30 % conservan metas históricas, con justificación retrospectiva
en `documentos/proyecto/Semana5_Hito_I_v1.2.md`, §5.2. No se atribuyen a AACE ni
se presentan como umbrales optimizados o preregistrados en S4 original.

## 4. Sensibilidad diseñada, todavía pendiente

| Escenario | Modificación de referencia/entradas | Comparación y límite |
|---|---|---|
| E0 | Históricos cerrados completos | Caso principal retrospectivo |
| E1 | Retirar cada obra cerrada por turno | Seis exclusiones; no llamar validación independiente entre escenarios solapados |
| E2 | Últimos 2, 4 y 6 años de referencia disponibles | Comprobar cobertura antes de error; no sustituir faltantes con futuro |
| E3 | Primer registro histórico ordenado por ID con tarifa ×1,30, solo en copia | Aplicar igual cambio a ambos métodos; estudiar robustez, no cambiar originales |
| E4 | Cantidades presupuestadas ×0,5 y ×2 | Escalar también verdad en copia únicamente como prueba algebraica; no son nuevas obras independientes |
| E5 | Sin referencias, duplicados, NaN o costos/cantidades cero | Debe invalidar/registrar faltantes; no producir éxito engañoso |
| E6 | Metas alternativas 10/15/20 % y mejora 20/30/40 % | Reporte de sensibilidad de decisión; la decisión principal no se escoge después |

Métricas por escenario: cobertura, tamaño, MAPE_B0, MAPE_M1, reducción, errores
individuales, decisión y advertencias. No promediar escenarios no comparables.
El 30 % de contaminación es estrés interno, no frecuencia de errores empresarial.
Los métodos son deterministas; no requieren nueva semilla. Si se incorporan datos
sintéticos nuevos, registrar generador/versión/semilla y no elegir la mejor salida.

## 5. Preservación y límites de inferencia

No se han generado nuevas predicciones ni resultados. Este archivo es diseño,
no ejecución. La futura ejecución, si se autoriza, escribirá exclusivamente en
un subdirectorio nuevo `revision-v1.2/ejecuciones/<id>/`, con manifiesto y resultados.
No ejecutar `src/synthetic_erp_data.py` ni `pruebas/verificar_poc.py` para este fin:
sus salidas históricas no están aisladas para la nueva metodología.

No se demuestra ahorro real, superioridad estadística, adopción, impacto en ERP,
viabilidad de tablero ni representatividad de constructoras. Una obra y seis
partidas son exploración didáctica. Costos/históricos comparten generador; diferencias
de tipología, inflación y disponibilidad futura siguen siendo amenazas.

## 6. Fuentes metodológicas

Scikit-learn developers. (s. f.-b). Mean absolute percentage error. Recuperado el
25 de octubre de 2026, de https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html

Scikit-learn developers. (s. f.-a). Common pitfalls and recommended practices:
Data leakage. Recuperado el 25 de octubre de 2026, de https://scikit-learn.org/stable/common_pitfalls.html#data-leakage

Python Software Foundation. (s. f.). Statistics: Mathematical statistics functions.
Python 3.12 documentation. Recuperado el 25 de octubre de 2026, de
https://docs.python.org/3.12/library/statistics.html#statistics.median

Estas páginas fueron consultadas; respaldan definiciones y controles, no metas
internas. No se instaló scikit-learn ni se utiliza un modelo avanzado.
