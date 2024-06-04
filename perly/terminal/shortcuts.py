from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Label

class Shortcuts(Container):
    def __init__(self):
        super().__init__(Container(Horizontal(
            Label("""
                  Addition
                  Subtraction
                  Muliplication
                  Division
                  Power
                  Factorial
                  Sin
                  Cos
                  Tan
                  Asin
                  Acos
                  Atan
"""), Label("""
            +
            -
            *
            /
            ^
            !
            s
            c
            t
            shift + s
            shift + c
            shift + t"""))))
        self.border_title = "Shortcuts"