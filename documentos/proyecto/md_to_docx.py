#!/usr/bin/env python3
"""Convierte el documento Markdown de la Semana 4 a DOCX (OOXML puro).

No requiere dependencias externas. Uso:
    python3 md_to_docx.py <entrada.md> <salida.docx>
"""

import os
import re
import struct
import sys
import zipfile
from datetime import datetime, timezone

EMU_POR_TWIP = 635
ANCHO_UTIL_TWIPS = 11906 - 2 * 1134
ANCHO_UTIL_EMU = ANCHO_UTIL_TWIPS * EMU_POR_TWIP
EMU_POR_PX = 9525  # 96 dpi


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def runs(texto):
    """Convierte texto con **negrita** y `code` en runs OOXML."""
    salida = []
    partes = re.split(r"(\*\*.+?\*\*|`[^`]+`)", texto)
    for p in partes:
        if not p:
            continue
        if p.startswith("**") and p.endswith("**"):
            salida.append(
                f'<w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">{esc(p[2:-2])}</w:t></w:r>')
        elif p.startswith("`") and p.endswith("`"):
            salida.append(
                '<w:r><w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>'
                f'<w:sz w:val="20"/></w:rPr><w:t xml:space="preserve">{esc(p[1:-1])}</w:t></w:r>')
        else:
            salida.append(f'<w:r><w:t xml:space="preserve">{esc(p)}</w:t></w:r>')
    return "".join(salida) or "<w:r><w:t/></w:r>"


def parrafo(texto, estilo=None, bullet=False, cursiva=False):
    ppr = "<w:pPr>"
    if estilo:
        ppr += f'<w:pStyle w:val="{estilo}"/>'
    if bullet:
        ppr += '<w:ind w:left="567" w:hanging="283"/>'
    if cursiva:
        pass
    ppr += "</w:pPr>"
    contenido = runs(texto)
    if cursiva:
        contenido = contenido.replace("<w:r>", '<w:r><w:rPr><w:i/></w:rPr>')
    prefijo = '<w:r><w:t xml:space="preserve">\u2022  </w:t></w:r>' if bullet else ""
    return f"<w:p>{ppr}{prefijo}{contenido}</w:p>"


def tabla(filas):
    ncols = max(len(f) for f in filas)
    grid = "".join('<w:gridCol w:w="1800"/>' for _ in range(ncols))
    bordes = (
        "<w:tblBorders>"
        '<w:top w:val="single" w:sz="4" w:color="999999"/>'
        '<w:left w:val="single" w:sz="4" w:color="999999"/>'
        '<w:bottom w:val="single" w:sz="4" w:color="999999"/>'
        '<w:right w:val="single" w:sz="4" w:color="999999"/>'
        '<w:insideH w:val="single" w:sz="4" w:color="999999"/>'
        '<w:insideV w:val="single" w:sz="4" w:color="999999"/>'
        "</w:tblBorders>")
    out = [
        "<w:tbl><w:tblPr><w:tblW w:w=\"0\" w:type=\"auto\"/>"
        f"{bordes}</w:tblPr><w:tblGrid>{grid}</w:tblGrid>"
    ]
    for i, fila in enumerate(filas):
        celdas = ""
        for c in fila:
            texto = c.strip()
            contenido = runs(texto)
            if i == 0:
                contenido = (contenido.replace("<w:r>", "<w:r><w:rPr><w:b/></w:rPr>")
                             .replace("<w:r><w:rPr><w:b/></w:rPr><w:rPr>",
                                      "<w:r><w:rPr>"))
            celdas += (f'<w:tc><w:tcPr><w:tcW w:w="1800" w:type="dxa"/>'
                       f"</w:tcPr><w:p><w:pPr><w:spacing w:after=\"0\"/></w:pPr>"
                       f"{contenido}</w:p></w:tc>")
        header = ""
        if i == 0:
            header = ('<w:trPr><w:tblHeader/></w:trPr>')
        out.append(f"<w:tr>{header}{celdas}</w:tr>")
    out.append("</w:tbl>")
    return "".join(out)


def dimensiones_png(ruta):
    with open(ruta, "rb") as f:
        cabecera = f.read(24)
    if cabecera[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"No es un PNG: {ruta}")
    ancho, alto = struct.unpack(">II", cabecera[16:24])
    return ancho, alto


def imagen(alt, ruta, rid, numero):
    ancho_px, alto_px = dimensiones_png(ruta)
    ancho = min(ancho_px * EMU_POR_PX, ANCHO_UTIL_EMU)
    alto = int(alto_px * ancho / (ancho_px * EMU_POR_PX))
    nombre = f"Imagen {numero}"
    dibujo = (
        '<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="120" w:after="60"/></w:pPr>'
        '<w:r><w:drawing>'
        f'<wp:inline distT="0" distB="0" distL="0" distR="0">'
        f'<wp:extent cx="{ancho}" cy="{alto}"/>'
        f'<wp:docPr id="{numero}" name="{esc(nombre)}" descr="{esc(alt)}"/>'
        '<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:pic><pic:nvPicPr>'
        f'<pic:cNvPr id="{numero}" name="{esc(nombre)}"/>'
        '<pic:cNvPicPr/></pic:nvPicPr>'
        f'<pic:blipFill><a:blip r:embed="{rid}"/>'
        '<a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{ancho}" cy="{alto}"/>'
        '</a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
        '</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>')
    leyenda = parrafo(alt, cursiva=True) if alt else ""
    return dibujo + leyenda


