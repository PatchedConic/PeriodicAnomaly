from .calculator import Calculator
from .token import Token
from .consts import *
import sys

def main(args):
    calculator = Calculator()
    for arg in args:
        if arg in MATH_TOKENS:
            calculator.receive(Token(arg))
        else:
            try:
                float(arg)
                calculator.receive(Token('num', arg))
            except ValueError:
                pass
    print(calculator.stack)

if __name__ == "__main__":
    main(sys.argv[1:])