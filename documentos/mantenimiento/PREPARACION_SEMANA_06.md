# Mantenimiento mínimo y preparación de Semana 6

Fecha: 26/10/2026. Grupo 1. Documento operativo, **no entregable S6 ni revisión académica v1.3**.
Base de trabajo: `7f962facba3abc78c38921e656fadb6852c17fe4`.
Hito I vigente: [v1.2](../proyecto/Semana5_Hito_I_v1.2.md), **Pendiente de validación humana**.

## 1. Tres operaciones distintas

| Operación | Contrato para trabajo nuevo |
|---|---|
| verify | Solo lectura de entradas/artefactos; resultados por stdout y código de salida. No llamar generadores, modelos o pipelines. |
| generate | Identificador de ejecución nuevo; crear destino exclusivo y fallar si existe. Validar destinos antes de escribir; no usar rutas de entrega como área de trabajo. |
| publish | Tras revisión humana real, copiar solo archivos revisados a una versión nueva; comprobar hashes y registrar origen/fecha/revisor. Fallar si el destino existe. No aprobar mediante IA. |

Estas reglas **no cambian automáticamente el comportamiento de los scripts históricos**.
No se implementó un publicador ni se ejecutó una generación experimental. Para una futura
implementación: no añadir `--force`, no truncar archivos con `w` antes de comprobar el
destino, usar `mkdir(exist_ok=False)` para la ejecución y creación exclusiva `x`/`xb`.
Si la biblioteca necesita un nombre de archivo, generar dentro de ese directorio exclusivo.
Una validación fallida conserva salida/logs como ejecución fallida, nunca como entrega aprobada.

## 2. Matriz de scripts y efectos

Rutas en esta tabla relativas a la raíz. No ejecutar los comandos históricos sobre
el árbol preservado para “comprobar” el proyecto. No se refactorizan por riesgo de
alterar fuentes históricas; su lectura no equivale a una prueba de ejecución.

| Script / grupo | Tipo real | Escritura o dependencia | Acción segura |
|---|---|---|---|
| `arquitectura/generar_diagramas.py` | generate v1.1 | Sobrescribe SVG de `revision-v1.1/` | Conservar; no ejecutar para verificar. |
| `arquitectura/render_diagramas.py` | generate/export | Escribe PDF/PNG al lado del SVG; por defecto v1.1 | No confundir con verify; destinos ya publicados no son scratch. |
| `arquitectura/generar_revision_v12.py` | generate v1.2 | Figuras SVG/PNG/PDF y presentación S2 en rutas finales fijas | No ejecutar durante mantenimiento. |
| `arquitectura/figuras_a.py`, `figuras_b.py`, `figuras_revision.py`, `svg_lib.py` | Utilidades de generación | Construyen figuras; importadas por generadores | Conservar sus versiones; no cambiar para alterar silenciosamente revisiones anteriores. |
| `documentos/proyecto/artefactos_hito.py` | generate v1.1 | DOCX/PDF; Arial de Windows | No invocar como verificador. |
| `documentos/proyecto/generar_hito_v12.py` | generate v1.2 | DOCX/PDF, XLSX y complemento S2; destinos fijos | No ejecutado. Cambios futuros necesitan una revisión distinta y destino nuevo autorizado. |
| `documentos/proyecto/md_to_docx.py` | generate | Escribe el DOCX indicado sin protección general de sobrescritura | No apuntar a entregables conservados. |
| `gestion/registros/actualizar_registros_semana4.py` | generate histórico | Reconstruye XLSX S4; no preservador general de fórmulas/estilos | No ejecutar sobre libros históricos. |
| `gestion/registros/actualizar_registros_semana5.py` | generate v1.1 | Escribe libro S5 v1.1 | No usar para registros S6. |
| `poc/POC-01-estimacion-historicos/src/synthetic_erp_data.py` | generate histórico | Sobrescribe siete CSV de `datos/` | No ejecutar en el repositorio actual. |
| `poc/POC-01-estimacion-historicos/src/experimento_bi.py` | Experimento con escritura | Sobrescribe `resultados/resultados.csv` | No equivale al protocolo B0/M1 v1.2. |
| `poc/POC-01-estimacion-historicos/pruebas/verificar_poc.py` | generate + verify | Ejecuta los dos scripts anteriores | **No es solo lectura**. |
| `poc/POC-01-estimacion-historicos/pruebas/test_metricas.py` | Pruebas unitarias históricas | Importa funciones; Python puede crear caché sin `-B` | No necesario para mantenimiento; no ejecutado aquí. |
| `documentos/proyecto/verificar_hito.py` | Verificación histórica con escritura | Regenera PoC y escribe evidencias v1.1 | No ejecutar desde índices históricos para validar el estado actual. |
| `documentos/proyecto/verificar_hito_v12.py` | Verificación de aquella intervención | HEAD exacto antiguo y archivos locales; `--guardar` sobrescribe JSON antiguo | Conservado sin cambios. No sirve como verificador reusable ni como prueba de que un HEAD nuevo es histórico. |
| `documentos/proyecto/verificar_repositorio.py` | verify actual | Solo lectura; bibliotecas ya declaradas en `requirements-hito.txt` | Comando recomendado; no requiere `.git`, auditoría inicial ni skills. |
| `documentos/proyecto/inventario_repositorio.py` | verify / capture explícito | `verify` solo lee; `capture-*` crea un JSON nuevo con `x`, rechaza sobrescritura | Distingue blobs Git de bytes sin commit. No reinterpretar manifiestos antiguos. |
| `documentos/proyecto/test_mantenimiento.py` | Pruebas de herramientas | Solo fixtures temporales; no código experimental | Ejecutar con `-B`; no escribe entregables. |

