import unittest
from .token import Token
from .stack import Stack
from math import pi
import math

class TokenTest(unittest.TestCase):
    def test_creation(self):
        test_token = Token('Num', '1')
        self.assertEqual(test_token.type, 'Num', "Token should be num")
        self.assertEqual(test_token.value, '1', 'Token value should be 1')

class StackTest(unittest.TestCase):
    def test_invalid_type(self):
        test_stack = Stack()
        test_token = Token('Blargh', '1')
        with self.assertRaises(Exception):
            test_stack.add_token(test_token)
    
    def test_invalid_num_value(self):
        test_stack = Stack()
        test_token = Token('num', 'A')
        with self.assertRaises(Exception):
            test_stack.add_token(test_token)
    
    def test_blank_stack(self):
        test_stack = Stack()
        test_token = Token('num', '1')
        test_stack.add_token(test_token)
        self.assertEqual(test_stack.stack[-1], '1', "Invalid stack entry")
    
    def test_single_stack(self):
        test_stack = Stack()
        test_token = Token('num', '1')
        test_stack.add_token(test_token)
        test_token = Token('num', '2')
        test_stack.add_token(test_token)
        self.assertEqual(test_stack.stack[-1], '12', "Invalid stack entry")

    def test_enter(self):
        test_stack = Stack()
        test_token = Token('num', '123')
        test_stack.add_token(test_token)
        test_stack.enter()
        test_token = Token('num', '1')
        test_stack.add_token(test_token)
        self.assertEqual(test_stack.stack, ['123','1'], "Invalid stack entry")
    
    def test_long_entry(self):
        test_stack = Stack()
        test_token = Token('num', '123.4')
        try:
            test_stack.add_token(test_token)
        except:
            self.fail("Couldn't add long number to stack")

    def test_long_entry_invalid(self):
        test_stack = Stack()
        test_token = Token('num', '12.34.5')
        with self.assertRaises(Exception):
            test_stack.add_token(test_token)

class ArithmeticTest(unittest.TestCase):

    def test_decimal(self):
        test_stack = Stack()
        test_token = Token('.')
        test_token_2 = Token('num', '1')
        test_token_3 = Token('num', '.')
        test_stack.add_token(test_token,test_token_2,test_token_3)
        self.assertEqual(test_stack.stack[-1], '.1', "Failed append decimal")

    def test_addition(self):
        test_stack = Stack()
        test_token = Token('num', '3')
        test_token_2 = Token('num', '2')
        test_token_add = Token('+')
        test_stack.add_token(test_token)
        test_stack.enter()
        test_stack.add_token(test_token_2)
        test_stack.add_token(test_token_add)
        self.assertEqual(float(test_stack.stack[-2]), float('5'), "Failed addition operation...")
    
    def test_subtraction(self):
        test_stack = Stack()
        test_token = Token('num', '3')
        test_token_2 = Token('num', '2')
        test_op = Token('-')
        test_stack.add_token(test_token)
        test_stack.enter()
        test_stack.add_token(test_token_2)
        test_stack.add_token(test_op)
        self.assertEqual(float(test_stack.stack[-2]), float('1'), "Failed subtraction operation...")
    
    def test_multiplication(self):
        test_stack = Stack()
        test_token = Token('num', '3')
        test_token_2 = Token('num', '2')
        test_op = Token('*')
        test_stack.add_token(test_token)
        test_stack.enter()
        test_stack.add_token(test_token_2)
        test_stack.add_token(test_op)
        self.assertEqual(float(test_stack.stack[-2]), float('6'), "Failed multiplication operation...")
    
    def test_division(self):
        test_stack = Stack()
        test_token = Token('num', '3')
        test_token_2 = Token('num', '2')
        test_op = Token('/')
        test_stack.add_token(test_token)
        test_stack.enter()
        test_stack.add_token(test_token_2)
        test_stack.add_token(test_op)
        self.assertEqual(float(test_stack.stack[-2]), float(3/2), "Failed division operation...")
    
    def test_power(self):
        test_stack = Stack()
        test_token = Token('num', '3')
        test_token_2 = Token('num', '2')
        test_op = Token('^')
        test_stack.add_token(test_token)
        test_stack.enter()
        test_stack.add_token(test_token_2)
        test_stack.add_token(test_op)
        self.assertEqual(float(test_stack.stack[-2]), float('9'), "Failed raise-to operation...")

    def test_negate(self):
        test_stack = Stack()
        test_token = Token('num', '5')
        test_op = Token('n')
        test_stack.add_token(test_token, test_op)
        self.assertEqual(float(test_stack.stack[-1]), -5.0, "Failed negate operation...")
    
    def test_factorial(self):
        test_stack = Stack()
        test_token = Token('num', '5')
        test_op = Token('!')
        test_stack.add_token(test_token, test_op)
        self.assertEqual(float(test_stack.stack[-2]), 120.0, "Failed factorial operation")
    
    def test_pi(self):
        test_stack = Stack()
        test_token = Token('pi')
        test_stack.add_token(test_token)
        self.assertAlmostEqual(float(test_stack.stack[-2]), pi, 3, "Failed to append Pi to stack...")

    def test_e(self):
        test_stack = Stack()
        test_token = Token('e')
        test_stack.add_token(test_token)
        self.assertAlmostEqual(float(test_stack.stack[-2]), math.e, 3, "Failed to append E to stack...")
    
    def test_nat_log(self):
        test_stack = Stack()
        test_token = Token('e')
        test_op = Token('ln')
        test_stack.add_token(test_token, test_op)
        self.assertEqual(float(test_stack.stack[-2]), 1.0, "Failed natural log test...")

