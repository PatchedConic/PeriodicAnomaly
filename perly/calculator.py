from .consts import *
import math

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
        self.stack = []

    def __repr__(self):
        return self.stack
    
    def __len__(self):
        return len(self.stack)

    def pop(self, n: int = 0) -> float:
        try:
            return self.stack.pop(n)
        except IndexError:
            return None


    def push(self, *tokens:float | str) -> None:
        for token in tokens:
            try:
                float(token)
                self.stack.insert(-1, token)
            except:
                if token in MATH_TOKENS:
                    try:
                        self.push(FUNCTIONS_DICT[token](self))
                    except ZeroDivisionError:
                        return math.nan
                elif token == None:
                    pass
                else:
                    raise Exception(f"Invalid token: {token}")
