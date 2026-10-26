# Auditoría S6 v0.1 — contra guía oficial

26/10/2026 · Grupo 1 · **BORRADOR / PENDIENTE DE VALIDACIÓN HUMANA**.
Auditoría por el mismo asistente que generó los artefactos: no independiente.
Autoridad: `proyectoIntegrador.pdf`, p. 8 (S6, peso 6 %), p. 3 (fuentes/aportes),
pp. 14–15 (uso de IA, evidencia y responsabilidad). El contrato añade controles
técnicos locales; no son obligaciones adicionales atribuidas al docente.

| ID / criterio | Estado | Evidencia y límite |
|---|---|---|
| S6-01 Mapa SDLC actual | CUMPLE | Informe §4; arquitectura/semana-06/mapa-sdlc.svg, PNG/PDF; distingue repositorio de empresa desconocida |
| S6-02 Oportunidades por fases | CUMPLE | Informe §§4–5: requisitos, diseño, código, pruebas, revisión, seguridad, integración, despliegue, mantenimiento y documentación |
| S6-03 Autonomía/riesgo/revisión | CUMPLE | Informe §6, escala A0–A3 propia, controles/roles/aceptación; A2 local con puerta humana pendiente |
| S6-04 PoC real asistida | CUMPLE | poc/POC-02-ai-native-sdlc/src/validador.py; resultados/S6-001/resultados.json y unittest.log |
| S6-05 Métricas de productividad/calidad | CUMPLE | Informe §§13–14 y PROTOCOLO; fórmulas/denominadores; esfuerzo humano y ahorro ND |
| S6-06 Errores/deuda/privacidad/dependencia | CUMPLE | Informe §§17–20; cero defectos detectados en corpus no equivale a ausencia universal |
| S6-07 Registro reproducible | CUMPLE | README PoC, runner --id exclusivo, casos JSON, copias iniciales, logs y manifiestos |
| S6-08 Entrada/salida/modelo/prompts | PARCIAL | Informe §§10–11, prompts.md y primera_version; extractos, no exportación íntegra de conversación/configuración de modelo |
| S6-09 Evaluación humana real | PENDIENTE DE VALIDACIÓN HUMANA | revision_humana.md sin resultados humanos, responsable/intervalos/decisión pendientes |
| S6-10 Comparación cuando posible | NO VERIFICABLE | Sin brazo manual por instrucción vigente; no compara productividad ni calidad antes/después inexistente |
| S6-11 Fuentes mínimas y APA 7 | CUMPLE | Informe §23 y fuentes/semana-06/VERIFICACION_FUENTES.md; 4 fuentes, NIST nivel 1; DORA solo página/resumen |
| S6-12 Trazabilidad Hito/ADR/DT | CUMPLE | Informe §§2 y 20; ADR-03/04/06, DT-01/02/07/08; no se declaran deudas empresariales cerradas |
| S6-13 Identidad/versión/fecha | CUMPLE | Portada del informe, BORRADOR v0.1, 26/10/2026, curso/Grupo 1/integrantes |
| S6-14 Aportes individuales auténticos | PENDIENTE DE VALIDACIÓN HUMANA | gestion/registros/Registro_Semana6_v0.1.md: separa usuario/asistente, no inventa programación de estudiantes |
| S6-15 Aprobación de contenido IA | PENDIENTE DE VALIDACIÓN HUMANA | Guía pp. 14–15; todos los formatos marcados borrador, sin aprobación/presentación automática |
| S6-16 Calidad PDF/DOCX | PARCIAL | PDF 8 páginas, render y revisión visual IA en REVISION_VISUAL_IA.md; DOCX estructura verificada, no render Word |
| S6-17 Conservación de históricos | CUMPLE | integridad_antes.json y verificación final; 169 archivos iguales, README cambia solo navegación autorizada |
| S6-18 Evidencias/contrato previos al código | CUMPLE | congelacion_previa.json con 5 SHA-256; primera_version/manifiesto.json antes de ejecutar suite |
| S6-19 Evaluación independiente | PARCIAL | Mismo autor IA, casos públicos; declarado no ciego/no independiente, revisión externa futura |
| S6-20 APU como futuro, no implementación | CUMPLE | Informe §21; sin tarifas/materiales inventados ni motor APU |

Balance de los 20 criterios: 13 CUMPLE, 3 PARCIAL, 3 PENDIENTE DE VALIDACIÓN HUMANA,
1 NO VERIFICABLE. Es un checklist propio trazado a la guía, no rúbrica oficial ni
calificación/porcentaje de aprobación. 100 % de casos técnicos no es 100 % académico.

## Comprobaciones finales

El verificador S6 es de solo lectura: `python -X utf8 -B documentos/proyecto/verificar_semana6.py`.
Comprueba hashes previos/congelados/primera versión/corrida/exportaciones, recomputa
métricas, revisa enlaces Markdown nuevos, estructura PDF/DOCX y patrones de secretos.
El verificador general seguro se ejecuta por separado; no se llama al generador o
verificador histórico con efectos. Logs finales se conservan con destino nuevo.

El primer intento del verificador general detectó el enlace a esta auditoría aún
no creada; fue un fallo de consolidación documental, no del validador ni retrabajo
de la PoC. Se conserva su diagnóstico en el registro final. La comprobación se
repite tras completar el paquete. No se alteran resultados S6-001.

## Veredicto

**Preparado técnicamente y documentado como borrador para revisión del equipo.**
No está aprobado para presentación final. Faltan revisión humana, aceptación y
aportes individuales acreditados; productividad comparativa no determinada.
