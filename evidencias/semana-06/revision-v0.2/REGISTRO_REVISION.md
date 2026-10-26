# Registro de revisión v0.1 → v0.2

26/10/2026 · Grupo 1 · OpenCode / GPT-6.1 Sol · BORRADOR.

## Base preservada

Inicio: rama `feat/semana-06-ai-native-sdlc`, árbol limpio, HEAD
`94955116f63b3ae28afc750ddc43145c8670254f` (v0.1 incorporada previamente por el usuario).
Esta intervención no realiza commits, push o staging. El inventario
`integridad_antes.json` captura SHA-256 de los 220 archivos versionados iniciales,
incluidos todos los artefactos S6 v0.1. Solo se añaden rutas nuevas; no se edita su README.

## Entrada del usuario y alcance

Solicitud de esta conversación: «SEMANA 6 — Evaluación adicional, mejora académica
y rediseño profesional del PDF». Extractos literales:

> Estos resultados deben permanecer intactos como evidencia histórica.

> No utilices los tiempos del benchmark como si fueran tiempos de desarrollo humano.

> Si puedes utilizar una sesión o agente de evaluación con contexto separado de la implementación, hazlo y documenta cómo se consiguió dicha separación.

> Mantén la versión como BORRADOR mientras no exista aceptación real.

Registro de extractos y contexto, no exportación íntegra de conversación. Herramienta
y modelo declarados; semilla, sampling, tokens y costo NO DETERMINADOS.

## Separación de tareas por sesión

Se lanzó un subagente general con contexto inicial fresco:
`ses_e86c54611ffe0SjiHvoug0z6CH`, encargado únicamente de nuevas pruebas contractuales
y S6-002. Instrucciones: leer contrato y corpus previo para evitar duplicaciones,
no leer fuente antes de congelar esperados, vincular cada expectativa a RF explícitas,
conservar fallos, no corregir implementación y escribir solo rutas nuevas de evaluación.
El proceso principal ya conoce la fuente y se ocupa del benchmark y documentación.

La sesión hija comparte filesystem, herramienta/proveedor y familia de modelo;
no hay custodio humano, permisos que oculten la fuente o evaluador materialmente
aislado. Por tanto se denomina **evaluación técnica automatizada adicional**,
con separación de contexto de trabajo, no evaluación ciega, humana o totalmente
independiente. Las fechas/hashes aportan trazabilidad local, no sello independiente.

## Cambios de la revisión

| Área | v0.1 preservada | v0.2 nueva |
|---|---|---|
| Evaluación | S6-001, 36 casos +12 controles | Casos posteriores derivados del contrato, congelación y S6-002 |
| Métricas | Una duración de suite y CLI | Benchmark repetido API/CLI/suite, observaciones y estadísticos |
| Evidencia | Rutas/logs y JSON | Ejemplo real de CSV, comando y respuesta visible en informe |
| Edición | PDF denso de 8 páginas | Portada, jerarquía, paleta marina/teal, figuras vectoriales y lectura por secciones |
| Análisis | Cumplimiento local | Distinguir productividad, revisión y rendimiento; amenazas de validez y deuda |
| Decisión | Revisión humana pendiente | Sigue pendiente; no se infiere aprobación del nuevo benchmark |

El conteo de páginas, casos, fallos y mediciones procede de los artefactos finales,
no se preasigna aquí. Si surgen defectos, el detalle de evaluación prevalece sobre
la primera aceptación acotada; nunca se reescribe S6-001 para ocultarlos.

Resultados finales: S6-002 conserva 0/35 bruto por EV-01/EV-02 del arnés; nueva
congelación y S6-003 alcanzan 35/35 según los oráculos revisados, incluidos dos
parcialmente ambiguos. Una iteración correctiva del arnés, cero correcciones del
validador. S6-BENCH-002 conserva 125 observaciones (120 API/CLI y cinco suites),
sin esfuerzo/ahorro humanos inferidos. Dos builds editoriales de 12 páginas;
editorial-02 corrige navegación y añade cita Python/fondos de extractos. La
inspección visual no detectó recortes. La v0.1 y los 220 archivos iniciales no se
editaron. Los informes del subagente preservan su propia secuencia y resultados.

## Contribuciones y responsabilidad

Usuario: define objetivos, solicita separación de sesión y autoriza esta revisión.
Asistente principal: benchmark, interpretación, informe, figuras, exportación e inspección.
Subagente QA: casos nuevos y evaluación automatizada posterior. Ninguna de esas tareas
se atribuye como programación manual de estudiantes. Anthony Romani, Max Astuhuaman,
Guillermo Calle y Pablo Mendoza: aportes individuales/revisión v0.2 pendientes de
evidencia real. No se heredan aportes S1 ni se inventan tiempos/firma/aceptación.
