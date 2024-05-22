import math
# from perly.calculator import Calculator

def addition(item) -> float:
    if len(item)>1 : return item.pop() + item.pop()
    else:
        pass

def subtraction(item) -> float:
    if len(item)>1 : return item.pop(1)-item.pop()
    else:
        pass

def multiply(item) -> float:
    if len(item)>1 : return item.pop() * item.pop()
    else:
        pass

def divide(item) -> float:
    if len(item)>1 : return item.pop(1) / item.pop()
    else:
        pass