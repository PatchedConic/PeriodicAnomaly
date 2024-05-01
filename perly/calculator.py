from .stack import Stack
from .consts import MATH_TOKENS, UNARY_OPERATORS, BINARY_OPERATORS, FUNCTIONS
import math

class Calculator():
    def __init__(self):
        self.stack = Stack()

    def __repr__(self):
        return self.stack

    def receive(self, *tokens:float | int | str) -> None:
        for token in tokens:
            if not isinstance(token, float | int) and token not in MATH_TOKENS:
                raise Exception(f"Invalid token, not number or math operator {token}")
            else:
                if isinstance(token, float | int):
                    self.add_entry(token)
                elif token in MATH_TOKENS:
                    self.operate(token)
    
    def operate(self, token:str) -> None:
        if token in UNARY_OPERATORS:
            self.unary(token)
        elif token in BINARY_OPERATORS:
            self.binary(token)
        elif token in FUNCTIONS:
            self.func(token)

    def func(self, token:str) -> None:
        try:
            match token:
                case 'clear':
                    self.stack.clear()
                case 'del':
                    self.stack.pop()
                case 'pi':
                    self.receive(math.pi)
                case  'e':
                    self.receive(math.e)
                case "sin":
                    self.receive(math.sin(self.stack.pop()))
                case "cos":
                    self.receive(math.cos(self.stack.pop()))
                case "tan":
                    self.receive(math.tan(self.stack.pop()))
                case "sind":
                    self.receive(math.sin(self.stack.pop()*2*math.pi/360))
                case "cosd":
                    self.receive(math.cos(self.stack.pop()*2*math.pi/360))
                case "tand":
                    self.receive(math.tan(self.stack.pop()*2*math.pi/360))
                case 'asin':
                    self.receive(math.asin(self.stack.pop()))
                case 'acos':
                    self.receive(math.cos(self.stack.pop()))
                case'atan':
                    self.receive(math.atan(self.stack.pop()))
                case 'asind':
                    self.receive(math.asin(self.stack.pop())*360/(2*math.pi))
                case 'acosd':
                    self.receive(math.acos(self.stack.pop())*360/(2*math.pi))
                case 'atand':
                    self.receive(math.atan(self.stack.pop())*360/(2*math.pi))
                case 'ln':
                    self.receive(math.log(self.stack.pop()))
                case 'log':
                    val1 = self.stack.pop()
                    val2 = self.stack.pop()
                    self.receive(math.log(val2, val1))
                case'swap':
                    try:
                        val1 = self.stack.pop()
                        val2 = self.stack.pop()
                        self.receive(val1, val2)
                    except IndexError:
                        try:
                            self.receive(val1)
                        except: pass
                case 'square':
                    self.receive(self.stack.pop()**2)
                case 'sqrt':
                    self.receive(self.stack.pop()**0.5)
        except IndexError:
            pass

    def binary(self, token:str) -> None:
        try:
            match token:
                case "+":
                    self.receive(self.stack.pop()+self.stack.pop())
                case "-":
                    self.receive(-1*self.stack.pop()+self.stack.pop())
                case 'x'|'X|*':
                    self.receive(self.stack.pop()*self.stack.pop())
                case "/":
                    self.receive((1/self.stack.pop())*self.stack.pop())
                case '^':
                    val1 = self.stack.pop()
                    val2 = self.stack.pop()
                    self.receive(val2**val1)
        except IndexError:
            pass

    def unary(self, token:str) -> None:
        try:
            match token:
                case 'n':
                    self.receive(-1*self.stack.pop())
                case '!':
                    self.receive(math.factorial(int(self.stack.pop())))
        except IndexError:
            pass

    def add_entry(self, token:float | int) -> None:
        self.stack.append(token)