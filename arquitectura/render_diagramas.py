#!/usr/bin/env python3
"""Exporta SVG v1.1 a PDF vectorial/PNG con PyMuPDF, sin Chrome/WSL.

La apertura y dimensiones no prueban legibilidad: se requiere revisión visual.
No renderiza los directorios históricos por defecto.
"""

from pathlib import Path
import sys

import pymupdf

ROOT = Path(__file__).resolve().parents[1]


def renderizar(ruta):
    ruta = Path(ruta)
    with pymupdf.open(stream=ruta.read_bytes(), filetype="svg") as svg:
        pdf = svg.convert_to_pdf()
    with pymupdf.open(stream=pdf, filetype="pdf") as documento:
        assert len(documento) == 1
        documento.save(ruta.with_suffix(".pdf"))
        pagina = documento[0]
        pagina.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5), alpha=False).save(ruta.with_suffix(".png"))
        assert pagina.rect.width > 0 and pagina.rect.height > 0
    print(f"[OK] {ruta.name}: PDF/PNG exportados; legibilidad requiere revisión visual")


if __name__ == "__main__":
    rutas = [Path(p) for p in sys.argv[1:]] if sys.argv[1:] else sorted((ROOT / "arquitectura/revision-v1.1").glob("*.svg"))
    if not rutas:
        raise SystemExit("Genere primero los diagramas v1.1")
    for ruta in rutas:
        renderizar(ruta)
