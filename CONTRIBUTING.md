# Guía de contribución

## Propósito

Esta guía establece cómo colaborar en el proyecto, conservar evidencia auténtica y evitar inconsistencias entre documentos, registros, diagramas y entregas.

## Flujo recomendado

1. Actualizar la rama local `main`.
2. Crear una rama específica para la actividad.
3. Modificar únicamente los artefactos relacionados con la tarea.
4. Revisar que no se haya incorporado información sensible.
5. Realizar commits claros desde la cuenta del autor real.
6. Abrir un Pull Request y solicitar revisión a otro integrante.
7. Actualizar el registro de contribuciones y, cuando corresponda, el registro de decisiones.
8. Integrar a `main` después de la revisión.

## Nombres de ramas

```text
docs/s02-arquitectura-as-is
docs/s02-fuentes
feat/s03-poc-analitica
fix/s01-citas-apa
chore/s02-evidencias
```

## Mensajes de commit

Usar mensajes breves que indiquen el artefacto y la finalidad:

```text
docs(s01): ajusta alcance y restricciones del Charter
docs(fuentes): agrega evidencia para arquitectura analítica
feat(radar): actualiza posición de observabilidad
docs(riesgos): registra controles para datos e IA
fix(s02): corrige correspondencia entre cita y referencia
```

No crear commits retroactivos o artificiales para aparentar participación. El primer entregable puede respaldarse con evidencia documental; desde las siguientes semanas, el historial debe generarse naturalmente.

## Convención de archivos entregables

```text
TISG_EXX_S##_NombreEntregable_vX.Y_AAAA-MM-DD.ext
```

Ejemplo:

```text
TISG_E03_S01_ProyectoIntegrador_2026-09-04.pdf
```

## Control de versiones

- Incremento menor: corrección o ampliación sin cambiar el planteamiento central.
- Incremento mayor (`v0.x` a `v1.0`): artefacto validado o cambio sustancial acordado.
- Cada entrega semanal debe registrar fecha, versión, cambio y responsable.
- Los cambios de decisiones deben conservar el motivo; no se eliminan silenciosamente.

## Fuentes y citas

- Cada entrega semanal incluirá al menos tres fuentes relevantes.
- Al menos una será de nivel 1, 2 o 4.
- Para tendencias actuales se priorizarán publicaciones recientes.
- Las fuentes fundacionales se usarán solo cuando corresponda al concepto.
- Se mantendrá APA 7 en citas y referencias.
- No se afirmarán beneficios tecnológicos sin contexto, evidencia y condiciones de validez.

## Diagramas y figuras

Todo diagrama debe incluir:

- Título.
- Leyenda cuando los símbolos no sean evidentes.
- Fecha y versión.
- Fuente externa o texto `Elaboración propia`.
- Archivo editable cuando exista, además de PDF o imagen exportada.

## Seguridad y privacidad

Está prohibido subir credenciales, información personal no autorizada, secretos comerciales, configuraciones internas sensibles o datos empresariales identificables. Antes de subir una captura se debe anonimizar nombres, correos, montos, clientes, proveedores, URLs internas e identificadores.

## Revisión antes de integrar

- [ ] El cambio responde al problema del proyecto.
- [ ] Las decisiones tienen evidencia o están marcadas como supuestos.
- [ ] Las citas aparecen en la bibliografía.
- [ ] Los diagramas coinciden con el texto.
- [ ] Se actualizó el registro de contribuciones.
- [ ] No existe información sensible.
- [ ] Los archivos abren correctamente.
- [ ] La versión y fecha son correctas.
