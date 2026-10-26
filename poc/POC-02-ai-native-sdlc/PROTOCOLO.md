# POC-02 — Protocolo v1.0

UNMSM · FISI · TISG · Grupo 1 · S6 · 26/10/2026.
Estado: ejecución técnica asistida autorizada; revisión humana pendiente.

## Pregunta, hipótesis y alcance

¿Puede un agente de IA producir un validador pequeño que cumpla RF-01–RF-10 bajo
las pruebas especificadas? H-S6-F: la implementación cumple todos los casos de
aceptación y controles técnicos definidos; se rechaza técnicamente si falla alguno.
La decisión de uso empresarial permanece pendiente aun si pasa la suite.

No se contrasta una hipótesis causal de productividad: **no hay condición manual,
participantes medidos ni cronometraje humano**. No se calcula ahorro. Esta ejecución
es desarrollo generado por IA, iniciado por solicitud del usuario, bajo responsabilidad
académica futura del equipo; no evidencia de que un estudiante programó/revisó.

Se conserva el ERP. Validador previo a staging, vinculado a ADR-03/04/06,
DT-01/02/07/08. Costos/metrados son datos sintéticos existentes de solo lectura.
No acceder a `obra_nueva_real.csv`, catálogo generador ni al experimento histórico.
APU es trabajo futuro: no se inventan tarifas, recursos o materiales.

## Secuencia y congelación

1. Inspeccionar Git/guía y capturar integridad inicial de los 170 archivos previos.
2. Escribir contrato, casos públicos y este protocolo antes del código; registrar
   sus SHA-256 en `evidencias/semana-06/congelacion_previa.json`.
3. Implementar `src/validador.py`; preservar copia auténtica inicial antes de probar.
4. Runner nuevo con ID exclusivo: copia fuente/suite, verifica congelación, ejecuta
   unittest y CLI sobre originales, guarda logs reales y resultados estructurados.
5. Si aparecen errores, conservar corrida fallida; corregir y crear otro ID.
   No alterar expectativas para favorecer implementación sin enmienda explícita.
6. Calcular métricas de resultados; redactar borrador y revisión crítica. Revisar
   formatos e integridad. No publicar como aprobado ni fabricar validación humana.

Evaluación **no ciega y no independiente**: diseño y código por el mismo asistente.
Congelar esperados antes evita ajuste posterior, pero no elimina sesgo compartido.
La revisión independiente del equipo queda pendiente. No se ejecutan otros modelos
ni evaluadores pagados. Ninguna biblioteca adicional es necesaria para la PoC.

## Métricas y denominadores

| Métrica | Método/fórmula | Límite |
|---|---|---|
| M1 desarrollo hasta aceptación humana | NO DETERMINADO; no hay cronometraje humano completo ni aceptación humana | Duración de suite no es tiempo de desarrollo |
| M1-t ejecución automática | perf_counter alrededor de suite y CLI; segundos y UTC de inicio/fin | Una ejecución local, no benchmark ni ahorro |
| M2 revisión humana | NO DETERMINADO hasta revisión real | No confundir inspección IA con revisión de equipo |
| M3 retrabajo | Corridas fallidas que requieran cambio de implementación, registradas por ID | No inventar defectos ni contar redacción como fallo del validador |
| M4 diferencia manual/IA | NO DETERMINADO, sin Tmanual | No generar un brazo manual con IA |
| Q1 casos correctos | 100 × casos con estado/códigos/estructura esperados / casos ejecutados | Reportar unittest por separado; un test técnico no es otro conjunto de datos |
| Q2 falsas aceptaciones | Inválidos aceptados / inválidos evaluados, cantidad y porcentaje | Solo corpus público; no tasa poblacional |
| Q3 falsos rechazos | Válidos rechazados / válidos evaluados, cantidad y porcentaje | Casos sintéticos pequeños |
| Q4 requisitos | IDs RF con todas sus comprobaciones satisfechas /10 | Matriz explícita; no equivale a cumplimiento académico |
| Q5 defectos | Fallos confirmados con corrida, causa, impacto y corrección | Si no aparecen, declarar cero detectados en suite, no ausencia universal |

## Amenazas y controles

Caso único, modelo único y mismo autor/evaluador: sin inferencia estadística causal.
Datos ya conocidos y sintéticos: no prueba empresarial. Casos públicos: no generalizar
calidad. PythonDecimal y límites propios: declarar formatos soportados y rechazados.
Solo ejecución local, destinos exclusivos, sin secretos, red o producción. Un futuro
estudio humano requiere otro protocolo/entrada/ID; no retrofechar la presente corrida.

## Evidencia y estados

Entrada: solicitud del usuario en esta conversación, `prompts.md`, contrato y casos.
Salida inicial/final: copias reales en cada ejecución, con hashes. Herramienta:
OpenCode; modelo declarado GPT-6.1 Sol. Temperatura, semilla del modelo y tokens:
NO DETERMINADOS. No confundir con parámetros del generador histórico.

Estado técnico: se determina por la ejecución, nunca se prellena como aprobado.
Estado humano: PENDIENTE DE VALIDACIÓN HUMANA. Registros de contribución no asignan
automáticamente el código generado a ningún integrante.
