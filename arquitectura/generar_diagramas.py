#!/usr/bin/env python3
"""Genera los cuatro diagramas SVG corregidos del Hito I (v1.1).

Uso:
    python3 arquitectura/generar_diagramas.py

Escribe:
    arquitectura/revision-v1.1/figura-*.svg

Los originales as-is/to-be y sus generadores figuras_a/b son históricos
y contienen el stack sustituido documentalmente; no se regeneran.
"""

import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from figuras_revision import (figura_asis, figura_flujo,  # noqa: E402
                              figura_dependencias, figura_tobe)

SALIDAS = [
    ("revision-v1.1", "figura-01-arquitectura-as-is.svg", figura_asis),
    ("revision-v1.1", "figura-02-flujo-de-informacion-as-is.svg", figura_flujo),
    ("revision-v1.1", "figura-03-arquitectura-to-be-v0-1.svg", figura_tobe),
    ("revision-v1.1", "figura-04-mapa-de-dependencias.svg", figura_dependencias),
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
