# Evaluación contractual adicional S6 v0.2

## Resultado y advertencia principal

Se diseñaron **35 escenarios nuevos** derivados de RF-01–RF-10 y se ejecutaron
contra el validador original mediante **109 procesos reales**. No se modificaron
el código, contrato, suite pública ni resultados previos. No se leyó ni ejecutó
POC-01. Todos los archivos de este trabajo son nuevos y están en esta carpeta o
en `../resultados/S6-002/`.

**El resultado automatizado congelado es 0/35 y salida 1; no ocultarlo ni
presentarlo como aceptación técnica satisfactoria.** Dos errores del evaluador
explican todos esos fallos:

* **EV-01 (35/35):** `runner.py` exige contadores planos en `archivos`. El contrato
  solo pide filas leídas por archivo lógico, y la implementación devuelve
  `{"costos":{"filas":n},"metrados":{"filas":n}}`, que no contradice ese texto.
* **EV-02 (A20):** la expectativa congelada dice fila 5, pero el segundo registro
  está en la línea física 4. La salida original, fila 4, es correcta. Cabecera
  línea 1, primer registro líneas 2–3, segundo registro línea 4.

Se conservaron sin cambios el runner, los casos, la congelación, `resumen.json`
y cada resultado/log original. `postanalisis.py` crea una auditoría **posterior**,
sin ejecutar nuevamente el validador ni reescribir evidencias. Descontando
explícitamente EV-01/EV-02, los **35 escenarios no muestran defectos del
validador** en los controles ejecutados. Esto NO es un nuevo 35/35 precongelado
ni autoriza declarar aceptación contractual completa.

## Procedencia y secuencia verificable

Modelo declarado: **GPT-6.1 Sol**, proveedor **openai**, herramienta **OpenCode**.
Es una sesión con contexto separado del principal, pero mismo
modelo/proveedor/herramienta y sin aislamiento material. No se afirma ceguera
ni independencia total.

1. Se leyeron únicamente `../CONTRATO.md` y `../pruebas/casos.json` como fuentes
   del proyecto antes del diseño; no se consultó `src/validador.py`.
2. Se añadieron `casos.json`, `runner.py` y `congelar.py`. Cada caso contiene RF,
   motivación, entradas declarativas y códigos/multiplicidades esperados.
3. `congelar.py` creó exclusivamente `congelacion.json` a las
   **2026-10-26T17:26:21.347593+00:00**, con SHA256 de esos tres archivos,
   contrato y casos públicos. Fue anterior a cualquier ejecución/lectura de
   la implementación. La congelación es evidencia local, no sello externo.
4. El runner ejecutó el original desde **17:26:28.331769Z** hasta
   **17:26:46.177995Z**, en Python **3.12.10**, Windows AMD64.
5. Solo tras finalizar se leyeron resultados y fuente para diagnosticar los
   fallos. El postanálisis quedó fechado **17:28:43.065918Z**.

SHA256 de la fuente evaluada (`../src/validador.py`):

```text
38e9bdaac54ecf76d92969ff931c1b43cee03556528da8c88f7bf9c161c67e85
```

SHA256 de `congelacion.json`:

```text
6a4016079f4a1c7c3371f9fd46debf936dd53540603b0a44ac641fcf815b8275
```

## Escenarios y oráculos

`casos.json` es la fuente completa de expectativas **anteriores a ejecutar**.
No se repiten los 36 casos públicos como nuevos casos. Se amplían fronteras,
interacciones y formatos, aunque necesariamente se reutilizan reglas ya
cubiertas en ejemplos simples. En la tabla, `×n` indica multiplicidad; donde
no se indica, es una aparición. Todos los errores implican INVALIDO/exit 1;
los casos sin errores requieren VALIDO/exit 0.

