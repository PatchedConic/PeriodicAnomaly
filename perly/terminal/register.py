from textual.widgets import Digits
from textual import events
from perly.calculator import Calculator
from perly.consts import DIGITS

class Register(Digits):

    register_position = {
        'x':0,
        'y':1,
        'z':2,
        't':3
    }

    title = {
        'x': "X Register",
        'y': "Y Register",
        'z': "Z Register",
        't': "T Register"
    }


    def __init__(self, register_name, calc):
        super().__init__("")
        self.border_title = Register.title[register_name]
        self.register_position = Register.register_position[register_name]
        self.calc = calc
        self.update(str(self.calc.peek(self.register_position)))
        self.entry = ""

    # def ping(self):
    #      if self.entry == "":
    #         self.update(str(self.calc.peek(self.register_position)))
    #         return
    #      self.update(self.entry)

    
    def clear(self):
         self.entry = ""
    
    # def enter(self):
    #      self.calc.push(self.entry)
    #      self.entry = ""
    #      self.ping()

    # def __init__(self, calculator: Calculator, position: str):
    #     self.calc = calculator
    #     self.id = position
    #     self.register = Register.register_position[position]
    #     self.value = ""
    #     self.observers = []


    # def getValue(self) -> float:
    #     if self.value == "":
    #         return self.calc.peek(self.register)
    #     else:
    #         return self.value
    
    # def writeValue(self, value: str) -> None:
    #     if self.register != 0:
    #         raise Exception("Cannot write to register that is not X")
    #     else:
    #         self.value.append(value)
    
    # def addObserver(self, observer) -> None:
    #     pass