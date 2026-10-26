# Registro S6 v0.1 — decisiones y contribuciones

Fecha: 26/10/2026. Grupo 1. **BORRADOR — pendiente de revisión humana**.
Registro separado; no modifica el XLSX ni las decisiones históricas D-01–D-22.

| ID | Decisión nueva y motivo | Evidencia / efecto |
|---|---|---|
| S6-D01 | Validador pequeño previo a staging; conservar CodeIgniter/MySQL | Contrato POC-02; concreta ADR-03/04/06 sin integración productiva |
| S6-D02 | Sin brazo manual por instrucción expresa; no contrastar ahorro | PROTOCOLO v1.0; hipótesis funcional H-S6-F, productividad ND |
| S6-D03 | Casos públicos congelados antes del código; mismo asistente genera ambos | congelacion_previa.json; evaluación no ciega/no independiente |
| S6-D04 | Decimal y límites locales explícitos; diagnósticos sin valores privados | src/validador.py; contrato v1.0; no se deduce validez económica |
| S6-D05 | Preservar primera versión y corrida exclusiva | primera_version/ y resultados/S6-001/; 48 pruebas sin correcciones |
| S6-D06 | Exportar solo borradores; revisión humana bloquea aprobación | revision_humana.md; PDF/DOCX no son entrega aprobada |
| S6-D07 | APU diferido: requiere modelo/unidades/recursos/tarifas autorizados | Informe §21; no inventar columnas ni materiales |

## Contribuciones efectivamente observadas

| Actor | Actividad | Evidencia / límite |
|---|---|---|
| Usuario solicitante en la conversación | Definió alcance S6 integral sin comparación manual y restricciones | Extractos en prompts.md; no identifica revisión ni programación de integrante |
| Asistente OpenCode / GPT-6.1 Sol | Diseñó contrato/casos, generó código, ejecutó pruebas y redactó/exportó borradores | Archivos S6, primera versión, logs y manifiestos; no es autoría manual estudiantil |
| Anthony Romani | Aporte individual S6 no acreditado todavía | PENDIENTE de actividad/fecha/evidencia real |
| Max Astuhuaman | Aporte individual S6 no acreditado todavía | PENDIENTE de actividad/fecha/evidencia real |
| Guillermo Calle | Aporte individual S6 no acreditado todavía | PENDIENTE de actividad/fecha/evidencia real |
| Pablo Mendoza | Aporte individual S6 no acreditado todavía | PENDIENTE de actividad/fecha/evidencia real |

Los nombres proceden del Hito I v1.2; no se heredan responsabilidades S1 como aportes S6.
No hubo commits ni push del asistente. Fecha/hash locales no constituyen firma,
custodia independiente ni cronometraje de participación humana.
