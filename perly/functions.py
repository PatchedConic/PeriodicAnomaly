import math
# from perly.calculator import Calculator

def addition(item) -> float:
    if len(item)>1 : return item.pop() + item.pop()
    else:
        pass

def subtract(item) -> float:
    if len(item)>1 : return -1*item.pop()+item.pop()
    else:
        pass

def multiply(item) -> float:
    if len(item)>1 : return item.pop() * item.pop()
    else:
        pass

def divide(item) -> float:
    if len(item)>1 : return (1/item.pop()) * item.pop()
    else:
        pass
def negate(item) -> float:
    if len(item) > 0: return item.pop()*-1
    else:
        pass

def factorial(item) -> int:
    if len(item) > 0:
        number = item.pop()
        if type(number) == 'int': return math.factorial(number)
        else: pass
    else: pass
