# Revisión 02 del arnés — S6-003

## Resultado real

**S6-003: 35/35 escenarios satisfactorios (100%)** bajo el oráculo revisado y
congelado antes de esta ejecución. **S6-002 permanece 0/35 bruto**, sin modificar
sus resultados, expectativas, código de evaluación, informe ni logs.

Se documentan **dos defectos del arnés**, **una iteración correctiva del arnés**
y **cero correcciones del validador**. No se demostraron defectos del validador
en estas ejecuciones. El resultado no es validación contractual absoluta.

| Medida | Resultado |
|---|---:|
| Escenarios | 35 |
| nvalidos: parejas de archivos declaradas VALIDO | 10 |
| ninvalidos: parejas declaradas INVALIDO | 25 |
| Válidos satisfactorios / tasa | 10/10 — 100% |
| Inválidos satisfactorios / tasa | 25/25 — 100% |
| Total satisfactorio / tasa | 35/35 — 100% |
| Determinismo entre tres seeds | 35/35 — 100% |
| Procesos de escenarios | 105 = 35 × 3 |
| Exit 0 / exit 1 en escenarios | 30 / 75 |
| Controles de argumentos CLI, exit 2 | 3/3 |
| Control symlink, exit 1 | 1/1 PASS |
| Total procesos del validador | 109 = 105 + 3 + 1 |
| Originales, entradas y evidencia previa alterados | 0 |

`nvalidos` y `ninvalidos` cuentan escenarios/parejas, no filas CSV ni procesos.
Los 25 inválidos se rechazan correctamente; no son 25 pruebas fallidas.

## Corrección acotada y trazabilidad

* **EV-01:** el primer arnés exigía contadores planos en `archivos`, forma no
  impuesta por el contrato. El nuevo chequeo verifica la API histórica conocida:
  `archivos.costos.filas` y `archivos.metrados.filas`, enteros no negativos
  (excluye bool). No prohíbe metadatos adicionales ni exige enteros planos.
* **EV-02:** A20 tenía esperada la fila física 5, pero la cabecera ocupa la línea
  1, el primer registro las líneas 2–3 y el segundo la línea 4. Solo se cambió
  esa ubicación a **4** y su texto explicativo. `preparar.py` comprueba que
  todos los demás casos y expectativas sean idénticos a los originales.

El nuevo `runner.py` contiene el chequeo corregido completo, aplicado **antes**
de ejecutar los casos; no descarta fallos ni reclasifica resultados después.
Para evitar duplicar infraestructura reutiliza, mediante importación local, las
funciones del runner histórico: generación de entradas, subprocess, seeds,
logs, hashes, directorio nuevo obligatorio y controles adicionales. Ese archivo
histórico es una dependencia congelada por SHA256 y permanece intacto.
**No se importa el validador:** se ejecuta su CLI original con Python `-X utf8 -B`.

Las verificaciones de códigos/multiplicidades, estado, exit code, stderr, orden,
ubicaciones, primera aparición de duplicados, rutas y efectos locales se
mantienen. Se conserva rechazo de IDs existentes mediante `mkdir(exist_ok=False)`.
No se ejecutó una prueba adicional del rechazo en esta revisión; el control ya
está probado en S6-002 y el mecanismo reutilizado no cambió.

## Congelación e integridad

La congelación nueva se creó a las **2026-10-26T17:35:12.052804+00:00**, antes
de reejecutar. Incluye **345 hashes**: archivos nuevos ejecutables/declarativos,
dependencia histórica, fuente original, contrato/suite y todos los archivos
previos de `evaluacion_v02/` y `resultados/S6-002/` existentes al congelar.
Se verifican antes de importar el arnés histórico y después de la ejecución.
Todos permanecieron iguales. El README nuevo se redactó después y no forma
parte de esa congelación previa.

Fuente evaluada, idéntica a S6-002 (`src/validador.py`), SHA256:

```text
38e9bdaac54ecf76d92969ff931c1b43cee03556528da8c88f7bf9c161c67e85
```

Nueva `congelacion.json`, SHA256:

