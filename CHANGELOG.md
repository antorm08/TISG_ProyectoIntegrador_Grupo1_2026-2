# Registro de cambios

Este archivo resume los cambios relevantes del proyecto. Los detalles y las razones de decisiones deben conservarse también en el Registro de Decisiones.

## [No publicado]

### Pendiente

- Los datos reales del Grupo 1 y sus integrantes ya fueron registrados.
- Elaborar el mapa arquitectónico AS-IS.
- Validar volumen, frecuencia, latencia y calidad de los datos.
- Formalizar la matriz de riesgos.
- Desarrollar el roadmap 2026–2029.

## [Semana 1] — 2026-09-04

### Agregado

- Definición explícita de los anillos Adoptar, Probar, Evaluar y Esperar.
- Registro inicial de cinco decisiones.
- Distribución de responsabilidades para cuatro integrantes.
- Evidencia documental de contribuciones.
- Metadatos, justificaciones y trazabilidad ampliada del Radar.
- Guía explicativa para la preparación de los integrantes.

### Modificado

- Ajustes de legibilidad del documento, Radar y evidencias.
- Consolidación de los registros en el libro Excel.

## [0.2] — 2026-08-29

### Modificado

- Actualización de fuentes con prioridad en publicaciones de 2025–2026.
- Incorporación de evidencia oficial, industrial y académica.
- Revisión de posiciones del Technology Radar según actualidad, riesgo y proporcionalidad.

## [0.1] — 2026-08-29

### Agregado

- Planteamiento inicial del caso.
- Ficha de la organización.
- Project Charter.
- Mapa inicial de stakeholders.
- Technology Radar v0.1.
- Tres Impact Canvas.
- Registro inicial de supuestos.

## [Semana 5] — 2026-10-09 (Hito I)

### Agregado

- Documento consolidado `documentos/proyecto/Semana5_Hito_I.md` que integra las semanas 1–5.
- Entrega `entregas/semana-05/` con `TISG_E01_S05_ProyectoIntegrador_2026-10-09.docx` e imágenes incrustadas.
- Diagramas SVG/PNG/PDF: AS-IS (figuras 1–2) y TO-BE v0.1 (figuras 3–4) con leyenda.
- Generadores `arquitectura/{svg_lib,figuras_a,figuras_b,generar_diagramas}.py` y verificador `render_diagramas.py` con Chrome headless.
- Seis decisiones arquitectónicas (ADR-01 a ADR-06), deuda técnica DT-01 a DT-11 y mapa de dependencias E-1–E-10.
- Extensión de `documentos/proyecto/md_to_docx.py` para incrustar imágenes PNG en DOCX.
- Alcance explícito: fuera de alcance v0.1 (agentes, RAG, eventos, lakehouse, reemplazo de ERP).
- Nota de reconciliación de IDs (D-06–D-08 S4 renumerados a D-11–D-13 en el Hito I).

### Modificado

- `README.md` actualizado a Semana 5 (Hito I) y tabla de entregas.
- Arquitectura documentada para evolución por capas sin reemplazar Odoo 16.

### Verificado

- Los cuatro diagramas superan el umbral mínimo de contenido en PNG.
- El DOCX contiene 4 dibujos e imágenes y pasa validación XML.
