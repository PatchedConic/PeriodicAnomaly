from perly.calculator import Calculator
import unittest

class CalculatorTest(unittest.TestCase):
    def test_push_nums(self):
        calc = Calculator()
        calc.push(1, 2, 3.14159)
        self.assertEqual(calc.stack, [3.14159, 2, 1], 'Error: pushing nums to calc failed')

    def test_arithmetic(self):
        calc = Calculator()
        calc.push(1, 3, 9, '+','+', 13, '-', 5, '-', 'negate', 2.5, '/', 'invert', 8, '*', '!',
                  8, '-', 'sqrt', 2, '-', 'square', 'e', 'log', '-', 9, 'swap', '/', 2, '^')
        self.assertEqual(calc.stack, [9], "Test failed: arithmetic")

