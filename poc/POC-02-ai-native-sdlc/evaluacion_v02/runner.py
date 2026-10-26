"""Additional contract evaluation. Standard library only; never imports target.

Usage: python -X utf8 -B runner.py --id S6-002
Every run requires a NEW output directory; existing IDs fail, never overwrite.
"""
import argparse
from collections import Counter
import csv
import datetime
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = ROOT / "src" / "validador.py"
SEEDS = ("1", "987654321", "random")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write("\n")


def atom(value):
    if isinstance(value, str):
        return value
    if "repeat" in value:
        return value["repeat"] * value["n"]
    return "".join(atom(x) for x in value["concat"])


def fixture(spec, logical):
    header = ["obra_id", "partida_id", "costo_real" if logical == "costos" else "cantidad"]
    if "exact_size" in spec:
        # 300 distinct keys, <4096 characters per field; exact byte padding.
        text = ",".join(header + ["nota"]) + "\n"
        prefixes = [f"OB-{i},P,1," for i in range(300)]
        available = spec["exact_size"] - len(text.encode()) - sum(len(p) + 1 for p in prefixes) - (3 if spec.get("bom") else 0)
        quotient, remainder = divmod(available, 300)
        for i, prefix in enumerate(prefixes):
            count = quotient + (i < remainder)
            padding = "ñ" * (count // 2) + "x" * (count % 2) if spec.get("unicode") else "x" * count
            text += prefix + padding + "\n"
        data = text.encode("utf-8")
        if spec.get("bom"):
            data = b"\xef\xbb\xbf" + data
        assert len(data) == spec["exact_size"]
        return data
    if "raw" in spec:
        return spec["raw"].encode("utf-8") + bytes.fromhex(spec.get("suffix_hex", ""))
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\r\n" if spec.get("crlf") else "\n")
    writer.writerow(spec.get("header", header))
    rows = [[f"OB-{i}", "P", "1"] for i in range(300)] if spec.get("size_peer") else spec.get("rows", [["OB-1", "P-1", "1"]])
    for row in rows:
        writer.writerow([atom(cell) for cell in row])
    return ("\ufeff" if spec.get("bom") else "").encode("utf-8") + output.getvalue().encode("utf-8")


def invoke(args, seed, destination, tag):
    env = os.environ.copy()
    env.update(PYTHONHASHSEED=seed, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")
    command = [sys.executable, "-X", "utf8", "-B", str(SOURCE)] + args
    start = time.perf_counter()
    completed = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, timeout=30)
    elapsed = time.perf_counter() - start
    for suffix, content in (("stdout", completed.stdout), ("stderr", completed.stderr)):
        with (destination / f"{tag}.{suffix}.log").open("xb") as f:
            f.write(content)
    result = {"command": command, "seed": seed, "returncode": completed.returncode,
              "seconds": elapsed, "stdout_sha256": hashlib.sha256(completed.stdout).hexdigest(),
              "stderr_sha256": hashlib.sha256(completed.stderr).hexdigest()}
    try:
        result["json"] = json.loads(completed.stdout.decode("utf-8"))
    except (ValueError, UnicodeError):
        result["json"] = None
    result["stderr_empty"] = not completed.stderr
    return result


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
        if not isinstance(obj["archivos"], dict) or set(obj["archivos"]) != {"costos", "metrados"} or not all(type(v) is int and v >= 0 for v in obj["archivos"].values()):
            issues.append("Conteos de archivos no son enteros no negativos por archivo lógico")
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", required=True)
    args = parser.parse_args()
    if not args.id or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for c in args.id):
        parser.error("ID simple obligatorio")
    freeze = json.loads((HERE / "congelacion.json").read_text(encoding="utf-8"))
    for relative, digest in freeze["sha256"].items():
        if sha(ROOT / relative) != digest:
            raise SystemExit(f"Congelación alterada: {relative}")
    destination = ROOT / "resultados" / args.id
    destination.mkdir(exist_ok=False)
    start_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    # Read-only baseline: original source, public suite and contract, never POC-01.
    originals = [ROOT / "CONTRATO.md"]
    originals += [p for folder in (ROOT / "src", ROOT / "pruebas") for p in folder.rglob("*") if p.is_file()]
    before = {p.relative_to(ROOT).as_posix(): sha(p) for p in originals}
    save(destination / "originales_antes.json", before)
    save(destination / "congelacion_copia.json", freeze)
    cases = json.loads((HERE / "casos.json").read_text(encoding="utf-8"))["casos"]
    results = []
    input_hashes = {}
    for case in cases:
        directory = destination / case["id"]
        directory.mkdir()
        paths = []
        for logical in ("costos", "metrados"):
            path = directory / f"{logical}.csv"
            spec = case.get(logical, {})
            if spec.get("directory"):
                path.mkdir()
            else:
                with path.open("xb") as f:
                    f.write(fixture(spec, logical))
                input_hashes[str(path.relative_to(destination))] = sha(path)
            paths.append(path)
        before_tree = sorted(str(p.relative_to(directory)) for p in directory.rglob("*"))
        runs = [invoke(["--costos", str(paths[0]), "--metrados", str(paths[1])], seed, directory, f"seed-{seed}") for seed in SEEDS]
        issues, ambiguities = check(case, runs, paths + [ROOT, destination])
        # Only runner-created stdout/stderr logs may have appeared.
        after_tree = sorted(str(p.relative_to(directory)) for p in directory.rglob("*") if not p.name.endswith(".log"))
        if before_tree != after_tree:
            issues.append("Efectos laterales inesperados en carpeta de entradas")
        result = {"id": case["id"], "rf": case["rf"], "motivo": case["motivo"],
                  "passed": not issues, "issues": issues, "ambiguities": ambiguities,
                  "seconds": sum(r["seconds"] for r in runs), "runs": runs}
        save(directory / "resultado.json", result)
        results.append(result)
    cli = []
    for index, argv in enumerate(([], ["--costos"], ["--costos", "x", "--metrados", "y", "--desconocida"])):
        run = invoke(argv, "1", destination, f"cli-2-{index}")
        run["passed"] = run["returncode"] == 2 and run["json"] is None and not run["stderr_empty"]
        cli.append(run)
    save(destination / "cli_argumentos.json", cli)
    # Optional symlink test: no privilege escalation; skip if Windows denies creation.
    linkdir = destination / "symlink_probe"
    linkdir.mkdir()
    target = destination / "A01_ids_128" / "costos.csv"
    link = linkdir / "link.csv"
    try:
        link.symlink_to(target)
    except OSError as exc:
        symlink = {"status": "SKIP", "reason": type(exc).__name__, "winerror": getattr(exc, "winerror", None)}
    else:
        run = invoke(["--costos", str(link), "--metrados", str(destination / "A01_ids_128" / "metrados.csv")], "1", linkdir, "symlink")
        obj = run["json"] or {}
        symlink = {"status": "PASS" if run["returncode"] == 1 and Counter(e["codigo"] for e in obj.get("errores", [])) == Counter(["E_ARCHIVO_TIPO"]) else "FAIL", "run": run}
    save(destination / "symlink.json", symlink)
    after = {p.relative_to(ROOT).as_posix(): sha(p) for p in originals}
    save(destination / "originales_despues.json", after)
    changed_inputs = [relative for relative, digest in input_hashes.items() if sha(destination / relative) != digest]
    save(destination / "entradas_sha256.json", input_hashes)
    summary = {"start_utc": start_utc, "end_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "python": sys.version, "executable": sys.executable, "source_sha256": before["src/validador.py"],
               "freeze_sha256": sha(HERE / "congelacion.json"), "total": len(results),
               "passed": sum(r["passed"] for r in results), "failed": [r["id"] for r in results if not r["passed"]],
               "ambiguous_cases": [r["id"] for r in results if r["ambiguities"]],
               "cli_2_passed": all(r["passed"] for r in cli), "symlink": symlink["status"],
               "originals_unchanged": before == after, "changed_inputs": changed_inputs,
               "processes": len(results) * len(SEEDS) + len(cli) + (symlink["status"] != "SKIP"),
               "seconds_cases": sum(r["seconds"] for r in results)}
    save(destination / "resumen.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if not summary["failed"] and summary["cli_2_passed"] and before == after and not changed_inputs and symlink["status"] != "FAIL" else 1


if __name__ == "__main__":
    raise SystemExit(main())
