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
- Versión vigente: Semana 5 — Hito I v1.1 corregido el 24/10/2026 (pendiente de aprobación humana)

> El equipo y los integrantes están identificados con sus datos reales.

## Descripción del caso

El proyecto analiza la evolución tecnológica del ecosistema ERP de una inmobiliaria-constructora peruana ficticia de tamaño mediano. El ERP registra obras, partidas de control, actividades, horas-hombre, metrados, materiales y costos, pero la información histórica todavía no se aprovecha de manera integrada para presupuestar nuevas obras y comparar lo previsto con lo ejecutado.

La propuesta no consiste en reemplazar el ERP. El equipo confirmó que es **propio, desarrollado en CodeIgniter y MySQL**; versiones, infraestructura y dotación no confirmadas. Las menciones de Odoo/PostgreSQL en el Hito I original fueron una caracterización incorrecta, corregida y conservada solo como antecedente histórico.

Se diseña una estrategia de adopción tecnológica 2026–2029 que evalúa integración, calidad de datos, BI, arquitectura analítica, IA supervisada, seguridad y operación de forma proporcional. El diagnóstico de madurez es **hipotético y académico**, no una entrevista o auditoría empresarial.

## Revisión vigente del Hito I

- [Paquete corregido PDF/DOCX v1.1](entregas/semana-05/revision-v1.1/README.md).
- [Documento fuente y consolidación de semanas 1–5](documentos/proyecto/Semana5_Hito_I_v1.1.md).
- [Registros consolidados v1.1](gestion/registros/Registros_y_Radar_Semana5_v1.1.xlsx).
- [Diagramas editables y exportados v1.1](arquitectura/revision-v1.1/).

Las entregas originales de semanas 1–5 permanecen intactas. La revisión no acredita entrega retroactiva, aprobación del equipo ni nuevas contribuciones individuales. Los anexos de S2/S3 se reconstruyen ahora desde el contenido histórico. No se inventan entrevistas ni resultados para cubrir pendientes.

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
| Technology Radar | v0.1, sin cambios de anillo; T5 en Probar | Evolucionar con evidencia; v1.0 final en S14 |
| AS-IS | ERP propio CodeIgniter/MySQL, diagramas v1.1 | Validar versiones, infraestructura y capacidades |
| TO-BE | v0.1 revisada, lotes y almacenamiento analítico separado | Medir y aprobar antes de implementar |
| Deuda técnica | DT-01 a DT-11; priorización cualitativa | Validar con responsables |
| ADR | ADR-01 a ADR-06 revisadas; D-01–D-16 reconciliadas | Aprobación humana pendiente |
| Mapa de dependencias | F-01, E-1–E-10 con criterios de avance | No es ruta crítica calculada |
| PoC | Escenario sintético favorable; H2/H3 pendientes | No inferir ahorro real ni significancia |

## Entregas

| Semana | Contenido | Versión | Estado |
|---|---|---:|---|
| 01 | Caso, Project Charter, Radar e Impact Canvas | Histórica | Archivos disponibles; cierre externo no verificado |
| 02 | Business Model Canvas y registro ampliado | v1.0 histórica | Archivos disponibles; correcciones integradas en Hito I v1.1 |
| 03 | Stakeholders, madurez y plan de adopción | v1.0 histórica | Diagnóstico aclarado como hipotético en v1.1 |
| 04 | Problema, propuesta de valor, hipótesis y PoC | v1.0 histórica | Límites metodológicos corregidos en v1.1 |
| 05 | Hito I revisado: ERP propio y TO-BE mínimo | v1.1 | PDF/DOCX, registros y diagramas; aprobación pendiente |
| 06–14 | Según cronograma del curso | — | Pendiente |

Consultar las respectivas carpetas en `entregas/` para ver el manifiesto de cada entrega.

## Reglas de trabajo

1. Cada integrante utilizará su propia cuenta de Git.
2. No se fabricarán commits, capturas, enlaces ni fechas.
3. Cada cambio relevante deberá relacionarse con una fuente, supuesto, decisión o experimento.
4. Las carpetas de trabajo pueden evolucionar; las carpetas dentro de `entregas/` no se modifican después del cierre.
5. Todo diagrama incluirá título, leyenda, fecha, versión y fuente o indicación de elaboración propia.
6. El Hito I es fotografía hasta la semana 5; las correcciones se registran con fecha real y sin sobrescribir históricos.
