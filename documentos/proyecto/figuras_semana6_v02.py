"""Figuras editoriales propias v0.2; solo crea un directorio nuevo de figuras.

Fuente editable: este script y SVG. Exporta PDF vectorial y PNG con PyMuPDF.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
DESTINO = ROOT / "arquitectura/semana-06/revision-v0.2"


def figuras():
    from reportlab.graphics.shapes import Drawing, Rect, String, Line, Polygon
    from reportlab.lib.colors import HexColor
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    for name, file in [("Editorial", "arial.ttf"), ("EditorialBold", "arialbd.ttf")]:
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, "C:/Windows/Fonts/" + file))
    navy, teal, gray, ink = map(HexColor, ["#102C46", "#087F83", "#EDF3F6", "#334A5C"])

    def text(d, x, y, txt, size=10, bold=False, color=ink):
        d.add(String(x, y, txt, fontName="EditorialBold" if bold else "Editorial", fontSize=size, fillColor=color))

    def box(d, x, y, w, h, title, lines, active=False):
        d.add(Rect(x, y, w, h, rx=6, fillColor=gray if not active else HexColor("#E3F1EF"), strokeColor=HexColor("#CAD8E0"), strokeWidth=.6))
        d.add(Rect(x, y+h-4, w, 4, fillColor=teal if active else navy, strokeColor=None))
        text(d, x+12, y+h-24, title, 10, True, navy)
        for i, linea in enumerate(lines):
            text(d, x+12, y+h-44-i*15, linea, 9)

    def arrow(d, x1, y1, x2, y2):
        d.add(Line(x1, y1, x2, y2, strokeColor=teal, strokeWidth=1.3))
        if y1 == y2:
            d.add(Polygon([x2, y2, x2-5, y2+3, x2-5, y2-3], fillColor=teal, strokeColor=None))
        else:
            d.add(Polygon([x2, y2, x2-3, y2+5, x2+3, y2+5], fillColor=teal, strokeColor=None))

    sdlc = Drawing(490, 310)
    nodes = [
        ("01  Requisitos", ["Hito I + contrato RF", "IA propone; custodio confirma"]),
        ("02  Diseño", ["ADR + alternativas", "IA explora; equipo decide"]),
        ("03  Código", ["Validador local Python", "IA produce; revisión pendiente"]),
        ("04  Pruebas", ["Corpus + evaluación adicional", "Automatizar no es certificar"]),
        ("05  Revisión y seguridad", ["Hashes, límites, privacidad", "Persona acepta o rechaza"]),
        ("06  Integración y despliegue", ["Git; sin despliegue del ERP", "TI autoriza; no autonomía A3"]),
    ]
    for i, (titulo, lineas) in enumerate(nodes):
        x = (i % 2)*255
        y = 220 - (i//2)*96
        box(sdlc, x, y, 235, 82, titulo, lineas, i in [2, 3])
        if i % 2 == 0:
            arrow(sdlc, 237, y+40, 252, y+40)
    text(sdlc, 0, 15, "Transversal: mantenimiento, documentación y revisión de cada cambio.", 9, True, navy)
    text(sdlc, 0, 0, "Verde: actividades ejecutadas. Empresa: SDLC no determinado. Elaboración propia / IA.", 8)

    flujo = Drawing(490, 230)
    box(flujo, 0, 145, 235, 76, "01  Especificar", ["Contrato + casos antes del código", "Congelación y SHA-256"])
    box(flujo, 255, 145, 235, 76, "02  Producir con IA", ["Primera versión preservada", "Fuente y prompts trazables"], True)
    arrow(flujo, 237, 183, 252, 183)
    box(flujo, 0, 47, 235, 76, "03  Evaluar", ["S6-001; S6-002 posterior", "Benchmark separado del esfuerzo"], True)
    box(flujo, 255, 47, 235, 76, "04  Autorizar", ["Revisión académica del equipo", "Pendiente; no publicar como aprobado"])
    flujo.add(Line(372, 144, 372, 133, strokeColor=teal, strokeWidth=1.3))
    flujo.add(Line(372, 133, 117, 133, strokeColor=teal, strokeWidth=1.3))
    arrow(flujo, 117, 133, 117, 126)
    arrow(flujo, 237, 85, 252, 85)
    text(flujo, 0, 22, "Si hay discrepancias: conservar resultado, identificar revisión y volver a evaluar.", 9)
    text(flujo, 0, 5, "Sesión QA distinta ≠ aislamiento material ni evaluación humana.", 9, True, teal)

    arquitectura = Drawing(490, 255)
    box(arquitectura, 0, 170, 150, 76, "ERP conservado", ["CodeIgniter / MySQL", "Sin acceso en esta PoC"])
    box(arquitectura, 170, 170, 150, 76, "Extracción", ["Autorizada y acotada", "Propuesta, no ejecutada"])
    box(arquitectura, 340, 170, 150, 76, "POC-02", ["Puerta de validación", "CSV sintéticos locales"], True)
    arrow(arquitectura, 151, 208, 167, 208)
    arrow(arquitectura, 322, 208, 337, 208)
    box(arquitectura, 0, 70, 150, 76, "Staging y SQL/Python", ["Contrato, transformaciones", "Propuesto en Hito I"])
    box(arquitectura, 170, 70, 150, 76, "Analítica y BI", ["Históricos comparables", "Propuesto, no desplegado"])
    box(arquitectura, 340, 70, 150, 76, "Revisión humana", ["Interpretar y autorizar", "No decisiones automáticas"])
    arquitectura.add(Line(415, 168, 415, 158, strokeColor=teal, strokeWidth=1.3))
    arquitectura.add(Line(415, 158, 75, 158, strokeColor=teal, strokeWidth=1.3))
    arrow(arquitectura, 75, 158, 75, 149)
    arrow(arquitectura, 151, 108, 167, 108)
    arrow(arquitectura, 322, 108, 337, 108)
    text(arquitectura, 0, 40, "Secuencia lógica: extracción → POC-02 → staging → analítica → revisión.", 9, True, navy)
    text(arquitectura, 0, 23, "Solo el recuadro verde está implementado como componente local en S6.", 9)
    text(arquitectura, 0, 6, "APU futuro exige recursos, unidades, tarifas vigentes y gobierno; no se calcula aquí.", 9)
    return {"mapa-sdlc-v02": sdlc, "flujo-evaluacion-v02": flujo, "poc-arquitectura-v02": arquitectura}


def main():
    import pymupdf
    from reportlab.graphics import renderPDF, renderSVG
    DESTINO.mkdir(parents=True, exist_ok=False)
    for nombre, d in figuras().items():
        renderSVG.drawToFile(d, str(DESTINO / (nombre + ".svg")))
        renderPDF.drawToFile(d, str(DESTINO / (nombre + ".pdf")))
        with pymupdf.open(DESTINO / (nombre + ".pdf")) as pdf:
            pdf[0].get_pixmap(matrix=pymupdf.Matrix(2, 2)).save(DESTINO / (nombre + ".png"))
    print("Tres figuras nuevas SVG/PDF vectorial/PNG. Históricos intactos.")


if __name__ == "__main__":
    main()
