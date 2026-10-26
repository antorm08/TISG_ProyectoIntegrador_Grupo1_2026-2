"""Auditoría de consolidación v0.2: solo lectura, sin PoC/generadores/red."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import statistics
import subprocess
import sys
from urllib.parse import unquote, urlsplit
import zipfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
POC = ROOT / "poc/POC-02-ai-native-sdlc"
EVID = ROOT / "evidencias/semana-06/revision-v0.2"


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    import pymupdf
    from docx import Document
    from editar_pdf_semana6_v02 import tokens, plain
    checks = []

    def check(ok, mensaje):
        if not ok:
            raise ValueError(mensaje)
        checks.append(mensaje)

    baseline = load(EVID / "integridad_antes.json")
    changed = [n for n, h in baseline["sha256"].items() if not (ROOT/n).is_file() or sha(ROOT/n) != h]
    check(not changed, "Los 220 archivos iniciales, incluida v0.1, permanecen intactos: " + str(changed))
    check(subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip() == baseline["head"], "HEAD preservado, sin commits nuevos")
    for freeze in [POC / "evaluacion_v02/congelacion.json", POC / "evaluacion_v02/revision-02/congelacion.json"]:
        for n, h in load(freeze)["sha256"].items():
            check(sha(POC/n) == h, "Congelación intacta: " + n)
    old = load(POC / "resultados/S6-002/resumen.json")
    new = load(POC / "resultados/S6-003/resumen.json")
    check(old["total"] == 35 and old["passed"] == 0 and len(old["failed"]) == 35, "S6-002 conserva 0/35 bruto")
    check(new["total"] == new["passed"] == 35 and not new["failed"], "S6-003: 35/35 según oráculos revisados")
    check(old["source_sha256"] == new["source_sha256"] == sha(POC / "src/validador.py"), "Misma fuente original, sin correcciones de implementación")
    nv = ni = fa = fr = 0
    newcases = load(POC / "evaluacion_v02/revision-02/casos.json")["casos"]
    for case in newcases:
        directory = POC / "resultados/S6-003" / case["id"]
        result = load(directory / "resultado.json")
        expected_valid = not case["codigos"] and not case.get("min_errores", 0)
        nv += expected_valid
        ni += not expected_valid
        runs = result["runs"]
        check(result["passed"] and len(runs) == 3, "Tres procesos satisfactorios: " + case["id"])
        check(len({r["stdout_sha256"] for r in runs}) == 1, "Determinismo de stdout: " + case["id"])
        actual_valid = runs[0]["json"]["estado"] == "VALIDO"
        fa += not expected_valid and actual_valid
        fr += expected_valid and not actual_valid
        for run in runs:
            prefix = directory / ("seed-" + run["seed"])
            stdout = Path(str(prefix) + ".stdout.log")
            stderr = Path(str(prefix) + ".stderr.log")
            check(sha(stdout) == run["stdout_sha256"] and sha(stderr) == run["stderr_sha256"], "Logs auténticos coherentes: " + case["id"] + "/" + run["seed"])
            check(json.loads(stdout.read_text(encoding="utf-8")) == run["json"], "JSON conservado: " + case["id"] + "/" + run["seed"])
        observed = Counter(e["codigo"] for e in runs[0]["json"]["errores"])
        for code, (minimum, maximum) in case.get("ambiguo", {}).items():
            check(minimum <= observed.pop(code, 0) <= maximum, "Intervalo ambiguo conservado: " + case["id"] + "/" + code)
        check(observed == Counter(case["codigos"]), "Códigos esperados: " + case["id"])
    check(nv == 10 and ni == 25 and fa == fr == 0, "Q2/Q3 recomputados: 0/25 y 0/10")
    for r in [old, new]:
        check(r["cli_2_passed"] and r["originals_unchanged"] and not r["changed_inputs"], "CLI/integridad: " + r["start_utc"])
        check(r["symlink"] == "PASS" and r["processes"] == 109, "Symlink y 109 procesos: " + r["start_utc"])
    b = load(POC / "resultados/S6-BENCH-002/benchmark.json")
    for group, summary in b["resumen"].items():
        values = [t["segundos"] for t in b["tiempos_individuales"] if t["grupo"] == group]
        check(len(values) == summary["n"] == (5 if group == "SUITE_48" else 30), "Repeticiones: " + group)
        check(summary["mediana_s"] == statistics.median(values) and summary["min_s"] == min(values) and summary["max_s"] == max(values), "Estadísticos recomputados: " + group)
    check(len(b["tiempos_individuales"]) == 125 and b["entradas_fuente_intactas"], "125 observaciones técnicas y entradas intactas")
    for n,h in b["parametros"]["hashes_antes"].items():
        check(sha(ROOT/n) == h, "Benchmark: hash intacto " + n)
    for n,h in load(POC / "resultados/S6-BENCH-002/manifiesto.json").items():
        check(sha(POC / "resultados/S6-BENCH-002" / n) == h, "Benchmark: manifiesto " + n)
    source = ROOT / "documentos/proyecto/Semana6_AI_Native_SDLC_v0.2.md"
    text = source.read_text(encoding="utf-8")
    check(not re.search(r"PENDIENTE_(?:DE_CONSOLIDAR|COMANDO|SALIDA|RESULTADOS|TABLA|RF|HALLAZGOS)", text), "Informe sin marcadores de consolidación")
    code = [v for k,v in tokens(text) if k == "code"]
    demo = EVID / "ejemplo-cli"
    for name in ["costos.csv", "comando.txt", "stdout.json"]:
        literal = (demo/name).read_text(encoding="utf-8").rstrip("\n")
        check(literal in code, "Extracto textual fiel: " + name)
    historical_log = (POC/"resultados/S6-001/unittest.log").read_text(encoding="utf-8")
    check("Ran 48 tests in 1.435s\n\nOK" in historical_log and "Ran 48 tests in 1.435s\n\nOK" in code, "Extracto unittest histórico fiel")
    check(load(demo/"registro.json")["exit_code"] == 1 and sha(demo/"validador.py") == sha(POC/"src/validador.py"), "Demostración de CLI sobre copia idéntica")
    for key in ["M1_desarrollo", "M2_revision_humana", "M4_ahorro"]:
        check(load(POC/"resultados/S6-001/resultados.json")["metricas"][key] == "NO DETERMINADO", "Sin modificar métrica humana: " + key)
    deliver = ROOT/"entregas/semana-06"
    for name, digest in load(deliver/"manifiesto_v0.2.json")["sha256"].items():
        check(sha(ROOT/name) == digest, "Manifiesto de borrador: " + name)
    pdf = deliver/"TISG_E01_S06_AI_Native_SDLC_v0.2_BORRADOR.pdf"
    with pymupdf.open(pdf) as d:
        pages = len(d)
        alltext = "\n".join(p.get_text() for p in d)
        check(9 <= pages <= 12, "PDF dentro de 9–12 páginas")
        check(all("BORRADOR" in p.get_text() for p in d), "Todas las páginas identificadas como borrador")
        check(all(len(p.get_text()) > 300 for p in d), "Sin páginas vacías/de relleno")
        for kind,val in tokens(text):
            if kind == "heading":
                heading = plain(val[1])
                check(heading in alltext, "Encabezado Markdown presente en PDF: " + heading)
        compacto = re.sub(r"\s+", "", alltext)
        for kind,val in tokens(text):
            fragments = ([plain(val)] if kind in {"text", "callout"} else
                         [plain(cell) for row in val for cell in row] if kind == "table" else
                         [val] if kind == "code" else [])
            for fragment in fragments:
                check(re.sub(r"\s+", "", fragment) in compacto, "Contenido Markdown/PDF: " + fragment[:70])
        check(all(not [b for b in p.get_text("blocks") if b[0]<0 or b[1]<0 or b[2]>p.rect.width+.5 or b[3]>p.rect.height+.5] for p in d), "PDF sin texto fuera del lienzo")
    docx = deliver/"TISG_E01_S06_AI_Native_SDLC_v0.2_BORRADOR.docx"
    with zipfile.ZipFile(docx) as z:
        check(z.testzip() is None, "DOCX ZIP íntegro")
    doc = Document(docx)
    check(len(doc.tables) == sum(k == "table" for k,v in tokens(text)), "Tablas DOCX y Markdown concuerdan")
    check(len(doc.inline_shapes) == 3, "Tres figuras en DOCX")
    files = [ROOT/n for n in subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard", "-z"], cwd=ROOT).decode().split("\0") if n]
    enlaces = 0
    for p in files:
        if p.suffix.lower() != ".md" or not p.is_file():
            continue
        for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
            url = urlsplit(link)
            if not url.scheme and url.path:
                check((p.parent/unquote(url.path)).resolve().exists(), "Enlace válido: " + str(p.relative_to(ROOT)) + " -> " + link)
                enlaces += 1
    secrets = re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----|\bgh[pousr]_[A-Za-z0-9]{30,}|\bAKIA[A-Z0-9]{16}\b")
    scanned = 0
    for p in files:
        if not p.is_symlink() and p.is_file() and p.suffix.lower() in {".md", ".py", ".json", ".log", ".csv", ".txt", ".svg"}:
            check(not secrets.search(p.read_text(encoding="utf-8", errors="replace")), "Sin patrones de secreto: " + str(p.relative_to(ROOT)))
            scanned += 1
    print(json.dumps({"estado":"OK", "comprobaciones":len(checks), "historicos_intactos":len(baseline["sha256"]), "paginas_pdf":pages, "enlaces_locales":enlaces, "archivos_escaneados":scanned, "limite":"No evaluación humana, ciega o auditoría exhaustiva de seguridad", "revision_humana":"PENDIENTE"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(json.dumps({"estado":"ERROR", "detalle":str(e)}, ensure_ascii=False))
        raise SystemExit(1)
