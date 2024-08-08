from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Label, Switch, Button
from perly.calculator import Calculator
from perly.terminal.trig_switch import Trig_Switch


from perly.terminal.register import Register
from perly.consts import DIGITS
from perly.terminal.keybindings import KEYBINDINGS

class Stack(Container):
    def __init__(self, calc: Calculator):
        self.x_reg = Register('x', calc)
        self.y_reg = Register('y', calc)
        self.z_reg = Register('z', calc)
        self.t_reg = Register('t', calc)
        self.calc = calc
        self.trig_label = Label(f"{self.calc.trigMode}")
        self.trig_container = Container(self.trig_label, id = "trig_container")
        self.trig_container.border_title = "Mode"
        self.thankyou_label = Label("""Thanks for checking out Anomaly! Check out the source code at Github""", id="thankyou")
        super().__init__(Vertical(
            self.t_reg,
            self.z_reg,
            self.y_reg,
            self.x_reg,
            Horizontal(self.thankyou_label, self.trig_container
                )))
        self.calc.add_listeners(self)
        self.update()

    def clear(self) -> None:
        self.x_reg.entry = ""
        self.calc.clear()
        self.update()

    def backspace(self) -> None:
        if self.x_reg.entry != "":
            self.x_reg.entry = self.x_reg.entry[0:-1]
        else:
            self.calc.pop()
        self.update()

    def enter(self) -> None:
        self.calc.push(self.x_reg.value)
        self.x_reg.clear()
        self.update()

    def update(self) -> None:
        if self.x_reg.entry == "":
            self.t_reg.update(str(self.calc.peek(3)))
            self.z_reg.update(str(self.calc.peek(2)))
            self.y_reg.update(str(self.calc.peek(1)))
            self.x_reg.update(str(self.calc.peek(0)))
        else:
            self.t_reg.update(str(self.calc.peek(2)))
            self.z_reg.update(str(self.calc.peek(1)))
            self.y_reg.update(str(self.calc.peek(0)))
            self.x_reg.update(self.x_reg.entry)

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