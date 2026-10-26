# Semana 6 v0.2 — paquete para revisión final

**BORRADOR — pendiente de revisión del equipo.** 26/10/2026 · Grupo 1.
La [v0.1](README.md) se conserva intacta; este índice no reemplaza sus evidencias.

## Informe

- [PDF editorial v0.2](TISG_E01_S06_AI_Native_SDLC_v0.2_BORRADOR.pdf).
- [DOCX editable v0.2](TISG_E01_S06_AI_Native_SDLC_v0.2_BORRADOR.docx).
- [Markdown fuente](../../documentos/proyecto/Semana6_AI_Native_SDLC_v0.2.md).
- [Figuras SVG/PDF/PNG nuevas](../../arquitectura/semana-06/revision-v0.2/).
- [Manifiesto del paquete](manifiesto_v0.2.json).

## Evaluación y mediciones

- [Evaluación inicial adicional](../../poc/POC-02-ai-native-sdlc/evaluacion_v02/README.md): S6-002 conserva 0/35 bruto por dos errores del arnés; no esconderlos.
- [Corrección identificada del arnés](../../poc/POC-02-ai-native-sdlc/evaluacion_v02/revision-02/README.md): nueva congelación y S6-003; sin cambiar el validador.
- [Benchmark técnico](../../poc/POC-02-ai-native-sdlc/resultados/S6-BENCH-002/benchmark.json): tiempos individuales API/CLI/suite y resumen.
- [Ejemplo real de ejecución](../../evidencias/semana-06/revision-v0.2/ejemplo-cli/registro.json): comando, entradas y stdout, no captura simulada.

## Control académico

- [Auditoría v0.2](../../evidencias/semana-06/revision-v0.2/AUDITORIA_S6_v0.2.md).
- [Cambios y contribuciones](../../evidencias/semana-06/revision-v0.2/REGISTRO_REVISION.md).
- [Checklist de revisión humana](../../evidencias/semana-06/revision-v0.2/REVISION_EQUIPO.md).
- [Inspección visual por IA](../../evidencias/semana-06/revision-v0.2/REVISION_VISUAL_v0.2.md).

La sesión QA tuvo contexto separado pero compartió filesystem/proveedor/modelo:
evaluación automatizada adicional, **no ciega ni totalmente independiente**.
El benchmark mide ejecución; desarrollo total, revisión humana y ahorro manual/IA
siguen NO DETERMINADOS. No hubo aceptación humana o programación manual acreditadas.

## Reproducción segura

Desde la raíz, elegir IDs nuevos:

```powershell
python -X utf8 -B poc/POC-02-ai-native-sdlc/evaluacion_v02/revision-02/runner.py --id S6-003-REPLICA-01
python -X utf8 -B poc/POC-02-ai-native-sdlc/benchmark_v02.py --id S6-BENCH-REPLICA-01
python -X utf8 -B documentos/proyecto/verificar_semana6_v02.py
python -X utf8 -B documentos/proyecto/verificar_repositorio.py
```

Los dos primeros comandos generan carpetas nuevas de resultados; los dos últimos
son de solo lectura. No repetir congelaciones ya existentes ni reutilizar IDs.
El script editorial `editar_pdf_semana6_v02.py --id <nuevo>` crea un build nuevo en
evidencias; no publica ni sobrescribe paquetes. La exportación final se copió como
borrador después de inspeccionar el build. No hay publicador aprobado automático.

DOCX comprobado estructuralmente, no renderizado en Word/LibreOffice. Aprobar exige
que el equipo revise fuentes, código, expectativas, hallazgos, figuras y defensa;
registre aportes e intervalos auténticos y emita decisión. No confundir calidad
editorial, aceptación de tests o benchmark con aprobación académica.
