from textual.containers import Container, Vertical
from textual.widgets import Label
from perly.calculator import Calculator

from perly.terminal.register import Register
from perly.consts import DIGITS
from perly.terminal.keybindings import KEYBINDINGS

class Stack(Container):
    def __init__(self, calc: Calculator):
        self.x_reg = Register('x', calc)
        self.y_reg = Register('y', calc)
        self.z_reg = Register('z', calc)
        self.t_reg = Register('t', calc)
        super().__init__(Vertical(
            self.x_reg,
            self.y_reg,
            self.z_reg,
            self.t_reg,
            Label("This area for command shortcuts", id="shortcuts")
        ))
        self.calc = calc
        self.calc.add_listeners(self)
        self.update()

    def enter(self) -> None:
        self.calc.push(self.x_reg.value)
        self.x_reg.clear()
        self.update()

    def update(self) -> None:
        if self.x_reg.entry == "":
            self.x_reg.update(str(self.calc.peek(0)))
            self.y_reg.update(str(self.calc.peek(1)))
            self.z_reg.update(str(self.calc.peek(2)))
            self.t_reg.update(str(self.calc.peek(3)))
        else:
            self.x_reg.update(self.x_reg.entry)
            self.y_reg.update(str(self.calc.peek(0)))
            self.z_reg.update(str(self.calc.peek(1)))
            self.t_reg.update(str(self.calc.peek(2)))

    def push(self, token) -> None:
        if token in DIGITS:
            self.x_reg.entry += token
            self.update()
        elif token in KEYBINDINGS.keys():
            if self.x_reg.entry != "":
                self.enter()
            self.calc.push(KEYBINDINGS[token])
        else:
            raise Exception(f"Couldn't append {token} to register. Not a float")