# Registro de cambios

Este archivo resume los cambios relevantes del proyecto. Los detalles y las razones de decisiones deben conservarse también en el Registro de Decisiones.

## [No publicado]

### Mantenimiento previo a Semana 6 — 26/10/2026

- Rama de trabajo `chore/preparacion-semana-06`, basada en `7f962fa`; sin commit ni push de esta intervención.
- Navegación hacia Hito I v1.2, índice actual de originales y revisiones, y convención para documentos futuros.
- Verificación actual de solo lectura separada de herramientas/evidencias históricas; inventarios nuevos sin sustituir los anteriores.
- Guía compartida `proyectoIntegrador.pdf` idéntica a la copia local citada históricamente; archivos personales siguen opcionales/ignorados.
- Matriz de comandos con escritura, flujo verify/generate/publish aislado y plan de ubicaciones S6, sin desarrollar su entregable ni ejecutar experimentos.
- Protección preventiva de `.env` y credenciales locales. Los cuatro `.pyc` versionados se identifican, pero no se retiran sin autorización.
- Detalles, pruebas y pendientes: [informe de mantenimiento](documentos/mantenimiento/INFORME_MANTENIMIENTO_S06.md).

### Hito I v1.2 — revisión del 25/10/2026, incorporada a Git el 26/10/2026

- Revisión consolidada vigente, **Pendiente de validación humana**, publicada separadamente en `entregas/semana-05/revision-v1.2/`.
- AS-IS lógico y datos conceptuales; instrumento de madurez con ND; métricas y umbrales con fundamento interno retrospectivo; seis dimensiones de capacidades recomendadas.
- Nuevo protocolo B0/M1 **diseñado, no ejecutado**; resultados sintéticos anteriores preservados. Presentación S2 sustituida y atribuciones CAPECE rectificadas.
- [Registro completo de correcciones](CORRECCIONES_ACADEMICAS_S01_S05_v1.2.md) y [auditoría posterior histórica](AUDITORIA_POST_CORRECCIONES_S01_S05_v1.2.md); no equivalen a aprobación humana o nueva nota.

Las entradas anteriores se conservan como historia: las menciones de Odoo y Chrome describen estados/instrucciones antiguos, no el stack ni los comandos vigentes. Los generadores actuales antiguos siguen requiriendo cautela; consultar la matriz de mantenimiento.

### Hito I v1.1 — corrección del 24/10/2026

- Se conserva el Hito I v1.0 y las entregas S1–S4. La corrección se publica separada en `entregas/semana-05/revision-v1.1/`.
- Se rectifica el stack: ERP propio CodeIgniter/MySQL, sin versiones ni inventario supuestos como hechos. Odoo/PostgreSQL en entradas históricas no describen el caso vigente.
- Diagnóstico S3 declarado hipotético; anexos BMC, stakeholders, madurez, brechas, supuestos y contribuciones reconstruidos con procedencia.
- Decisiones D-01–D-16 y ADR-01–ADR-06 sincronizadas con el documento fuente v1.1; S4 D-06/D-07/D-08 se reconcilian como D-11/D-12/D-13.
- TO-BE mínimo por lotes y destino separado; herramientas avanzadas condicionadas a evidencia. No se conecta a producción ni se reemplaza el ERP.
- Diagramas nuevos con metadatos y exportaciones; generación de PDF/DOCX desde la misma fuente, sin afirmar que píxeles no blancos demuestren legibilidad.
- PoC: MAPE promedio, límites sintéticos, decisión uniforme y costo real cero rechazado explícitamente; pruebas adicionales. No se modifican umbrales para lograr aceptación.
- Seis referencias oficiales consultadas; fuentes históricas no revalidadas separadas. Validación humana y medición empresarial pendientes.

### Pendiente

- Los datos reales del Grupo 1 y sus integrantes ya fueron registrados.
- Validar el AS-IS revisado (diagrama disponible en v1.1).
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
