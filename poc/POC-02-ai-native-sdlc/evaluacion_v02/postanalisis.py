"""Post-hoc audit of authentic logs; does NOT replace the frozen evaluator.

Creates only NEW files inside resultados/S6-002. Refuses existing audit output.
No implementation changes, no rewriting expectations or original results.
"""
from collections import Counter
import csv
import datetime
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "resultados" / "S6-002"
SCHEMA_ISSUE = "Conteos de archivos no son enteros no negativos por archivo lógico"
LINE_ISSUE = "Ubicación ausente: costos/5/None/E_SIN_METRADO"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot():
    return {p.relative_to(OUT).as_posix(): sha(p) for p in OUT.rglob("*") if p.is_file()}


def main():
    destination = OUT / "postanalisis.json"
    if destination.exists():
        raise SystemExit("Postanálisis ya existe; no sobrescribir")
    original_snapshot = snapshot()
    cases = json.loads((HERE / "casos.json").read_text(encoding="utf-8"))["casos"]
    outcomes = []
    for case in cases:
        folder = OUT / case["id"]
        original = json.loads((folder / "resultado.json").read_text(encoding="utf-8"))
        residual = [issue for issue in original["issues"] if issue != SCHEMA_ISSUE]
        rows = []
        for run in original["runs"]:
            obj = run["json"]
            # Accept nested count schema; contract does not mandate flat counts.
            if not all(isinstance(obj["archivos"][logical], dict) and type(obj["archivos"][logical].get("filas")) is int and obj["archivos"][logical]["filas"] >= 0 for logical in ("costos", "metrados")):
                residual.append("Conteo anidado inválido")
            if case["id"] == "A20_multilinea_correspondencia":
                with (folder / "costos.csv").open(encoding="utf-8", newline="") as f:
                    reader = csv.reader(f, strict=True)
                    physical = [(row, reader.line_num) for row in reader]
                expected_line = next(line for row, line in physical if row[:2] == ["OB-1", "P-2"])
                if expected_line != 4 or not any(e["codigo"] == "E_SIN_METRADO" and e["fila"] == expected_line for e in obj["errores"]):
                    residual.append("Fila física real no coincide con salida")
                else:
                    residual = [issue for issue in residual if issue != LINE_ISSUE]
            # Logs must actually match the hashes recorded by the original runner.
            for stream in ("stdout", "stderr"):
                log = folder / f"seed-{run['seed']}.{stream}.log"
                if sha(log) != run[f"{stream}_sha256"]:
                    residual.append(f"Hash de log {stream} alterado")
            rows.append({"seed": run["seed"], "returncode": run["returncode"],
                         "estado": obj["estado"], "codigos": dict(Counter(e["codigo"] for e in obj["errores"])),
                         "archivos": obj["archivos"], "seconds": run["seconds"]})
        outcomes.append({"id": case["id"], "frozen_passed": original["passed"],
                         "posthoc_no_validator_defect": not residual,
                         "residual_issues": sorted(set(residual)), "runs": rows})
    # Verify refusal when reusing an output ID; no target subprocess is reached.
    refusal = subprocess.run([sys.executable, "-X", "utf8", "-B", str(HERE / "runner.py"), "--id", "S6-002"], cwd=ROOT, capture_output=True, timeout=30)
    unchanged = snapshot() == original_snapshot
    refusal_ok = refusal.returncode != 0 and b"FileExistsError" in refusal.stderr and unchanged
    for stream in ("stdout", "stderr"):
        with (OUT / f"rechazo_id_existente.{stream}.log").open("xb") as f:
            f.write(getattr(refusal, stream))
    freeze = json.loads((HERE / "congelacion.json").read_text(encoding="utf-8"))
    freeze_unchanged = all(sha(ROOT / path) == digest for path, digest in freeze["sha256"].items())
    original_hashes = json.loads((OUT / "originales_antes.json").read_text(encoding="utf-8"))
    originals_still_unchanged = all(sha(ROOT / path) == digest for path, digest in original_hashes.items())
    input_hashes = json.loads((OUT / "entradas_sha256.json").read_text(encoding="utf-8"))
    inputs_still_unchanged = all(sha(OUT / path) == digest for path, digest in input_hashes.items())
    report = {"utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "nature": "POST HOC: errores del evaluador identificados tras leer salidas e implementación; no es nueva aceptación precongelada.",
              "frozen_passed": sum(x["frozen_passed"] for x in outcomes),
              "total": len(outcomes),
              "posthoc_cases_without_validator_defect": sum(x["posthoc_no_validator_defect"] for x in outcomes),
              "evaluator_defects": [
                  {"id": "EV-01", "affects": "35/35", "reason": "El contrato no obliga archivos.costos a ser entero; {filas: entero} satisface filas leídas por archivo lógico."},
                  {"id": "EV-02", "affects": "A20", "reason": "Cabecera línea 1; primer registro líneas 2-3; segundo registro línea 4, no 5."}],
              "reuse_id_refused": refusal_ok, "reuse_returncode": refusal.returncode,
              "existing_evidence_unchanged_during_refusal": unchanged,
              "frozen_files_unchanged": freeze_unchanged,
              "originals_still_unchanged": originals_still_unchanged,
              "inputs_still_unchanged": inputs_still_unchanged,
              "cases": outcomes}
    with destination.open("x", encoding="utf-8", newline="\n") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps({k: v for k, v in report.items() if k != "cases"}, ensure_ascii=False, indent=2))
    return 0 if all(x["posthoc_no_validator_defect"] for x in outcomes) and refusal_ok and freeze_unchanged and originals_still_unchanged and inputs_still_unchanged else 1


if __name__ == "__main__":
    raise SystemExit(main())
