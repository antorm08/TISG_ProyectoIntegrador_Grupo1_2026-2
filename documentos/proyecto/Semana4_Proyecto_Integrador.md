# Proyecto Integrador — Semana 4

## Innovación, propuesta de valor e hipótesis

**Transformación Digital de Constructora Andina S.A.C.**
*Hacia el control integrado de costos previsto vs. ejecutado a partir de los históricos de obra*

Universidad Nacional Mayor de San Marcos (UNMSM) — FISI — Ingeniería de Software
Curso: Tendencias en Ingeniería de Software y Gestión — Proyecto Integrador 2026-2
Grupo 1 · Docente: Mg. PMP Yamil Quiñones Nieto

---

### Control de versiones

| Versión | Fecha | Cambio principal | Responsable |
|---|---|---|---|
| v1.0 | 02/10/2026 | Declaración de problema, propuesta de valor, hipótesis, PoC, métricas e Impact Canvas actualizado | Equipo |

**Objetivo de la semana (guía del curso):** transformar el problema en hipótesis comprobables y definir cómo se validará el valor antes de escalar una solución.
**Peso en el proyecto:** 5 % (acumulado 17 %). **Tendencia principal:** BI y analítica operacional (anillo *Adoptar* del Technology Radar v0.1).

---

## 1. Declaración precisa del problema y usuarios afectados

### 1.1 Problema

Constructora Andina S.A.C. registra en su ERP los datos de producción de obra (tareo, horas-hombre, metrados, costos de materiales y partidas de control), pero **no reutiliza de forma integrada y automática esos históricos para presupuestar nuevas obras ni para comparar el costo previsto con el ejecutado**. Cada presupuesto se elabora con hojas de cálculo locales y criterio individual del analista; el estado económico real de una obra tarda hasta 15 días en consolidarse (diagnóstico de madurez, Semana 3).

Formulación estructurada:

| Elemento | Descripción |
|---|---|
| ¿Quién? | Analistas de Costos y Presupuestos, Jefes de Obra y Gerencia General de Constructora Andina S.A.C. |
| ¿Qué? | El histórico de producción no se convierte en una base reutilizable para estimar partidas ni para controlar desviaciones previsto vs. ejecutado en el momento oportuno. |
| ¿Por qué ocurre? | Datos en silos, uso de planillas locales, ausencia de un modelo analítico y de gobierno de datos (Semana 3, dimensiones Cultura, Collaboration y Talent en Nivel 2). |
| ¿Por qué importa? | Afecta el margen operativo del contratista: las estimaciones inexactas y el control tardío son causas centrales de sobrecostos (Abdelalim et al., 2025; Elserougy et al., 2024). |
| Evidencia | Supuesto S-08 (Semana 1), resistencias 4.1–4.5 y matriz de brechas (Semana 3). |

### 1.2 Usuarios afectados y su relación con el problema

| Usuario | Rol en el problema | Necesidad |
|---|---|---|
| Analista de Costos y Presupuestos | Elabora presupuestos sin base histórica integrada | Estimar partidas con ratios reales de obras cerradas |
| Jefe de Obra / Residente | Registra tareo y metrados; recibe control tardío | Ver desviaciones durante la ejecución, no semanas después |
| Gerencia General / Operaciones | Decide con información consolidada tardía | Visibilidad económica temprana del margen por obra |
| Compras / Logística | Sufre variaciones de precio no previstas | Anticipar consumo y precios a partir de históricos |

---

## 2. Propuesta de valor para la capacidad tecnológica

**Capacidad propuesta:** una capa de **BI y analítica operacional** que integre los históricos de obras cerradas (tareo, metrados, costos por partida) en un modelo de datos gobernado, exponga **tableros de previsto vs. ejecutado** y entregue **estimaciones asistidas de partidas** para nuevas obras.

Se aplica *Value Proposition Canvas* (Osterwalder et al., 2014) sobre el usuario principal: el Analista de Costos y el Jefe de Obra.

### 2.1 Mapa del cliente

| Tareas del usuario (jobs) | Dolores (pains) | Ganancias esperadas (gains) |
|---|---|---|
| Presupuestar partidas de nuevas obras | No hay base histórica confiable; se estima "a ojo" | Estimar con referencias reales de rendimiento |
| Controlar costo previsto vs. ejecutado | Consolidación manual y tardía (hasta 15 días) | Ver desviaciones en el momento oportuno |
| Sustentar valorizaciones y margen | Reprocesos y discusiones por cifras dispares | Cifras trazables y auditables, una sola versión |

