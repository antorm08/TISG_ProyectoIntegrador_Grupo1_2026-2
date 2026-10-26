# Auditoría posterior a correcciones — S1–S5 / Hito I v1.2

UNMSM — FISI — Ingeniería de Software. Curso: Tendencias en Ingeniería de Software y Gestión.
Grupo 1. Fecha: 25/10/2026. Versión: v1.2. **Pendiente de validación humana.**

## 1. Alcance y reglas constantes

Se conserva sin modificar `AUDITORIA_CUMPLIMIENTO_S01_S05.md`. Esta revisión aplica
sus mismos **69 criterios**, IDs, clasificación y denominador al estado acumulado
v1.2. No recalifica las entregas originales ni determina puntualidad o nota docente.
No es auditoría de una organización real, validación humana ni revisión externa
independiente: fue realizada por el mismo asistente que preparó las correcciones,
contrastando guía, fuentes y artefactos finales. La comprobación automática es
complementaria, no suficiente por sí sola para clasificar calidad académica.

Autoridad: `proyectoIntegrador (1).pdf`, pp. 3–8 y 13–16. Su hash y los de archivos
previos están en `evidencias/revision-v1.2/integridad_antes.json` y
`fuentes_locales_antes.json`. No se ejecutó de nuevo la PoC histórica.

Estados: CUMPLE = evidencia suficiente para el criterio; PARCIAL = contenido o
sustento incompleto; NO CUMPLE = ausencia comprobada; NO VERIFICABLE = contenido
necesario no inspeccionable; NO APLICA = inaplicabilidad justificada. PARCIAL no
vale medio punto. No se excluyen pendientes para aumentar el porcentaje.

## 2. Matriz cuantitativa y comparación

Cumplimiento estricto = CUMPLE / criterios definidos ×100. Pesos iguales solo
para conteo de cobertura documental, no rúbrica, nota o estadística de calidad.

| Semana | Evaluados | Cumple | Parcial | No cumple | No verificable | No aplica | Estricto v1.2 | Estricto anterior |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| S1 | 13 | 12 | 1 | 0 | 0 | 0 | 92,3 % | 92,3 % |
| S2 | 11 | 11 | 0 | 0 | 0 | 0 | 100,0 % | 81,8 % |
| S3 | 11 | 10 | 1 | 0 | 0 | 0 | 90,9 % | 81,8 % |
| S4 | 13 | 13 | 0 | 0 | 0 | 0 | 100,0 % | 84,6 % |
| S5 | 21 | 21 | 0 | 0 | 0 | 0 | 100,0 % | 90,5 % |
| **Total** | **69** | **67** | **2** | **0** | **0** | **0** | **97,1 %** | **87,0 %** |

Cambio exacto: 60/69 →67/69, aumento de siete criterios y 10,14 puntos porcentuales
antes de redondear. Quedan 1.10 y 3.09 PARCIAL. El P0 de revisión humana y otros
pendientes transversales permanecen fuera de estos 69, como en la auditoría inicial.
**Un 100 % documental de una semana no acredita aprobación humana ni entrega válida.**

## 3. Evidencias utilizadas

