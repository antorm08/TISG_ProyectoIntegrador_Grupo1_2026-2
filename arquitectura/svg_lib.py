#!/usr/bin/env python3
"""Utilidades mínimas para generar los SVG del Hito I (Semana 5)."""

FUENTE = "Arial, Helvetica, sans-serif"
T_INK = "#0F172A"
T_SUB = "#475569"

C_ACTOR = ("#FFF7ED", "#B45309")
C_APP = ("#DBEAFE", "#1D4ED8")
C_DATA = ("#DCFCE7", "#15803D")
C_INFRA = ("#E2E8F0", "#475569")
C_EXT = ("#EDE9FE", "#6D28D9")
C_GAP = ("#F8FAFC", "#94A3B8")
C_SHEET = ("#FEF3C7", "#B45309")
C_DARK = ("#E0F2FE", "#0369A1")
C_WARN = ("#FFF7ED", "#B45309")
C_GREY = ("#E2E8F0", "#475569")
C_CLOUD = ("#F5F3FF", "#6D28D9")


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def rect(x, y, w, h, fill, stroke, dash=None, rx=6, sw=2):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def txt(x, y, s, size=14, fill=T_INK, bold=False, anchor="start", italic=False):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    b = ' font-weight="bold"' if bold else ""
    i = ' font-style="italic"' if italic else ""
    return (f'<text x="{x}" y="{y}" font-family="{FUENTE}" font-size="{size}" '
            f'fill="{fill}"{a}{b}{i}>{esc(s)}</text>')


def multi(x, y, lineas, size=11, fill=T_SUB, anchor="middle", lh=14):
    out = [f'<text x="{x}" y="{y}" font-family="{FUENTE}" font-size="{size}" '
           f'fill="{fill}" text-anchor="{anchor}">']
    for k, l in enumerate(lineas):
        dy = 0 if k == 0 else lh
        out.append(f'<tspan x="{x}" dy="{dy}">{esc(l)}</tspan>')
    out.append("</text>")
    return "".join(out)


def caja(x, y, w, h, colores, titulo, subs=(), tsize=13.5, ssize=10.5, dash=None):
    fill, stroke = colores
    partes = [rect(x, y, w, h, fill, stroke, dash=dash)]
    ty = y + 20 if subs else y + h / 2 + 5
    if len(subs) > 1:
        ty = y + 19
    partes.append(txt(x + w / 2, ty, titulo, size=tsize, bold=True, anchor="middle"))
    if subs:
        partes.append(multi(x + w / 2, ty + 11, list(subs), size=ssize, lh=13))
    return "".join(partes)


def label_capa(x, y, w, h, texto):
    return (rect(x, y, w, h, "#F1F5F9", "#94A3B8", dash="6 4", rx=4)
            + txt(x + w / 2, y + h / 2 + 5, texto, size=13, fill=T_SUB, bold=True,
                  anchor="middle"))


def defs():
    return ('<defs><marker id="a0" markerWidth="10" markerHeight="8" refX="9" '
            'refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 z" fill="#334155"/>'
            '</marker></defs>')


def flecha(pts, dash=None, w=2, mid=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    p = " ".join(f"{x},{y}" for x, y in pts)
    etiqueta = txt(mid[0], mid[1], mid[2], size=10.5, fill=T_SUB, anchor="middle") if mid else ""
    return (f'<polyline points="{p}" fill="none" stroke="#334155" stroke-width="{w}"{d} '
            f'marker-end="url(#a0)"/>' + etiqueta)


def leyenda(x, y, items, ancho_col=350, alto=26, cols=4, size=11.5):
    out = []
    for i, (tipo, col, texto) in enumerate(items):
        cx = x + (i % cols) * ancho_col
        cy = y + (i // cols) * (alto + 10)
        if tipo in ("box", "dashbox"):
            out.append(rect(cx, cy + 2, 34, 17, col[0], col[1],
                            dash="5 3" if tipo == "dashbox" else None, rx=3, sw=1.5))
        elif tipo == "line":
            out.append(f'<polyline points="{cx},{cy + 11} {cx + 34},{cy + 11}" fill="none" '
                       f'stroke="#334155" stroke-width="2" marker-end="url(#a0)"/>')
        elif tipo == "dashed":
            out.append(f'<line x1="{cx}" y1="{cy + 11}" x2="{cx + 34}" y2="{cy + 11}" '
                       f'stroke="#334155" stroke-width="2" stroke-dasharray="6 4"/>')
        out.append(txt(cx + 42, cy + 15, texto, size=size))
    return "".join(out)


def cabecera(titulo, sub, ancho):
    return (f'<rect width="{ancho}" height="70" fill="#1F4E79"/>'
            + txt(30, 32, titulo, size=22, fill="#FFFFFF", bold=True)
            + txt(30, 56, sub, size=13, fill="#C7DDF3"))


def marco(ancho, alto, margen=20, top=78):
    return rect(margen, top, ancho - 2 * margen, alto - top - margen,
                "#FFFFFF", "#CBD5E1", rx=0, sw=1.5)


def svg(ancho, alto, cuerpo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" '
            f'viewBox="0 0 {ancho} {alto}">\n'
            f'<rect width="{ancho}" height="{alto}" fill="#FFFFFF"/>\n'
            + cuerpo + "\n</svg>\n")
