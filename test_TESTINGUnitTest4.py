import unittest

from TESTINGUnitTest4 import area

from math import pi

class TestArea(unittest.TestCase):

    def test_area(self):
        print('-----Test valores de resultado conocido-----')
        self.assertAlmostEqual(area(1), pi)
        print ('pi')
        self.assertAlmostEqual(area(0), 0)
        print ('0')
        self.assertAlmostEqual(area(3), pi*(3**2))
        print ('pi*(*3**2)')

#Test de valores negativos
    def test_negativos(self):
        print('-----Test de valores negativos-----')

#Indicamos el tipo de excepción, la función y el valor esperado.

        self.assertRaises(ValueError, area, -1)

# Test de tipos no compatibles. Verificamos si el tipo de los parámetros es el correcto.
# El tipo de la excepción debe ser TypeError
# Hacemos una pueba para que cada tipo conocido no válido

    def test_tipos(self):
        print('-----Test de tipos no compatibles-----')
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, 'hola')
        self.assertRaises(TypeError, area, 2+3j)
