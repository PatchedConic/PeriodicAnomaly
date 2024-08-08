import math
def sin(item) -> float:
    try:
        if item.trigMode == 'radians':
            theta = item.pop()
            if theta % math.pi == 0: return 0
            else: return math.sin(theta)
        elif item.trigMode == 'degrees':
            return sind(item)
        else: raise Exception("Holy fuck")
    except:
        raise Exception("Holy fuck")

def cos(item) -> float:
    try:
        if item.trigMode == 'radians':
            theta = item.pop()
            if (theta+math.pi/2) % (math.pi) == 0: return 0
            else: return math.cos(theta)
        elif item.trigMode == 'degrees':
            return cosd(item)
    except:
        pass

def tan(item) -> float:
    try:
        if item.trigMode == 'radians':
            theta = item.pop()
            if (theta+math.pi/2) % math.pi == 0: return math.nan
            elif (theta % math.pi) == 0: return 0
            else: return math.tan(theta)
        elif item.trigMode == 'degrees':
            return tand(item)
    except:
        pass

def sind(item) -> float:
    try:
        theta = item.pop()
        if theta % 180 == 0:
            return 0
        else:
            return math.sin(theta*2*math.pi/360)
    except:
        pass

def cosd(item) -> float:
    try:
        theta = item.pop()
        if (theta+90) % 180 == 0: return 0
        else:
            return sin(theta*2*math.pi/360)
    except:
        pass

def tand(item) -> float:
    try:
        theta = item.pop()
        if (theta + 90) % 180 == 0: return math.nan
        elif theta % 180 == 0: return 0
        else:
            return tan(theta*2*math.pi/360)
    except:
        pass

def asin(item) -> float:
    try:
        if item.trigMode == 'radians':
            return math.asin(item.pop())
        elif item.trigMode == 'degrees':
            return asind(item)
    except:
        raise Exception

def acos(item) -> float:
    try:
        if item.trigMode == 'radians':
            return math.acos(item.pop())
        elif item.trigMode == 'degrees':
            return acosd(item)
    except:
        pass

def atan(item) -> float:
    try:
        if item.trigMode == 'radians':
            return math.atan(item.pop())
        elif item.trigMode == 'degrees':
            return atand(item)
    except:
        pass

def asind(item) -> float:
    try:
        return (math.asin(item.pop())*360/(math.pi*2))
    except:
        pass

def acosd(item) -> float:
    try:
        return math.acos(item.pop())*360/(math.pi*2)
    except:
        pass

def atand(item) -> float:
    try:
        return math.atan(item.pop())*360/(math.pi*2)
    except:
        pass

def addition(item) -> float:
    if len(item)>1 : return item.pop() + item.pop()
    else:
        pass

def subtract(item) -> float:
    if len(item)>1 : return item.pop(1)-item.pop()
    else:
        pass

def multiply(item) -> float:
    if len(item)>1 : return item.pop() * item.pop()
    else:
        pass

def divide(item) -> float:
    if len(item)>1 : 
        return (item.pop(1) / item.pop())
    else:
        pass
def negate(item) -> float:
    if len(item) > 0: return item.pop()*-1
    else:
        pass

def factorial(item) -> int:
    if len(item) > 0:
        try:
            return math.factorial(int(item.pop()))
        except:
            pass
    else: pass

def power(item) -> float:
    if len(item) > 1:
        return math.pow(item.pop(1), item.pop())
    else: pass

def invert(item) -> float:
    if len(item) > 0:
        return 1/item.pop() 
    else: pass

def square(item) -> float:
    if len(item) > 0:
        return math.pow(item.pop(), 2)
    else: pass

def sqrt(item) -> float:
    if len(item) > 0:
        return math.sqrt(item.pop())
    else: pass

def pi(item) -> float:
    return math.pi

def e(item) -> float:
    return math.e

def log(item) -> float:
    if len(item) > 0:
        return math.log(item.pop())
    else: pass

def swap(item) -> None:
    if len(item) > 1:
        first = item.pop()
        second = item.pop()
        item.push(first, second)