### 2.2 Lienzo de propuesta de valor

| Aliviadores de dolor (pain relievers) | Creadores de ganancia (gain creators) |
|---|---|
| Repositorio histórico único de ratios de rendimiento y costo por partida | Estimación de partidas asistida por históricos |
| Tablero previsto vs. ejecutado en línea | Detección temprana de desviaciones |
| Un solo origen de verdad, con reglas de calidad y trazabilidad | Reducción del tiempo de elaboración de valorizaciones |

**Encaje (fit):** la propuesta ataca directamente la causa raíz S-08 y los dolores declarados por Costos y Obra en la Semana 3, sin reemplazar el ERP transaccional (decisión D-02).

---

## 3. Hipótesis

Toda hipótesis se declara de forma **falsable**, con una variable observable y un sujeto de comparación.

### H1 — Hipótesis de valor *(principal)*

> **Si** se integran los históricos de tareo, metrados y costos de obras cerradas en un modelo analítico y se usan para estimar las partidas de una obra nueva, **entonces** el desvío entre el costo estimado y el costo real ejecutado se reduce a un máximo de **±15 %** (rango compatible con una estimación de Clase 2–3 según AACE 18R-97), frente a la línea base de estimación manual actual.

- **Variable observable:** error porcentual absoluto de la estimación por partida (|estimado − real| / real).
- **Se falsa si:** el desvío del método analítico no es estadísticamente menor que el de la línea base manual.

### H2 — Hipótesis de viabilidad técnica

> **Es viable** construir un prototipo extracción → modelo dimensional → tablero, a partir de extractos sintéticos del ERP, **sin** degradar el ERP transaccional y **con** el equipo TI actual, en un horizonte académico de **≤ 4 semanas** de esfuerzo.

- **Variable observable:** pipeline ejecutado de extremo a extremo, reproducible con un comando, y ausencia de impacto sobre el sistema transaccional.
- **Se falsa si:** el prototipo no se completa, no es reproducible, o exige tocar el ERP en producción.

### H3 — Hipótesis de adopción / operación

> **Si** el tablero previsto vs. ejecutado reduce el tiempo de elaboración de la valorización en **≥ 80 %** (meta de la "marcha en paralelo", Semana 3) y exige un esfuerzo de registro aceptable, **entonces** al menos **70 %** de los usuarios de Costos y Jefes de Obra mantendrán su uso semanal tras 4 semanas, abandonando las planillas paralelas.

- **Variable observable:** porcentaje de usuarios activos semanales y tiempo de elaboración (min).
- **Se falsa si:** el uso semanal es menor al 70 % o el tiempo no se reduce.
- **Nota de integridad:** el umbral del 80 % proviene de la meta interna fijada en la Semana 3; el umbral del 70 % es un **supuesto operativo del equipo** (S-11) y deberá validarse con datos reales de adopción, no se presenta como benchmark externo.

**Nota metodológica:** las hipótesis no incluyen IA generativa como componente principal. La IA (T5) permanece en anillo *Probar/Evaluar* y su valor depende de que H1 y H2 se validen primero; priorizarla antes de resolver la calidad y el control de datos contradiría la decisión D-03.

---

## 4. Diseño del experimento / PoC (valida H1)

**Tipo:** experimento controlado de comparación de método de estimación sobre datos sintéticos.
**Alcance:** académico, reproducible, sin datos reales ni confidenciales.

