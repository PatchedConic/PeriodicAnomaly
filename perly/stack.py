from .token import Token
from .consts import *



class Stack:
    def __init__(self):
        """A representation of a computational stack
        Parameters
        ----------
        stack: list
            the computational stack
            
        Methods
        -------
        add_token
            adds a token to the class which either adds a number to the stack or performs a calculation on the stack"""
        
        
        self.stack = []
        self.SIGNIFICANT_DIGITS = 3

    def pop(self) -> float:
        try:
            return self.stack.pop()
        except IndexError:
            raise IndexError
    
    def get_significant_digits(self) -> int:
        return self.SIGNIFICANT_DIGITS

    def set_significant_digits(self, value:int) -> None:
        try:
            int(value)
            self.SIGNIFICANT_DIGITS = value
        except ValueError:
            raise Exception(f"Invalid value for significant digits: {value}")

    def clear(self) -> None:
        self.stack = []

    def add_token(self, token:Token) -> None:
        """
        Takes a token or list of tokens and adds them to the stack or executes a computation as appropriate
        """
        if not isinstance(token, Token):
            raise Exception(f"Invalid token: {token}")
        
        if not token.type == 'num':
            raise Exception(f"Invalid token type: {token.type}")
        
        else:
            if token.value != '':
                try:
                    self.stack.append(float(token.value))
                except ValueError:
                    raise Exception(f"Invalid number token, unable to convert {token.value} to float")
                
    
    def __repr__(self) -> str:
        if self.stack != []:
            rep_string = ''
            for x in self.stack[:-1]:
                rep_string += str(x) + '\n'
            rep_string += str(self.stack[-1])
        else: rep_string = ''
        return rep_string
