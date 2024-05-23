from perly.calculator import Calculator
import unittest

class CalculatorTest(unittest.TestCase):
    def test_push_nums(self):
        calc = Calculator()
        calc.push(1, 2, 3.14159)
        self.assertEqual(calc, '[1, 2, 3.14159]', 'Error: pushing nums to calc failed')

# class StackTest(unittest.TestCase):
#     def test_append(self):
#         stack = Stack()
#         stack.append(3.14)
#         stack.append("2")
#         self.assertEqual(stack.stack, [3.14, 2.0], 'Failed to append number to stack')

#     def test_append_multiple(self):
#         stack = Stack()
#         stack.append(3.14159, 2.0)
#         self.assertEqual(stack.stack, [3.14159, 2.0], 'Failed to append multiple parameters to stack')
    
#     def test_number_validation(self):
#         stack = Stack()
#         with self.assertRaises(Exception):
#             stack.append(1.23, "A")
    
#     def test_clear_stack(self):
#         stack = Stack()
#         stack.append(3.14159)
#         stack.clear()
#         self.assertEqual(stack.stack, [], 'Failed to clear stack')
    
#     def test_pop(self):
#         stack = Stack()
#         stack.append(3.14159, 2)
#         stack.pop()
#         self.assertEqual(stack.stack, [3.14159], 'Failed to pop from stack')
#         with self.assertRaises(Exception):
#             stack.pop()
#             stack.pop()

#     def test_get_sig_figs(self):
#         stack = Stack()
#         self.assertEqual(stack.get_significant_digits(), 3, "Failed to get sig figs from stack")

#     def test_set_sig_figs(self):
#         stack = Stack()
#         stack.set_significant_digits(2)
#         self.assertEqual(stack.get_significant_digits(), 2, "Failed to get sig figs from stack")
#         with self.assertRaises(Exception):
#             stack.set_significant_digits("A")



# test = Calculator()
# # test.stack.set_significant_digits(3)
# test.receive(Token('num', '123.45'))
# test.receive(Token('num', '6.78'))
# test.receive(Token('!'))
# test.receive(Token('n'))
# test.receive(Token('del'))
# print(test.stack)
# test = Calculator()
# test.receive(Token('num', '3'))
# test.receive(Token('num', '2'))
# test.receive(Token('^'))
# test.receive(Token('clear'))
# test.receive(Token('num', '3'), Token('num','2'), Token('+'))
# print(test.stack)
# test.receive(Token('pi'), Token('num', '2'), Token('/'), Token('cos'))
# print(test.stack)
# test.set_angular_mode('deg')
# test.receive(Token('clear'), Token('num', '90'), Token('sin'), Token('num', '1'), Token('asin'), 
#              Token('swap'), Token('clear'), Token('num', 1), Token('swap'))
# print(test.stack)
