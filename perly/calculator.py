from .stack import Stack
from .token import Token
from .consts import MATH_TOKENS, UNARY_OPERATORS, BINARY_OPERATORS, FUNCTIONS
import math

class Calculator():
    def __init__(self):
        self.stack = Stack()
        self.ANGULAR_MODE = 'rad'

    def __repr__(self):
        return self.stack

    def get_angular_mode(self) -> str:
        '''Returns the current angular mode of the calculator'''
        return self.ANGULAR_MODE

    def set_angular_mode(self, value:str) -> None:
        '''Sets the angular mode of the calculator to \'deg\' or \'rad\''''
        if value == 'deg' or 'rad':
            self.ANGULAR_MODE = value
        else:
            raise Exception(f"Invalid angular mode set: {value}")

    def receive(self, *tokens:Token) -> None:
        for token in tokens:
            if not isinstance(token, Token):
                raise Exception("Invalid token, not of class Token...")
            else:
                if token.type == 'num':
                    self.add_entry(token)
                elif token.type in MATH_TOKENS:
                    self.operate(token)
                else:
                    raise Exception("Invalid token type...")
    
    def operate(self, token:Token) -> None:
        if token.type in UNARY_OPERATORS:
            self.unary(token)
        elif token.type in BINARY_OPERATORS:
            self.binary(token)
        elif token.type in FUNCTIONS:
            self.func(token)

    def func(self, token:Token) -> None:
        try:
            if token.type == 'clear':
                self.stack.clear()
            elif token.type == 'del':
                self.stack.pop()
            elif token.type == 'pi':
                self.receive(Token('num', math.pi))
            elif token.type == 'e':
                self.receive(Token('num', str(math.e)))
            elif token.type == 'sin' and self.ANGULAR_MODE == 'rad':
                self.receive(Token('num', str(math.sin(self.stack.pop()))))
            elif token.type == 'cos' and self.ANGULAR_MODE == 'rad':
                self.receive(Token('num', str(math.cos(self.stack.pop()))))
            elif token.type == 'tan' and self.ANGULAR_MODE == 'rad':
                self.receive(Token('num', str(math.tan(self.stack.pop()))))
            elif token.type == 'sin' and self.ANGULAR_MODE == 'deg':
                self.receive(Token('num', str(math.sin(self.stack.pop()*2*math.pi/360))))
            elif token.type == 'cos' and self.ANGULAR_MODE == 'deg':
                self.receive(Token('num', str(math.cos(self.stack.pop()*2*math.pi/360))))
            elif token.type == 'tan' and self.ANGULAR_MODE == 'deg':
                self.receive(Token('num', str(math.tan(self.stack.pop()*2*math.pi/360))))
            elif token.type == 'asin' and self.ANGULAR_MODE == 'rad':
                self.receive(Token('num', str(math.asin(self.stack.pop()))))
            elif token.type == 'acos' and self.ANGULAR_MODE == 'rad':
                self.receive(Token('num', str(math.cos(self.stack.pop()))))
            elif token.type == 'atan' and self.ANGULAR_MODE == 'rad':
                self.receive(Token('num', str(math.atan(self.stack.pop()))))
            elif token.type == 'asin' and self.ANGULAR_MODE == 'deg':
                self.receive(Token('num', str(math.asin(self.stack.pop())*360/(2*math.pi))))
            elif token.type == 'acos' and self.ANGULAR_MODE == 'deg':
                self.receive(Token('num', str(math.acos(self.stack.pop())*360/(2*math.pi))))
            elif token.type == 'atan' and self.ANGULAR_MODE == 'deg':
                self.receive(Token('num', str(math.atan(self.stack.pop())*360/(2*math.pi))))
            elif token.type == 'ln':
                self.receive(Token('num', str(math.log(self.stack.pop()))))
            elif token.type == 'log':
                val1 = self.stack.pop()
                val2 = self.stack.pop()
                self.receive(Token('num', str(math.log(val2, val1))))
            elif token.type == 'swap':
                try:
                    val1 = self.stack.pop()
                    val2 = self.stack.pop()
                    self.receive(Token('num', val1), Token('num', val2))
                except IndexError:
                    try:
                        self.receive(Token('num', val1))
                    except: pass
            elif token.type == 'square':
                self.receive(Token('num', self.stack.pop()**2))
            elif token.type == 'sqrt':
                self.receive(Token('num', self.stack.pop()**0.5))
        except IndexError:
            pass

    def binary(self, token:Token) -> None:
        try:
            if token.type == "+":
                self.receive(Token('num',
                                str(self.stack.pop()+self.stack.pop())))
            elif token.type == "-":
                self.receive(Token('num',
                                str(-1*self.stack.pop()+self.stack.pop())))
            elif token.type == "*":
                self.receive(Token('num',
                                str(self.stack.pop()*self.stack.pop())))
            elif token.type == "/":
                self.receive(Token('num',
                                str((1/self.stack.pop())*self.stack.pop())))
            elif token.type == '^':
                val1 = self.stack.pop()
                val2 = self.stack.pop()
                self.receive(Token('num', str(val2**val1)))
        except IndexError:
            pass

    def unary(self, token:Token) -> None:
        try:
            if token.type == 'n':
                self.receive(Token('num',str(-1*self.stack.pop())))
            elif token.type =='!':
                self.receive(Token('num', str(math.factorial(int(self.stack.pop())))))
        except IndexError:
            pass

    def add_entry(self, token:Token) -> None:
        try:
            float(token.value)
            self.stack.add_token(token)
        except ValueError:
            print(token)
            raise Exception("Invalid number")
