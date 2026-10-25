# Arquitectura AS-IS

> **Revisión vigente:** [diagramas v1.1](../revision-v1.1/) y [Hito I corregido](../../documentos/proyecto/Semana5_Hito_I_v1.1.md), 24/10/2026. El ERP es propio CodeIgniter/MySQL. Las figuras originales de esta carpeta se conservan como antecedente y contienen la caracterización errónea Odoo/PostgreSQL; no utilizarlas como AS-IS vigente. El texto siguiente es el estado inicial de S1.

## Estado

Versión funcional inicial. En Semana 1 se describe el proceso y la brecha; el diagrama arquitectónico completo se elaborará después de validar los componentes y flujos reales.

## Alcance

El AS-IS representa cómo el ERP registra la ejecución de las obras y consolida información de producción y costos. No pretende revelar una arquitectura empresarial confidencial.

## Flujo funcional conocido

```text
Obra
  → Partidas de control
    → Actividades
      → Tareo y distribución de horas
      → Registro diario de metrados
      → Costos de mano de obra y materiales
        → Resumen de producción
          → Histórico de costos y rendimientos
```

## Componentes funcionales identificados

| Componente | Responsabilidad | Datos principales |
|---|---|---|
| Gestión de obras | Organizar obras, partidas y actividades | Obra, partida, actividad |
| Tareo | Registrar asistencia y horas de jornada | Trabajador, fecha, horas |
| Asignación de actividades | Distribuir horas entre actividades | Actividad, trabajador, horas |
| Metrados | Registrar producción o avance diario | Actividad, fecha, metrado |
| Compras y abastecimiento | Originar costos de materiales | Material, cantidad, costo |
| Resumen de producción | Consolidar esfuerzo, producción y costos | Horas, metrados, ratios, costos |
| Presupuesto | Gestionar valores previstos | Obra, partidas, costos previstos |

## Problemas observados

- La información histórica no se reutiliza de manera integrada para presupuestar nuevas obras.
- La comparación previsto-real todavía no está consolidada sistemáticamente.
- Algunos reportes dependen de numerosas relaciones operativas y pueden presentar latencia.
- Falta validar la calidad, frecuencia, volumen y granularidad de los históricos.
- No se ha determinado si una plataforma analítica separada es necesaria o proporcional.

## Supuestos relacionados

Los supuestos `S-02` a `S-09` del registro de Semana 1 describen el ERP, las obras, el tareo, los metrados, los costos, el resumen y la capacidad del equipo TI. Cualquier cambio deberá actualizarse en el Registro de Supuestos.

## Información pendiente de validar

- Componentes físicos y servicios reales.
- Bases de datos y mecanismos actuales de integración.
- Volumen, frecuencia y retención de datos.
- Dependencias responsables de la latencia.
- Controles de acceso y auditoría.
- Capacidades y tamaño del equipo TI.

## Requisitos del futuro diagrama

El diagrama AS-IS deberá incluir título, leyenda, fecha, versión, límites del sistema, fuentes de datos, flujos principales y la indicación `Elaboración propia`. No se representarán nombres internos o configuraciones sensibles.
