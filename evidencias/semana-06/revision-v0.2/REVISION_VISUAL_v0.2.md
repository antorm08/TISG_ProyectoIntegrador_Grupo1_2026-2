# Inspección visual editorial — v0.2 BORRADOR

26/10/2026 · Realizada por el asistente IA, **no por estudiantes ni revisores humanos**.
Build seleccionado: `editorial-02`. PDF final: 12 páginas A4, sin páginas vacías.
Todas se renderizaron con PyMuPDF a escala 1.5 (aproximadamente 108 dpi).

## Inspección de cada página

Se abrieron individualmente las doce imágenes de `editorial-01/paginas/`.
Después de corregir la referencia páginas/secciones, añadir cita Python y mejorar
el contraste de los extractos, se generó `editorial-02`. Las páginas 2, 6 y 7 se
abrieron de nuevo. Las otras nueve imágenes finales tienen exactamente el mismo
SHA-256 que las ya inspeccionadas; no se presupuso equivalencia solo por número.

| Página | Contenido revisado | Resultado visual observado |
|---|---|---|
| 01 | Portada, identidad, fecha y estado | Jerarquía clara, sin logo inventado, margen/estado legibles |
| 02 | Resumen y tabla de resultados | Tasas contextualizadas; navegación corregida a páginas |
| 03 | Mapa del SDLC y oportunidades | Figura vectorial legible; tabla y leyenda dentro de márgenes |
| 04 | Matriz de autonomía | Once tareas, cuatro columnas, sin filas partidas o apretadas |
| 05 | Arquitectura, ADR y contrato | Flujo POC→staging correcto; distinción actual/propuesto |
| 06 | Flujo de desarrollo/evaluación | Flechas, cita y advertencia de independencia legibles |
| 07 | CSV, comando, JSON y log reales | Extractos sobre gris claro, sin recortes; no captura simulada |
| 08 | Evaluación/RF/hallazgos | Tabla completa, fallos de arnés explícitos, texto sin desbordes |
| 09 | Rendimiento y métricas humanas | Unidades ms visibles y cinco grupos; límites separados |
| 10 | Riesgos y amenazas de validez | Tabla y discusión sin cortes; párrafos equilibrados |
| 11 | APU, conclusiones y pendientes | Actual/propuesto/futuro distinguibles; BORRADOR destacado |
| 12 | Referencias y anexos | URLs/citas y tabla legibles; declaración de IA y cierre |

No se observaron superposiciones, glifos ausentes, recortes de tablas o pies fuera
de margen. Los doce folios son continuos. Cada sección principal empieza en una
página; no se añadieron páginas vacías para alcanzar extensión. Las tres figuras
se incrustan como vectores en PDF y se conservan además como SVG/PDF/PNG editables.
Arial/Consolas son fuentes locales existentes; no se instalaron tipografías.

## Comprobaciones complementarias y límites

La extracción de texto registra cero bloques fuera del lienzo. El verificador
contrasta títulos, párrafos, celdas y extractos del Markdown con el texto PDF,
normalizando whitespace para los saltos de maquetación. Los extractos se contrastan
por separado con sus archivos originales. Ninguna comprobación automática sustituye
lectura visual o validación semántica humana.

DOCX: estructura ZIP/python-docx, tablas y tres figuras verificadas. **No se renderizó
en Word/LibreOffice**; su paginación visual no está verificada. No se renderizó ni
modificó Excel histórico. Queda revisión final humana de contenido y presentación.
