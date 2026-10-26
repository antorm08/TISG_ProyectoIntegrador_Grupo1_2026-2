# Correcciones académicas — S1–S5 / Hito I v1.2

UNMSM — FISI — Ingeniería de Software. Curso: Tendencias en Ingeniería de Software y Gestión.
Grupo 1. Semana 5, integración S1–S5. Fecha: 25/10/2026. Versión: v1.2.
**Estado general: Pendiente de validación humana.** Elaboración con asistencia de IA.

## 1. Resultado y alcance

Se conservan los originales S1–S5, v1.1, resultados de la PoC y auditoría inicial.
La guía oficial sigue siendo la autoridad normativa. La revisión corrige el conjunto
documental vigente, no las entregas históricas ni su fecha de presentación.

Los mismos 69 criterios pasan de **60 CUMPLE, 8 PARCIAL y 1 NO CUMPLE (87,0 %)** a
**67 CUMPLE, 2 PARCIAL y 0 NO CUMPLE (97,1 %)**. Las siete transiciones y sus
evidencias están en [la auditoría posterior](AUDITORIA_POST_CORRECCIONES_S01_S05_v1.2.md).
El porcentaje es cobertura documental, no nota, aprobación humana o preparación final.

## 2. Hallazgos y estado comprobado

Las referencias § remiten al [Hito I v1.2](documentos/proyecto/Semana5_Hito_I_v1.2.md).
“Verificado” se limita al contenido y formatos efectivamente comprobados; no acredita implantación.

| Hallazgo | Estado anterior | Corrección realizada | Evidencia | Estado nuevo |
|---|---|---|---|---|
| H-01 | P0: aprobación humana pendiente | Checklist de fuentes, supuestos, experimento, arquitectura, diagramas, coherencia y defensa, sin marcar como realizado | §11; XLSX `Revision_Humana` | REQUIERE VALIDACIÓN HUMANA |
| H-02 | P1: AS-IS sin relaciones e infraestructura suficientes | Cuatro nodos lógicos, módulos, actores, tres fronteras y relaciones conceptuales; conocidos y supuestos separados | §6; figuras 1/2 SVG/PNG/PDF; XLSX `Topologia` y `Datos_Relaciones` | CORREGIDO Y VERIFICADO |
| H-03 | P1: puntuaciones sin criterios suficientes | Escala propia de cinco niveles, nueve dimensiones, reglas y acciones; ocho ND y datos 2-H bajo S-24, sin promedio | §4; XLSX `Instrumento_Madurez` y `Madurez_SocioTecnica`; criterio 3.09 aún PARCIAL | CORREGIDO PARCIALMENTE |
| H-04 | P1: metas sin fundamento metodológico suficiente | Fórmulas/unidades, tolerancias internas reproducibles, decisiones y sensibilidad; justificación retrospectiva explícita, sin equivalencia AACE | §5.1–5.2; XLSX `Metricas`/`Umbrales` | CORREGIDO Y VERIFICADO |
| H-05 | P1: comparador usa el real evaluado | Protocolo B0 mediana histórica frente a M1 ponderado; columnas permitidas, separación, cobertura, sensibilidad y reproducibilidad | §5.3; `poc/POC-01-estimacion-historicos/revision-v1.2/DISENO_EXPERIMENTAL.md` | CORREGIDO Y VERIFICADO |
| H-06 | P1: segmentos/canales contradictorios | Presentación sustituta de cinco láminas: segmentos, canales comerciales/digitales e ingresos/eficiencia coherentes | §3.1; `entregas/semana-02/revision-v1.2/Presentacion_S2_v1.2.pdf`; Markdown/SVG/DOCX editables | CORREGIDO Y VERIFICADO |
| H-07 | P1: cifras CAPECE atribuidas a edición/periodo no acreditados | Se retiran cifras H1 2026 y fundamento de D-10; página consultada identificada 2024–2025, sin atribuir lectura del informe completo | §3.2; `fuentes/revision-v1.2/VERIFICACION_FUENTES.md`, CAP-01–CAP-06 | CORREGIDO Y VERIFICADO |
| H-08 | P1: seis dimensiones incompletas en capacidades recomendadas | Matriz para BI, analítica, IA, APIs, gobierno y SSDF; sin Canvas obligatorios para tecnologías postergadas | §2.3; XLSX `Impact_Canvas` | CORREGIDO Y VERIFICADO |
| H-09 | P2: identificación/versionado mejorables | Curso, equipo, semana, versión, fecha y estado en nuevos documentos y artefactos; portadas históricas preservadas | Portada y pies PDF/DOCX, figuras y manifiestos v1.2 | CORREGIDO Y VERIFICADO |
| H-10 | P2: atribución individual débil | Se preservan veinte declaraciones y se vinculan archivos/commits existentes; no se atribuyen cambios v1.2 a integrantes | `gestion/registros/Contribuciones_Evidencia_v1.2.md`; XLSX `Evidencia_Aportes`; 1.10 PARCIAL | CORREGIDO PARCIALMENTE |
| H-11 | P2: procedencia visual incompleta | Presentación vigente sustituida por figuras propias sin fotos/iconos ajenos; activos históricos no reutilizados | Láminas SVG/PNG/PDF y README S2 v1.2; procedencia histórica aún desconocida | CORREGIDO PARCIALMENTE |
| H-12 | P2: enlaces genéricos/ediciones/estado de publicación | Referencias activas específicas, fechas y APA; NIST 1.1 final distinto de 1.2 IPD; límites históricos y acceso fallido documentados | §12; registro FV-01–FV-13 y límites; antecedentes no todos reinspeccionados | CORREGIDO PARCIALMENTE |
| H-13 | P2: identificación de versión vigente | README principal y manifiestos separan v1.2, originales y v1.1; enlaces a protocolo, fuentes e informes | `README.md`; README de paquetes S2/S5 y evidencias | CORREGIDO Y VERIFICADO |

