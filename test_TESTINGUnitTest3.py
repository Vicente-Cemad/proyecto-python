import unittest

from TESTINGUnitTest3 import area

from math import pi

class TestArea(unittest.TestCase):
# Test de tipos no compatibles. 
# Verificamos si el tipo de los parámetros es el correcto.
# El tipo de la excepción debe ser TypeError
# Hacemos una prueba para que cada tipo conocido no válido
    def test_tipos(self):
        print('-----Test de tipos no compatibles-----')
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, 'hola')
        self.assertRaises(TypeError, area, 2+3j)