def md_a_cuerpo(md, base_dir, imagenes):
    lineas = md.splitlines()
    cuerpo = []
    i = 0
    while i < len(lineas):
        ln = lineas[i].rstrip()
        if not ln.strip():
            i += 1
            continue
        mimg = re.match(r"^!\[(.*?)\]\((.+?)\)\s*$", ln.strip())
        if mimg:
            alt = mimg.group(1).strip()
            ruta_rel = mimg.group(2).strip()
            ruta = ruta_rel if os.path.isabs(ruta_rel) else os.path.join(base_dir, ruta_rel)
            if os.path.exists(ruta):
                numero = len(imagenes) + 1
                rid = f"rIdImg{numero}"
                nombre_media = f"imagen-{numero}.png"
                imagenes.append((rid, nombre_media, ruta))
                cuerpo.append(imagen(alt, ruta, rid, numero))
            else:
                cuerpo.append(parrafo(f"[Imagen no encontrada: {ruta_rel}]", cursiva=True))
            i += 1
            continue
        if ln.startswith("|"):
            filas = []
            while i < len(lineas) and lineas[i].lstrip().startswith("|"):
                celdas = [c for c in lineas[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r"\s*:?-{2,}:?\s*", c) for c in celdas):
                    filas.append(celdas)
                i += 1
            if filas:
                cuerpo.append(tabla(filas))
            continue
        if ln.strip() == "---":
            cuerpo.append('<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="6" '
                          'w:color="BBBBBB"/></w:pBdr></w:pPr></w:p>')
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", ln)
        if m:
            nivel = len(m.group(1))
            estilo = {1: "Title", 2: "Heading1", 3: "Heading2", 4: "Heading3"}.get(nivel, "Heading3")
            cuerpo.append(parrafo(m.group(2), estilo=estilo))
            i += 1
            continue
        if re.match(r"^[-*]\s+", ln):
            cuerpo.append(parrafo(re.sub(r"^[-*]\s+", "", ln), bullet=True))
            i += 1
            continue
        if re.match(r"^\d+\.\s+", ln):
            cuerpo.append(parrafo(ln, bullet=True))
            i += 1
            continue
        # párrafo normal (puede ser continuación)
        cuerpo.append(parrafo(ln))
        i += 1
    return "".join(cuerpo)


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr>
<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/>
<w:pPr><w:spacing w:before="240" w:after="120"/></w:pPr>
<w:rPr><w:b/><w:sz w:val="40"/><w:color w:val="1F4E79"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/>
<w:pPr><w:keepNext/><w:spacing w:before="280" w:after="120"/><w:outlineLvl w:val="0"/></w:pPr>
<w:rPr><w:b/><w:sz w:val="30"/><w:color w:val="1F4E79"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/>
<w:pPr><w:keepNext/><w:spacing w:before="200" w:after="80"/><w:outlineLvl w:val="1"/></w:pPr>
<w:rPr><w:b/><w:sz w:val="26"/><w:color w:val="2E74B5"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/>
<w:pPr><w:keepNext/><w:spacing w:before="160" w:after="60"/><w:outlineLvl w:val="2"/></w:pPr>
<w:rPr><w:b/><w:sz w:val="23"/><w:color w:val="2E74B5"/></w:rPr></w:style>
</w:styles>"""


def construir(md, titulo, base_dir="."):
    imagenes = []
    cuerpo = md_a_cuerpo(md, base_dir, imagenes)
    sect = (
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" '
        'w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>')
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
        'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
        'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        f"<w:body>{cuerpo}{sect}</w:body></w:document>")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    core = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        f"<dc:title>{esc(titulo)}</dc:title>"
        "<dc:creator>Grupo 1 - TISG 2026-2</dc:creator>"
        f'<dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>'
        "</cp:coreProperties>")
    app = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
        'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
        "<Application>Grupo1-TISG</Application></Properties>")
    return document, core, app, imagenes


def main():
    if len(sys.argv) != 3:
        print("Uso: python3 md_to_docx.py <entrada.md> <salida.docx>")
        sys.exit(1)
    entrada, salida = sys.argv[1], sys.argv[2]
    with open(entrada, encoding="utf-8") as f:
        md = f.read()
    base_dir = os.path.dirname(os.path.abspath(entrada))
    titulo = md.splitlines()[0].lstrip("# ").strip() if md else "Documento"
    document, core, app, imagenes = construir(md, titulo, base_dir)
    rels_img = "".join(
        f'<Relationship Id="{rid}" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
        f'Target="media/{nombre}"/>'
        for rid, nombre, _ in imagenes)
    doc_rels = DOC_RELS.replace("</Relationships>", rels_img + "</Relationships>")
    content_types = CONTENT_TYPES
    if imagenes:
        content_types = content_types.replace(
            '<Default Extension="xml" ContentType="application/xml"/>',
            '<Default Extension="xml" ContentType="application/xml"/>\n'
            '<Default Extension="png" ContentType="image/png"/>')
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    with zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/document.xml", document)
        z.writestr("word/_rels/document.xml.rels", doc_rels)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("docProps/core.xml", core)
        z.writestr("docProps/app.xml", app)
        for _, nombre, ruta in imagenes:
            z.write(ruta, f"word/media/{nombre}")
    print(f"[OK] DOCX generado: {salida} ({len(imagenes)} imagen(es))")


if __name__ == "__main__":
    main()
