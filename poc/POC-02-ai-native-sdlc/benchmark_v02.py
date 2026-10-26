"""Benchmark técnico local; crea solo resultados/<id> nuevo. No mide esfuerzo humano.

Dos tamaños (35 filas originales y 1000 sintéticas), API/CLI y suite histórica.
Congela parámetros antes de medir. No ejecuta generadores ni modifica históricos.
"""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import re
import statistics
import subprocess
import sys
import time
import unittest

sys.dont_write_bytecode = True
POC = Path(__file__).resolve().parent
ROOT = POC.parents[1]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def cargar_modulo(nombre, ruta):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", args.id):
        parser.error("ID inválido")
    out = POC / "resultados" / args.id
    out.mkdir(parents=True, exist_ok=False)
    originales = ROOT / "poc/POC-01-estimacion-historicos/datos"
    origenes = [originales / "costos.csv", originales / "metrados.csv"]
    hashes = {p.relative_to(ROOT).as_posix(): sha(p) for p in origenes + [POC / "src/validador.py", POC / "pruebas/test_validador.py", POC / "pruebas/casos.json"]}
    config = {"id": args.id, "inicio_utc": datetime.now(timezone.utc).isoformat(),
              "repeticiones_api_cli": 30, "calentamientos_api_cli": 3,
              "repeticiones_suite": 5, "calentamientos_suite": 1,
              "orden": "35 API, 35 CLI, 1000 API, 1000 CLI, suite; secuencial sin paralelismo del runner",
              "reloj": time.get_clock_info("perf_counter")._asdict() if hasattr(time.get_clock_info("perf_counter"), "_asdict") else str(time.get_clock_info("perf_counter")),
              "python": sys.version, "plataforma": platform.platform(), "maquina": platform.machine(),
              "procesadores_logicos": os.cpu_count(), "temporizador": "time.perf_counter",
              "hashes_antes": hashes, "script_sha256": sha(Path(__file__)),
              "limites": "Cache del SO caliente, carga externa/afinidad/frecuencia no controladas; no benchmark comparativo ni tiempo humano"}
    (out / "parametros_congelados.json").write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "benchmark_v02.py").write_bytes(Path(__file__).read_bytes())
    fixtures = out / "datos_1000"
    fixtures.mkdir()
    grandes = [fixtures / "costos.csv", fixtures / "metrados.csv"]
    for ruta, campo in zip(grandes, ["costo_real", "cantidad"]):
        with ruta.open("x", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["obra_id", "partida_id", campo])
            w.writerows(["BENCH", f"P{i:04}", "10.25" if campo == "costo_real" else "2.5"] for i in range(1000))
    val = cargar_modulo("benchmark_validador", POC / "src/validador.py")
    tiempos, comandos = [], []
    for etiqueta, rutas in [("35", origenes), ("1000", grandes)]:
        for modo in ["API", "CLI"]:
            comando = [sys.executable, "-X", "utf8", "-B", str(POC / "src/validador.py"), "--costos", str(rutas[0]), "--metrados", str(rutas[1])]
            if modo == "CLI":
                comandos.append({"filas": int(etiqueta), "argv": comando})
            for i in range(-3, 30):
                inicio = time.perf_counter()
                if modo == "API":
                    respuesta = val.validar(*rutas)
                    elapsed = time.perf_counter() - inicio
                else:
                    r = subprocess.run(comando, capture_output=True, text=True, encoding="utf-8", timeout=30)
                    elapsed = time.perf_counter() - inicio
                    assert r.returncode == 0 and not r.stderr
                    respuesta = json.loads(r.stdout)
                assert respuesta["estado"] == "VALIDO"
                assert respuesta["archivos"] == {"costos": {"filas": int(etiqueta)}, "metrados": {"filas": int(etiqueta)}}
                if i >= 0:
                    tiempos.append({"grupo": f"{modo}_{etiqueta}", "repeticion": i+1, "segundos": elapsed})
    tmp = out / "fixtures_suite"
    tmp.mkdir()
    os.environ["POC02_TMP"] = str(tmp)
    sys.path.insert(0, str(POC / "src"))
    suite_mod = cargar_modulo("test_validador_benchmark", POC / "pruebas/test_validador.py")
    for i in range(-1, 5):
        suite_mod.OBSERVACIONES.clear()
        suite = unittest.defaultTestLoader.loadTestsFromModule(suite_mod)
        with (out / ("suite_calentamiento.log" if i == -1 else f"suite_{i+1:02}.log")).open("x", encoding="utf-8") as log:
            inicio = time.perf_counter()
            result = unittest.TextTestRunner(stream=log, verbosity=2).run(suite)
            elapsed = time.perf_counter() - inicio
        assert result.wasSuccessful() and result.testsRun == 48
        if i >= 0:
            tiempos.append({"grupo": "SUITE_48", "repeticion": i+1, "segundos": elapsed})
    tmp.rmdir()
    resumen = {}
    for grupo in dict.fromkeys(t["grupo"] for t in tiempos):
        valores = [t["segundos"] for t in tiempos if t["grupo"] == grupo]
        resumen[grupo] = {"n": len(valores), "mediana_s": statistics.median(valores), "min_s": min(valores), "max_s": max(valores)}
    assert all(sha(ROOT / n) == h for n, h in hashes.items())
    record = {"parametros": config, "fin_utc": datetime.now(timezone.utc).isoformat(), "resumen": resumen,
              "tiempos_individuales": tiempos, "comandos_cli": comandos, "entradas_fuente_intactas": True,
              "esfuerzo_desarrollo": "NO DETERMINADO", "revision_humana": "NO DETERMINADO", "ahorro_manual": "NO DETERMINADO"}
    (out / "benchmark.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    with (out / "tiempos.csv").open("x", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["grupo", "repeticion", "segundos"])
        w.writeheader()
        w.writerows(tiempos)
    manifiesto = {p.relative_to(out).as_posix(): sha(p) for p in out.rglob("*") if p.is_file()}
    (out / "manifiesto.json").write_text(json.dumps(manifiesto, indent=2), encoding="utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