| Elemento | Definición |
|---|---|
| Objetivo | Medir si la estimación basada en históricos reduce el error frente a una línea base manual simulada. |
| Unidad de análisis | Partida de control de una obra. |
| Población | 6 obras cerradas (histórico) + 1 obra nueva a estimar. |
| Tratamiento | Estimación por ratios históricos (HH/unidad y S//unidad) calculados del histórico. |
| Control | Estimación "manual" simulada con la variabilidad observada en la estimación sin base integrada. |
| Datos | Extractos **sintéticos** generados por `poc/POC-01-estimacion-historicos/src/synthetic_erp_data.py` (semilla fija). |
| Métrica | MAPE (error porcentual absoluto medio) por partida, para tratamiento y control. |
| Duración | Ejecución en minutos; diseño y análisis en ≤ 4 semanas académicas. |
| Recursos | Python estándar (sin dependencias externas), un entorno local. |

**Pasos:**
1. Generar extractos sintéticos (`synthetic_erp_data.py`) y guardarlos en `poc/experimento_bi/data/`.
2. Calcular ratios históricos por partida desde obras cerradas.
3. Estimar la obra nueva con el método analítico y con la línea base manual.
4. Calcular MAPE de ambos métodos y contrastar con los umbrales.
5. Emitir `resultados.csv` y registrar la decisión (continuar / modificar / detener).

**Riesgos del experimento y control:** datos sintéticos pueden no representar al caso real (se declara como limitación, no como resultado de negocio); el diseño prioriza verificar el **método y las métricas**, no afirmar desempeño real (regla de integridad de la guía).

El guion reproducible y los archivos se detallan en `poc/POC-01-estimacion-historicos/README.md`.

---

## 5. Tabla hipótesis – experimento – métrica – umbral – decisión

| ID | Hipótesis | Experimento | Métrica | Umbral de aceptación | Criterio de decisión |
|---|---|---|---|---|---|
| H1 | La estimación con históricos reduce el desvío a ≤ ±15 % | Comparar MAPE del método analítico vs. línea base manual sobre obra sintética | MAPE partida (%) | Analítico ≤ 15 % **y** reducción ≥ 30 % del error frente a la base | **Continuar** si cumple; **modificar** el modelo si no mejora; **detener** si MAPE analítico > 30 % |
| H2 | Es viable un PoC reproducible sin afectar el ERP | Ejecutar el pipeline completo con un comando y verificar aislamiento | Éxito de ejecución + tiempo | 100 % reproducible y sin tocar el transaccional, en ≤ 4 semanas | **Continuar** si cumple; **detener** si requiere acceso a producción |
| H3 | ≥ 70 % de uso semanal con −80 % de tiempo | Piloto de tablero con usuarios sintéticos/entrevistas de usabilidad | % usuarios activos semanales; tiempo (min) | Uso ≥ 70 %; tiempo ≤ 20 % del actual | **Continuar** si cumple; **modificar** UX si el uso es menor; **detener** si no reduce tiempo |

### 5.1 Justificación de umbrales con fuentes

| Umbral | Valor | Fuente / razón |
|---|---|---|
| Exactitud de estimación por clases | Clase 5: −20 %/−50 % a +30 %/+100 %; Clase 1: −3 %/−10 % a +3 %/+15 % (80 % de confianza) | AACE International (2020), RP 18R-97 |
| Meta de desvío H1 | ≤ ±15 % | Dentro del rango de estimación de Clase 2–3 (factibilidad / autorización de presupuesto) de AACE 18R-97 |
| Severidad del problema | 30–40 % de proyectos globales con pobre desempeño de costo; estimación inexacta entre los 7 factores clave de sobrecosto | Elserougy et al. (2024); Abdelalim et al. (2025) |
| Benchmark financiero del sector | Rangos de margen/costo para contextualizar el impacto | CFMA (2025) |
| Viabilidad/automatización de la entrega | Las capacidades y la automatización impactan el desempeño de entrega | DORA (2025) |
| Madurez tecnológica de la tendencia | BI/analítica operacional en anillo *Adoptar* | Thoughtworks (2025) |

**Nota:** todos los valores numéricos provienen de las fuentes citadas, salvo el umbral operativo de adopción (70 %), declarado como supuesto S-11.

---

## 6. Impact Canvas actualizado — BI y analítica operacional

| Dimensión | Análisis actualizado (Semana 4) |
|---|---|
| **Valor** | Habilita estimación de partidas con históricos y control previsto vs. ejecutado; ataca directamente S-08. El valor se mide como reducción del desvío (H1) y del tiempo de control. |
| **Arquitectura** | Capa analítica desacoplada del ERP: extracción → modelo dimensional (partidas, obra, tiempo) → serving. No reemplaza el transaccional (D-02). Habilita la T4 (arquitectura de datos analítica) en anillo *Probar*. |
| **Personas** | Requiere capacidades de modelado y análisis (brecha Semana 3: Analista de Presupuestos → Ingeniero de Costos Basado en Datos) y adopción de Jefes de Obra (resistencia 4.2). |
| **Seguridad** | Permisos por rol y por obra; control de acceso a información económica; trazabilidad de origen (NIST SSDF, 2025). |
| **Economía** | Costos de licencias, desarrollo y operación deben compararse con el ahorro de esfuerzo y el valor de decisión; complejidad proporcional a la escala (CFMA, 2025). |
| **Sostenibilidad** | Evitar duplicación de datos y procesamiento innecesario; reutilizar el histórico existente antes de añadir plataforma. |

**Cambio respecto de la Semana 1:** se refuerza la dimensión de valor con umbrales medibles (H1) y se precisan los riesgos de adopción (H3), antes ausentes. El anillo (*Adoptar*) se mantiene; ver sección 7.

---

## 7. Registros actualizados

### 7.1 Registro de decisiones (nuevas / actualizadas)

| ID | Fecha | Decisión | Alternativas consideradas | Evidencia / razón | Responsable | Estado |
|---|---|---|---|---|---|---|
| D-06 | 02/10/2026 | Fijar BI y analítica operacional como tendencia principal de la Semana 4 | Arquitectura de datos analítica; IA generativa | Ataca directamente S-08 y es el anillo *Adoptar* del Radar v0.1 | Equipo | Vigente |
| D-07 | 02/10/2026 | Validar H1 con un PoC de estimación por históricos sobre datos sintéticos | Encuesta de percepción; piloto en producción | Permite medir desvío real sin riesgo y a escala académica | Equipo | Vigente |
| D-08 | 02/10/2026 | Mantener la IA generativa en *Probar/Evaluar* subordinada a H1/H2 | Priorizar IA como primera capa | Depende de datos confiables y trazables (D-03) | Equipo | Vigente |

### 7.2 Supuestos nuevos

| ID | Supuesto | Tipo | Estado |
|---|---|---|---|
| S-11 | El umbral de adopción operativa se fija en 70 % de uso semanal tras 4 semanas | Operación | Por validar |
| S-12 | Existen históricos suficientes de obras cerradas con granularidad por partida | Datos | Por validar |

### 7.3 Registro de contribuciones

| Integrante | Responsabilidad | Artefacto | Fecha | Evidencia |
|---|---|---|---|---|
| Anthony Romani | Declaración del problema y usuarios afectados | Sección 1 | 02/10/2026 | Documento: Sección 1 |
| Max Astuhuaman | Hipótesis y tabla hipótesis–experimento–métrica–umbral–decisión; fuentes y umbrales | Secciones 3 y 5 | 02/10/2026 | Documento: Secciones 3 y 5; hoja Fuentes |
| Guillermo Calle | Diseño y construcción del PoC (generador de datos y experimento) | Sección 4 y `poc/POC-01-estimacion-historicos/` | 02/10/2026 | `synthetic_erp_data.py`, `experimento_bi.py`, `resultados.csv` |
| Pablo Mendoza | Propuesta de valor, Impact Canvas actualizado y revisión de coherencia integral | Secciones 2 y 6 | 02/10/2026 | Documento: Secciones 2 y 6; revisión final |

*(El registro editable se mantiene en `gestion/registros/` con autor, actividad, fecha y evidencia verificable.)*

---

## 8. Referencias

AACE International. (2020). *Recommended Practice No. 18R-97: Cost Estimate Classification System – As Applied in Engineering, Procurement, and Construction for the Process Industries* (Rev. August 7, 2020). AACE International. https://web.aacei.org/docs/default-source/toc/toc_18r-97.pdf

Abdelalim, A. M., Salem, M., Salem, M., Al-Adwani, M., & Tantawy, M. (2025). An analysis of factors contributing to cost overruns in the global construction industry. *Buildings, 15*(1), 18. https://doi.org/10.3390/buildings15010018

Construction Financial Management Association. (2025). *2025 Construction Financial Benchmarker*. CFMA. https://cfma.org/

DORA. (2025). *State of AI-assisted Software Development 2025*. https://dora.dev/research/2025/dora-report/

Elserougy, M., Khodeir, L. M., & Fathy, F. (2024). Practices and techniques for construction projects cost control – a critical review. *HBRC Journal, 20*(1), 525–552. https://doi.org/10.1080/16874048.2024.2337060

National Institute of Standards and Technology. (2025). *Secure Software Development Framework (SSDF) Version 1.2* (NIST SP 800-218 Rev. 1). https://csrc.nist.gov/

Osterwalder, A., Pigneur, Y., Bernarda, G., & Smith, A. (2014). *Value Proposition Design*. Wiley.

Thoughtworks. (2025). *Technology Radar, Volume 33*. https://www.thoughtworks.com/radar

---

*Documento elaborado por el Grupo 1. Las cifras de desempeño del PoC son simuladas con datos sintéticos y sirven para validar método y métricas, no para afirmar resultados de negocio reales.*
