# Evidencia de la corrección v1.1 — 24/10/2026

## Comprobaciones realizadas

- `verificacion.json`: resumen generado por `documentos/proyecto/verificar_hito.py`.
- `salida_verificacion_poc.txt`: salida real del generador, experimento, fixture y pruebas unitarias; no es una transcripción inventada.
- Libro Excel: comparación de las tablas revisadas con el documento fuente; decisiones únicas D-01–D-16, seis ADR, anexos S2/S3 y veinte contribuciones históricas declaradas.
- DOCX: ZIP/XML válidos, cuatro imágenes y todas las tablas del Markdown; mismo contenido de origen que el PDF.
- PDF: texto completo de párrafos, encabezados, tablas y pies de figuras; cuatro imágenes; sin bloques fuera de página.
- Cuatro SVG parseables y sus PDF/PNG exportados. Inspección visual de las cuatro figuras y del PDF mediante vistas de páginas. No se usa cobertura de píxeles como prueba de legibilidad.
- Entregas originales: comprobación de que no hay diferencias en archivos históricos versionados de `entregas/` frente a HEAD de la rama.
- PoC: nueve pruebas unitarias y reproducción del escenario fijo: MAPE analítico 11,31 %, control 20,19 %, reducción 43,98 %. Dos partidas superan 15 % individual.

El verificador se puede volver a ejecutar con `python documentos/proyecto/verificar_hito.py`. El número de páginas y resultados concretos se obtienen del JSON generado, no de una expectativa de tamaño del informe.

## Límites

Esto es evidencia de ejecución y consistencia técnica, no entrevistas, revisión humana del equipo, validación docente ni efectos empresariales. No hubo conexión al ERP ni al aula virtual. H2 y H3 permanecen pendientes. Los aportes de la corrección no se atribuyen individualmente a integrantes sin su validación.

Las fuentes oficiales consultadas se detallan en el [registro de fuentes de revisión](../../fuentes/revision-v1.1/README.md). Las citas históricas que no se revalidaron conservan ese estado y no respaldan cifras nuevas.