```text
859a55ca954375767be506d0f8ecf72921ebcfc32b58064d577f4bc96303ccb5
```

Ejecución en Python **3.12.10**, Windows AMD64:

* Inicio: **2026-10-26T17:35:22.052667+00:00**.
* Fin: **2026-10-26T17:35:40.663629+00:00**.
* Suma observada de subprocess de escenarios: **16.6092709 s**.
* Seeds: `1`, `987654321`, `random`; stdout, stderr y exit idénticos por caso.
* Runner: **exit 0**. No quedan procesos activos de esta evaluación.

Son tiempos operativos de esta ejecución, no un benchmark. No se realizaron
ejecuciones adicionales después del resultado para dejar libre el entorno.

## Ambigüedades y límites preservados

* **A15:** se mantiene el rango congelado 0–1 para E_CLAVE_DUPLICADA en claves
  con IDs inválidos. Se observó **0**. No se convierte esa elección en defecto.
* **A28:** se mantiene la exigencia de entrada inválida y ausencia de cascada
  relacional, con códigos alternativos de RF-07 explícitamente admitidos por
  el oráculo original. Se observó **E_FILA_ESTRUCTURA ×1**.

Por tanto, 35/35 incluye **dos casos con oráculos parcialmente ambiguos**, no
35 expectativas de código totalmente inequívocas. No se ampliaron ni relajaron
sus intervalos al revisar. Las fronteras 128/129 caracteres, 4096/4097 caracteres,
1048576/1048577 bytes, Unicode, CSV multilínea y correspondencias son las mismas
que en S6-002, salvo la ubicación errónea de A20.

Esta evaluación es **posterior, con fuente conocida, no ciega**. Modelo declarado
**GPT-6.1 Sol**, proveedor **openai**, herramienta **OpenCode**; contexto separado,
sin aislamiento material ni independencia total. Los hashes prueban igualdad
en puntos muestreados, no ausencia de escrituras transitorias. No hay trazado
de syscalls/red ni prueba exhaustiva de RF-09; los límites de observación del
informe inicial siguen aplicando. No se ejecutó la suite pública ni se afirma
garantía fuera de estos casos.

## Archivos y formatos

En `evaluacion_v02/revision-02/`:

* `casos.json`: 35 entradas declarativas, RF, motivos y expectativas.
* `runner.py`: chequeo corregido e infraestructura histórica hash-pinned.
* `preparar.py`: creación exclusiva de casos corregidos y congelación.
* `congelacion.json`: UTC, procedencia, delta autorizado y mapa SHA256.
* `README.md`: este informe nuevo.

En `resultados/S6-003/`:

* `resumen.json`: métricas, tasas, control totals, resultados y hashes.
* `A*/resultado.json`: controles por caso y tres respuestas JSON auténticas,
  comandos, seed, returncode, tiempo y hashes stdout/stderr.
* `A*/seed-*.stdout.log`, `seed-*.stderr.log`: bytes auténticos sin reconstruir.
* `A*/costos.csv`, `metrados.csv`: entradas; A34 usa un directorio como entrada.
* `originales_antes.json`, `originales_despues.json`, `entradas_sha256.json`.
* `congelacion_copia.json`, `cli_argumentos.json`, `cli-2-*.log`,
  `symlink.json` y logs del control symlink.

No se añade postanálisis correctivo de resultados en esta revisión: el resultado
35/35 procede del runner corregido y congelado antes de ejecutar.

## Reproducción

Desde la raíz, **con un ID nuevo autorizado**:

```powershell
python -X utf8 -B poc/POC-02-ai-native-sdlc/evaluacion_v02/revision-02/runner.py --id S6-003-REPRO-01
```

No repetir `preparar.py` sobre esta entrega: crea archivos con modo exclusivo y
rechaza sobrescribir. Tampoco repetir ID S6-003. La reproducción comprueba los
345 hashes congelados y requiere conservar las dependencias/evidencias previas.
No necesita instalaciones. Esta tarea solo ejecutó S6-003; no creó otros IDs.
No se modificaron archivos previos, implementación, documentación principal,
PDF, benchmark ni evidencias generales; no hubo instalaciones, commits o push.
