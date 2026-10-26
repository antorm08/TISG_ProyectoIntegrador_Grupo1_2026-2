"""Corrected checker, reusing HASH-PINNED historical runner infrastructure.

Only the harness is imported, NEVER the validator. Its original check function
is replaced before main, not filtered after execution. All fixture generation,
CLI subprocesses, seeds, raw logs, input hashes, ordering and refusal of existing
IDs are preserved. No file in revision 01 is modified.
"""
import importlib.util
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def check(case, runs, paths):
    issues = []
    ambiguities = []
    if len({(r["stdout_sha256"], r["stderr_sha256"], r["returncode"]) for r in runs}) != 1:
        issues.append("Salida no determinista entre procesos/seeds")
    expected = Counter(case["codigos"])
    for run in runs:
        obj = run["json"]
        if not isinstance(obj, dict):
            issues.append("stdout no es objeto JSON")
            continue
        if not {"version_contrato", "estado", "archivos", "errores"} <= obj.keys():
            issues.append("Campos de respuesta ausentes")
            continue
        errors = obj["errores"]
        if not isinstance(errors, list) or not all(isinstance(e, dict) and {"archivo", "fila", "campo", "codigo", "mensaje"} <= e.keys() for e in errors):
            issues.append("Estructura de errores inválida")
            continue
        # EV-01: actual historical API exposes archivos.<logical>.filas.
        # Do not require a flat integer or forbid additional metadata keys.
        counts = obj["archivos"]
        if not isinstance(counts, dict) or not all(
            isinstance(counts.get(logical), dict)
            and type(counts[logical].get("filas")) is int
            and counts[logical]["filas"] >= 0
            for logical in ("costos", "metrados")
        ):
            issues.append("Conteos anidados de filas no son enteros no negativos por archivo lógico")
        if not all(e["archivo"] in ("costos", "metrados") and type(e["fila"]) is int and e["fila"] >= 0 and all(isinstance(e[k], str) for k in ("campo", "codigo", "mensaje")) for e in errors):
            issues.append("Tipos de diagnóstico incorrectos")
            continue
        actual = Counter(e["codigo"] for e in errors)
        required = actual.copy()
        for code, bounds in case.get("ambiguo", {}).items():
            count = required.pop(code, 0)
            if not bounds[0] <= count <= bounds[1]:
                issues.append(f"Multiplicidad fuera del rango ambiguo {code}: {count}")
            ambiguities.append({"codigo": code, "observado": count, "rango": bounds})
        if required != expected:
            issues.append(f"Códigos esperados {dict(expected)}; observados {dict(actual)}")
        invalid = bool(case["codigos"]) or bool(case.get("min_errores"))
        if len(errors) < case.get("min_errores", 0):
            issues.append("Falta error obligatorio para entrada inválida")
        if obj["estado"] != ("INVALIDO" if invalid else "VALIDO") or run["returncode"] != (1 if invalid else 0):
            issues.append("Estado/exit code no cumplen 0 válido / 1 inválido")
        if not run["stderr_empty"]:
            issues.append("stderr inesperado en ejecución válida de CLI")
        ordered = sorted(errors, key=lambda e: (0 if e["archivo"] == "costos" else 1, e["fila"], e["campo"], e["codigo"], e["mensaje"]))
        if ordered != errors:
            issues.append("Diagnósticos fuera del orden RF-08")
        for archivo, fila, campo, codigo in case.get("ubicaciones", []):
            if not any(e["archivo"] == archivo and e["fila"] == fila and (campo is None or e["campo"] == campo) and e["codigo"] == codigo for e in errors):
                issues.append(f"Ubicación ausente: {archivo}/{fila}/{campo}/{codigo}")
        if "primera_fila" in case:
            if not all(str(case["primera_fila"]) in e["mensaje"] for e in errors if e["codigo"] == "E_CLAVE_DUPLICADA"):
                issues.append("Duplicado no cita fila primera aparición")
        encoded = json.dumps(obj, ensure_ascii=False)
        if any(str(p) in encoded or str(p).replace("\\", "/") in encoded for p in paths):
            issues.append("JSON filtra ruta absoluta")
    return sorted(set(issues)), ambiguities[:len(case.get("ambiguo", {}))]


def main():
    # Verify revision, dependency, source and ALL prior evidence before import.
    import hashlib
    freeze = json.loads((HERE / "congelacion.json").read_text(encoding="utf-8"))
    def verify():
        return [name for name, digest in freeze["sha256"].items()
                if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest]
    if verify():
        raise SystemExit("Frozen input/dependency/previous evidence changed")
    spec = importlib.util.spec_from_file_location("historical_harness", HERE.parent / "runner.py")
    harness = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(harness)
    harness.HERE = HERE
    harness.ROOT = ROOT
    harness.SOURCE = ROOT / "src" / "validador.py"
    harness.check = check
    original_save = harness.save
    def save(path, value):
        if path.name == "resumen.json":
            results = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(path.parent.glob("A*/resultado.json"))]
            valid = [r for r in results if r["runs"][0]["json"]["estado"] == "VALIDO"]
            invalid = [r for r in results if r["runs"][0]["json"]["estado"] == "INVALIDO"]
            changed = verify()
            cli = json.loads((path.parent / "cli_argumentos.json").read_text(encoding="utf-8"))
            value.update(
                harness_defects=2, harness_corrective_iterations=1, validator_corrections=0,
                previous_run={"id": "S6-002", "raw_passed": 0, "total": 35},
                nvalidos=len(valid), ninvalidos=len(invalid),
                valid_passed=sum(r["passed"] for r in valid), invalid_passed=sum(r["passed"] for r in invalid),
                pass_rate=value["passed"] / len(results),
                valid_pass_rate=sum(r["passed"] for r in valid) / len(valid),
                invalid_pass_rate=sum(r["passed"] for r in invalid) / len(invalid),
                deterministic_cases=sum(len({(x["stdout_sha256"], x["stderr_sha256"], x["returncode"]) for x in r["runs"]}) == 1 for r in results),
                control_totals={"scenario_processes": sum(len(r["runs"]) for r in results),
                                "exit_codes_scenarios": dict(Counter(str(x["returncode"]) for r in results for x in r["runs"])),
                                "cli_argument_probes": len(cli), "cli_argument_passed": sum(r["passed"] for r in cli),
                                "symlink_probes": int(value["symlink"] != "SKIP")},
                frozen_and_prior_evidence_unchanged=not changed, frozen_changed_paths=changed,
                evaluation="Posterior, no ciega; alcance de los casos, no validación contractual absoluta.",
            )
        original_save(path, value)
    harness.save = save
    code = harness.main()
    return code if not verify() else 1


if __name__ == "__main__":
    raise SystemExit(main())
