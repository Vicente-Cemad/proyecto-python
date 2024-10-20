import unittest

from TESTINGUnitTest2 import area

from math import pi

class TestArea(unittest.TestCase):

    #Test de valores negativos
    def test_negativos(self):
        print('-----Test de valores negativos-----')
    #Indicamos el tipo de excepción, la función y el valor esperado.
        self.assertRaises(ValueError, area, -1)
