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

def power(item) -> float:
    if len(item) > 1:
        return math.pow(y = item.pop(), x = item.pop())
    else: pass

def invert(item) -> float:
    if len(item) > 0:
        return item.pop() * -1
    else: pass

def square(item) -> float:
    if len(item) > 0:
        return math.pow(item.pop(), 2)
    else: pass

def sqrt(item) -> float:
    if len(item) > 0:
        return math.sqrt(item.pop())
    else: pass

def pi() -> float:
    return math.pi

def e() -> float:
    return math.e

def log(item) -> float:
    if len(item) > 0:
        return math.log(item.pop())
    else: pass

def swap(item) -> None:
    if len(item) > 1:
        first = item.pop()
        second = item.pop()
        item.push(second, first)