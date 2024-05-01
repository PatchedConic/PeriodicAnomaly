from .calculator import Calculator
from .token import Token

test = Calculator()
# test.stack.set_significant_digits(3)
test.receive(Token('num', '123.45'))
test.receive(Token('num', '6.78'))
test.receive(Token('!'))
test.receive(Token('n'))
test.receive(Token('del'))
print(test.stack)
test = Calculator()
test.receive(Token('num', '3'))
test.receive(Token('num', '2'))
test.receive(Token('^'))
test.receive(Token('clear'))
test.receive(Token('num', '3'), Token('num','2'), Token('+'))
print(test.stack)
test.receive(Token('pi'), Token('num', '2'), Token('/'), Token('cos'))
print(test.stack)
test.set_angular_mode('deg')
test.receive(Token('clear'), Token('num', '90'), Token('sin'), Token('num', '1'), Token('asin'), 
             Token('swap'), Token('clear'), Token('num', 1), Token('swap'))
print(test.stack)
