
import unittest
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from datos import Venta
from transformaciones import (
    filtrar_por_fecha,
    filtrar_por_hora,
    calcular_ingresos,
    contar_ventas_por_cafe
)


class TestTransformaciones(unittest.TestCase):

    def setUp(self):
        self.ventas = (
            Venta("2024-03-01", 10, "Latte", 38.7),
            Venta("2024-03-01", 12, "Americano", 28.9),
            Venta("2024-03-02", 12, "Latte", 38.7),
            Venta("2024-03-03", 15, "Cappuccino", 38.7)
        )

    def test_filtrar_por_fecha(self):
        resultado = filtrar_por_fecha(self.ventas, "2024-03-01")
        self.assertEqual(len(resultado), 2)

    def test_filtrar_por_hora(self):
        resultado = filtrar_por_hora(self.ventas, 12)
        self.assertEqual(len(resultado), 2)

    def test_calcular_ingresos(self):
        resultado = calcular_ingresos(self.ventas)
        self.assertAlmostEqual(resultado, 145.0)

    def test_contar_ventas_por_cafe(self):
        resultado = contar_ventas_por_cafe(self.ventas)
        esperado = (
            ("Americano", 1),
            ("Cappuccino", 1),
            ("Latte", 2)
        )
        self.assertEqual(resultado, esperado)


if __name__ == "__main__":
    unittest.main()