Los scripts de skills son herramientas de terceros locales, no parte del pipeline
académico. No ejecutarlos para validar Hito I. Ver [política portable de skills](SKILLS_COMPARTIBLES.md).
No se instalaron dependencias. Las limitaciones Office/Arial y fuentes con contenido
codificado en Python permanecen documentadas: no hay regeneración portable garantizada.

## 3. Comprobación actual frente a fotografía histórica

Desde la raíz:

```powershell
python -X utf8 -B documentos/proyecto/verificar_repositorio.py
python -X utf8 -B documentos/proyecto/inventario_repositorio.py verify evidencias/mantenimiento-s06/fotografia_git_7f962fa.json
python -X utf8 -B documentos/proyecto/inventario_repositorio.py verify evidencias/mantenimiento-s06/inventario_actual.json
python -X utf8 -B documentos/proyecto/test_mantenimiento.py
```

- **Estado actual:** contenido/estructura y conservación respecto al inicio de este
  mantenimiento. No exige un HEAD histórico. Comprueba enlaces desde cada Markdown.
- **Fotografía Git:** el manifiesto nuevo de `7f962fa` registra sus blobs exactos y
  se comprueba contra ese commit, aunque HEAD avance. Necesita los objetos Git.
- **Inventario actual:** registra los bytes compartibles del árbol modificado, base
  Git, fecha y SHA-256. No afirma que esos cambios estén contenidos en el commit base.
  `verify` detecta diferencias en las rutas registradas; no certifica ausencia de
  archivos nuevos posteriores. Excluye su propio archivo para evitar autorreferencia.
- **Evidencia antigua:** inventarios y resultados v1.1/v1.2 no se sobrescriben. El
  verificador original v1.2 documenta una intervención anterior al commit v1.2, no
  una fotografía Git completa equivalente a cualquier HEAD posterior.

La conservación actual compara hashes de bytes originales. En una exportación Git
se acepta exclusivamente conversión LF/CRLF de archivos textuales, que se informa
por separado; binarios permanecen estrictos. Esto no cambia ningún hash antiguo ni
presenta normalización como igualdad binaria. La comprobación de blobs Git siempre
es exacta y no normaliza saltos de línea.

