# Registro y matriz de riesgos

## Estado

Estructura inicial. En Semana 1 se identificaron riesgos y cautelas, pero todavía no se ha aprobado su probabilidad, impacto ni nivel residual.

## Escalas propuestas

- Probabilidad: 1 (rara) a 5 (casi segura).
- Impacto: 1 (menor) a 5 (crítico).
- Nivel inicial: probabilidad × impacto.
- Tratamiento: evitar, mitigar, transferir o aceptar.

La escala definitiva deberá aprobarse antes de evaluar formalmente los riesgos.

## Riesgos preliminares

| ID | Categoría | Riesgo | Consecuencia | Control candidato | P | I | Estado |
|---|---|---|---|---|---:|---:|---|
| R-01 | Datos | Históricos incompletos o inconsistentes | Indicadores y presupuestos poco confiables | Reglas de calidad, conciliación y linaje | — | — | Por evaluar |
| R-02 | Arquitectura | Diseñar una plataforma sobredimensionada | Mayor costo y dificultad de mantenimiento | PoC y comparación de alternativas simples | — | — | Por evaluar |
| R-03 | Rendimiento | Consultas analíticas afectan al ERP | Lentitud en procesos operativos | Medición, observabilidad y separación de cargas | — | — | Por evaluar |
| R-04 | Seguridad | Acceso indebido a información económica | Exposición o uso no autorizado | Acceso por roles, mínimo privilegio y auditoría | — | — | Por evaluar |
| R-05 | IA | Respuestas incorrectas o no sustentadas | Decisiones equivocadas | Evaluación, trazabilidad y revisión humana | — | — | Por evaluar |
| R-06 | IA | Prompt injection o fuga de datos | Exposición o ejecución no autorizada | Guardrails, aislamiento y validación de entradas | — | — | Por evaluar |
| R-07 | Gestión | Falta de capacidades del equipo | Dependencia externa o abandono | Capacitación y adopción gradual | — | — | Por evaluar |
| R-08 | Economía | Costos variables de cloud o IA | Presupuesto tecnológico impredecible | Límites, monitoreo y prácticas FinOps | — | — | Por evaluar |
| R-09 | Privacidad | Uso accidental de datos reales en una PoC | Incumplimiento y exposición empresarial | Datos sintéticos o anonimizados | — | — | Por evaluar |
| R-10 | Adopción | Indicadores no aceptados por usuarios | Bajo uso de la solución | Definiciones comunes y validación con stakeholders | — | — | Por evaluar |

## Campos para la matriz formal

Cada riesgo deberá registrar:

- Identificador y categoría.
- Evento, causa y consecuencia.
- Probabilidad e impacto inherentes.
- Nivel de riesgo.
- Tratamiento seleccionado.
- Controles existentes y propuestos.
- Responsable.
- Fecha de revisión.
- Riesgo residual.
- Evidencia o fuente relacionada.

## Reglas de actualización

- No eliminar riesgos cerrados; cambiar su estado y conservar la evidencia.
- Relacionar riesgos con decisiones, componentes y PoC.
- Revisar la matriz cuando cambie el Radar o la arquitectura.
- No afirmar que un control elimina completamente un riesgo sin evidencia.

