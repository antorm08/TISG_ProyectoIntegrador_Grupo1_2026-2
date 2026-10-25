# Hito I corregido — v1.1

Curso: Tendencias en Ingeniería de Software y Gestión · Grupo 1 · Semana 5.
Fecha real de corrección: **24/10/2026**. Caso ficticio académico: Constructora Andina S.A.C.
Estado: artefactos generados; **revisión y aprobación humana del equipo pendientes**.

## Archivos vigentes

- `TISG_E01_S05_HitoI_v1.1_2026-10-24.pdf`: informe corregido.
- `TISG_E01_S05_HitoI_v1.1_2026-10-24.docx`: versión editable del mismo contenido.
- [Fuente Markdown](../../../documentos/proyecto/Semana5_Hito_I_v1.1.md).
- [Excel consolidado v1.1](../../../gestion/registros/Registros_y_Radar_Semana5_v1.1.xlsx): decisiones, ADR, Radar, supuestos, contribuciones históricas y anexos reconstruidos S2/S3.
- [Cuatro figuras SVG/PNG/PDF](../../../arquitectura/revision-v1.1/).
- [Resultados de verificación](../../../evidencias/revision-v1.1/README.md).

El ERP es propio CodeIgniter/MySQL. No se sustituye por Odoo ni se migra a PostgreSQL. El TO-BE es una propuesta mínima por lotes, no un despliegue empresarial. Madurez y resistencias son hipótesis académicas. H2/H3 siguen pendientes; H1 solo tiene resultado descriptivo sintético. La corrección y el uso de IA se declaran en el informe; no se atribuyen aportes nuevos a integrantes sin validación.

Los archivos originales del directorio padre y de S1–S4 se preservan. No interpretar esta revisión como entrega dentro del plazo original ni como aprobación docente. Consultar sección 11 del informe para límites y verificación contra la guía.

## Reproducción

Desde la raíz del repositorio, Python 3 con las dependencias de `documentos/proyecto/requirements-hito.txt`:

```powershell
python arquitectura/generar_diagramas.py
python arquitectura/render_diagramas.py
python gestion/registros/actualizar_registros_semana5.py
python documentos/proyecto/artefactos_hito.py
python documentos/proyecto/verificar_hito.py
```

La generación PDF usa Arial de `C:/Windows/Fonts`. No requiere Word ni LibreOffice, ni acceso de red o al ERP. Los diagramas PDF son vectoriales; los PNG se incrustan en los informes. La verificación técnica no reemplaza lectura y aprobación humana.