| Código | Ruta exacta relativa a raíz |
|---|---|
| V12 | `documentos/proyecto/Semana5_Hito_I_v1.2.md` |
| PDF12 | `entregas/semana-05/revision-v1.2/TISG_E01_S05_HitoI_v1.2_2026-10-25.pdf` |
| DOC12 | `entregas/semana-05/revision-v1.2/TISG_E01_S05_HitoI_v1.2_2026-10-25.docx` |
| X12 | `gestion/registros/Registros_y_Radar_Semana5_v1.2.xlsx` |
| A12 | `arquitectura/revision-v1.2/figura-01-arquitectura-as-is.svg` |
| R12 | `arquitectura/revision-v1.2/figura-02-relaciones-datos.svg` |
| T12 | `arquitectura/revision-v1.2/figura-03-arquitectura-to-be-v0-1.svg` |
| D12 | `arquitectura/revision-v1.2/figura-04-mapa-de-dependencias.svg` |
| B12 | `documentos/proyecto/Semana2_MaterialComplementario_v1.2.md` |
| BP12 | `entregas/semana-02/revision-v1.2/Presentacion_S2_v1.2.pdf` |
| EXP12 | `poc/POC-01-estimacion-historicos/revision-v1.2/DISENO_EXPERIMENTAL.md` |
| F12 | `fuentes/revision-v1.2/VERIFICACION_FUENTES.md` |
| C12 | `gestion/registros/Contribuciones_Evidencia_v1.2.md` |
| S1 | `entregas/semana-01/TISG_E01_S01_ProyectoIntegrador_2026-09-04.pdf` |
| E1 | `entregas/semana-01/TISG_E01_S01_EvidenciasParticipacion_2026-09-04.pdf` |
| S2 | `entregas/semana-02/TISG_E01_S02_ProyectoIntegrador_2026-09-18.pdf` |
| S3 | `entregas/semana-03/TISG_E01_S03_ProyectoIntegrador_2026-09-25.pdf` |
| S4 | `documentos/proyecto/Semana4_Proyecto_Integrador.md` |

Localización por sección/hoja para fuentes editables; no se reutilizan números de
línea v1.1 como si correspondieran a v1.2. Las evidencias de páginas originales
son antecedentes conservados, no nuevas entregas retroactivas.

## 4. Checklist completo de 69 criterios

### Semana 1 — 13 criterios

| ID | Requisito | Estado | Evidencia y localización | Hallazgo posterior | Acción / prioridad |
|---|---|---|---|---|---|
| 1.01 | Ficha de organización | CUMPLE | S1 §2, pp. 2–3; V12 §2.1 | Sector, tamaño, actores, ERP y contexto preservados como caso ficticio | — |
| 1.02 | Charter ≤2 páginas y contenido exigido | CUMPLE | S1 §4, p. 4; V12 §2.1 | Charter original de una página y contenido consolidado coherente | — |
| 1.03 | Mapa inicial de stakeholders | CUMPLE | S1 §5, p. 5; V12 §4.3 | Actores iniciales preservados y ampliados, no eliminados | — |
| 1.04 | Radar con ≥10 tendencias | CUMPLE | S1 §6, pp. 6–8; V12 §2.2 | Doce tendencias | — |
| 1.05 | Cuadrantes y cuatro anillos | CUMPLE | V12 §2.2; `radar/exportado/Technology_Radar_v0.1.png` | Cuadrantes, cuatro anillos y significado explícitos | — |
| 1.06 | Justificación técnica y contextual | CUMPLE | V12 §2.2; S1 §6.1 | Función contextual y proporcionalidad mantenidas; sin cambio de anillos | — |
| 1.07 | Canvas de tres tendencias prioritarias | CUMPLE | S1 §7, pp. 9–10; V12 §2.3 | Tres originales conservados y complementados, no reemplazados por lista genérica | — |
| 1.08 | Seis dimensiones por Canvas | CUMPLE | V12 §2.3; X12 `Impact_Canvas` | Seis dimensiones localizables en seis capacidades recomendadas | — |
| 1.09 | Registro de supuestos | CUMPLE | V12 §10.1; X12 `Supuestos` y `Supuestos_Economicos` | S-01–S-26 con naturaleza y procedencia; no observaciones fabricadas | — |
| 1.10 | Contribuciones verificables de todos | PARCIAL | E1 pp. 1–2; C12; X12 `Contribuciones`/`Evidencia_Aportes` | Mejor vínculo a archivos y actividad Git, pero no corroboración suficiente de todos los aportes individuales S1 | Confirmar aportes con evidencia real disponible, sin fabricar commits. **P2** |
| 1.11 | ≥3 fuentes relevantes y verificables | CUMPLE | S1 §§9/11; F12; V12 §12 | Mínimo permanece cubierto; no se convierte un enlace genérico en evidencia del volumen exacto | —; límites históricos en F12 |
| 1.12 | Radar editable y exportado | CUMPLE | `entregas/semana-01/TISG_E01_S01_TechnologyRadar_v0.1_2026-09-04.svg`; `radar/exportado/Technology_Radar_v0.1.pdf` y `.png` | Formatos originales preservados | — |
| 1.13 | Coherencia de caso, Charter, Radar y Canvas | CUMPLE | V12 §§2/8/9 | Datos antes de IA y conservación del ERP; complemento de dimensiones no amplía stack | — |

