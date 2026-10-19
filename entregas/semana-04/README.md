# Entrega — Semana 4

## Identificación

- Curso: Tendencias en Ingeniería de Software y Gestión
- Equipo: Grupo 1
- Semana: 04
- Caso: Constructora Andina S.A.C. (organización ficticia)
- Tendencia principal: BI y analítica operacional
- Versión: v1.0
- Fecha: 2026-10-02
- Estado: documento generado; pendiente de exportar a PDF

## Objetivo

Transformar el problema en hipótesis comprobables y definir cómo se validará el valor antes de escalar una solución (guía del Proyecto Integrador, Semana 4).

## Contenido de la entrega

| Archivo | Propósito | Naturaleza |
|---|---|---|
| `TISG_E01_S04_ProyectoIntegrador_2026-10-02.docx` | Informe principal de la Semana 4 | Editable (DOCX) |

## Artefactos de apoyo (fuera de esta carpeta)

| Ruta | Propósito |
|---|---|
| `documentos/proyecto/Semana4_Proyecto_Integrador.md` | Fuente en Markdown del informe |
| `documentos/proyecto/md_to_docx.py` | Script que genera el DOCX desde el Markdown |
| `poc/POC-01-estimacion-historicos/` | PoC que valida la hipótesis principal (H1) |
| `gestion/registros/Registros_y_Radar_Semana4.xlsx` | Registros consolidados (decisiones, contribuciones, supuestos, fuentes) |
| `gestion/registros/actualizar_registros_semana4.py` | Script que consolida los registros |

## Cumplimiento de Semana 4

- Declaración precisa del problema y usuarios afectados (sección 1).
- Propuesta de valor del producto/servicio/capacidad (sección 2, Value Proposition Canvas).
- Tres hipótesis: valor (H1), viabilidad técnica (H2) y adopción/operación (H3) (sección 3).
- Diseño de un experimento/PoC para la hipótesis principal (sección 4 y `poc/POC-01`).
- Métricas de éxito, umbrales de aceptación y criterio de abandono (sección 5).
- Impact Canvas actualizado para la tendencia principal (sección 6).
- Al menos tres fuentes verificables, con al menos una de nivel 1/2/4 (sección 8).
- Registro de decisiones y contribuciones actualizados (sección 7 y XLSX).

## Ejecución del PoC

```bash
cd poc/POC-01-estimacion-historicos
python3 src/synthetic_erp_data.py
python3 src/experimento_bi.py
python3 pruebas/verificar_poc.py
```

Resultado con semilla `20261002`: MAPE analítico 11,31 % frente a 20,19 % de la línea base manual (reducción 43,98 %) → H1 respaldada en el experimento sintético.

## Verificación antes de presentar

- [ ] El DOCX abre correctamente y refleja la versión final.
- [ ] El PDF exportado coincide con el DOCX.
- [ ] El problema, la propuesta de valor y las hipótesis están conectados.
- [ ] Cada umbral tiene su fuente citada (AACE 18R-97, Abdelalim et al., Elserougy et al., CFMA, DORA).
- [ ] Los resultados del PoC se presentan como simulados, no como desempeño real.
- [ ] El registro de contribuciones coincide con los aportes reales.
- [ ] No se incluyeron datos personales, credenciales o información confidencial.

## Cierre de versión

```bash
git tag -a entrega-s04 -m "Entrega oficial Semana 4"
git push origin entrega-s04
```
