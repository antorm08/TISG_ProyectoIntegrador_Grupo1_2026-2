# POC-02 — Validador de costos y metrados

**BORRADOR S6 · Pendiente de validación humana.** Python 3.12, sin dependencias
externas para validar y probar. No integra el ERP ni calcula presupuestos/APU.

## Reproducción desde la raíz

Validar los originales sintéticos (solo lectura):

```powershell
python -X utf8 -B poc/POC-02-ai-native-sdlc/src/validador.py --costos poc/POC-01-estimacion-historicos/datos/costos.csv --metrados poc/POC-01-estimacion-historicos/datos/metrados.csv
```

Repetir evaluación con **otro ID nuevo** (crea archivos solo en resultados/ID):

```powershell
python -X utf8 -B poc/POC-02-ai-native-sdlc/ejecutar_evaluacion.py --id S6-REPLICA-001
```

No reutilizar `S6-001`: el runner falla si existe. No ejecutar la suite directamente
sin POC02_TMP; el runner controla su ubicación. Los fixtures se materializan desde
JSON en un temporal dentro de la corrida y se eliminan al terminar cada test.
Los datos declarativos originales permanecen conservados en cada corrida.

## Evidencia auténtica

- [Contrato RF-01–RF-10](CONTRATO.md) y [protocolo](PROTOCOLO.md), congelados antes del código.
- [Casos públicos](pruebas/casos.json), [suite](pruebas/test_validador.py) y [prompts](prompts.md).
- [Primera versión real](../../evidencias/semana-06/primera_version/), preservada antes de probar.
- [Resultados S6-001](resultados/S6-001/resultados.json): 48/48 pruebas; 36/36 casos, 8 válidos y 28 inválidos.
- [Log real](resultados/S6-001/unittest.log), [salida sobre originales](resultados/S6-001/cli_stdout.json), [CSV](resultados/S6-001/casos.csv) y [hashes](resultados/S6-001/manifiesto.json).
- [Informe](../../documentos/proyecto/Semana6_AI_Native_SDLC_v0.1.md) y [revisión humana pendiente](../../evidencias/semana-06/revision_humana.md).

S6-001: cero fallos/errores, cero correcciones de implementación. No se ocultan
iteraciones fallidas: no hubo ninguna. Tiempo suite 1,448975 s, CLI 0,178095 s;
duraciones automáticas locales, **no tiempo de desarrollo ni ahorro humano**.
Evaluación pública no ciega/no independiente; mismo asistente diseñó y programó.
Sin baseline manual; productividad comparativa NO DETERMINADA. No se midió cobertura
de líneas/ramas. Hashes detectan cambios accidentales, no certifican autoría/fecha.

## Límites

Archivos regulares UTF-8 ≤1 MiB, campos ≤4096, ID/número ≤128 caracteres.
Decimal positivo, sin formato localizado. No valida unidades, monedas, catálogos,
veracidad económica ni coherencia con un presupuesto. No es un servicio expuesto a
entradas hostiles; no se garantiza resistencia a carreras de filesystem/enlaces.
`INVALIDO` y exit 1 significan datos rechazados; exit 2, uso CLI incorrecto.