### Semana 2 — 11 criterios

| ID | Requisito | Estado | Evidencia y localización | Hallazgo posterior | Acción / prioridad |
|---|---|---|---|---|---|
| 2.01 | Modelo AS-IS mediante lienzo | CUMPLE | V12 §3.1; BP12 p. 1; B12 lámina 1 | Nuevo lienzo ubica clientes en segmentos; PDF anterior explícitamente histórico | — |
| 2.02 | Ingresos y costos claros | CUMPLE | V12 §3.1; BP12 p. 2 | Ingresos contractuales separados de costos; posventa no se añade sin contrato | — |
| 2.03 | Canales digitales y actores | CUMPLE | BP12 pp. 1/3; V12 §3.1 | Canales comerciales/digitales separados; ERP como recurso interno | — |
| 2.04 | Dependencias de plataformas/servicios | CUMPLE | BP12 p. 3; V12 §§3/6/8 | Stack aclarado; infraestructura/licencias/API no confirmadas no se presentan como existentes | — |
| 2.05 | Oportunidades digitales pertinentes | CUMPLE | BP12 p. 4; V12 §3.1 | SaaS consumo, integración y e-Business; no nuevos negocios impuestos | — |
| 2.06 | Dos o tres cambios propuestos | CUMPLE | V12 §3.1; BP12 p. 5 | P-01/P-02/P-03 conservadas | — |
| 2.07 | Beneficio y riesgo por propuesta | CUMPLE | V12 §3.1; X12 `Propuestas` | Beneficios condicionados y riesgos por propuesta | — |
| 2.08 | Registro de Decisiones actualizado | CUMPLE | V12 §10.1; X12 `Decisiones` | D-06–D-10 conservadas; nota D-10 y D-21 retiran fundamento CAPECE inválido | — |
| 2.09 | ≥3 fuentes y una cualificada | CUMPLE | S2 referencias históricas; V12 §12; B12 referencias; F12 | Fuentes oficiales/tecnológicas/académicas disponibles; CAPECE se usa solo para rectificación, no benchmark | — |
| 2.10 | Lienzo editable | CUMPLE | B12 lámina 1; X12 `Canvas_Data`; `entregas/semana-02/revision-v1.2/lamina-01.svg` | Markdown, XLSX y SVG editables; nuevo PDF final inspeccionable | — |
| 2.11 | Supuestos económicos identificados | CUMPLE | V12 §3; X12 `Supuestos_Economicos` | Diez supuestos preservados, sin ahorro o ingresos inventados | — |

### Semana 3 — 11 criterios

