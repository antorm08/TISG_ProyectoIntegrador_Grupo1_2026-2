# Auditoría S6 v0.2 — BORRADOR

26/10/2026 · Grupo 1 · Revisión automatizada, no auditoría independiente ni aprobación.
Autoridad: guía oficial p. 8 (S6, 6 %), p. 3 (fuentes/aportes), pp. 14–15 (IA y responsabilidad).
Continúa el checklist v0.1 sin modificarlo. Controles de benchmark/edición son mejoras
solicitadas, no nuevos requisitos atribuidos al docente.

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| S6-01 Mapa SDLC actual | CUMPLE | Informe v0.2 §02 y Figura 1; distingue evidencia académica/empresa desconocida |
| S6-02 Oportunidades por fase | CUMPLE | §§02–03, requisitos a operación y documentación; beneficio potencial, no ahorro supuesto |
| S6-03 Autonomía/riesgo/revisión | CUMPLE | §03; escala propia A0–A3, roles y criterios; A2 sin aceptación humana completada |
| S6-04 PoC real | CUMPLE | Validador original, S6-001 y evaluaciones posteriores; no integración ERP |
| S6-05 Métricas significativas | CUMPLE | §§07–08; calidad por corpus, rendimiento y esfuerzo humano separados |
| S6-06 Errores/deuda/privacidad/dependencia | CUMPLE | §09; incluye defectos del evaluador y límites de inferencia |
| S6-07 Registro reproducible | CUMPLE | Ejemplo CLI auténtico, casos, logs, JSON, scripts exclusivos y manifiestos |
| S6-08 Entradas/salidas/modelo/prompts | PARCIAL | §06 y REGISTRO_REVISION.md; extractos, no conversación/sampling completos |
| S6-09 Evaluación humana real | PENDIENTE DE VALIDACIÓN HUMANA | REVISION_EQUIPO.md sin revisor, firma, intervalos o decisión inventados |
| S6-10 Comparación de productividad | NO VERIFICABLE | Sin Tmanual ni cronometraje completo; benchmark no satisface una comparación humana |
| S6-11 Fuentes y APA 7 | CUMPLE | §11; cuatro fuentes originales, NIST nivel 1; DORA solo resumen, METR complemento |
| S6-12 Hito/ADR/DT | CUMPLE | §04 y §09: ADR-03/04/06, DT-01/02/07/08; no cierre empresarial ficticio |
| S6-13 Identidad/fecha/versión | CUMPLE | Portada completa v0.2, 26/10/2026, Grupo 1, curso/docente e integrantes vigentes |
| S6-14 Contribuciones individuales | PENDIENTE DE VALIDACIÓN HUMANA | REGISTRO_REVISION.md separa usuario, asistente y sesión QA; estudiantes pendientes |
| S6-15 Aprobación de material IA | PENDIENTE DE VALIDACIÓN HUMANA | Todos los formatos BORRADOR; no se publica como versión aprobada |
| S6-16 Calidad documental | PARCIAL | PDF renderizado e inspeccionado página a página; DOCX estructura, sin render Word |
| S6-17 Conservación | CUMPLE | integridad_antes.json y comprobación final; 220 archivos iniciales preservados byte a byte |
| S6-18 Congelación y primera versión | CUMPLE | S6-001 intacta; casos/runner S6-002 congelados; corrección de arnés en revisión nueva |
| S6-19 Independencia | PARCIAL | Sesión QA con contexto separado, mismo filesystem/proveedor; no ciega ni totalmente independiente |
| S6-20 APU futuro | CUMPLE | §10; recursos/unidades/tarifas propuestos, no motor ni precios inventados |
| S6-21 Casos adicionales | CUMPLE | evaluacion_v02 y revisión de arnés; fallos S6-002 conservados, nueva ejecución identificada |
| S6-22 Benchmark repetido | CUMPLE | S6-BENCH-002: parámetros, tiempos individuales, mediana/mín/máx y entorno |
| S6-23 Evidencia visible | CUMPLE | §06: CSV, comando real, stdout y extracto exacto de log; sin capturas simuladas |

Balance del checklist propio: 16 CUMPLE, 3 PARCIAL, 3 PENDIENTE DE VALIDACIÓN HUMANA,
1 NO VERIFICABLE. No es rúbrica oficial, calificación o porcentaje de aprobación.
La nueva evaluación no convierte errores de arnés en defectos del validador ni
reinterpreta retrospectivamente el 0/35 inicial como éxito.

## Verificaciones finales

El verificador nuevo de v0.2 es de solo lectura; comprueba preservación, congelaciones,
resultados, medianas, fidelidad de extractos, enlaces y estructura de PDF/DOCX. El
verificador general seguro se ejecuta por separado. Se conservan comandos, stdout,
stderr y exit codes en un destino nuevo. No se llama al verificador S6 v0.1 como si
su HEAD fijo describiera el nuevo commit base; se preserva como antecedente.

La inspección visual por IA se registra en REVISION_VISUAL_v0.2.md, con build ID y
páginas efectivamente abiertas. No sustituye la evaluación humana de exactitud,
legalidad, semántica empresarial o defensa oral. El escaneo de secretos usa patrones
acotados y revisión del contexto sintético; no certifica seguridad integral.

## Veredicto

Parte técnica/documental preparada para revisión final del equipo, no aprobada para
presentación académica. Pendientes auténticos: revisión y aceptación, contribuciones
individuales y comprobación visual DOCX con procesador de texto. Productividad laboral
y comparación manual/IA siguen NO DETERMINADAS.
