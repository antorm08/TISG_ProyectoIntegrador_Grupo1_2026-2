#!/usr/bin/env python3
"""Consolida los registros de la Semana 1 y añade los de la Semana 4.

Lee `Registros_y_Radar_Semana1.xlsx`, agrega filas en Decisiones,
Contribuciones, Supuestos y Fuentes, y escribe
`Registros_y_Radar_Semana4.xlsx` (sin dependencias externas).
"""

import os
import zipfile
import xml.etree.ElementTree as ET

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
RNS = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
BASE = os.path.dirname(os.path.abspath(__file__))
ENTRADA = os.path.join(BASE, "Registros_y_Radar_Semana1.xlsx")
SALIDA = os.path.join(BASE, "Registros_y_Radar_Semana4.xlsx")

NUEVAS = {
    "Decisiones": [
        ["D-06", "02/10/2026", "Fijar BI y analitica operacional como tendencia principal de la Semana 4",
         "Arquitectura de datos analitica; IA generativa", "Ataca S-08 y es el anillo Adoptar del Radar v0.1", "Equipo", "Vigente"],
        ["D-07", "02/10/2026", "Validar H1 con un PoC de estimacion por historicos sobre datos sinteticos",
         "Encuesta de percepcion; piloto en produccion", "Mide el desvio real sin riesgo y a escala academica", "Equipo", "Vigente"],
        ["D-08", "02/10/2026", "Mantener IA generativa en Probar/Evaluar subordinada a H1 y H2",
         "Priorizar IA como primera capa", "Depende de datos confiables y trazables (D-03)", "Equipo", "Vigente"],
    ],
    "Contribuciones": [
        ["Anthony Romani", "Declaracion del problema y usuarios afectados", "Seccion 1", "02/10/2026",
         "Documento: Seccion 1", "Registrado", "-"],
        ["Max Astuhuaman", "Hipotesis y tabla hipotesis-experimento-metrica-umbral-decision; fuentes y umbrales",
         "Secciones 3 y 5", "02/10/2026", "Documento: Secciones 3 y 5; hoja Fuentes", "Registrado", "-"],
        ["Guillermo Calle", "Diseno y construccion del PoC (generador de datos y experimento)",
         "Seccion 4 y poc/POC-01-estimacion-historicos", "02/10/2026",
         "synthetic_erp_data.py; experimento_bi.py; resultados.csv", "Registrado", "-"],
        ["Pablo Mendoza", "Propuesta de valor, Impact Canvas actualizado y revision integral",
         "Secciones 2 y 6", "02/10/2026", "Documento: Secciones 2 y 6", "Registrado", "-"],
    ],
    "Supuestos": [
        ["S-11", "El umbral de adopcion operativa se fija en 70% de uso semanal tras 4 semanas",
         "Operacion", "Por validar", "Validar con datos reales de adopcion de usuarios", "Supuesto del equipo (Semana 4)"],
        ["S-12", "Existen historicos suficientes de obras cerradas con granularidad por partida",
         "Datos", "Por validar", "Confirmar disponibilidad y volumen de historicos", "Supuesto del equipo (Semana 4)"],
    ],
    "Fuentes": [
        ["F-20", "1", "AACE International - RP 18R-97 Cost Estimate Classification System", "2020",
         "Umbral de exactitud de estimacion (H1)", "https://web.aacei.org/docs/default-source/toc/toc_18r-97.pdf"],
        ["F-21", "4", "Abdelalim, Salem, Salem, Al-Adwani & Tantawy - An Analysis of Factors Contributing to Cost Overruns in the Global Construction Industry", "2025",
         "Sustento del problema: estimacion inexacta como factor de sobrecosto", "https://doi.org/10.3390/buildings15010018"],
        ["F-22", "4", "Elserougy, Khodeir & Fathy - Practices and techniques for construction projects cost control", "2024",
         "Benchmark de control de costos (30-40% pobre desempeno)", "https://doi.org/10.1080/16874048.2024.2337060"],
        ["F-23", "2", "CFMA - 2025 Construction Financial Benchmarker", "2025",
         "Benchmark financiero del sector construccion", "https://cfma.org/"],
        ["F-24", "2", "DORA - State of AI-assisted Software Development 2025", "2025",
         "Viabilidad y automatizacion de la entrega", "https://dora.dev/research/2025/dora-report/"],
    ],
}


def leer_libro(ruta):
    z = zipfile.ZipFile(ruta)
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    relmap = {r.get("Id"): r.get("Target") for r in rels}
    shared = ET.fromstring(z.read("xl/sharedStrings.xml"))
    strs = ["".join(t.text or "" for t in si.iter(NS + "t")) for si in shared]
    hojas = []
    for sh in wb.iter(NS + "sheet"):
        nombre = sh.get("name")
        target = relmap[sh.get(RNS + "id")].lstrip("/")
        if not target.startswith("xl/"):
            target = "xl/" + target
        ws = ET.fromstring(z.read(target))
        filas = []
        for row in ws.iter(NS + "row"):
            celdas = []
            for c in row.iter(NS + "c"):
                v = c.find(NS + "v")
                if v is None:
                    celdas.append("")
                elif c.get("t") == "s":
                    celdas.append(strs[int(v.text)])
                else:
                    celdas.append(v.text or "")
            filas.append(celdas)
        hojas.append((nombre, filas))
    return hojas


def col_letra(n):
    letra = ""
    while n >= 0:
        letra = chr(n % 26 + 65) + letra
        n = n // 26 - 1
    return letra


def hoja_xml(filas):
    partes = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
              '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>']
    for i, fila in enumerate(filas, start=1):
        celdas = ""
        for j, valor in enumerate(fila):
            v = "" if valor is None else str(valor)
            celdas += (f'<c r="{col_letra(j)}{i}" t="inlineStr"><is>'
                       f'<t xml:space="preserve">{_esc(v)}</t></is></c>')
        partes.append(f'<row r="{i}">{celdas}</row>')
    partes.append("</sheetData></worksheet>")
    return "".join(partes)


def _esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def main():
    hojas = leer_libro(ENTRADA)
    for nombre, filas in hojas:
        if nombre in NUEVAS:
            filas.extend(NUEVAS[nombre])

    n = len(hojas)
    ct = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
          '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
          '<Default Extension="xml" ContentType="application/xml"/>',
          '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>']
    for i in range(1, n + 1):
        ct.append(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>')
    ct.append("</Types>")

    rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>',
            "</Relationships>"]

    sheets_xml = ""
    wbrels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
              '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">']
    for i, (nombre, _) in enumerate(hojas, start=1):
        sheets_xml += f'<sheet name="{_esc(nombre)}" sheetId="{i}" r:id="rId{i}"/>'
        wbrels.append(f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>')
    wbrels.append("</Relationships>")

    workbook = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                f"<sheets>{sheets_xml}</sheets></workbook>")

    with zipfile.ZipFile(SALIDA, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", "".join(ct))
        z.writestr("_rels/.rels", "".join(rels))
        z.writestr("xl/workbook.xml", workbook)
        z.writestr("xl/_rels/workbook.xml.rels", "".join(wbrels))
        for i, (_, filas) in enumerate(hojas, start=1):
            z.writestr(f"xl/worksheets/sheet{i}.xml", hoja_xml(filas))
    print(f"[OK] Registro consolidado: {SALIDA}")
    for nombre, filas in hojas:
        print(f"     {nombre}: {len(filas)} filas")


if __name__ == "__main__":
    main()