H-05 está corregido como **diseño**, no como nuevo experimento ejecutado. S4 no exige
ejecución adicional. Las metas de H-04 requieren aceptación humana antes de un piloto;
el razonamiento documentado no convierte los supuestos en datos empresariales.

## 3. Archivos creados y modificados

Inventario exhaustivo de rutas, tamaños y SHA-256: `evidencias/revision-v1.2/inventario_final.json`.
Se agrupan aquí las entregas para facilitar lectura:

- `documentos/proyecto/Semana5_Hito_I_v1.2.md`: fuente consolidada.
- `documentos/proyecto/Semana2_MaterialComplementario_v1.2.md`: sustituto S2 editable.
- `documentos/proyecto/generar_hito_v12.py` y `verificar_hito_v12.py`: generación y comprobación aisladas.
- `arquitectura/generar_revision_v12.py` y `arquitectura/revision-v1.2/`: cuatro diagramas, cada uno SVG/PNG/PDF.
- `entregas/semana-05/revision-v1.2/`: Hito I PDF de 17 páginas, DOCX y README.
- `entregas/semana-02/revision-v1.2/`: cinco láminas SVG/PNG/PDF, presentación combinada PDF, DOCX y README.
- `gestion/registros/Registros_y_Radar_Semana5_v1.2.xlsx`: 34 hojas; registros actuales e históricos identificados.
- `gestion/registros/Contribuciones_Evidencia_v1.2.md`: atribución y límites.
- `poc/POC-01-estimacion-historicos/revision-v1.2/DISENO_EXPERIMENTAL.md`: diseño no ejecutado.
- `fuentes/revision-v1.2/VERIFICACION_FUENTES.md`: fuentes y rectificaciones.
- Este informe, `AUDITORIA_POST_CORRECCIONES_S01_S05_v1.2.md` y `evidencias/revision-v1.2/`: auditoría, manifiestos y pruebas.

