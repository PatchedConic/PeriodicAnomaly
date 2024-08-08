from textual.widgets import Switch


class Trig_Switch(Switch):
    BINDINGS = [
        ("ctrl+m", "toggle", "Toggle Switch")
    ]