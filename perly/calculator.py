from .stack import Stack
from .consts import *

class Calculator():
    """An RPN Calculator that can be sent tokens such as numbers, operator or functions.
    Parameters
    ----------
    stack
        The calculator's stack
        
    Methods
    -------
    receive(*tokens:float or int or str)
        Accepts a number or valid math operator or function and performs the appropriate operation
    """
    
    def __init__(self):
        self.stack = Stack()

    def __repr__(self):
        return self.stack

    def receive(self, *tokens:float | int | str) -> None:
        for token in tokens:
            try:
                self.add_entry(float(token))
            except:
                if token in MATH_TOKENS:
                    self.operate(token)
                elif token == None:
                    pass
                else:
                    raise Exception(f"Invalid token: {token}")
                
    def operate(self, token:str) -> None:
        self.receive(FUNCTIONS_DICT[token](self.stack))

    def add_entry(self, token:float | int) -> None:
        self.stack.append(token)