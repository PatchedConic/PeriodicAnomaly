from .calculator import Calculator
from .consts import *
import sys

def main(args:list[float|str]):
    calculator = Calculator()
    for arg in args:
        if arg in MATH_TOKENS:
            calculator.receive(arg)
        else:
            try:
                float(arg)
                calculator.receive(float(arg))
            except ValueError:
                raise Exception(f"Invalid entry {arg}")
    print(calculator.stack)

if __name__ == "__main__":
    main(sys.argv[1:])