| ID | Derivación / expectativa congelada |
|---|---|
| A01 | RF-02: ambos IDs de 128 caracteres, válido. |
| A02 | RF-02/06: ID de 129, E_ID_FORMATO + E_SIN_COSTO. |
| A03 | RF-02/03: ID de 128 después de strip y número con whitespace, válido. |
| A04 | RF-02/06: tab interior, E_ID_FORMATO + E_SIN_COSTO. |
| A05 | RF-02: DEL U+007F fuera del rango prohibido explícito, válido. |
| A06 | RF-02/06: caja distinta, E_SIN_METRADO + E_SIN_COSTO. |
| A07 | RF-02/06: Unicode NFC/NFD no se equipara, ambas relaciones ausentes. |
| A08 | RF-03/04: número de 128 caracteres, válido. |
| A09 | RF-03/06: número de 129, E_NUMERO_FORMATO sin cascada relacional. |
| A10 | RF-03: dígitos árabes/fullwidth, E_NUMERO_FORMATO ×2. |
| A11 | RF-03/04: `.5`, `1.`, `+.25`, exponentes ±999999999, válido. |
| A12 | RF-04: -0E999, +0.0, negativo pequeño, E_NO_POSITIVO ×3. |
| A13 | RF-03: miles por espacio, hex, exponente incompleto, menos Unicode: E_NUMERO_FORMATO ×4. |
| A14 | RF-03/04/05/06: E_CLAVE_DUPLICADA ×4 + E_NUMERO_FORMATO + E_NO_POSITIVO; cita primera fila 2. |
| A15 | RF-02/05/06: E_ID_VACIO ×2 + E_SIN_COSTO; duplicado de ID inválido ambiguo. |
| A16 | RF-03/06: E_NUMERO_FORMATO ×2 y ambas relaciones; números inválidos conservan claves. |
| A17 | RF-05/06: claves de tupla sin colisión por concatenación/separador, válido. |
| A18 | RF-01/07/08: columna extra multilínea LF/CRLF, comillas escapadas; E_NUMERO_FORMATO en fila 5. |
| A19 | RF-02/08: LF en ID, E_ID_FORMATO en fila física 3 + E_SIN_COSTO. |
| A20 | RF-06/08: E_SIN_METRADO; fila congelada 5 es EV-02, fila correcta observada 4. |
| A21 | RF-01: BOM ambos archivos, CRLF, órdenes distintos, extra único, válido. |
| A22 | RF-01/10: cabecera extra duplicada, E_CABECERA_DUPLICADA, sin cascada. |
| A23 | RF-01/10: cabecera obligatoria con espacio, E_COLUMNA_FALTANTE. |
| A24 | RF-01: cabecera de metrados con caja distinta, E_COLUMNA_FALTANTE. |
| A25 | RF-07/10: línea vacía interior, E_FILA_ESTRUCTURA fila 3, sin relaciones. |
| A26 | RF-07/10: fila con campo sobrante, E_FILA_ESTRUCTURA, sin relaciones. |
| A27 | RF-07: extra de 4096 caracteres multibyte, válido. |
| A28 | RF-07/10: extra de 4097, INVALIDO sin relaciones; código específico ambiguo. |
| A29 | RF-07: exactamente 1048576 bytes ASCII, 300 claves distintas, válido. |
| A30 | RF-07/10: exactamente 1048577 bytes, E_LIMITE, sin relaciones. |
| A31 | RF-01/07: 1048576 bytes incluyendo BOM y multibyte, válido. |
| A32 | RF-07/10: comillas sin cierre tras fila legible, E_CSV, sin relaciones. |
| A33 | RF-07/10: byte UTF-8 inválido tras fila legible, E_CODIFICACION, sin relaciones. |
| A34 | RF-07: directorio en lugar de archivo, E_ARCHIVO_TIPO. |
| A35 | RF-02/03/05/06/08: E_NUMERO_FORMATO ×2, E_ID_VACIO ×2, E_CLAVE_DUPLICADA ×2, E_NO_POSITIVO y ambas relaciones; orden global. |

### Ambigüedades separadas de defectos

* **A15:** RF-05 no explicita si claves con IDs inválidos se deduplican.
  Se congeló un intervalo 0–1 para E_CLAVE_DUPLICADA; se observaron **0**.
  RF-06 sí exige conservar únicamente claves con IDs válidos para relaciones.
* **A28:** RF-07 lista códigos sin correspondencia individual inequívoca para
  campos mayores de 4096. Se exigió al menos un error y ninguna relación,
  admitiendo E_LIMITE/E_FILA_ESTRUCTURA/E_CSV en el oráculo exploratorio.
  Se observó **un E_FILA_ESTRUCTURA**.
* La forma exacta del contenedor `archivos` no está fijada en el contrato;
  EV-01 fue una suposición excesiva del evaluador, no un defecto del producto.

## Resultados técnicos auténticos

* 35 escenarios × 3 procesos con `PYTHONHASHSEED=1`, `987654321` y `random`:
  **105 procesos**, JSON/stdout/stderr/exit idénticos entre seeds por escenario.
