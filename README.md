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
- Versión vigente: Semana 5 — Hito I v1.2, revisión académica del 25/10/2026 (**Pendiente de validación humana**)

> El equipo y los integrantes están identificados con sus datos reales.

## Descripción del caso

El proyecto analiza la evolución tecnológica del ecosistema ERP de una inmobiliaria-constructora peruana ficticia de tamaño mediano. El ERP registra obras, partidas de control, actividades, horas-hombre, metrados, materiales y costos, pero la información histórica todavía no se aprovecha de manera integrada para presupuestar nuevas obras y comparar lo previsto con lo ejecutado.

La propuesta no consiste en reemplazar el ERP. El equipo confirmó que es **propio, desarrollado en CodeIgniter y MySQL**; versiones, infraestructura y dotación no confirmadas. Las menciones de Odoo/PostgreSQL en el Hito I original fueron una caracterización incorrecta, corregida y conservada solo como antecedente histórico.

Se diseña una estrategia de adopción tecnológica 2026–2029 que evalúa integración, calidad de datos, BI, arquitectura analítica, IA supervisada, seguridad y operación de forma proporcional. El diagnóstico de madurez es **hipotético y académico**, no una entrevista o auditoría empresarial.

## Revisión vigente del Hito I

- [Guía oficial compartida](proyectoIntegrador.pdf): referencia canónica operativa; coincide por SHA-256 con la copia local `proyectoIntegrador (1).pdf`. Las citas históricas conservan su nombre original.
- [Guía de contribución](CONTRIBUTING.md), [índice actual de entregas S1–S5](entregas/INDICE_ACTUAL.md) y [mantenimiento/preparación S6](documentos/mantenimiento/PREPARACION_SEMANA_06.md).

- [Paquete vigente PDF/DOCX v1.2 y límites de validación](entregas/semana-05/revision-v1.2/README.md).
- [Documento fuente v1.2 y consolidación de semanas 1–5](documentos/proyecto/Semana5_Hito_I_v1.2.md).
- [Registros consolidados v1.2](gestion/registros/Registros_y_Radar_Semana5_v1.2.xlsx).
- [Diagramas editables y exportados v1.2](arquitectura/revision-v1.2/).
- [Presentación S2 corregida y fuentes editables](entregas/semana-02/revision-v1.2/README.md).
- [Nuevo diseño experimental: no ejecutado](poc/POC-01-estimacion-historicos/revision-v1.2/DISENO_EXPERIMENTAL.md).
- [Correcciones y pendientes](CORRECCIONES_ACADEMICAS_S01_S05_v1.2.md).
- [Auditoría posterior de los mismos 69 criterios](AUDITORIA_POST_CORRECCIONES_S01_S05_v1.2.md).
- [Verificación de fuentes](fuentes/revision-v1.2/VERIFICACION_FUENTES.md).
- [Revisión v1.1 conservada como antecedente](entregas/semana-05/revision-v1.1/README.md).

Las entregas originales de semanas 1–5 y la v1.1 permanecen intactas: son históricos, no versiones vigentes contradictorias. La revisión no acredita entrega retroactiva, aprobación del equipo ni nuevas contribuciones individuales. Los anexos reconstruidos en v1.1 se conservan con su procedencia; v1.2 añade instrumento, metodología y correcciones explícitas. No se inventan entrevistas ni resultados para cubrir pendientes.

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
| AS-IS | ERP propio CodeIgniter/MySQL, topología lógica y datos v1.2 | Validar supuestos; no confundir nodos lógicos con servidores reales |
| TO-BE | v0.1 revisada, lotes y almacenamiento analítico separado | Medir y aprobar antes de implementar |
| Deuda técnica | DT-01 a DT-11; priorización cualitativa | Validar con responsables |
| ADR | ADR-01 a ADR-06 precisadas; D-01–D-22 trazables | Validación humana pendiente |
| Mapa de dependencias | F-01, E-1–E-10 con criterios de avance | No es ruta crítica calculada |
| PoC | Resultado sintético anterior histórico; nuevo protocolo B0/M1 no ejecutado | Evaluación futura separada; H2/H3 pendientes; no inferir ahorro |

## Entregas

| Semana | Contenido | Versión | Estado |
|---|---|---:|---|
| [01](entregas/semana-01/) | Caso, Project Charter, Radar e Impact Canvas | Histórica | Archivos disponibles; cierre externo no verificado |
| [02](entregas/semana-02/) | Business Model Canvas y registro ampliado | v1.0 histórica + complemento v1.2 | Usar nueva presentación; cifras CAPECE no respaldadas retiradas del material vigente |
| [03](entregas/semana-03/) | Stakeholders, madurez y plan de adopción | v1.0 histórica + revisión v1.2 | Instrumento propio; ND donde falta sustento, no entrevistas simuladas |
| [04](entregas/semana-04/) | Problema, propuesta de valor, hipótesis y PoC | v1.0 histórica + diseño v1.2 | Baseline independiente diseñado; resultado histórico no se transfiere al nuevo método |
| [05](entregas/semana-05/revision-v1.2/) | Hito I revisado: ERP propio y TO-BE mínimo | v1.2 | PDF/DOCX, registros y diagramas; validación humana pendiente |
| 06–14 | Según cronograma del curso | — | Pendiente |

Consultar el [índice actual](entregas/INDICE_ACTUAL.md): complementa los manifiestos históricos sin modificarlos e identifica PDFs existentes y revisiones posteriores.

## Comprobación actual de solo lectura

```powershell
python -X utf8 -B documentos/proyecto/verificar_repositorio.py
python -X utf8 -B documentos/proyecto/inventario_repositorio.py verify evidencias/mantenimiento-s06/inventario_actual.json
```

El [verificador v1.2 original](documentos/proyecto/verificar_hito_v12.py) se conserva como herramienta histórica de aquella intervención, no como comando de comprobación actual. No requiere publicarse la auditoría inicial local para ejecutar el nuevo verificador. Su eventual distribución sigue pendiente de autorización del equipo; véase el [informe de mantenimiento](documentos/mantenimiento/INFORME_MANTENIMIENTO_S06.md).

## Reglas de trabajo

1. Cada integrante utilizará su propia cuenta de Git.
2. No se fabricarán commits, capturas, enlaces ni fechas.
3. Cada cambio relevante deberá relacionarse con una fuente, supuesto, decisión o experimento.
4. Las carpetas de trabajo pueden evolucionar; las carpetas dentro de `entregas/` no se modifican después del cierre.
5. Todo diagrama incluirá título, leyenda, fecha, versión y fuente o indicación de elaboración propia.
6. El Hito I es fotografía hasta la semana 5; las correcciones se registran con fecha real y sin sobrescribir históricos.
