from .token import Token
from .consts import *
import math




class Stack:
    def __init__(self):
        self.stack = ['']
        self.ANGULAR_MODE = 'rad'


    def add_token(self, *args):
        for token in args:
            if not isinstance(token, Token):
                raise Exception("Invalid token...")
            
            if not token.type in TOKENTYPES:
                raise Exception("Invalid token type...")
            
            if token.type in BINARY_OPERATORS and len(self.stack)<2:
                raise Exception("Insufficient items on stack")
            
            if token.type == "num":
                self.append_digit(token.value)

            if token.type == '.':
                self.append_digit(token.type)
            
            if token.type in OPERATORS:
                self.operator(token.type)
            
            if token.type in FUNCTIONS:
                self.function(token.type)
            
    def function(self, value):
        if self.stack[-1] == '' and len(self.stack) > 1: self.stack.pop()
        elif self.stack[-1] == '' and len(self.stack) <=1 and value != 'pi' and value != 'e': return

        if self.ANGULAR_MODE == 'deg' and value in TRIG_FUNCS:
            parameter = float(self.stack[-1])*2*math.pi/360
        elif value in TRIG_FUNCS and self.ANGULAR_MODE == 'rad': parameter = float(self.stack[-1])

        match value:
            case 'sin':
                self.stack[-1] = str(math.sin(parameter))
            case 'cos':
                self.stack[-1] = str(math.cos(parameter))
            case 'tan':
                self.stack[-1] = str(math.tan(parameter))
            case 'asin':
                if self.ANGULAR_MODE == 'rad':
                    self.stack[-1] = str(math.asin(float(self.stack[-1])))
                elif self.ANGULAR_MODE == 'deg':
                    self.stack[-1] = str(math.asin(float(self.stack[-1]))*360/(2*math.pi))
            case 'acos':
                if self.ANGULAR_MODE == 'rad':
                    self.stack[-1] = str(math.acos(float(self.stack[-1])))
                elif self.ANGULAR_MODE == 'deg':
                    self.stack[-1] = str(math.acos(float(self.stack[-1]))*360/(2*math.pi))
            case 'atan':
                if self.ANGULAR_MODE == 'rad':
                    self.stack[-1] = str(math.atan(float(self.stack[-1])))
                elif self.ANGULAR_MODE == 'deg':
                    self.stack[-1] = str(math.atan(float(self.stack[-1]))*360/(2*math.pi))
            case 'sq':
                self.stack[-1] = str(float(self.stack[-1])**2)
            case 'sqrt':
                self.stack[-1] = str(math.sqrt(float(self.stack[-1])))
            case 'ln':
                self.stack[-1] = str(math.log(float(self.stack[-1])))
            case 'e':
                if self.stack[-1] == '':
                    self.stack[-1]=(str(math.e))
                else:
                    self.stack.append(str(math.e))
            case 'pi':
                if self.stack[-1] == '':
                    self.stack[-1]=(str(math.pi))
                else:
                    self.stack.append(str(math.pi))
            case 'log':
                try:
                    val1 = float(self.stack.pop())
                    val2 = float(self.stack.pop())
                    self.stack.append(str(math.log(val2, val1)))
                except IndexError:
                    return
        
        self.enter()

    def append_digit(self, value):
        if len(value) >1:
            try:
                float(value)
                self.stack[-1] = value
                self.enter()
                return
            except:
                raise Exception("Invalid number...")
        else:
            if not value in DIGITS:
                raise Exception("Invalid number...")
            else:
                if value == '.' and '.' not in self.stack[-1]:
                    self.stack[-1] = self.stack[-1] + value
                elif value != '.':
                    self.stack[-1] = self.stack[-1] + value

    def operator(self, type):
        if self.stack[-1] == '' and len(self.stack)>=2: self.stack.pop()
        elif self.stack[-1] == '' and len(self.stack)<2: return

        if type in BINARY_OPERATORS and len(self.stack)<2: return

        match type:
            case '+':
                if self.stack[-1] == '': self.stack.pop
                val1 = float(self.stack.pop())
                if self.stack[-1] == '': self.stack.pop
                val2 = float(self.stack.pop())
                self.stack.append(str(val2+val1))
            case '-':
                if self.stack[-1] == '': self.stack.pop
                val1 = float(self.stack.pop())
                if self.stack[-1] == '': self.stack.pop
                val2 = float(self.stack.pop())
                self.stack.append(str(val2-val1))
            case '*':
                if self.stack[-1] == '': self.stack.pop
                val1 = float(self.stack.pop())
                if self.stack[-1] == '': self.stack.pop
                val2 = float(self.stack.pop())
                self.stack.append(str(val2*val1))
            case '/':
                try: 
                    if self.stack[-1] == '': self.stack.pop
                    val1 = float(self.stack.pop())
                    if self.stack[-1] == '': self.stack.pop
                    val2 = float(self.stack.pop())
                    self.stack.append(str(val2/val1))
                except ZeroDivisionError:
                    try:
                        self.stack[-1] = None
                    except IndexError:
                        self.stack.append('')
            case '^':
                if self.stack[-1] == '': self.stack.pop
                val1 = float(self.stack.pop())
                if self.stack[-1] == '': self.stack.pop
                val2 = float(self.stack.pop())
                self.stack.append(str(val2**val1))
            case '!':
                if self.stack[-1] == '': self.stack.pop()
                self.stack.append(str(math.factorial(int(float(self.stack.pop())))))
            case 'n':
                if self.stack[-1] == '': self.stack.pop()
                self.stack[-1] = str(float(self.stack[-1])*-1)
                return

        self.enter()
        
    def enter(self):
        if len(self.stack) == 0: return
        
        elif self.stack[-1] == '':return

        else:
            self.stack.append("")