| ID | Requisito | Estado | Evidencia y localización | Hallazgo posterior | Acción / prioridad |
|---|---|---|---|---|---|
| 3.01 | Stakeholders actualizados | CUMPLE | V12 §4.3; X12 `Stakeholders` | Mapa actualizado y funciones propuestas diferenciadas | — |
| 3.02 | Influencia, interés, impacto y estrategia | CUMPLE | V12 §4.3 | Cuatro atributos presentes por actor | — |
| 3.03 | Diagnóstico de madurez | CUMPLE | V12 §§4.1–4.2; X12 `Instrumento_Madurez`/`Madurez_SocioTecnica` | Instrumento ordinal con descriptores, regla acumulativa y ND; se retiran puntuaciones arbitrarias | —; alcance hipotético, no certificación |
| 3.04 | Dimensiones organizacionales exigidas | CUMPLE | V12 §4.1 | Cultura, colaboración, DevEx, equipos virtuales, datos, seguridad y cambio, además de skills/IA | — |
| 3.05 | Matriz de habilidades y roles | CUMPLE | V12 §4.3; X12 `Skills Gap` | Brechas por rol y acciones responsables | — |
| 3.06 | Actual, objetivo y acción por brecha | CUMPLE | V12 §§4.2–4.3 | Estado de partida o ND, objetivo propuesto y acción; no diferencias numéricas falsas | — |
| 3.07 | Tres a cinco resistencias | CUMPLE | V12 §4.3 | Cinco hipótesis de resistencia y mitigación; no incidentes observados | — |
| 3.08 | Plan de adopción, comunicación y formación | CUMPLE | V12 §4.3 | Secuencia organizacional, comunicación y formación ligadas a brechas | — |
| 3.09 | Sustento del diagnóstico | PARCIAL | V12 §4.2; S-24; X12 `Madurez_SocioTecnica` | Una asignación 2-H trazable; faltan condiciones de escenario suficientes para caracterizar ocho dimensiones ND. El instrumento no llena esa falta | El equipo debe fundamentar el escenario o aportar evidencia autorizada; no se exigen entrevistas reales obligatorias. **P1** |
| 3.10 | Contribuciones actualizadas | CUMPLE | C12; X12 `Contribuciones`/`Evidencia_Aportes` | Veinte declaraciones históricas preservadas y cuatro vínculos de actividad; sin nuevos aportes simulados | — para actualización; límite individual en 1.10 |
| 3.11 | ≥3 fuentes pertinentes | CUMPLE | S3 referencias; V12 §12; F12 FV-05/10/11 | DORA y otras fuentes pertinentes, artículo específico de Atlassian y límites de uso | — |

### Semana 4 — 13 criterios

| ID | Requisito | Estado | Evidencia y localización | Hallazgo posterior | Acción / prioridad |
|---|---|---|---|---|---|
| 4.01 | Problema y usuarios precisos | CUMPLE | V12 §§2.1/5.1 | Costos, Obra y Gerencia; históricos y desvíos | — |
| 4.02 | Propuesta de valor alineada | CUMPLE | V12 §5.1 | Tareas, dolores, ganancias y respuesta conectadas | — |
| 4.03 | Tres hipótesis diferenciadas | CUMPLE | V12 §5.1; X12 `Hipotesis` | Valor, viabilidad y adopción separados; estados pendientes | — |
| 4.04 | Hipótesis falsables | CUMPLE | V12 §§5.1–5.2; EXP12 §3 | Condiciones de rechazo y denominadores explícitos | — |
| 4.05 | Diseño de experimento principal | CUMPLE | EXP12 §§1–5; V12 §5.3 | B0 mediana histórica y M1 ponderado, mismos datos, sin real futuro; separación y sensibilidad diseñadas | —; ejecución no requerida en S4 y no realizada |
| 4.06 | Métricas observables | CUMPLE | V12 §5.2; X12 `Metricas` | Fórmula/unidad, costo cero, baseline cero, uso útil y tiempos pareados | — |
| 4.07 | Umbrales explícitos | CUMPLE | V12 §5.2; X12 `Umbrales` | Metas conservadas y tolerancias expresadas como internas, no estándares | — |
| 4.08 | Abandono explícito | CUMPLE | V12 §5.1; EXP12 §3 | Prioridad a validez/seguridad y reglas de desempeño | — |
| 4.09 | Impact Canvas actualizado | CUMPLE | V12 §§2.3/5.4; X12 `Impact_Canvas` | BI conectado con H1/H2/H3 y seis dimensiones | — |
| 4.10 | Lienzo de valor o equivalente | CUMPLE | V12 §5.1 | Representación editable equivalente, sin encaje empírico simulado | — |
| 4.11 | Tabla hipótesis → decisión | CUMPLE | V12 §5.1 | Hipótesis, experimento, métrica y tres decisiones localizables | — |
| 4.12 | Fuentes/benchmarks para definir métricas | CUMPLE | V12 §5.2; F12 FV-06/07/08; EXP12 §6 | Fuentes metodológicas verificadas y derivación interna de metas; no equivalencia AACE, no preregistro retrospectivo | — para diseño; equipo debe aprobar supuestos antes de piloto |
| 4.13 | ≥3 fuentes pertinentes | CUMPLE | EXP12 §6; V12 §12; S4 §8 histórico | Más de tres referencias pertinentes; NIST/DORA y literatura histórica para el mínimo cualificado | — |

