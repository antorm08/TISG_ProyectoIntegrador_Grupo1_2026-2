# Contrato funcional POC-02 v1.0

Grupo 1 · UNMSM · TISG · S6 · 26/10/2026. Diseño académico, aprobación humana pendiente.
Este contrato se escribe antes de la implementación. No implementa presupuestos/APU.

## Interfaz y estado

Python 3.12, biblioteca estándar. API `validar(costos: Path, metrados: Path) -> dict`.
CLI desde la raíz: `python -X utf8 -B poc/POC-02-ai-native-sdlc/src/validador.py --costos <csv> --metrados <csv>`.
No existe opción de escritura. JSON UTF-8 por stdout: `version_contrato`, `estado`,
`archivos` (filas leídas por archivo lógico) y `errores`. Cada error contiene
`archivo` (costos/metrados), `fila`, `campo`, `codigo`, `mensaje`.
Estado VALIDO solo con cero errores y ambos archivos con datos. Salida de proceso:
0 válido, 1 inválido, 2 argumentos CLI incorrectos (argparse).
Aceptación técnica del software no equivale a aprobación humana/empresarial.

## Reglas y códigos

| ID | Regla operativa | Códigos |
|---|---|---|
| RF-01 | CSV coma, UTF-8/UTF-8 BOM; cabeceras exactas, orden libre; obligatorias obra_id,partida_id y costo_real/cantidad. Columnas extra únicas permitidas. No corregir cabeceras silenciosamente. | E_COLUMNA_FALTANTE, E_CABECERA_DUPLICADA |
| RF-02 | IDs tras strip no vacíos, máximo 128 caracteres y sin controles U+0000–001F. Comparación distingue mayúsculas. Normalización solo en memoria. | E_ID_VACIO, E_ID_FORMATO |
| RF-03 | Decimal ASCII con signo opcional, punto y exponente opcional; strip externo; máximo 128 caracteres. No separadores de miles, coma decimal ni guiones bajos. Decimal finito, sin conversión a float. | E_NUMERO_FORMATO, E_NUMERO_NO_FINITO |
| RF-04 | Valor decimal estrictamente >0; cero, -0 y negativos inválidos. Valores finitos muy grandes/pequeños admitidos sin cuantizar. No se imponen tarifas/moneda inexistentes. | E_NO_POSITIVO |
| RF-05 | Duplicado de clave normalizada por archivo: un diagnóstico por repetición posterior, citando fila de primera aparición. | E_CLAVE_DUPLICADA |
| RF-06 | Si ambos archivos tienen estructura legible, cada clave con IDs válidos debe aparecer en ambos. Claves de filas con número inválido sí cuentan para correspondencia; evita errores de relación en cascada. | E_SIN_METRADO, E_SIN_COSTO |
| RF-07 | Archivo regular no symlink; máximo 1 MiB leído. Vacío o solo whitespace inválido; solo cabecera inválido. Filas con diferente cantidad de campos o campos >4096 caracteres inválidas; CSV estricto y decodificación estricta. | E_LECTURA, E_ARCHIVO_TIPO, E_LIMITE, E_ARCHIVO_VACIO, E_SIN_FILAS, E_FILA_ESTRUCTURA, E_CSV, E_CODIFICACION |
| RF-08 | Diagnósticos ordenados por costos antes que metrados, fila, campo, código y mensaje. Sin rutas absolutas, reloj o excepciones del sistema en el JSON. Fila 0 para fallo de archivo/cabecera; registro CSV usa número de línea física final del reader. | Todos |
| RF-09 | Abrir entradas solo para lectura. No escribir resultados, no consultar ERP/red, no leer catálogo, verdad futura o resultados POC-01. Evidencias las escribe un runner separado solo en una ejecución nueva. | Comprobación de hashes y efectos |
| RF-10 | Todo error invalida la pareja; datos estructuralmente inválidos no producen correspondencias artificiales. Filas inválidas no se excluyen para declarar éxito. | estado INVALIDO |

Para RF-06, cabecera/fila ilegible, tamaño, decodificación, ausencia, CSV malformado
o ausencia de datos deshabilita correspondencias para la pareja; los errores de
ID/número/duplicado no deshabilitan la estructura del archivo completo. Líneas
vacías interiores son filas estructuralmente inválidas. Mensajes fijos en español;
no reproducir valores potencialmente sensibles. No es un parser CSV universal ni
un servicio endurecido contra entradas hostiles; límites son decisiones locales.

## Aceptación y evaluación

Casos públicos en `pruebas/casos.json`, esperados congelados antes del código.
Se evalúa estado, conjunto/multiplicidad de códigos y estructura; pruebas técnicas
adicionales verifican orden, mensajes, salida CLI, inmutabilidad y originales.
Todos los casos y pruebas deben pasar para aceptación técnica de esta versión.
No es garantía fuera de los casos ni evaluación independiente: el mismo asistente
conoce contrato, casos e implementación. No hay casos ocultos ni comparación manual.
