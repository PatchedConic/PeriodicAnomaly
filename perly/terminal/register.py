from textual.widgets import Digits


class Register(Digits):

    register_position = {
        'x':0,
        'y':1,
        'z':2,
        't':3
    }

    title = {
        'x': "X Register",
        'y': "Y Register",
        'z': "Z Register",
        't': "T Register"
    }


    def __init__(self, register_name, calc):
        super().__init__("")
        self.border_title = Register.title[register_name]
        self.register_position = Register.register_position[register_name]
        self.calc = calc
        self.update(str(self.calc.peek(self.register_position)))
        self.entry = ""

    def clear(self):
         self.entry = ""
