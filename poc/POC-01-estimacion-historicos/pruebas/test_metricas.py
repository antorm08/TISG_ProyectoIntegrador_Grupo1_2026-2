"""Pruebas de reglas, no evidencia de impacto real ni de adopción."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from experimento_bi import decidir, mape  # noqa: E402


class MetricasTest(unittest.TestCase):
    def test_error_absoluto(self):
        self.assertAlmostEqual(mape(90, 100), .10)
        self.assertAlmostEqual(mape(110, 100), .10)

    def test_real_cero_no_es_error_cero(self):
        with self.assertRaises(ValueError):
            mape(100, 0)

    def test_continuar_ambos_umbrales(self):
        self.assertEqual(decidir(.10, .20), "CONTINUAR")

    def test_aceptacion_en_limite(self):
        self.assertEqual(decidir(.15, .25), "CONTINUAR")

    def test_modificar_si_reduccion_insuficiente(self):
        self.assertEqual(decidir(.14, .15), "MODIFICAR")

    def test_modificar_aunque_mejore_si_error_alto(self):
        self.assertEqual(decidir(.20, .50), "MODIFICAR")

    def test_abandono_estricto(self):
        self.assertEqual(decidir(.30, .60), "MODIFICAR")
        self.assertEqual(decidir(.30001, .60), "DETENER")

    def test_control_perfecto(self):
        self.assertEqual(decidir(.10, 0), "MODIFICAR")

    def test_porcentajes_no_negativos(self):
        with self.assertRaises(ValueError):
            decidir(-.1, .2)


if __name__ == "__main__":
    unittest.main()
