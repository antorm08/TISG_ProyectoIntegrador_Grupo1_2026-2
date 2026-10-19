#!/usr/bin/env python3
"""POC-01: Estimación de partidas con históricos vs. línea base manual.

Valida H1. Calcula el ratio histórico (costo/unidad) por partida desde
obras cerradas, estima una obra nueva y compara contra una línea base
manual simulada. Sin dependencias externas.

Uso:
    python3 synthetic_erp_data.py   # primero genera los datos
    python3 experimento_bi.py

Salidas: ../resultados/resultados.csv
"""

import csv
import os
import random
from collections import defaultdict

SEED = 20261002
SIGMA_MANUAL = 0.25  # variabilidad de estimación SIN histórico integrado (supuesto)
UMBRAL_MAPE = 0.15   # H1: MAPE del método analítico <= 15%
UMBRAL_REDUC = 0.30  # H1: reduccion >= 30% del error vs. base manual

BASE = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(os.path.dirname(BASE), "datos")
RESULTADOS = os.path.join(os.path.dirname(BASE), "resultados")


def leer(nombre):
    with open(os.path.join(DATOS, nombre), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def escribir(nombre, header, rows):
    os.makedirs(RESULTADOS, exist_ok=True)
    with open(os.path.join(RESULTADOS, nombre), "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(header)
        wr.writerows(rows)


def mape(estimado, real):
    if real == 0:
        return 0.0
    return abs(estimado - real) / abs(real)


def main():
    random.seed(SEED)

    catalogo = {r["partida_id"]: r for r in leer("catalogo_partidas.csv")}
    costos = leer("costos.csv")
    # metrados por obra y partida
    cant_por_obra = {(r["obra_id"], r["partida_id"]): float(r["cantidad"])
                     for r in leer("metrados.csv")}

    # Ratios históricos: costo total / cantidad total por partida (solo obras cerradas)
    costo_por_partida = defaultdict(float)
    cant_por_partida = defaultdict(float)
    for r in costos:
        if r["obra_id"] == "OB-N01":
            continue
        pid = r["partida_id"]
        costo_por_partida[pid] += float(r["costo_real"])
        cant_por_partida[pid] += cant_por_obra.get((r["obra_id"], pid), 0.0)

    ratio_historico = {}
    sin_historico = []
    for pid, c_tot in costo_por_partida.items():
        if cant_por_partida[pid] > 0:
            ratio_historico[pid] = c_tot / cant_por_partida[pid]

    # Obra nueva a estimar y su costo real (verdad de referencia)
    nueva = {r["partida_id"]: float(r["cantidad_presupuestada"]) for r in leer("obra_nueva.csv")}
    real = {r["partida_id"]: float(r["costo_real"]) for r in leer("obra_nueva_real.csv")}

    filas = []
    errs_modelo, errs_manual = [], []
    for pid, cantidad in sorted(nueva.items()):
        # Método analítico: ratio histórico (fallback: costo unitario del catálogo)
        if pid in ratio_historico:
            costo_modelo = cantidad * ratio_historico[pid]
            origen = "historico"
        else:
            costo_modelo = cantidad * float(catalogo[pid]["costo_unitario_base"])
            origen = "catalogo_fallback"
            sin_historico.append(pid)

        # Línea base manual: simulada con variabilidad sigma_manual sobre el real
        costo_real_p = real[pid]
        costo_manual = costo_real_p * (1 + random.gauss(0.0, SIGMA_MANUAL))

        e_modelo = mape(costo_modelo, costo_real_p)
        e_manual = mape(costo_manual, costo_real_p)
        errs_modelo.append(e_modelo)
        errs_manual.append(e_manual)

        filas.append([
            pid, cantidad, f"{ratio_historico.get(pid, float(catalogo[pid]['costo_unitario_base'])):.2f}",
            origen, f"{costo_real_p:.2f}", f"{costo_manual:.2f}", f"{costo_modelo:.2f}",
            f"{e_manual:.4f}", f"{e_modelo:.4f}",
        ])

    escribir(
        "resultados.csv",
        ["partida_id", "cantidad", "ratio_hist", "origen_ratio",
         "costo_real", "costo_manual", "costo_modelo", "error_manual", "error_modelo"],
        filas,
    )

    mape_modelo = sum(errs_modelo) / len(errs_modelo)
    mape_manual = sum(errs_manual) / len(errs_manual)
    reduccion = (mape_manual - mape_modelo) / mape_manual if mape_manual else 0.0

    print("=" * 66)
    print("POC-01 — Estimación con históricos vs. línea base manual")
    print("=" * 66)
    print(f"Obras cerradas usadas   : {len(set(r['obra_id'] for r in costos if r['obra_id'] != 'OB-N01'))}")
    print(f"Partidas de la obra nueva: {len(nueva)}")
    if sin_historico:
        print(f"Partidas sin histórico (fallback catálogo): {', '.join(sin_historico)}")
    print("-" * 66)
    print(f"MAPE línea base manual : {mape_manual * 100:6.2f} %")
    print(f"MAPE método analítico  : {mape_modelo * 100:6.2f} %")
    print(f"Reducción de error     : {reduccion * 100:6.2f} %")
    print("-" * 66)
    c_umbral = mape_modelo <= UMBRAL_MAPE
    c_reduc = reduccion >= UMBRAL_REDUC
    print(f"¿MAPE analítico <= {UMBRAL_MAPE*100:.0f}%?  {'SÍ' if c_umbral else 'NO'}")
    print(f"¿Reducción >= {UMBRAL_REDUC*100:.0f}%?       {'SÍ' if c_reduc else 'NO'}")
    if c_umbral and c_reduc:
        print("DECISIÓN: CONTINUAR (H1 respaldada en este experimento sintético)")
    elif c_umbral or c_reduc:
        print("DECISIÓN: MODIFICAR el modelo o los umbrales")
    else:
        print("DECISIÓN: DETENER H1 (no se observa reducción)")
    print("=" * 66)
    print("Limitación: datos sintéticos; el método subestima obras más difíciles")
    print("porque el ratio histórico promedia tipos. Ajustar por tipo en la fase 2.")
    print(f"Detalle por partida: {os.path.join('..', 'resultados', 'resultados.csv')}")


if __name__ == "__main__":
    main()
