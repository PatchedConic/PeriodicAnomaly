import math
import perly.functions as funcs

FUNCTIONS_DICT = {
    "+":funcs.addition,
    "-":funcs.subtract,
    "*":funcs.multiply,
    "/":funcs.divide,
    "negate":funcs.negate,
    "!":funcs.factorial,
    "^":funcs.power,
    "invert":funcs.invert,
    "sin":funcs.sin,
    "cos":funcs.cos,
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
    "square":funcs.square,
    "sqrt":funcs.sqrt,
    "log":funcs.log,
    "e":funcs.e,
    "pi":funcs.pi,
    "swap": funcs.swap
}

MATH_TOKENS = FUNCTIONS_DICT.keys()