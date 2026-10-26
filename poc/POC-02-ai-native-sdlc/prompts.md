# Registro de instrucciones y contexto — POC-02

26/10/2026. Herramienta: OpenCode. Modelo declarado por el entorno: GPT-6.1 Sol.
No se invocó otra sesión/modelo. Desarrollo por el asistente en esta conversación,
no programación manual de un estudiante. Configuración de sampling/tokens desconocida.

## Entrada del usuario — extractos literales relevantes

Solicitud titulada «DESARROLLAR SEMANA 6 COMPLETA — AI-NATIVE SDLC», en esta conversación:

> Implementa mediante IA una pequeña herramienta Python capaz de validar datos sintéticos antes de que ingresen a un proceso analítico.

> No afirmes ahorro de tiempo frente a desarrollo manual, porque no realizaremos una línea base manual.

> Prioriza un evaluador independiente de la implementación. Si no puedes garantizar aislamiento entre desarrollo y evaluación, declara explícitamente esa limitación.

> Si la primera versión no presenta defectos, no inventes errores ni iteraciones.

> No sobrescribas el Hito I, los CSV históricos, sus resultados o los inventarios anteriores.

Este archivo preserva extractos, **no una transcripción íntegra/exportación de la sesión**.
La solicitud completa permanece en la conversación del usuario. No se afirma que un
prompt resumido haya sido enviado a una segunda API.

## Especificación operativa usada para generar la primera versión

Implementar el contrato `CONTRATO.md` v1.0 y atender RF-01–RF-10 del pedido. Leer
costos y metrados CSV UTF-8 estrictos, IDs normalizados solo en memoria, números
decimales finitos positivos, duplicados y correspondencia. Emitir JSON determinista,
códigos estables y salidas 0/1/2. No escribir entradas/resultados desde el validador.
Preparar casos antes de implementación y congelarlos. Ejecutar evaluación local
no ciega; conservar primera versión y cada corrida sin sobrescritura. No estimar
costos, construir APU, usar catálogo/verdad futura ni acceder al ERP.

Contexto consultado: guía compartida pp. 3–4/8/13–15, Hito I v1.2 §§2/6–11/13,
ADR-03/04/06, protocolo POC-01 v1.2 como documento de reglas, cabeceras y 35 filas
de cada CSV de costos/metrados, documentación y verificadores de mantenimiento.
También existe contexto previo de esta conversación: no se declara aislamiento.

## Salidas y correcciones

La primera salida de código y suite se preserva antes de la primera ejecución en
`evidencias/semana-06/primera_version/`. Cada corrida conserva otra copia de fuente,
suite/casos y manifiesto. Los resultados reales se registran en su JSON/log, no
en valores supuestos aquí. Las correcciones solo se atribuyen si existe un fallo
auténtico; el informe final debe distinguir defectos del validador y del arnés.
