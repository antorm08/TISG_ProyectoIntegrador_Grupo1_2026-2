# Skills opcionales: procedimiento portable

26/10/2026. No publica la configuración local ni requiere instalar herramientas
para verificar el repositorio. Las copias existentes se conservan intactas e ignoradas.

| Skill | Fuente fijada | Licencia y alcance |
|---|---|---|
| pdf | `https://github.com/openai/skills`, commit `49f948faa9258a0c61caceaf225e179651397431`, `skills/.curated/pdf` | Apache-2.0; lectura/generación/revisión PDF, no render Office. |
| skill-creator | `https://github.com/anthropics/skills`, commit `dbd4588f9e1033efb41dad4bef2f7947c8993d44`, `skills/skill-creator` | Apache-2.0; no asumir disponibilidad de Claude CLI o evaluación portable a Windows. |

## Instalación futura, manual y revisada

1. Con autorización y conectividad, obtener exclusivamente esas rutas de los commits
   indicados desde sus repositorios oficiales. No ejecutar instaladores o scripts.
2. Leer `SKILL.md` y `LICENSE.txt`; comprobar procedencia antes de ejecutar ejemplos.
3. Copiar cada directorio completo a `.agents/skills/<id>/`, **solo si el destino no
   existe**. Si ya existe, revisar diferencias; no sobrescribir adaptaciones locales.
4. Conservar licencias y documentar cualquier modificación en `SKILL.md`. Adaptar
   temporales al equipo del integrante sin copiar rutas privadas del equipo de origen.
5. Para PDF, usar bibliotecas disponibles y PyMuPDF cuando exista; no instalar
   automáticamente Cairo, Poppler, OCR u Office. Las instrucciones locales deben
   impedir sobrescribir entregables o subir información a conversores externos.
6. Para skill-creator, no ejecutar evaluadores pagados, `claude -p`, helpers que
   terminen procesos ni iniciar servicios sin autorización. No son necesarios para S6.
7. Registrar fecha, commit, licencia, adaptaciones y hashes locales. Este procedimiento
   fija procedencia, pero no promete reproducción byte a byte de adaptaciones no publicadas.

`skills-lock.json` actual apunta a staging local y **no es una restauración portable**.
No se publica ni se utiliza como dependencia de las verificaciones. Una eventual
versión compartida de las adaptaciones requiere revisar/eliminar detalles personales
y aprobación del equipo. Tampoco se publica `.opencode/` automáticamente.

Este mantenimiento no descarga, reinstala, actualiza ni ejecuta ninguna skill.
