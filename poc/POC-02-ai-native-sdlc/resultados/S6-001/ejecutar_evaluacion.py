"""Escribe exclusivamente una corrida NUEVA bajo resultados/<id>; nunca sobrescribe."""
import argparse
import csv
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
import unittest

sys.dont_write_bytecode = True
POC = Path(__file__).resolve().parent
ROOT = POC.parents[1]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", args.id):
        parser.error("ID inválido")
    congelacion = json.loads((ROOT / "evidencias/semana-06/congelacion_previa.json").read_text(encoding="utf-8"))
    for nombre, esperado in congelacion["sha256"].items():
        if sha(ROOT / nombre) != esperado:
            raise RuntimeError(f"Cambió artefacto congelado: {nombre}")
    salida = POC / "resultados" / args.id
    salida.mkdir(parents=True, exist_ok=False)
    inicio = dt.datetime.now(dt.timezone.utc).isoformat()
    archivos = [POC / n for n in ["src/validador.py", "pruebas/test_validador.py", "pruebas/casos.json", "ejecutar_evaluacion.py"]]
    for archivo in archivos:
        shutil.copyfile(archivo, salida / archivo.name)
    datos = ROOT / "poc/POC-01-estimacion-historicos/datos"
    originales = [datos / n for n in ["costos.csv", "metrados.csv"]]
    antes = {p.name: sha(p) for p in originales}
    temporal = salida / "fixtures_temporales"
    temporal.mkdir()
    os.environ["POC02_TMP"] = str(temporal)
    spec = importlib.util.spec_from_file_location("test_validador", POC / "pruebas/test_validador.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    suite = unittest.defaultTestLoader.loadTestsFromModule(modulo)

    class Resultado(unittest.TextTestResult):
        def startTest(self, test):
            super().startTest(test)
            self.reloj = time.perf_counter()

        def registrar(self, test, estado):
            registros.append({"test": test.id(), "estado": estado, "segundos": time.perf_counter() - self.reloj})

        def addSuccess(self, test):
            super().addSuccess(test)
            self.registrar(test, "OK")

        def addFailure(self, test, err):
            super().addFailure(test, err)
            self.registrar(test, "FALLO")

        def addError(self, test, err):
            super().addError(test, err)
            self.registrar(test, "ERROR")

    registros = []
    reloj = time.perf_counter()
    with (salida / "unittest.log").open("x", encoding="utf-8") as log:
        resultado = unittest.TextTestRunner(stream=log, verbosity=2, resultclass=Resultado).run(suite)
    segundos_suite = time.perf_counter() - reloj
    comando = [sys.executable, "-X", "utf8", "-B", str(POC / "src/validador.py"), "--costos", str(originales[0]), "--metrados", str(originales[1])]
    reloj = time.perf_counter()
    cli = subprocess.run(comando, capture_output=True, text=True, encoding="utf-8", timeout=30)
    segundos_cli = time.perf_counter() - reloj
    (salida / "cli_stdout.json").write_text(cli.stdout, encoding="utf-8")
    (salida / "cli_stderr.log").write_text(cli.stderr, encoding="utf-8")
    casos = modulo.OBSERVACIONES
    validos = [c for c in casos if c["valido_esperado"]]
    invalidos = [c for c in casos if not c["valido_esperado"]]
    metricas = {"casos": len(casos), "correctos": sum(c["correcto"] for c in casos),
                "Q1_porcentaje": 100 * sum(c["correcto"] for c in casos) / len(casos) if casos else None,
                "validos": len(validos), "invalidos": len(invalidos),
                "Q2_falsas_aceptaciones": sum(c["valido_observado"] for c in invalidos),
                "Q3_falsos_rechazos": sum(not c["valido_observado"] for c in validos),
                "tests_total": resultado.testsRun, "tests_fallos": len(resultado.failures), "tests_errores": len(resultado.errors),
                "segundos_suite": segundos_suite, "segundos_cli": segundos_cli,
                "M1_desarrollo": "NO DETERMINADO", "M2_revision_humana": "NO DETERMINADO", "M4_ahorro": "NO DETERMINADO"}
    intactos = antes == {p.name: sha(p) for p in originales}
    registro = {"id": args.id, "inicio_utc": inicio, "fin_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                "python": sys.version, "evaluacion": "PUBLICA NO CIEGA NO INDEPENDIENTE", "metricas": metricas,
                "aceptacion_tecnica": resultado.wasSuccessful() and len(casos) == 36 and all(c["correcto"] and c["entradas_intactas"] for c in casos) and cli.returncode == 0 and intactos,
                "revision_humana": "PENDIENTE", "originales_intactos": intactos, "hashes_originales": antes,
                "cli_exit": cli.returncode, "casos": casos, "tests": registros}
    (salida / "resultados.json").write_text(json.dumps(registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (salida / "casos.csv").open("x", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(casos[0]) if casos else ["id"])
        w.writeheader()
        w.writerows(casos)
    manifiesto = {p.name: sha(p) for p in salida.iterdir() if p.is_file()}
    (salida / "manifiesto.json").write_text(json.dumps(manifiesto, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"id": args.id, "aceptacion_tecnica": registro["aceptacion_tecnica"], **metricas}, ensure_ascii=False, indent=2))
    return 0 if registro["aceptacion_tecnica"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
