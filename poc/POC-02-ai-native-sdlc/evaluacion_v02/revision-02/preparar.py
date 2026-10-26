"""Create corrected declarative cases and freeze revision once; never overwrite."""
import copy
import datetime
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
source = json.loads((HERE.parent / "casos.json").read_text(encoding="utf-8"))
corrected = copy.deepcopy(source)
case = next(c for c in corrected["casos"] if c["id"] == "A20_multilinea_correspondencia")
assert case["ubicaciones"] == [["costos", 5, None, "E_SIN_METRADO"]]
case["ubicaciones"][0][1] = 4
case["motivo"] = case["motivo"].replace("final 5", "final 4")
with (HERE / "casos.json").open("x", encoding="utf-8", newline="\n") as f:
    json.dump(corrected, f, ensure_ascii=False, indent=2)
    f.write("\n")
# Assert no changed expectations other than A20 location and explanatory text.
comparison = copy.deepcopy(corrected)
original_case = next(c for c in source["casos"] if c["id"] == case["id"])
index = corrected["casos"].index(case)
comparison["casos"][index] = original_case
assert comparison == source
files = [p for p in HERE.parent.rglob("*") if p.is_file() and HERE not in p.parents]
files += [p for p in (ROOT / "resultados" / "S6-002").rglob("*") if p.is_file()]
files += [ROOT / "src" / "validador.py", ROOT / "CONTRATO.md", ROOT / "pruebas" / "casos.json"]
files += [HERE / name for name in ("casos.json", "runner.py", "preparar.py")]
record = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "revision": "02", "harness_defects": ["EV-01", "EV-02"],
    "harness_corrective_iterations": 1, "validator_corrections": 0,
    "model": "GPT-6.1 Sol", "provider": "openai", "tool": "OpenCode",
    "evaluation": "Posterior, fuente conocida; no ciega ni totalmente independiente.",
    "cases_delta": "Solo A20 ubicación fila 5 a 4 y texto explicativo; otras expectativas idénticas.",
    "sha256": {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(files))},
}
with (HERE / "congelacion.json").open("x", encoding="utf-8", newline="\n") as f:
    json.dump(record, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(json.dumps({k: v for k, v in record.items() if k != "sha256"}, ensure_ascii=False, indent=2))
print("Frozen files:", len(record["sha256"]))
