from perly.calculator import Calculator
import unittest
import math

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

    def test_sin(self):
        calc = Calculator()
        calc.push(8, 'pi', '*', 'sin')
        self.assertEqual(calc.stack, [0], f'Test failed: sin(8*pi) != 0')
        calc.push(3.5, '+', 'pi', '*', 'sin')
        self.assertEqual(calc.stack, [math.sin(3.5*math.pi)], f"""Test failed: sin(3.5*pi) evaluated as: {calc.stack[0]} 
Correct answer, {math.sin(3.5*math.pi)}""")

    def test_cos(self):
        calc = Calculator()
        calc.push(3, 'pi', 2, '/', '*', 'cos', 'pi', 'cos')
        self.assertEqual(calc.stack, [math.cos(math.pi), 0], 'Error in cos func') 
    
    def test_tan(self):
        calc = Calculator()
        calc.push('pi', 2, '/', 'tan', 'pi', 'tan')
        self.assertEqual(calc.stack, [0, math.nan], 'Error in tan func')