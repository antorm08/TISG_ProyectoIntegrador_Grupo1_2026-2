# Evidencia de comprobación — Hito I v1.2

UNMSM — FISI. Tendencias en Ingeniería de Software y Gestión. Grupo 1. S1–S5.
25/10/2026. Versión v1.2. **Pendiente de validación humana.**

## Archivos y alcance

- `integridad_antes.json`: 108 entradas previas y HEAD de referencia.
- `fuentes_locales_antes.json`: auditoría original, documento de skills y `.gitignore`.
- `verificacion_tecnica.json`: resultado del verificador final.
- `inventario_final.json`: rutas creadas/modificadas, tamaño y SHA-256; excluye su
  propio archivo para evitar un hash autorreferente. No es commit ni firma humana.

Única modificación prevista a contenido previo: `README.md`. Los hashes de históricos,
auditoría original y cambios preexistentes del usuario deben conservarse. HEAD:
`038ce87e1cb6e4d13478a0f83a94c2bf34b3ce0e`.

## Comandos reproducibles

Desde la raíz, usando dependencias ya disponibles:

```powershell
python -X utf8 -B arquitectura/generar_revision_v12.py
python -X utf8 -B documentos/proyecto/generar_hito_v12.py
python -X utf8 -B documentos/proyecto/verificar_hito_v12.py --guardar
```

Los dos generadores escriben solo artefactos v1.2 y no ejecutan la PoC. El
verificador es de solo lectura salvo `--guardar`, que guarda su JSON. Regenerar
puede cambiar hashes de binarios por metadatos; revisar de nuevo e inventariar.
No ejecutar los generadores/verificadores históricos de la PoC para validar esta
revisión: pueden sobrescribir CSV. No se ejecutaron en esta tarea.

Pruebas: integridad ZIP/XML; párrafos/tablas DOCX y PDF frente a Markdown; cuatro
imágenes; ausencia de texto fuera del lienzo PDF; contenido de tablas XLSX actuales;
copias históricas, veinte contribuciones y fórmulas previas (cero) preservadas;
D-01–D-22, S-01–S-26; cuatro figuras, cinco láminas; igualdad de 69 IDs/nombres de
criterios con auditoría inicial y conteo 67 CUMPLE/2 PARCIAL. La extracción de texto
PDF excluye los 40 puntos inferiores del pie para no intercalar pies en párrafos
que atraviesan páginas; se comprueba aparte el lienzo completo.

## Revisión visual efectivamente realizada

Renderizado PyMuPDF a escala 1,5; inspección mediante apertura de PNG:

- PDF Hito I: contactos de las 17 páginas (`contacto-1.png` a `contacto-3.png`).
- Inspección individual de páginas 3, 5, 7 y 9, y finales 10, 12 y 13.
- Cuatro diagramas PNG y cinco láminas S2 PNG completos.
- Se corrigieron cruces entre flechas/notas en AS-IS y relaciones; el TO-BE final
  dice “Alternativa local propuesta”, no una aprobación humana ya realizada.
- Tras ese último cambio se regeneraron los formatos, se renderizó y abrió la
  página 12 afectada y la figura TO-BE final. Páginas 10/13 también se abrieron en
  su render final. No cambió el contenido ni distribución de las otras páginas.

Directorio temporal de inspección (no requerido para usar los entregables):
`D:/OpenCode/cache/opencode/document-skills-tests/hito-v12-gxe5je1n/`.
Los PNG `final-pagina-10.png`, `final-pagina-12.png`, `final-pagina-13.png` corresponden
al último render detallado. Las imágenes/figuras publicadas están en los paquetes
v1.2. La inspección no encontró recortes o superposiciones visibles en lo revisado;
no constituye garantía de legibilidad universal ni revisión humana del equipo.

## Límites y acciones externas

- PDF de ReportLab y DOCX de python-docx se generan independientemente; el PDF
  no representa el render de Word. Sin Word/LibreOffice configurado no se verifica
  paginación DOCX; abrir y revisar en escritorio.
- XLSX se abrió con openpyxl para contenido/integridad; sin render de Excel ni
  motor de cálculo. No se certifican anchos/altos visuales ni recálculo Office.
- CairoSVG está instalado pero carece de DLL Cairo utilizable. PyMuPDF permitió
  exportar SVG/PDF/PNG sin nuevas instalaciones. No se usó conversión externa.
- Las páginas web consultadas y sus límites están en el registro de fuentes;
  OTexts respondió con desafío HTTP 202 y no se presenta como lectura realizada.
- Nuevo experimento **no ejecutado**. Resultados históricos solo preservados;
  aprobación humana y evaluación individual **pendientes**.

La auditoría fue realizada por el mismo asistente que corrigió los documentos;
no es aseguramiento externo independiente. Pruebas automáticas no prueban calidad
académica por sí solas. No se crearon commits ni se alteró el historial Git.
