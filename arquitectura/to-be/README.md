# Arquitectura TO-BE

## Estado

Pendiente de definición. Este archivo conserva los principios y preguntas que deberán guiar el diseño. No constituye todavía una arquitectura aprobada.

## Objetivo

Diseñar una evolución proporcional del ERP que permita utilizar información histórica confiable para planificación, presupuestación, análisis de desviaciones y control económico, sin reemplazar completamente el sistema existente.

## Principios acordados

1. Evolucionar el ERP en lugar de reemplazarlo.
2. Priorizar calidad, trazabilidad y gobierno de datos.
3. Desacoplar la explotación analítica cuando la evidencia lo justifique.
4. Mantener revisión humana en decisiones económicas.
5. Incorporar seguridad desde el ciclo de desarrollo.
6. Seleccionar componentes proporcionales al volumen, valor y capacidad del equipo.
7. Probar las tecnologías de mayor incertidumbre antes de adoptarlas.

## Capacidades candidatas

| Capacidad | Estado en el Radar | Condición antes de incorporarla |
|---|---|---|
| APIs e integración | Adoptar | Identificar contratos, consumidores y mecanismos existentes |
| Gobierno y calidad de datos | Adoptar | Definir propietarios, reglas, metadatos y controles |
| BI y analítica operacional | Adoptar | Acordar indicadores y una línea base |
| Arquitectura analítica | Probar | Medir volumen, frecuencia, latencia y costo |
| Observabilidad | Probar | Identificar servicios y métricas críticas |
| IA generativa | Probar | Contar con datos validados, evaluación y revisión humana |
| RAG | Evaluar | Confirmar un problema documental que BI no resuelva |
| Arquitectura de eventos | Evaluar | Demostrar una necesidad cercana al tiempo real |
| Agentes autónomos | Esperar | Controles maduros, mínimo privilegio y evidencia suficiente |

## Preguntas de diseño

- ¿Qué datos deben permanecer en el ERP transaccional?
- ¿Qué históricos deben copiarse o transformarse para análisis?
- ¿Se necesita un data warehouse, un lakehouse o una alternativa más sencilla?
- ¿Qué indicadores permiten comparar presupuesto y ejecución?
- ¿Qué latencia es realmente necesaria?
- ¿Qué roles pueden acceder a información económica?
- ¿Cómo se auditarán cambios, consultas y respuestas de IA?
- ¿Cuánto costará construir, operar y mantener cada alternativa?

## Criterios para considerar el TO-BE definido

- [ ] AS-IS validado.
- [ ] Requisitos funcionales y no funcionales priorizados.
- [ ] Volumen, frecuencia y latencia medidos.
- [ ] Alternativas comparadas con criterios explícitos.
- [ ] Flujos y límites de confianza representados.
- [ ] Riesgos y controles relacionados.
- [ ] Costos y capacidades humanas considerados.
- [ ] Decisión arquitectónica registrada.
- [ ] Diagrama con título, leyenda, versión, fecha y elaboración propia.

