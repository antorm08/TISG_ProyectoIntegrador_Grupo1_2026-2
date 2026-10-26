"""Pruebas públicas preparadas antes del validador; mismo autor IA, no ciegas.

Fixtures solo bajo POC02_TMP, establecido por el runner en una ejecución exclusiva.
"""

from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
POC = Path(__file__).resolve().parents[1]
ROOT = POC.parents[1]
sys.path.insert(0, str(POC / "src"))
from validador import validar

CORPUS = json.loads((Path(__file__).with_name("casos.json")).read_text(encoding="utf-8"))
OBSERVACIONES = []


def huella(p):
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None


class ValidadorTest(unittest.TestCase):
    def setUp(self):
        if "POC02_TMP" not in os.environ:
            raise RuntimeError("Ejecutar mediante ejecutar_evaluacion.py: falta directorio autorizado POC02_TMP")
        self.temp = tempfile.TemporaryDirectory(dir=os.environ["POC02_TMP"], prefix="caso-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.costos = self.base / "costos.csv"
        self.metrados = self.base / "metrados.csv"
        self.costos.write_text(CORPUS["base_costos"], encoding="utf-8", newline="")
        self.metrados.write_text(CORPUS["base_metrados"], encoding="utf-8", newline="")

    def caso(self, datos):
        for nombre, p in [("costos", self.costos), ("metrados", self.metrados)]:
            if nombre + "_hex" in datos:
                p.write_bytes(bytes.fromhex(datos[nombre + "_hex"]))
            elif nombre in datos:
                if datos[nombre] is None:
                    p.unlink()
                else:
                    p.write_text(datos[nombre], encoding="utf-8", newline="")
        antes = [huella(self.costos), huella(self.metrados)]
        r = validar(self.costos, self.metrados)
        actual = r["estado"] == "VALIDO"
        codigos = [e["codigo"] for e in r["errores"]]
        correcto = actual == datos["valido"] and Counter(codigos) == Counter(datos["codigos"])
        estructura = all(set(e) == {"archivo", "fila", "campo", "codigo", "mensaje"} and e["mensaje"] for e in r["errores"])
        OBSERVACIONES.append({"id": datos["id"], "valido_esperado": datos["valido"], "valido_observado": actual, "codigos_esperados": datos["codigos"], "codigos_observados": codigos, "correcto": bool(correcto and estructura), "entradas_intactas": antes == [huella(self.costos), huella(self.metrados)]})
        self.assertEqual(actual, datos["valido"])
        self.assertEqual(Counter(codigos), Counter(datos["codigos"]))
        self.assertTrue(estructura)
        self.assertEqual(antes, [huella(self.costos), huella(self.metrados)])

    def test_tecnico_01_orden_y_repeticion(self):
        self.costos.write_text("obra_id,partida_id,costo_real\nOB-1,P-1,-1\nOB-1,P-2,abc\n", encoding="utf-8")
        self.metrados.write_text("obra_id,partida_id,cantidad\nOB-1,P-1,0\nOB-1,P-2,NaN\n", encoding="utf-8")
        r = validar(self.costos, self.metrados)
        self.assertEqual(r, validar(self.costos, self.metrados))
        self.assertEqual([(e["archivo"], e["fila"], e["codigo"]) for e in r["errores"]], [("costos", 2, "E_NO_POSITIVO"), ("costos", 3, "E_NUMERO_FORMATO"), ("metrados", 2, "E_NO_POSITIVO"), ("metrados", 3, "E_NUMERO_NO_FINITO")])

    def test_tecnico_02_no_escribe_archivos(self):
        antes = {p.name: huella(p) for p in self.base.iterdir()}
        validar(self.costos, self.metrados)
        self.assertEqual(antes, {p.name: huella(p) for p in self.base.iterdir()})

    def test_tecnico_03_originales_solo_lectura(self):
        datos = ROOT / "poc/POC-01-estimacion-historicos/datos"
        c, m = datos / "costos.csv", datos / "metrados.csv"
        antes = [huella(c), huella(m)]
        r = validar(c, m)
        self.assertEqual(r["estado"], "VALIDO")
        self.assertEqual(r["archivos"], {"costos": {"filas": 35}, "metrados": {"filas": 35}})
        self.assertEqual(antes, [huella(c), huella(m)])

    def test_tecnico_04_limite_archivo(self):
        self.costos.write_bytes(b"x" * (1024 * 1024 + 1))
        self.assertEqual([e["codigo"] for e in validar(self.costos, self.metrados)["errores"]], ["E_LIMITE"])

    def test_tecnico_05_limite_campo(self):
        self.costos.write_text("obra_id,partida_id,costo_real,nota\nOB-1,P-1,10," + "x" * 4097 + "\n", encoding="utf-8")
        self.assertEqual([e["codigo"] for e in validar(self.costos, self.metrados)["errores"]], ["E_FILA_ESTRUCTURA"])

    def test_tecnico_06_limite_id(self):
        self.costos.write_text("obra_id,partida_id,costo_real\n" + "x" * 129 + ",P-1,10\n", encoding="utf-8")
        self.assertIn("E_ID_FORMATO", [e["codigo"] for e in validar(self.costos, self.metrados)["errores"]])

    def test_tecnico_07_limite_numero(self):
        self.costos.write_text("obra_id,partida_id,costo_real\nOB-1,P-1," + "1" * 129 + "\n", encoding="utf-8")
        self.assertEqual([e["codigo"] for e in validar(self.costos, self.metrados)["errores"]], ["E_NUMERO_FORMATO"])

    def test_tecnico_08_cli_valido_e_invalido(self):
        comando = [sys.executable, "-X", "utf8", "-B", str(POC / "src/validador.py"), "--costos", str(self.costos), "--metrados", str(self.metrados)]
        r = subprocess.run(comando, capture_output=True, text=True, encoding="utf-8", timeout=15)
        self.assertEqual(r.returncode, 0)
        self.assertEqual(json.loads(r.stdout)["estado"], "VALIDO")
        self.costos.write_text("", encoding="utf-8")
        r = subprocess.run(comando, capture_output=True, text=True, encoding="utf-8", timeout=15)
        self.assertEqual(r.returncode, 1)
        self.assertEqual(json.loads(r.stdout)["estado"], "INVALIDO")
        self.assertEqual(r.stderr, "")

    def test_tecnico_09_mensaje_sin_datos_privados(self):
        self.costos.write_text("obra_id,partida_id,costo_real\nOB-1,P-1,-1\n", encoding="utf-8")
        e = validar(self.costos, self.metrados)["errores"][0]
        self.assertEqual(e["mensaje"], "El valor debe ser estrictamente positivo.")
        self.assertNotIn(str(self.base), json.dumps(e))

    def test_tecnico_10_directorio_no_es_csv(self):
        r = validar(self.base, self.metrados)
        self.assertEqual([e["codigo"] for e in r["errores"]], ["E_ARCHIVO_TIPO"])

    def test_tecnico_11_cli_argumentos(self):
        r = subprocess.run([sys.executable, "-B", str(POC / "src/validador.py")], capture_output=True, timeout=15)
        self.assertEqual(r.returncode, 2)

    def test_tecnico_12_linea_vacia_interior(self):
        self.costos.write_text(CORPUS["base_costos"] + "\n", encoding="utf-8", newline="")
        self.assertEqual([e["codigo"] for e in validar(self.costos, self.metrados)["errores"]], ["E_FILA_ESTRUCTURA"])


def crear_test(caso):
    def ejecutar(self):
        self.caso(caso)
    return ejecutar


for caso_publico in CORPUS["casos"]:
    setattr(ValidadorTest, "test_" + caso_publico["id"], crear_test(caso_publico))

if __name__ == "__main__":
    unittest.main(verbosity=2)