* Salidas de escenarios: **30 procesos con exit 0**, **75 con exit 1**.
* Tres invocaciones de argumentos incorrectos: **exit 2**, stderr de argparse,
  sin objeto JSON de validación.
* Un proceso adicional con symlink real: **PASS**, E_ARCHIVO_TIPO/exit 1.
  El runner permite SKIP documentado si Windows deniega crear el enlace;
  en este entorno no fue necesario omitirlo.
* Los controles de códigos/multiplicidades, orden RF-08, estado, stderr vacío,
  ubicaciones salvo EV-02, y cita de primera fila de duplicados no reportaron
  otros fallos. Las comprobaciones de rutas absolutas no detectaron fugas.
* Suma de tiempos de los 105 procesos de escenarios: **16.1076912 s**;
  tiempo por escenario (tres procesos): **0.404815–0.724639 s**.
* Hashes originales antes/después idénticos: contrato y todos los archivos
  existentes en `src/` y `pruebas/`. Los hashes de entradas generadas tampoco
  cambiaron. El postanálisis volvió a verificar ambos y los archivos congelados.
* Reutilizar `--id S6-002` fue rechazado con FileExistsError/exit 1 antes de
  ejecutar el validador; snapshot completo de evidencias existentes idéntico.
  Los logs de este rechazo son nuevos y están separados.

## Evidencias y reproducción

Desde la raíz del repositorio:

```powershell
# En una copia inicial sin congelación, una sola vez y antes de inspeccionar src:
python -X utf8 -B poc/POC-02-ai-native-sdlc/evaluacion_v02/congelar.py

# En esta entrega ya existe la congelación: NO repetir el comando anterior.
# Reproducir la evaluación con un ID NUEVO aprobado por la sesión principal:
python -X utf8 -B poc/POC-02-ai-native-sdlc/evaluacion_v02/runner.py --id S6-002-REPRO-01
```

El runner congelado sigue conteniendo EV-01/EV-02 a propósito: una reproducción
debe reproducir también su salida 1. No se han ejecutado IDs adicionales ni
escrito otras carpetas de resultados en esta tarea. `congelar.py` y el runner
se niegan a sobrescribir sus destinos. No se requieren instalaciones.

En `../resultados/S6-002/`:

* `resumen.json`: resultado bruto congelado, tiempos, versión Python y hashes.
* `A*/resultado.json`: resultado por caso y tres respuestas JSON completas.
* `A*/seed-*.stdout.log`, `seed-*.stderr.log`: bytes auténticos de cada proceso.
* `A*/costos.csv`, `metrados.csv`: entradas reproducibles; A34 usa directorio.
* `originales_antes.json`, `originales_despues.json`, `entradas_sha256.json`.
* `congelacion_copia.json`, `cli_argumentos.json`, `cli-2-*.log`, `symlink.json`.
* `postanalisis.json`: auditoría posterior y errores EV-01/EV-02, sin reescritura.
* `rechazo_id_existente.*.log`: prueba auténtica de rechazo de ID existente.

`postanalisis.py` está fuera de la congelación porque se escribió **después**
de observar los fallos. En esta entrega ya se ejecutó; repetirlo se niega a
sobrescribir. En una copia sin esos tres archivos adicionales puede producir
el mismo análisis de los logs originales (con nueva fecha).

## Limitaciones para la sesión principal

No hay defectos funcionales inequívocos del validador demostrados por estas
ejecuciones. Sí hay **dos defectos del evaluador**, que impiden usar el 0/35
bruto o el postanálisis como aceptación limpia. Si se necesita una aceptación
precongelada satisfactoria, corresponde una nueva revisión/ejecución autorizada,
sin borrar S6-002 ni cambiar retrospectivamente sus expectativas.

Hashes y snapshots prueban igualdad de contenido en los momentos muestreados,
no ausencia de escrituras transitorias. No se instrumentaron syscalls, red,
ERP, accesos externos, permisos ACL ni cambios fuera de carpetas monitorizadas;
no se afirma prueba exhaustiva de RF-09. No se ejecutó la suite pública, solo
se leyó para evitar duplicación. Las pruebas de mensajes comprueban estabilidad
entre procesos y ausencia de rutas observadas, no toda posible fuga sensible.
Los contadores solo se validan en tipo/esquema tras el postanálisis, no contra
un oráculo completo de filas en todos los fallos de lectura. Las cifras de
tiempo son observaciones locales, no benchmark. No se instalaron paquetes,
hicieron commits/push, ejecutaron scripts históricos, ni editaron documentación
principal, PDF o evidencias generales.
