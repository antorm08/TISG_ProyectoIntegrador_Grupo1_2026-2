# Entrega — Semana 5

## Identificación

- Curso: Tendencias en Ingeniería de Software y Gestión
- Equipo: Grupo 1
- Semana: 05
- Caso: Constructora Andina S.A.C. (organización ficticia)
- Versión: v1.0
- Fecha: 2026-10-09
- Estado: documento consolidado de Hito I (fotografía hasta la semana 5)

## Objetivo

Consolidar las semanas 1–5 en un único documento de Hito I: arquitectura AS-IS y TO-BE v0.1, problemas y deuda técnica priorizada, ≥5 decisiones arquitectónicas justificadas, mapa de dependencias y trazabilidad con avances anteriores.

## Contenido de la entrega

| Archivo | Propósito |
|---|---|
| `TISG_E01_S05_ProyectoIntegrador_2026-10-09.docx` | Hito I consolidado (DOCX) con diagramas incrustados |
| `README.md` | Esta ficha de entrega |

## Artefactos de apoyo (fuera de esta carpeta)

| Ruta | Propósito |
|---|---|
| `documentos/proyecto/Semana5_Hito_I.md` | Fuente en Markdown del Hito I |
| `documentos/proyecto/md_to_docx.py` | Script que genera el DOCX e incrusta imágenes |
| `arquitectura/as-is/` | Figuras 1 y 2 (SVG, PNG, PDF) |
| `arquitectura/to-be/` | Figuras 3 y 4 (SVG, PNG, PDF) |
| `arquitectura/generar_diagramas.py`, `figuras_a.py`, `figuras_b.py`, `svg_lib.py`, `render_diagramas.py` | Generación y verificación de diagramas con Chrome headless |
| `gestion/registros/` | Registros consolidados |
| `entregas/semana-01`, `semana-02`, `semana-03`, `semana-04` | Entregas previas |

## Verificación de requisitos (guía del curso)

| Requisito | Estado | Evidencia |
|---|---|---|
| Diagrama AS-IS (aplicaciones, datos, integraciones, actores, infraestructura y límites) | OK | Figura 1 (sección 3) |
| Problemas arquitectónicos y deuda técnica priorizada | OK | DT-01 a DT-11 (sección 4) |
| Diagrama TO-BE v0.1 con capacidades objetivo | OK | Figura 3 (sección 5) |
| Tabla de decisiones arquitectónicas ≥5 | OK | ADR-01 a ADR-06 + D-11–D-13 registrados (sección 6 y 8) |
| Mapa de dependencias | OK | Figura 4 y habilitadores F-01, E-1–E-10 (sección 7) |
| Consolidación de semanas 1–5 en un único documento | OK | Sección 2 y contenido integral |
| Diagramas legibles con leyenda y PNG incrustado en DOCX | OK | 4 imágenes en el DOCX, con leyenda y cobertura >30 % |
| Tecnología sin función definida no adoptada | OK | "Fuera del alcance v0.1" explícito (sección 5.2) |
| Registro de decisiones versionado y trazabilidad | OK | Secciones 6, 8 y nota de reconciliación D-06–D-08 |
| Fuentes verificables | OK | Referencias con niveles (ISO/IEC/IEEE 42010, NIST SP 800-218 r1, Kruchten et al., DORA, Thoughtworks, AACE) |

## Generación (reproducible)

```bash
python3 arquitectura/generar_diagramas.py
python3 arquitectura/render_diagramas.py
python3 documentos/proyecto/md_to_docx.py documentos/proyecto/Semana5_Hito_I.md entregas/semana-05/TISG_E01_S05_ProyectoIntegrador_2026-10-09.docx
```

Los diagramas se verificaron con cobertura de píxeles ≥30 % en cada PNG, por lo que cumplen el requisito de contenido no blanco. El render utiliza Google Chrome headless (Windows).

## Regla del Hito I

Este documento es una fotografía hasta la semana 5. Las correcciones posteriores deberán registrarse y justificarse en el registro de decisiones. La elección de componentes se ajusta a proporcionalidad y no a moda tecnológica.

---

El equipo confirma que el presente documento consolida los avances de las semanas 1–4 sin alterarlos y cumple todos los requisitos de la Semana 5 para el Hito I.