### Semana 5 — 21 criterios

| ID | Requisito | Estado | Evidencia y localización | Hallazgo posterior | Acción / prioridad |
|---|---|---|---|---|---|
| 5.01 | Diagrama AS-IS | CUMPLE | A12 y PNG/PDF; V12 §6 | Nuevo diagrama con stack aclarado, roles y nodos | — |
| 5.02 | Aplicaciones/sistemas actuales | CUMPLE | A12; V12 §6.1 | ERP, módulos conceptuales, MySQL y exportación supuesta | — |
| 5.03 | Datos y relaciones relevantes | CUMPLE | R12; V12 §6.2; X12 `Datos_Relaciones` | Obra/partida/actividad, mediciones paralelas, rendimiento, costos e histórico; no FK ficticias | — |
| 5.04 | Integraciones existentes o supuestas | CUMPLE | A12; V12 §6.2 | Exportación/planilla delimitadas como supuestas; APIs reales desconocidas | — |
| 5.05 | Usuarios y actores | CUMPLE | A12; V12 §4.3 | Roles internos y terceros sin dotación inventada | — |
| 5.06 | Infraestructura y límites | CUMPLE | A12; V12 §6.1; S-22/23 | Nodos lógicos de puesto, ejecución, almacenamiento y exportación; F1/F2/F3, sin afirmar servidores reales | — |
| 5.07 | Problemas arquitectónicos | CUMPLE | V12 §7; X12 `Deuda_Trazabilidad` | Once problemas/riesgos del escenario, no vulnerabilidades confirmadas | — |
| 5.08 | Deuda priorizada | CUMPLE | V12 §7 | P1/P2/P3 definidos cualitativamente | — |
| 5.09 | TO-BE v0.1 | CUMPLE | T12; V12 §8 | Conserva ERP y separación analítica; no cambio de stack injustificado | — |
| 5.10 | Capacidades/componentes objetivo | CUMPLE | V12 §8.1; T12 | Extracción, staging, transformación, modelo, consumo y controles | — |
| 5.11 | Responsabilidad por componente | CUMPLE | V12 §8.1; T12 | Función y flujo sin escritura de retorno al ERP | — |
| 5.12 | Tabla de decisiones arquitectónicas | CUMPLE | V12 §8.2; X12 `ADR` | Tabla completa sincronizada | — |
| 5.13 | ≥5 decisiones justificadas | CUMPLE | V12 §8.2 | Seis ADR conservadas/precisadas | — |
| 5.14 | Alternativas y trade-offs | CUMPLE | V12 §8.2 | Alternativas y limitaciones por ADR | — |
| 5.15 | Evidencias y riesgos | CUMPLE | V12 §§7–9; F12 | Fuentes específicas y riesgos; referencias no reinspeccionadas no sustentan resultados actuales | — |
| 5.16 | Mapa de dependencias | CUMPLE | D12; V12 §9 | F-01 y E-1–E-10; condiciones y responsables | — |
| 5.17 | Problema → decisión → componente | CUMPLE | V12 §7 | DT → ADR → respuesta explícita | — |
| 5.18 | Decisiones versionadas | CUMPLE | V12 §10.1; X12 `Decisiones` | D-01–D-22, procedencia y cambios; sin aprobación ficticia | — |
| 5.19 | Diagramas legibles e identificados | CUMPLE | A12/R12/T12/D12 y exportaciones; PDF12 | Figuras renderizadas/inspeccionadas, con versión, fecha, título y elaboración propia; límites Word separados | — |
| 5.20 | Consolidado S1–S5 | CUMPLE | V12 §§2–10; PDF12/DOC12 | Integración de negocio, personas, hipótesis, arquitectura y registros | — |
| 5.21 | ≥3 fuentes pertinentes | CUMPLE | V12 §12; F12 | Fuentes oficiales específicas consultadas, incluida NIST final | — |

## 5. Justificación de los siete cambios de clasificación