class FunctionTest(unittest.TestCase):
    def test_sin(self):
        test_stack = Stack()
        test_stack.stack[-1] = str(pi/2)
        test_operator = Token('sin')
        test_stack.add_token(test_operator)
        self.assertAlmostEqual(float(test_stack.stack[-2]), 1.0, 3,"Failed sin operation...")
    
    def test_cos(self):
        test_stack = Stack()
        test_stack.stack[-1] = str(pi/2)
        test_operator = Token('cos')
        test_stack.add_token(test_operator)
        self.assertAlmostEqual(float(test_stack.stack[-2]), 0.0, 3,"Failed cos operation...")
    
    def test_tan(self):
        test_stack = Stack()
        test_stack.stack[-1] = str(pi)
        test_operator = Token('tan')
        test_stack.add_token(test_operator)
        self.assertAlmostEqual(float(test_stack.stack[-2]), 0.0, 3,"Failed tan operation...")

    def test_asin(self):
        test_stack = Stack()
        test_stack.stack[-1] = str(1)
        test_operator = Token('asin')
        test_stack.add_token(test_operator)
        self.assertAlmostEqual(float(test_stack.stack[-2]), pi/2, 3,"Failed asin operation...")

    def test_acos(self):
        test_stack = Stack()
        test_stack.stack[-1] = str(0)
        test_operator = Token('acos')
        test_stack.add_token(test_operator)
        self.assertAlmostEqual(float(test_stack.stack[-2]), pi/2, 3,"Failed asin operation...")

    def test_atan(self):
        test_stack = Stack()
        test_stack.stack[-1] = str(100)
        test_operator = Token('atan')
        test_stack.add_token(test_operator)
        self.assertAlmostEqual(float(test_stack.stack[-2]), pi/2, 1,"Failed asin operation...")

    def test_sind(self):
        test_stack = Stack()
        test_stack.ANGULAR_MODE = 'deg'
        test_stack.stack[-1] = str(90)
        test_operator = Token('sin')
        test_stack.add_token(test_operator)
        self.assertAlmostEqual(float(test_stack.stack[-2]), 1.0, 3,"Failed sin operation...")
    
    def test_cosd(self):
        test_stack = Stack()
        test_stack.ANGULAR_MODE = 'deg'
        test_stack.stack[-1] = str(90)
        test_operator = Token('cos')
        test_stack.add_token(test_operator)
        self.assertAlmostEqual(float(test_stack.stack[-2]), 0.0, 3,"Failed cos operation...")
    
    def test_tand(self):
        test_stack = Stack()
        test_stack.ANGULAR_MODE = 'deg'
        test_stack.stack[-1] = str(180)
        test_operator = Token('tan')
        test_stack.add_token(test_operator)
        self.assertAlmostEqual(float(test_stack.stack[-2]), 0.0, 3,"Failed tan operation...")

    def test_asind(self):
        test_stack = Stack()
        test_stack.ANGULAR_MODE = 'deg'
        test_stack.stack[-1] = str(1)
        test_operator = Token('asin')
        test_stack.add_token(test_operator)
        self.assertAlmostEqual(float(test_stack.stack[-2]), 90, 3,"Failed asin operation...")

    def test_acosd(self):
        test_stack = Stack()
        test_stack.ANGULAR_MODE = 'deg'
        test_stack.stack[-1] = str(0)
        test_operator = Token('acos')
        test_stack.add_token(test_operator)
        self.assertAlmostEqual(float(test_stack.stack[-2]), 90, 3,"Failed asin operation...")

    def test_atand(self):
        test_stack = Stack()
        test_stack.ANGULAR_MODE = 'deg'
        test_stack.stack[-1] = str(1000)
        test_operator = Token('atan')
        test_stack.add_token(test_operator)
        self.assertAlmostEqual(float(test_stack.stack[-2]), 90, 0,"Failed asin operation...")
    
    def test_sq(self):
        test_stack = Stack()
        test_number = Token('num', '2')
        test_op = Token('sq')
        test_stack.add_token(test_number, test_op)
        self.assertEqual(test_stack.stack[-2], '4.0', "Failed squaring operation")

    def test_sqrt(self):
        test_stack = Stack()
        test_number = Token('num', '9')
        test_op = Token('sqrt')
        test_stack.add_token(test_number, test_op)
        self.assertEqual(test_stack.stack[-2], '3.0', "Failed squaring operation")
    
    def test_log(self):
        test_stack = Stack()
        token_1 = Token('num', '100')
        token_2 = Token('num', '10')
        op = Token('log')
        test_stack.add_token(token_1, token_2, op)
        self.assertEqual(test_stack.stack[-2], '2.0', "Failed logarithm operation...")

class IntegrationTest(unittest.TestCase):
    def test_itegrated(self):
        test_stack = Stack()
        token_1 = Token('num', '2')
        token_2 = Token('num', '3')
        op1 = Token('+')
        op2 = Token('sq')
        token_3 = Token('num', '5')
        op3 = Token('/')
        op4 = Token('!')
        op5 = Token('n')
        token_4 = Token('num', '3.14')
        op6 = Token('sin')
        test_stack.add_token(token_1)
        test_stack.enter()
        test_stack.add_token(token_2)
        test_stack.add_token(op1, op2)
        test_stack.add_token(token_3)
        test_stack.add_token(op3)
        test_stack.add_token(op4)
        test_stack.add_token(op5)
        test_stack.enter()
        test_stack.add_token(token_4, op6)
        self.assertEqual(float(test_stack.stack[-3]), -120.0, "Failed integrated test...")
        self.assertAlmostEqual(float(test_stack.stack[-2]), 0.0, 1, "Failed integrated test...")

if __name__ == '__main__':
    unittest.main()