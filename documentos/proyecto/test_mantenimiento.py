"""Pruebas de herramientas de mantenimiento; escribe solo fixtures temporales.

No ejecuta la PoC ni generadores documentales. Biblioteca estándar de Python.
"""

import hashlib
import json
from pathlib import Path
import tempfile
import sys
import unittest

sys.dont_write_bytecode = True

from inventario_repositorio import seguro, verificar, capturar
from verificar_repositorio import identidad_exportada, verificar_enlaces


class MantenimientoTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="tisg-mantenimiento-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def inventario(self, nombre="dato.txt"):
        archivo = self.root / nombre
        archivo.write_bytes(b"evidencia\n")
        manifiesto = self.root / "inventario.json"
        manifiesto.write_text(json.dumps({"formato": "inventario-repositorio-1", "modo": "worktree", "archivos": {nombre: {"bytes": 10, "sha256": hashlib.sha256(archivo.read_bytes()).hexdigest()}}}), encoding="utf-8")
        return archivo, manifiesto

    def test_hash_actual_y_modificacion(self):
        archivo, manifiesto = self.inventario()
        self.assertEqual(verificar(self.root, manifiesto)["estado"], "OK")
        archivo.write_bytes(b"otro valor")
        self.assertEqual(verificar(self.root, manifiesto)["estado"], "DIVERGENCIA")

    def test_archivo_ausente(self):
        archivo, manifiesto = self.inventario()
        archivo.unlink()
        self.assertEqual(verificar(self.root, manifiesto)["estado"], "DIVERGENCIA")

    def test_no_reinterpreta_manifest_historico(self):
        manifiesto = self.root / "anterior.json"
        manifiesto.write_text('{"archivos": []}', encoding="utf-8")
        with self.assertRaises(ValueError):
            verificar(self.root, manifiesto)

    def test_no_sobrescribe_evidencia(self):
        destino = self.root / "existente.json"
        destino.write_bytes(b"no cambiar")
        with self.assertRaises(ValueError):
            capturar(self.root, destino, "worktree", None)
        self.assertEqual(destino.read_bytes(), b"no cambiar")

    def test_ruta_fuera_del_root_rechazada(self):
        with self.assertRaises(ValueError):
            seguro(self.root, "../fuera.txt")

    def test_conversion_saltos_no_oculta_cambio(self):
        archivo = self.root / "fuente.md"
        esperado = hashlib.sha256(b"texto\r\n").hexdigest()
        archivo.write_bytes(b"texto\n")
        self.assertEqual(identidad_exportada(archivo, esperado), "solo_LF_CRLF")
        archivo.write_bytes(b"texto cambiado\n")
        self.assertEqual(identidad_exportada(archivo, esperado), "diferente")

    def test_binario_no_normalizado(self):
        archivo = self.root / "informe.pdf"
        archivo.write_bytes(b"datos\n")
        esperado = hashlib.sha256(b"datos\r\n").hexdigest()
        self.assertEqual(identidad_exportada(archivo, esperado), "diferente")

    def test_enlace_desde_carpeta_real(self):
        carpeta = self.root / "sub"
        carpeta.mkdir()
        (self.root / "dato.txt").write_bytes(b"dato")
        (carpeta / "README.md").write_text("[dato](../dato.txt)\n", encoding="utf-8")
        self.assertEqual(verificar_enlaces(self.root), 1)
        (carpeta / "README.md").write_text("[roto](dato.txt)\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            verificar_enlaces(self.root)


if __name__ == "__main__":
    unittest.main()