**Único archivo previo modificado por esta tarea: `README.md`, para navegación.**
`.gitignore` ya estaba modificado por el usuario y conserva su hash inicial.
No se sobrescribieron archivos históricos ni se hicieron commits, push o cambios de historial.

## 4. Decisiones, fuentes y continuidad

- C-09–C-16 documentan las correcciones; D-17–D-22 registran las nuevas decisiones
  propuestas. D-01–D-16 conservan procedencia; D-10/D-12 reciben notas de actualización,
  sin retrofechar. Se añaden S-22–S-26; S-19 queda limitado al comparador histórico.
- Se conserva CodeIgniter/MySQL y el alcance de complementar el ERP. Las seis ADR
  no implican servicios desplegados; nube, Airflow, dbt y otros quedan condicionados.
- CAPECE deja de respaldar cifras 2026; Atlassian/Thoughtworks se citan mediante
  páginas específicas. Microsoft distingue gateway y RLS; scikit-learn/Python
  respaldan métodos, no metas. NIST 1.2 sigue identificado como borrador.
- S1→S2: problema de históricos y P-01; S2→S3: capacidades de datos/personas;
  S3→S4: diseño sintético viable sin acceso productivo; S4→S5: componentes para
  evaluar H1/H2/H3; S1→S5: mismos anillos y ERP. Matriz verificable en §9.

## 5. Verificación técnica y límites

El verificador compara 111 entradas de integridad (con alguna ruta repetida entre
manifiestos), HEAD, 23 tablas y párrafos DOCX/PDF, cuatro figuras, XML/ZIP, 34 hojas,
registros originales, veinte contribuciones y los IDs/nombres exactos de 69 criterios.
Los libros previos no contenían fórmulas; no se introdujo un recálculo simulado.
Detalle y ejecución: `evidencias/revision-v1.2/README.md` y `verificacion_tecnica.json`.

Se inspeccionaron las 17 páginas PDF por contactos, páginas detalladas, cuatro
diagramas y cinco láminas S2. No se observó recorte/superposición en lo inspeccionado.
DOCX no fue renderizado con Word/LibreOffice; XLSX no tuvo inspección de escritorio
ni motor de recálculo. Su integridad y contenido no prueban paginación o diseño Office.
CairoSVG no funciona por DLL Cairo ausente: se usó PyMuPDF ya disponible. No se
instalaron nuevas dependencias ni se subieron documentos a conversores externos.

## 6. Acciones humanas y externas pendientes

1. **H-01:** cada integrante debe revisar realmente fuentes, supuestos, resultados
   históricos, nuevo diseño, ADR, diagramas y coherencia; defender el conjunto y
   registrar su aprobación solo si efectivamente sucede. No cerrar mediante IA.
2. **3.09:** fundamentar las condiciones del escenario en ocho dimensiones o
   conservar ND. No es obligatorio inventar una empresa real ni realizar entrevistas.
3. **1.10:** confirmar aportes con evidencia existente; no fabricar commits o firmas.
4. Abrir DOCX/XLSX en escritorio y revisar tablas, saltos, filas y figuras antes de
   entregar. Si se exporta desde Office, revisar ese nuevo PDF por separado.
5. Revisar activos históricos si se pretende reutilizarlos; obtener atribución/licencia
   o descartarlos en futuras versiones. La presentación vigente ya evita esos activos.
6. Antes de piloto futuro: aprobar metas/supuestos, permisos, capacidad, licencias,
   protocolo y datos. H1-v1.2/H2/H3 no están ejecutadas. La PoC anterior no prueba
   ahorro real ni superioridad frente al nuevo baseline.
7. Verificar versión y envío en aula: Git no acredita puntualidad, aceptación o nota.

**No se declara el Hito I listo o aprobado: permanece Pendiente de validación humana.**
