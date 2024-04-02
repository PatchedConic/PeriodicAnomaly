from .stack import Stack
from .token import Token
from .consts import *
import re
import sys

def main(args):
    stack = Stack()
    for arg in args:
        if re.search(r'^\d+(\.\d+)?$', arg):
            token = Token('num', str(arg))
            stack.add_token(token)
            stack.enter()
        elif str(arg) in TOKENTYPES:
            token = Token(arg)
            stack.add_token(token)
    for x in stack.stack:
        if x != '':
            print(x)

if __name__ == "__main__":
    main(sys.argv[1:])