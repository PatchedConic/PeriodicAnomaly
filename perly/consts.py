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
    "tan":funcs.tan,
    "sind":funcs.sind,
    "cosd":funcs.cosd,
    "tand":funcs.tand,
    "asin":funcs.asin,
    "acos":funcs.acos,
    "atan":funcs.atan,
    "asind":funcs.asind,
    "acosd":funcs.acosd,
    "atand":funcs.atand,
    "square":funcs.square,
    "sqrt":funcs.sqrt,
    "log":funcs.log,
    "e":funcs.e,
    "pi":funcs.pi,
    "swap": funcs.swap
}

MATH_TOKENS = FUNCTIONS_DICT.keys()