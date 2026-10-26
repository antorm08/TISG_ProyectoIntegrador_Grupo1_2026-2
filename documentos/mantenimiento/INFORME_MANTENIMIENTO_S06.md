# Informe de mantenimiento controlado — preparación S6

Fecha: 26/10/2026. Grupo 1. Alternativa A: mejoras mínimas.
Base: `7f962facba3abc78c38921e656fadb6852c17fe4`, rama inicial `main`, árbol limpio.
Rama creada: `chore/preparacion-semana-06`. **Sin commit ni push.**
No es una auditoría académica nueva ni una versión v1.3 del Hito I.

## 1. Hallazgos reconfirmados y estado final

Se contrastaron los doce hallazgos con archivos actuales, Git, hashes y scripts
antes de editar. La incorporación de v1.2 a Git ya había ocurrido al iniciar.

| Hallazgo | Confirmación actual y acción | Estado |
|---|---|---|
| ORG-01 | AS-IS/TO-BE y POC-01 presentaban v1.1 como vigente; ahora enlazan v1.2 y rotulan antecedentes. | CORREGIDO |
| ORG-02 | El verificador original exige HEAD `038ce87`; se preserva intacto. Verificador actual independiente y fotografía Git exacta separadas. | CORREGIDO |
| ORG-03 | Dependencias de guía/auditoría/documentación ignoradas reconfirmadas. Nuevo verificador usa guía compartida y considera auditoría inicial opcional. Documentación personal no se publica. | CORREGIDO |
| ORG-04 | Divergencia del protocolo explicada mediante reconstrucción en memoria y hash; inventario viejo intacto y comprobación nueva diferenciada. | CORREGIDO |
| ORG-05 | Verificadores históricos escriben CSV/evidencias; advertencias y matriz de efectos, nuevo verify sin escritura. No se ejecutó POC-01. | CORREGIDO |
| ORG-06 | Libro S5 sin sufijo idéntico a S1; índice de registros señala cinco hojas y selecciona el consolidado v1.2 de 34. Sin editar libros. | CORREGIDO |
| ORG-07 | Cuatro `.pyc` siguen versionados; rutas exactas identificadas. No se retiraron automáticamente. | PENDIENTE |
| ORG-08 | Changelog sin v1.2; se añade su alcance, fecha documental, incorporación a Git y mantenimiento. Entradas anteriores conservadas como historia. | CORREGIDO |
| ORG-09 | Manifiestos S4/S5 y ausencia de fichas S2/S3 inducían a error; nuevo índice transversal enumera PDFs/editables sin alterar fichas históricas. | CORREGIDO |
| ORG-10 | Generadores de destinos fijos conservados; capture nuevo rechaza sobrescrituras y se documenta generate/publish aislado para futuro. Generadores antiguos no refactorizados. | PARCIAL |
| ORG-11 | Skills/configuración/lock siguen locales y no portables; procedimiento por commits/licencias documentado sin rutas privadas. Adaptaciones locales no publicadas ni instaladas en otro equipo. | PARCIAL |
| ORG-12 | Convención futura consistente en CONTRIBUTING, ejemplo Grupo 1/S6 y enlaces actuales; sin renombrar históricos. | CORREGIDO |

## 2. Divergencia del diseño experimental

Ruta: `poc/POC-01-estimacion-historicos/revision-v1.2/DISENO_EXPERIMENTAL.md`.

- Inventario anterior: `evidencias/revision-v1.2/inventario_final.json`, fecha
  `2026-10-26T08:50:07` sin zona horaria, HEAD observado `038ce87`.
- Hash registrado: `7949e0f75f20c864ff2b18140543f63b48fe797fde211e50acef6207df6a22e3`;
  7938 bytes.
- Archivo al iniciar mantenimiento: SHA-256
  `4a2f7a6a873552d91ef830fcf07fa751f360e448e672408770d1336fcc0b5648`;
  7993 bytes con CRLF. Su representación LF tiene 7871 bytes.
- Se reconstruyó **solo en memoria** su representación LF añadiendo, después de
  la identificación inicial, la línea:
  `**Estado: diseño no ejecutado; pendiente de validación humana.**` seguida de LF.
  El resultado tiene 7938 bytes y coincide exactamente con el SHA-256 anterior.
  Esto explica la diferencia por retirada de esa línea y conversión de saltos;
  no se alteró el archivo para comprobarlo ni se restauró la cabecera.
- Git contiene una sola incorporación de esa ruta: `7f962fa`, 26/10/2026 a las
  09:04:44 -05:00. Esa versión ya carece de la línea. No hay una revisión previa
  de la ruta en el historial accesible que permita fechar/atribuir la edición
  intermedia. El instante exacto y su autor no se infieren del snapshot.

Es divergencia entre fotografías, **no evidencia de corrupción**. El protocolo
actual aún declara en §5 que no se generaron predicciones/resultados. No se cambia
su contenido ni el del Hito I. Los hashes de blobs Git pueden diferir de bytes
locales por LF/CRLF: cada comprobación declara cuál utiliza.

## 3. Cambios delimitados

Archivos previos modificados, y solo estos siete:

