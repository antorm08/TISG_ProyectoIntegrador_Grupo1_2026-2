#!/usr/bin/env python3
"""Renderiza los diagramas SVG de `arquitectura/` a PNG y PDF con Chrome headless.

Requiere Google Chrome de Windows (WSL). Uso:
    python3 arquitectura/render_diagramas.py [svg ...]

Si no se indican SVG, se renderizan todos los `.svg` de `arquitectura/as-is`
y `arquitectura/to-be`.

Además verifica que el PNG no quede en blanco contando sus píxeles:
todo diagrama debe superar el porcentaje mínimo de contenido.
"""

import os
import struct
import subprocess
import sys
import zlib

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
MIN_COBERTURA = 1.0  # % mínimo de píxeles que no son blanco


def a_windows(ruta):
    """Convierte una ruta WSL a una ruta Windows estilo C:/..."""
    ruta = os.path.abspath(ruta)
    if ruta.startswith("/mnt/"):
        partes = ruta.split("/")[2:]
        return "/".join([partes[0].upper() + ":"] + partes[1:])
    return ruta


def decodificar_png(ruta):
    """Decodifica un PNG simple (RGB/RGBA) y devuelve (ancho, alto, pixeles)."""
    datos = open(ruta, "rb").read()
    assert datos[:8] == b"\x89PNG\r\n\x1a\n", "no es PNG"
    pos, raw = 8, b""
    idat, head = [], None
    while pos < len(datos):
        largo = struct.unpack(">I", datos[pos:pos + 4])[0]
        tipo = datos[pos + 4:pos + 8]
        cuerpo = datos[pos + 8:pos + 8 + largo]
        if tipo == b"IHDR":
            head = struct.unpack(">IIBBBBB", cuerpo)
        elif tipo == b"IDAT":
            idat.append(cuerpo)
        elif tipo == b"IEND":
            break
        pos += 12 + largo
    ancho, alto, prof, tipo_color, comp, filt, ent = head
    assert comp == 0 and filt == 0 and ent == 0, "PNG con filtros o interlazado no soportados"
    assert prof == 8, "solo PNG de 8 bits por canal"
    canales = 4 if datos else 0
    crudo = zlib.decompress(b"".join(idat))
    # determinar canales desde el primer byte de cada scanline por longitudes conocidas
    for c in (3, 4):
        if (len(crudo) // alto) == ancho * c + 1:
            canales = c
            break
    else:
        raise AssertionError("longitud de datos inesperada")
    stride = ancho * canales
    salida = bytearray()
    prev = bytearray(stride)
    i = 0
    for _ in range(alto):
        f = crudo[i]
        fila = bytearray(crudo[i + 1:i + 1 + stride])
        i += 1 + stride
        if f == 1:
            for x in range(canales, stride):
                fila[x] = (fila[x] + fila[x - canales]) & 0xFF
        elif f == 2:
            for x in range(stride):
                fila[x] = (fila[x] + prev[x]) & 0xFF
        elif f == 3:
            for x in range(stride):
                izq = fila[x - canales] if x >= canales else 0
                fila[x] = (fila[x] + ((izq + prev[x]) >> 1)) & 0xFF
        elif f == 4:
            for x in range(stride):
                a = fila[x - canales] if x >= canales else 0
                b = prev[x]
                cc = prev[x - canales] if x >= canales else 0
                p = a + b - cc
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - cc)
                fila[x] = (fila[x] + (a if pa <= pb and pa <= pc else b if pb <= pc else cc)) & 0xFF
        salida.extend(fila)
        prev = fila
    return ancho, alto, canales, bytes(salida)


def cobertura(png):
    ancho, alto, canales, pix = decodificar_png(png)
    no_blancos = 0
    total = ancho * alto
    for p in range(total):
        o = p * canales
        if not (pix[o] > 245 and pix[o + 1] > 245 and pix[o + 2] > 245):
            no_blancos += 1
    return ancho, alto, 100.0 * no_blancos / total


def dimensiones_svg(svg):
    """Lee width/height del elemento raíz del SVG (deben ser valores enteros)."""
    import re
    with open(svg, encoding="utf-8") as f:
        cabecera = f.read(600)
    m = re.search(r'width="(\d+)"\s+height="(\d+)"', cabecera)
    if not m:
        raise ValueError(f"SVG sin width/height numéricos: {svg}")
    return int(m.group(1)), int(m.group(2))


def renderizar(svg):
    svg_abs = os.path.abspath(svg)
    base, _ = os.path.splitext(svg_abs)
    png, pdf = base + ".png", base + ".pdf"
    win_svg = a_windows(svg_abs)
    win_png = a_windows(png)
    win_pdf = a_windows(pdf)
    ancho_svg, alto_svg = dimensiones_svg(svg_abs)
    comun = ["--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1"]
    if not os.path.exists(CHROME):
        print(f"[!] Chrome no encontrado: {CHROME}")
        return False
    subprocess.run([CHROME, *comun, f"--window-size={ancho_svg},{alto_svg}",
                    f"--screenshot={win_png}", f"file:///{win_svg}"],
                   check=True, capture_output=True)
    subprocess.run([CHROME, *comun, f"--no-pdf-header-footer",
                    f"--print-to-pdf={win_pdf}", f"file:///{win_svg}"],
                   check=True, capture_output=True)
    if not os.path.exists(png) or not os.path.exists(pdf):
        print(f"[X] Fallo al renderizar: {svg}")
        return False
    ancho, alto, pct = cobertura(png)
    ok = pct >= MIN_COBERTURA
    marca = "OK" if ok else "BAJO"
    print(f"[{marca}] {os.path.relpath(svg_abs, RAIZ)}  {ancho}x{alto}px  "
          f"contenido {pct:.2f}%  -> .png/.pdf")
    return ok


def main():
    objetivos = sys.argv[1:]
    if not objetivos:
        objetivos = []
        for sub in ("as-is", "to-be"):
            d = os.path.join(RAIZ, "arquitectura", sub)
            if os.path.isdir(d):
                objetivos += [os.path.join(d, f) for f in sorted(os.listdir(d))
                              if f.endswith(".svg")]
    if not objetivos:
        print("No hay diagramas SVG para renderizar.")
        sys.exit(1)
    fallos = [s for s in objetivos if not renderizar(s)]
    if fallos:
        print("\nDiagramas con problema:")
        for f in fallos:
            print(" -", f)
        sys.exit(1)
    print(f"\n[{len(objetivos)}] diagramas renderizados y verificados.")


if __name__ == "__main__":
    main()
