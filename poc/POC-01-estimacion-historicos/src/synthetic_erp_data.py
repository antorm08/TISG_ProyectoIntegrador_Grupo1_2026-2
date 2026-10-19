#!/usr/bin/env python3
"""Genera extractos sintéticos del ERP para el POC-01.

Constructora Andina S.A.C. (caso ficticio). Genera históricos de obras
cerradas + una obra nueva a estimar. Determinista (semilla fija).

Uso:
    python3 synthetic_erp_data.py

Salidas: ../datos/*.csv
"""

import csv
import os
import random

SEED = 20261002
N_OBRAS_CERRADAS = 6
BASE = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(os.path.dirname(BASE), "datos")

# Catálogo sintético: partida -> (unidad, costo unitario base, HH por unidad base)
CATALOGO = [
    ("EXC-01", "Excavación en material tipo II", "m3", 48.0, 0.35),
    ("HOR-01", "Hormigón estructural f'c=210", "m3", 320.0, 1.20),
    ("FIL-01", "Fierro de refuerzo colocado", "t", 4100.0, 8.50),
    ("CIM-01", "Cimbra en madera", "m2", 42.0, 0.45),
    ("ALB-01", "Albañilería en ladrillo", "m2", 65.0, 0.80),
    ("INS-01", "Instalaciones sanitarias", "punto", 240.0, 1.10),
    ("INS-02", "Instalaciones eléctricas", "punto", 195.0, 0.90),
    ("ACB-01", "Acabados interiores", "m2", 150.0, 1.40),
]

# Factor de dificultad por tipo de obra (afecta costo y productividad)
TIPOS = {
    "Vivienda multifamiliar": 1.00,
    "Edificio comercial": 1.12,
    "Nave industrial": 0.92,
}


def _ruido(sigma):
    return random.gauss(0.0, sigma)


def main():
    random.seed(SEED)
    os.makedirs(DATOS, exist_ok=True)

    obras = []
    tareo = []
    metrados = []
    costos = []

    # --- Obras cerradas (histórico) ---
    for i in range(1, N_OBRAS_CERRADAS + 1):
        obra_id = f"OB-C{i:02d}"
        tipo = random.choice(list(TIPOS))
        factor = TIPOS[tipo]
        area = round(random.uniform(1200, 5200), 0)
        obras.append((obra_id, f"Obra cerrada {i}", tipo, area, "Cerrada", 2020 + i))

        # Cada obra usa un subconjunto de partidas
        usadas = random.sample(CATALOGO, random.randint(5, len(CATALOGO)))
        for (pid, desc, unidad, costo_base, hh_base) in usadas:
            cantidad = round(random.uniform(40, 900), 1)

            # Ratios "verdaderos" de esta obra (con variación natural + dificultad)
            costo_unit = costo_base * factor * (1 + _ruido(0.08))
            hh_unit = hh_base * (1 + _ruido(0.10))
            costo_real = round(cantidad * costo_unit, 2)
            horas = round(cantidad * hh_unit, 1)

            metrados.append((obra_id, pid, cantidad))
            costos.append((obra_id, pid, costo_real))
            tareo.append((obra_id, pid, horas))

    # --- Obra nueva a estimar (solo cantidades; costo real oculto para el método) ---
    nueva_id = "OB-N01"
    factor_nueva = TIPOS["Edificio comercial"]
    obras.append((nueva_id, "Obra nueva (a estimar)", "Edificio comercial", 3100.0, "En ejecución", 2027))

    catalogo_map = {c[0]: c for c in CATALOGO}
    usadas_nueva = random.sample(CATALOGO, 6)
    obra_nueva = []      # entrada del método: cantidades
    obra_nueva_real = []  # verdad de referencia (para evaluación, no para estimar)
    for (pid, desc, unidad, costo_base, hh_base) in usadas_nueva:
        cantidad = round(random.uniform(60, 700), 1)
        obra_nueva.append((pid, cantidad))
        costo_unit_real = costo_base * factor_nueva * (1 + _ruido(0.06))
        obra_nueva_real.append((pid, round(cantidad * costo_unit_real, 2)))

    # --- Escritura ---
    def w(name, header, rows):
        with open(os.path.join(DATOS, name), "w", newline="", encoding="utf-8") as f:
            wr = csv.writer(f)
            wr.writerow(header)
            wr.writerows(rows)

    w("obras.csv",
      ["obra_id", "nombre", "tipo", "area_m2", "estado", "anio"], obras)
    w("catalogo_partidas.csv",
      ["partida_id", "descripcion", "unidad", "costo_unitario_base", "hh_unitario_base"], CATALOGO)
    w("metrados.csv", ["obra_id", "partida_id", "cantidad"], metrados)
    w("costos.csv", ["obra_id", "partida_id", "costo_real"], costos)
    w("tareo.csv", ["obra_id", "partida_id", "horas_hombre"], tareo)
    w("obra_nueva.csv", ["partida_id", "cantidad_presupuestada"], obra_nueva)
    w("obra_nueva_real.csv", ["partida_id", "costo_real"], obra_nueva_real)

    print(f"[OK] Datos sintéticos en {DATOS}")
    print(f"     Obras cerradas: {N_OBRAS_CERRADAS} | Partidas catalogo: {len(CATALOGO)}")
    print(f"     Filas metrados: {len(metrados)} | costos: {len(costos)} | tareo: {len(tareo)}")
    print("     Semilla:", SEED)


if __name__ == "__main__":
    main()
