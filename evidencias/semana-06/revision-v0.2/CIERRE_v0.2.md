# Cierre de revisión S6 v0.2

26/10/2026 · BORRADOR / pendiente de revisión auténtica del equipo.

## Resultados

- S6-001 y v0.1 intactos: 48/48 tests históricos.
- S6-002: 35 escenarios, 109 procesos, **0/35 bruto** por EV-01/EV-02 del arnés.
- S6-003: mismos 35 escenarios, 109 procesos, **35/35** según oráculo revisado;
  10 válidos/25 inválidos, Q2=0/25, Q3=0/10; dos escenarios parcialmente ambiguos.
- Determinismo: 35/35 entre tres seeds; CLI 0/1/2 y symlink real comprobados.
- Dos defectos del evaluador, una corrección de arnés y cero correcciones del validador.
- S6-BENCH-002: 125 observaciones medidas y calentamientos separados; medianas,
  mínimo/máximo y entorno conservados. No mide esfuerzo o ahorro humanos.
- PDF editorial final: 12 páginas; tres figuras vectoriales, evidencia auténtica
  visible y nueve tablas. DOCX estructuralmente comprobado; sin render Word.

## Conservación y verificadores

Inventario inicial: 220 archivos versionados, HEAD
`94955116f63b3ae28afc750ddc43145c8670254f`. Todos conservan sus bytes, incluidos
README de v0.1, Hito I, auditorías previas, POC-01 y S6-001. Se añaden solo rutas nuevas.

`verificar_semana6_v02.py` y el verificador general seguro terminaron correctamente.
El primero recomputa métricas/medianas, contrasta extractos y contenido Markdown/PDF,
revisa hashes/congelaciones/enlaces y estructura documental. Ambos son de solo lectura.

La primera comprobación de consolidación detectó enlaces relativos en copias del
Markdown dentro de los builds. Se conservaron sus contenidos como snapshots `.md.txt`
(no documentos navegables) y se corrigió el exportador para usar esa extensión.
No cambió el contenido del informe final o los experimentos por esa corrección.
Las comprobaciones posteriores pasan; este hallazgo es documental, no defecto del
validador o nueva iteración experimental. La evidencia del arnés no se reescribió.

Los comandos finales, stdout/stderr, exit codes y fecha UTC están en `verificacion-final/`.
El inventario final se captura después y excluye su propio archivo. Los hashes
prueban consistencia de bytes, no firma, autoría, fecha certificada o aprobación.
El escaneo de patrones es acotado y no certifica ausencia universal de secretos.

Límite de portabilidad observado: el symlink auténtico conservado en S6-002 apunta
al fixture mediante una ruta Windows absoluta. La congelación 02 incluye el hash
del contenido enlazado. La reproducción funciona en este checkout; en otra ruta,
SO o clonación que materialice enlaces como texto puede requerir recrear el enlace
en una copia y documentar el ajuste antes de validar hashes. No se altera aquí el
enlace histórico para simular portabilidad universal. El benchmark y validador no
dependen de ese enlace; la dependencia corresponde a la custodia del arnés posterior.

## Estado académico

Checklist propio: 16 CUMPLE, 3 PARCIAL, 3 PENDIENTE DE VALIDACIÓN HUMANA y
1 NO VERIFICABLE. No constituye nota ni porcentaje de aprobación. Pendientes:
revisión de fuentes/código/casos/documentos, contribuciones individuales auténticas,
decisión humana y render DOCX en un procesador de texto. Productividad laboral,
esfuerzo de revisión y ahorro manual/IA siguen NO DETERMINADOS.

Rama `feat/semana-06-ai-native-sdlc`; sin staging, commits o push del asistente.
No se accedió al ERP, instalaron dependencias, ejecutaron generadores históricos,
modificaron datos/contratos originales ni implementaron APU. La separación de contexto
QA no es aislamiento material: evaluación adicional posterior, no ciega ni totalmente
independiente. El paquete está preparado para revisión final, no aprobación automática.
