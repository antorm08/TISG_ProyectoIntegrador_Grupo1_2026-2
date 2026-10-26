# Evidencias de mantenimiento — 26/10/2026

No son resultados experimentales S6 ni sustituyen evidencias v1.1/v1.2.
Base inicial: `7f962facba3abc78c38921e656fadb6852c17fe4`.
Rama: `chore/preparacion-semana-06`. Cambios sin commit.

| Archivo | Qué demuestra |
|---|---|
| `integridad_antes.json` | SHA-256 de bytes locales de 156 archivos versionados antes de editar. No incluye configuración ignorada. |
| `investigacion_protocolo.json` | Hash esperado/actual y reconstrucción exclusivamente en memoria que explica divergencia del protocolo. |
| `fotografia_git_7f962fa.json` | Rutas, blobs y SHA-256 exactos del commit base; independiente de que HEAD avance. |
| `validacion.json` | Comprobaciones actuales, pruebas de herramientas y exportación limpia; no revisión humana ni ejecución experimental. |
| `inventario_actual.json` | Rutas, fecha UTC, HEAD observado y SHA-256 de bytes compartibles después del mantenimiento, incluidos cambios sin commit. Excluye solo su propio archivo de ese conjunto. |

Los manifiestos de `../revision-v1.2/` se preservan. Su HEAD anterior y el hash
anterior del protocolo no se corrigen para hacerlos pasar por una fotografía nueva.

Comandos de solo lectura desde raíz:

```powershell
python -X utf8 -B documentos/proyecto/verificar_repositorio.py
python -X utf8 -B documentos/proyecto/inventario_repositorio.py verify evidencias/mantenimiento-s06/fotografia_git_7f962fa.json
python -X utf8 -B documentos/proyecto/inventario_repositorio.py verify evidencias/mantenimiento-s06/inventario_actual.json
```

`capture-git --ref <commit> --salida <ruta-nueva.json>` y
`capture-worktree --salida <ruta-nueva.json>` son operaciones **con escritura**
explícita; rechazan destinos existentes y no regeneran documentos o experimentos.
Se usaron solo para crear las dos nuevas fotografías de esta carpeta.

La exportación de prueba no incluye `.git/`, skills, copia ignorada de guía,
auditoría inicial ni documentación personal. Los cambios propuestos se superponen
a HEAD para ensayar la futura combinación sin añadir al índice ni hacer commit.
Las rutas temporales de prueba son auxiliares; los JSON publicados no requieren
que sigan existiendo para interpretar sus resultados.

Informe y restricciones: [mantenimiento S6](../../documentos/mantenimiento/INFORME_MANTENIMIENTO_S06.md).
