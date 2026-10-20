# Proyecto Integrador — Tendencias en Ingeniería de Software y Gestión

## Datos generales

- Universidad: Universidad Nacional Mayor de San Marcos (UNMSM)
- Facultad: Facultad de Ingeniería de Sistemas e Informática
- Escuela: Ingeniería de Software
- Curso: Tendencias en Ingeniería de Software y Gestión
- Docente: Mg. PMP Yamil Quiñones Nieto
- Equipo: Grupo 1
- Periodo académico: 2026-2
- Caso: Estrategia de transformación tecnológica para el control y la planificación económica de obras
- Versión vigente: Semana 5 (Hito I)

> El equipo y los integrantes están identificados con sus datos reales.

## Descripción del caso

El proyecto analiza la evolución tecnológica del ecosistema ERP de una inmobiliaria-constructora peruana ficticia de tamaño mediano. El ERP registra obras, partidas de control, actividades, horas-hombre, metrados, materiales y costos, pero la información histórica todavía no se aprovecha de manera integrada para presupuestar nuevas obras y comparar lo previsto con lo ejecutado.

La propuesta no consiste en reemplazar el ERP. Se busca diseñar una estrategia de adopción tecnológica 2026–2029 que evalúe integración, calidad de datos, BI, arquitectura analítica, IA supervisada, seguridad y operación de forma progresiva y proporcional.

## Confidencialidad

El caso es académico, ficticio y realista, inspirado en un levantamiento funcional anonimizado. Este repositorio no debe contener:

- Credenciales, tokens, contraseñas o archivos `.env`.
- Nombres, documentos o información personal no autorizada.
- Montos, contratos, clientes o proveedores reales.
- Código fuente o configuraciones internas de la empresa de referencia.
- Capturas sin anonimizar del ERP.

Las pruebas futuras utilizarán información sintética, simulada o anonimizada.

## Integrantes y responsabilidades iniciales

| Integrante | Responsabilidad de Semana 1 | Evidencia principal |
|---|---|---|
| Anthony Romani | Caso, proceso AS-IS y supuestos | Documento, secciones 2, 3 y 8 |
| Max Astuhuaman | Investigación y verificación de fuentes | Documento, secciones 6.1, 9 y 11; hoja `Fuentes` |
| Guillermo Calle | Construcción del Technology Radar | SVG editable y hoja `Radar_Data` |
| Pablo | Project Charter, Impact Canvas y coherencia | Documento, secciones 4 y 7 |

La distribución identifica aportes principales, pero los cuatro integrantes son responsables de comprender y validar el entregable completo.

## Estructura del repositorio

- `documentos/`: documentos editables y materiales internos de apoyo.
- `arquitectura/`: documentación y diagramas AS-IS y TO-BE.
- `radar/`: fuente editable y exportaciones del Technology Radar.
- `gestion/`: decisiones, riesgos, supuestos y roadmap acumulativo.
- `fuentes/`: bibliografía y trazabilidad de evidencia por semana.
- `evidencias/`: contribuciones y pruebas de participación.
- `poc/`: experimentos y pruebas de concepto de semanas posteriores.
- `entregas/`: copia exacta e inmutable de cada entrega semanal.

## Estado de los artefactos acumulativos

| Artefacto | Estado en Semana 5 | Próxima acción |
|---|---|---|
| Technology Radar | v0.1 definido; evidencia consolidada | Actualizar a v1.0 tras pilotaje |
| AS-IS | Diagrama completado y con leyenda | Monitorear cambios operativos |
| TO-BE | v0.1 definido con capacidades acotadas | Validar con piloto y revisar alcance |
| Deuda técnica | DT-01 a DT-11 priorizadas | Ejecutar ruta crítica E-1–E-9 |
| ADR | ADR-01 a ADR-06 + D-11–D-13 | Mantener registro de revisiones |
| Mapa de dependencias | Definido (Figura 4) | Seguir orden mínimo |
| PoC | H1 validado sintéticamente (S4) | Alinearlo con capa analítica |

## Entregas

| Semana | Contenido | Versión | Estado |
|---|---|---:|---|
| 01 | Caso, Project Charter, Radar e Impact Canvas | v1.0 | Entregada |
| 02 | Business Model Canvas y registro ampliado | v1.0 | Entregada |
| 03 | Stakeholders, madurez y plan de adopción | v1.0 | Entregada |
| 04 | Problema, propuesta de valor, hipótesis y PoC | v1.0 | Entregada |
| 05 | Hito I: AS-IS / TO-BE v0.1 | v1.0 | Entregada |
| 06–14 | Según cronograma del curso | — | Pendiente |

Consultar las respectivas carpetas en `entregas/` para ver el manifiesto de cada entrega.

## Reglas de trabajo

1. Cada integrante utilizará su propia cuenta de Git.
2. No se fabricarán commits, capturas, enlaces ni fechas.
3. Cada cambio relevante deberá relacionarse con una fuente, supuesto, decisión o experimento.
4. Las carpetas de trabajo pueden evolucionar; las carpetas dentro de `entregas/` no se modifican después del cierre.
6. Todo diagrama incluirá título, leyenda, fecha, versión y fuente o indicación de elaboración propia.
7. El Hito I es fotografía hasta la semana 5; las correcciones se registran y justifican.
