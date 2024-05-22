import math

FUNCTIONS_DICT = {
    "+":lambda stack:stack.pop()+stack.pop(),
    "-":lambda stack:-stack.pop()+stack.pop(),
    "*":lambda stack:stack.pop()*stack.pop(),
    "/":lambda stack:(1/stack.pop()*stack.pop()),
    "n":lambda stack:-stack.pop(),
    "!":lambda stack:math.factorial(int(stack.pop())),
    "^":lambda stack:math.pow(y=stack.pop(), x=stack.pop()),
    "i":lambda stack:1/stack.pop(),
    "sin":lambda stack:math.sin(stack.pop()),
    "cos":lambda stack:math.cos(stack.pop()),
    "tan":lambda stack:math.tan(stack.pop()),
    "sind":lambda stack:math.sin(stack.pop()*2*math.pi/360),
    "cosd":lambda stack:math.cos(stack.pop()*2*math.pi/360),
    "tand":lambda stack:math.tan(stack.pop()*2*math.pi/360),
    "asin":lambda stack:math.asin(stack.pop()),
    "acos":lambda stack:math.acos(stack.pop()),
    "atan":lambda stack:math.atan(stack.pop()),
    "asind":lambda stack:math.asin(stack.pop())*360/(math.pi*2),
    "acosd":lambda stack:math.acos(stack.pop())*360/(2*math.pi),
    "atand":lambda stack:math.atan(stack.pop())*360/(2*math.pi),
    "square":lambda stack:math.pow(stack.pop(),2),
    "sqrt":lambda stack:math.sqrt(stack.pop()),
    "ln":lambda stack:math.log(stack.pop()),
    "e":lambda stack: math.e,
    "c":lambda stack:stack.clear(),
    "pi":lambda stack: math.pi,
    "s":lambda stack:stack.append(stack.pop(),stack.pop())
}

MATH_TOKENS = FUNCTIONS_DICT.keys()