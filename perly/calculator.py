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
        self.listeners = []

    def __repr__(self):
        return str(self.stack)
    
    def __len__(self):
        return len(self.stack)
    
    def update(self) -> None:
        for listener in self.listeners:
            listener.update()

    def add_listeners(self, listener) -> None:
        self.listeners.append(listener)

    def pop(self, n: int = 0) -> float:
        try:
            return self.stack.pop(n)
        except IndexError:
            return math.nan
        
    def peek(self, n: int = 0) -> float:
        try: 
            return self.stack[n]
        except IndexError:
            return math.nan
    
    def push(self, *tokens:float | str) -> None:
        for token in tokens:
            try:
                float(token)
                self.stack.insert(0, float(token))
                self.update()
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
    
    def clear(self) -> None:
        self.stack = []
        self.update()

if __name__ == '__main__':
    calc = Calculator()
    calc.push(1, 2, 3.14159)
    print(calc)