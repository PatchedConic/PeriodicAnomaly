import unittest
from .calculator import Calculator as Calc
from math import pi
import math

class CalculatorTest(unittest.TestCase):

    def test_arithmetic(self):
        calc = Calc()
        calc.receive(1, 2, '+', 3, 'x', 3.0, '/', 2.0, '-')
        self.assertEqual(calc.stack.stack[-1], 1.0, f"Couldn't add numbers, 1 + 2 * 3 / 3 -2 = {calc.stack.stack[-1]}")
    