Guía canónica operativa: [proyectoIntegrador.pdf](../../proyectoIntegrador.pdf),
idéntica a la copia local ignorada `proyectoIntegrador (1).pdf` al iniciar esta tarea.
No se cambian sus citas en documentos académicos. La auditoría inicial y el diagnóstico
personal de skills permanecen locales/opcionales; no es necesario divulgarlos para
verificar desde una clonación limpia. La distribución de la auditoría inicial requiere
decisión del equipo, aunque se revisó su contenido y no se detectaron credenciales
evidentes. No se usa `git add -f`.

## 4. Ubicaciones futuras de Semana 6 — no creadas anticipadamente

La guía, p. 8, exige mapa del SDLC, oportunidades de IA, matriz tarea/autonomía/riesgo/
revisión, una PoC o comparación, métricas de productividad **y calidad**, riesgos,
entrada/salida y evaluación humana, y comparación controlada cuando sea posible.
No exige ERP completo, RAG ni ejecutar el experimento B0/M1 de S4.

| Contenido futuro | Ubicación propuesta, crear solo con contenido real |
|---|---|
| Informe S6 | `documentos/proyecto/Semana6_AI_Native_SDLC_v0.1.md` |
| Actividad asistida por IA | `poc/POC-02-ai-native-sdlc/README.md`, con objetivo, alcance y cómo reproducir |
| Prompts y entradas congeladas | `poc/POC-02-ai-native-sdlc/prompts.md` y `entradas/` |
| Código y pruebas | `poc/POC-02-ai-native-sdlc/src/` y `pruebas/`, solo si corresponden |
| Resultados, métricas y logs | `poc/POC-02-ai-native-sdlc/resultados/<id-ejecucion>/` exclusivo |
| Revisión humana y capturas pertinentes | `evidencias/semana-06/`, enlazada a ejecución/archivos exactos |
| Registro acumulativo nuevo | `gestion/registros/Registros_y_Radar_Semana6.xlsx` cuando haya actualizaciones reales; no escribir sobre S5 |
| Paquete publicado | `entregas/semana-06/`, con fuente, versión, fecha y manifiesto cuando se cierre |

En cada ejecución registrar: ID único, fecha, herramienta, proveedor/modelo declarado,
versión/configuración disponible, fuente/commit, entradas y prompts con hash, salida
original, pruebas, errores, tiempo total (incluye revisión/retrabajo), métricas y
limitaciones. No registrar tokens, credenciales ni conversaciones privadas completas.
La evaluación humana identifica revisor real, cambios aceptados/rechazados y motivo;
queda pendiente hasta realizarse. No inventar una línea base ni tiempos anteriores.

Conectar S6 mediante referencias a DT/ADR/componentes concretos del Hito I v1.2,
sin cambiar su fotografía. POC-02 no escribe ni importa resultados en `POC-01`.
No se implementó todavía actividad, prompt experimental, modelo ni resultado S6.

## 5. Git y pendientes de autorización

Estos cachés siguen versionados; no se retiraron ni borraron:

- `arquitectura/__pycache__/figuras_a.cpython-314.pyc`
- `arquitectura/__pycache__/figuras_b.cpython-314.pyc`
- `arquitectura/__pycache__/svg_lib.cpython-314.pyc`
- `gestion/registros/__pycache__/actualizar_registros_semana4.cpython-314.pyc`

Su futura retirada del seguimiento necesita autorización separada. `.gitignore`
no elimina archivos ya versionados. Los temporales Office y cachés ya están ignorados;
se añaden patrones acotados para `.env`/variantes y nombres de credenciales privadas,
permitiendo `.env.example` y `.env.template` sin valores reales. No se ignoran JSON,
PDF, XLSX, CSV o evidencias en general. Skills/configuración/lock siguen ignorados.

No hay reorganización masiva, renombrado de históricos, limpieza Git, commit o push.
Antes de incorporar estos cambios, el equipo debe revisar diff, alcance y evidencias.
