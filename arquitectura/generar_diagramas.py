#!/usr/bin/env python3
"""Genera los cuatro diagramas SVG del Hito I (Semana 5).

Uso:
    python3 arquitectura/generar_diagramas.py

Escribe:
    arquitectura/as-is/figura-01-arquitectura-as-is.svg
    arquitectura/as-is/figura-02-flujo-de-informacion-as-is.svg
    arquitectura/to-be/figura-03-arquitectura-to-be-v0-1.svg
    arquitectura/to-be/figura-04-mapa-de-dependencias.svg
"""

import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from figuras_a import figura_asis, figura_flujo          # noqa: E402
from figuras_b import figura_dependencias, figura_tobe   # noqa: E402

SALIDAS = [
    ("as-is", "figura-01-arquitectura-as-is.svg", figura_asis),
    ("as-is", "figura-02-flujo-de-informacion-as-is.svg", figura_flujo),
    ("to-be", "figura-03-arquitectura-to-be-v0-1.svg", figura_tobe),
    ("to-be", "figura-04-mapa-de-dependencias.svg", figura_dependencias),
]


def main():
    for carpeta, nombre, generador in SALIDAS:
        destino = os.path.join(AQUI, carpeta, nombre)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        contenido = generador()
        with open(destino, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"[OK] {os.path.relpath(destino, AQUI)}  ({len(contenido)} bytes)")


if __name__ == "__main__":
    main()
