from textual.containers import Vertical, Container, Horizontal
from textual.widgets import Label


class Shortcuts(Container):

    KEYBINDINGS = [
        ("Add", "+"),
        ("Subtract", "-"),
        ("Multiply", "*"),
        ("Divide", "/"),
        ("Square", "q"),
        ("Square Root", "r"),
        ("Raise To", "^"),
        ("Ln", "l"),
        ("Swap", "ctrl+s"),
        ("Pi", "p"),
        ("Natural Exp", "e"),
        ("Sin", "s"),
        ("Cos", "c"),
        ("Tan", "t"),
        ("Asin", "shift+s"),
        ("Acos", "shift+c"),
        ("Atan", "shift+t"),
        ("Negate", "n"),
        ("Factorial", '!'),
        ("Delete", "backspace"),
        ("Clear", "escape or del"),
        ("Command Pallete", "ctrl+\\"),
        ("Quit", "ctrl+c")
    ]

    def __init__(self):
        rows = []
        for i, (text, key) in enumerate(Shortcuts.KEYBINDINGS):
            # Alternate row background color
            if i % 2 == 0:
                bg_class = "table_light"
            else:
                bg_class = "table_dark"
            # Create Label widgets for text and key, with zebra striping
            text_label = Label(text, classes = f"table_left {bg_class}")
            key_label = Label(key, classes = f"table_right {bg_class}")
            rows.append(Horizontal(text_label, key_label))
        super().__init__(Vertical(*rows), id="shotcuts")
        self.border_title = "Shortcuts"
