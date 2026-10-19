#!/usr/bin/env python3
"""Verificación mínima del POC-01: ejecuta el pipeline y valida umbrales de H1."""

import os
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
DATOS = os.path.join(ROOT, "datos")
RESULTADOS = os.path.join(ROOT, "resultados")


def run(script):
    subprocess.run([sys.executable, os.path.join(ROOT, "src", script)], check=True)


def main():
    run("synthetic_erp_data.py")
    run("experimento_bi.py")

    ruta = os.path.join(RESULTADOS, "resultados.csv")
    assert os.path.exists(ruta), "No se generó resultados.csv"
    with open(ruta, encoding="utf-8") as f:
        lineas = f.read().strip().splitlines()
    assert len(lineas) >= 2, "resultados.csv sin filas de datos"

    # MAPE analítico por partida debe ser <= 15 % en promedio
    encabezado = lineas[0].split(",")
    i_modelo = encabezado.index("error_modelo")
    i_manual = encabezado.index("error_manual")
    errores_m, errores_b = [], []
    for ln in lineas[1:]:
        cols = ln.split(",")
        errores_m.append(float(cols[i_modelo]))
        errores_b.append(float(cols[i_manual]))
    mape_modelo = sum(errores_m) / len(errores_m)
    mape_manual = sum(errores_b) / len(errores_b)
    reduccion = (mape_manual - mape_modelo) / mape_manual

    assert mape_modelo <= 0.15, f"MAPE analítico {mape_modelo:.2%} > 15%"
    assert reduccion >= 0.30, f"Reducción {reduccion:.2%} < 30%"
    print(f"[OK] H1 validada en el experimento sintético: "
          f"MAPE {mape_modelo:.2%} (reducción {reduccion:.2%}).")


if __name__ == "__main__":
    main()