| Criterio | Anterior → posterior | Evidencia que cambia el juicio |
|---|---|---|
| 2.01 | PARCIAL → CUMPLE | BP12 p. 1 y B12 sustituyen la representación contradictoria en el conjunto vigente |
| 2.03 | PARCIAL → CUMPLE | BP12 pp. 1/3 separan canales y clientes; mismo defecto original, no dos incidentes |
| 3.03 | PARCIAL → CUMPLE | Instrumento y regla definidos; puntuaciones arbitrarias retiradas; ND permitido sin imputación |
| 4.05 | PARCIAL → CUMPLE | B0 no recibe real evaluado; separación de columnas/datos, cobertura y sensibilidad explícitas en EXP12 |
| 4.12 | NO CUMPLE → CUMPLE | Métodos con fuentes accesibles y metas derivadas de supuestos internos reproducibles; no benchmark externo inventado |
| 5.03 | PARCIAL → CUMPLE | R12 y tabla conceptual explican relaciones y granularidad, sin fingir esquema SQL |
| 5.06 | PARCIAL → CUMPLE | A12 y supuestos trazables incorporan infraestructura lógica y fronteras exigidas |

Los demás criterios conservan su clasificación, aunque su evidencia se actualiza.
No se sube 1.10 solo por añadir una tabla ni 3.09 solo por crear un instrumento.

## 6. Revisión transversal y del Hito I

- **H-01:** requiere validación humana; checklist sin casillas marcadas. Impide
  declarar la versión lista para presentación final conforme a §16 de la guía.
- **H-03/3.09:** diagnóstico aún insuficiente en condiciones de escenario de ocho
  dimensiones. ND es una corrección honesta, no prueba de capacidad/inmadurez.
- **H-10:** vínculos Git mejorados, atribución individual aún limitada.
- **H-11:** material vigente sustituye fotos/iconos por figuras propias; procedencia
  de activos históricos no recuperada. Original conservado y no reutilizado.
- **H-12:** referencias activas precisadas; citas históricas pendientes siguen
  identificadas y no se usan para sostener metas o cifras nuevas.
- **H2/H3 y nuevo H1-v1.2:** pendientes de ejecución; no incumplimiento del diseño S4.
- **Formatos:** integridad/contenido comprobados; Word no renderizado y Excel sin
  evaluación visual en escritorio. No se afirma paginación Word ni recálculo Excel.
- **Contribuciones, fechas y permisos:** no se fabricaron; Git no prueba entrega
  o aprobación docente. Seguridad empresarial y acceso productivo fuera de alcance.

El TO-BE sigue proporcional: extracción por lotes, validación, modelo separado y
consumo condicionado. Las seis ADR conectan DT, P-01 y capacidades. No hay nueva
dependencia obligatoria de IA, Airflow, dbt o nube. La arquitectura es diseño,
no evidencia de una implementación funcional integral.

## 7. Verificación técnica y límites de confianza

Comprobaciones en `documentos/proyecto/verificar_hito_v12.py`: conservación por hash,
HEAD intacto, integridad ZIP/XML, párrafos y tablas DOCX/PDF frente al Markdown,
cuatro imágenes, correspondencia de hojas actuales/históricas y 69 filas de esta
auditoría. Evidencia de ejecución: `evidencias/revision-v1.2/verificacion_tecnica.json`.
Revisión visual y sus límites: `evidencias/revision-v1.2/README.md`.

No se asigna una nueva nota orientativa: estos conteos no sustituyen la rúbrica
30/25/20/15/10 ni la evaluación individual, y no justifican recalificar los originales.

## 8. Veredicto posterior

La v1.2 corrige las brechas documentales principales de arquitectura, comparador,
metodología, BMC y cobertura de capacidades. **67/69 criterios CUMPLE, dos PARCIAL**,
con un P0 transversal todavía abierto. S2/S4/S5 completan su checklist documental,
no aprobación académica integral. El equipo debe revisar fuentes, supuestos,
madurez, umbrales, decisiones, formatos, aportes y defensa antes de entregar.

No declarar cerrado H-01, beneficios reales, un experimento nuevo ejecutado,
puntualidad ni conformidad docente. Plan/manuales pendientes y cambios detallados:
`CORRECCIONES_ACADEMICAS_S01_S05_v1.2.md`.
