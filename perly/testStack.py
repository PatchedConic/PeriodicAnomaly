import unittest
from .stack import Stack

class StackTest(unittest.TestCase):
    def test_append(self):
        stack = Stack()
        stack.append(3.14)
        stack.append("2")
        self.assertEqual(stack.stack, [3.14, 2.0], 'Failed to append number to stack')

    def test_append_multiple(self):
        stack = Stack()
        stack.append(3.14159, 2.0)
        self.assertEqual(stack.stack, [3.14159, 2.0], 'Failed to append multiple parameters to stack')
    
    def test_number_validation(self):
        stack = Stack()
        with self.assertRaises(Exception):
            stack.append(1.23, "A")
    
    def test_clear_stack(self):
        stack = Stack()
        stack.append(3.14159)
        stack.clear()
        self.assertEqual(stack.stack, [], 'Failed to clear stack')
    
    def test_pop(self):
        stack = Stack()
        stack.append(3.14159, 2)
        stack.pop()
        self.assertEqual(stack.stack, [3.14159], 'Failed to pop from stack')
        with self.assertRaises(Exception):
            stack.pop()
            stack.pop()

    def test_get_sig_figs(self):
        stack = Stack()
        self.assertEqual(stack.get_significant_digits(), 3, "Failed to get sig figs from stack")

    def test_set_sig_figs(self):
        stack = Stack()
        stack.set_significant_digits(2)
        self.assertEqual(stack.get_significant_digits(), 2, "Failed to get sig figs from stack")
        with self.assertRaises(Exception):
            stack.set_significant_digits("A")