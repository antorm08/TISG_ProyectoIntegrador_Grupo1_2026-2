"""Freeze expectations and runner BEFORE implementation inspection/execution."""
import datetime
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FILES = [HERE / "casos.json", HERE / "runner.py", HERE / "congelar.py",
         ROOT / "CONTRATO.md", ROOT / "pruebas" / "casos.json"]
record = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "modelo": "GPT-6.1 Sol", "proveedor": "openai", "herramienta": "OpenCode",
    "alcance": "Contexto separado; mismo modelo/herramienta/proveedor; sin aislamiento material ni independencia total.",
    "antes_de_leer_o_ejecutar_src": True,
    "sha256": {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in FILES},
}
with (HERE / "congelacion.json").open("x", encoding="utf-8", newline="\n") as f:
    json.dump(record, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(json.dumps(record, ensure_ascii=False, indent=2))
