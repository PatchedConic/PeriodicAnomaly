from .calculator import Calculator
import argparse

def main(args:list[float|str]):
    calculator = Calculator()
    for arg in args:
        calculator.receive(arg)
    print(calculator.stack)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "perly", 
        description="A simple RPN calculator with CLI, TUI, and GUI options")
    parser.add_argument("args", 
                        help="A list of numbers, mathematical operators, and functions to process",
                        nargs='*')
    args = parser.parse_args()
    main(args.args)