1. `.gitignore`: patrones preventivos acotados; se mantienen exclusiones personales.
2. `README.md`: guía canónica, contribución, índice semanal y comandos actuales.
3. `CHANGELOG.md`: v1.2 y mantenimiento, sin reescribir entradas históricas.
4. `CONTRIBUTING.md`: nomenclatura futura y separación verify/generate/publish.
5. `arquitectura/as-is/README.md`: indicador vigente v1.2.
6. `arquitectura/to-be/README.md`: indicador vigente v1.2.
7. `poc/POC-01-estimacion-historicos/README.md`: vigencia, enlaces y advertencia de escritura.

Archivos nuevos:

- `entregas/INDICE_ACTUAL.md` y `gestion/registros/README.md`.
- `documentos/proyecto/verificar_repositorio.py`, `inventario_repositorio.py` y `test_mantenimiento.py`.
- Este informe, `PREPARACION_SEMANA_06.md` y `SKILLS_COMPARTIBLES.md`, en `documentos/mantenimiento/`.
- `evidencias/mantenimiento-s06/integridad_antes.json`.
- `evidencias/mantenimiento-s06/investigacion_protocolo.json`.
- `evidencias/mantenimiento-s06/fotografia_git_7f962fa.json`.
- `evidencias/mantenimiento-s06/validacion.json`.
- `evidencias/mantenimiento-s06/inventario_actual.json`.
- `evidencias/mantenimiento-s06/README.md`.

El inventario actual da las rutas/tamaños/hashes exactos; excluye su propio archivo
para evitar autorreferencia. No incluye las skills, configuraciones ni documentos
personales ignorados. Ningún binario, CSV, resultado, auditoría o inventario anterior
se sobrescribe. Los tres Markdown académicos del Hito I permanecen intactos.

## 4. Verificaciones y límites

Resultados ejecutados se guardan en `evidencias/mantenimiento-s06/validacion.json`;
véase el [índice de evidencias](../../evidencias/mantenimiento-s06/README.md).

| Prueba ejecutada | Resultado |
|---|---|
| Verificador actual | OK: 149 archivos previos protegidos, 23 tablas DOCX, 4 figuras, 34 hojas Excel y 105 enlaces locales. Sin archivos escritos por verify. |
| Fotografía Git | OK: 156 blobs del commit exacto `7f962fa`, sin exigir que HEAD retroceda. |
| Pruebas unitarias de mantenimiento | 8 OK; hashes, ausencia, formato antiguo, sobrescritura, rutas, LF/CRLF y enlaces relativos. |
| Patrones `.gitignore` | 17 casos comprobados; secretos/temporales ignorados, plantillas y artefactos legítimos no ocultos. |
| Exportación limpia temporal | OK sin Git ni archivos locales ignorados; 20 archivos textuales requieren únicamente conversión LF/CRLF respecto a bytes locales de origen. |
| Casos negativos | CSV histórico alterado, enlace inexistente, hash de fotografía Git alterado y destino de evidencia existente: los cuatro rechazados. Solo se alteraron fixtures/copias temporales. |
| Huella antes/después | Verificador y pruebas no modifican el repositorio; verify tampoco modifica la exportación. |

La comprobación del estado actual no reejecuta el antiguo verificador ni una PoC;
solo reutiliza sus dos funciones puras de parsing/normalización. No se requieren
Git, guía ignorada, skills ni auditoría inicial para verificar una exportación.

La [preparación operativa](PREPARACION_SEMANA_06.md) explica los comandos y los
alcances de cada evidencia. El verificador conserva 149 archivos previos fuera
de los siete índices/configuraciones autorizados. Los binarios son estrictos;
una conversión de saltos en exportaciones textuales se informa, no se oculta.

La simulación limpia usa una exportación temporal de HEAD con superposición de
los cambios compartibles del mantenimiento, **sin staging ni commit** y sin
archivos ignorados. No debe confundirse con una clonación del commit base que
ya contenga estos cambios todavía no incorporados. Se comprueba también la
integridad de esa exportación antes/después de ejecutar verify.

No se instalan dependencias, ejecutan modelos o experimentos, renderizan documentos
Office ni atribuye aprobación humana. Pruebas de mantenimiento no son resultados S6.

## 5. Autorizaciones y pendientes reales

- Retirar los cuatro `.pyc` del seguimiento necesita autorización separada.
- Los generadores antiguos siguen pudiendo sobrescribir sus destinos. La matriz
  los identifica; no ejecutarlos sobre el árbol conservado. Un futuro refactor o
  reproducción debe hacerse en copia aislada y requiere autorización.
- La auditoría inicial local fue revisada: contiene diagnóstico, referencias a
  integrantes/identidades Git y estimaciones académicas no oficiales. No se detectan
  credenciales evidentes, pero eso no autoriza su divulgación automáticamente.
  Se conserva ignorada y opcional hasta decisión del equipo; no se usó `git add -f`.
- Skills locales y adaptaciones personales no se publican. La instalación en otro
  equipo no fue ensayada ni debe suponerse idéntica por disponer de los commits upstream.
- El equipo debe revisar el diff y aprobar integración. El Hito I sigue **Pendiente
  de validación humana**; ninguna de sus condiciones académicas se cierra por este mantenimiento.

**Recomendación:** estructura preparada para iniciar S6 bajo el flujo aislado
documentado, sin confundirlo con una aprobación académica ni permiso para regenerar históricos.
