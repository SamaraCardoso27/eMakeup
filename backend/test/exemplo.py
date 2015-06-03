from unittest.case import TestCase

__author__ = 'samara'


def soma(param, param1):
    return 3


class OperacaoesTeste(TestCase):
    def test_soma(self):
        resultado = soma(1,2)
        self.assertEqual(3,resultado)
        self.assertEqual(3,soma(1,2))

    def test_balh(self):
        self.assertAlmostEqual(5.1,5.1001)




