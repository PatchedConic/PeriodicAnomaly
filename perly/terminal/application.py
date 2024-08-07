from textual.app import App, ComposeResult
from textual.widgets import Header, Label
from textual import events
from textual.containers import Container, Horizontal


from perly.terminal.stack import Stack
from perly.terminal.shortcuts import Shortcuts
from perly.calculator import Calculator
from perly.consts import DIGITS
from perly.terminal.keybindings import KEYBINDINGS

class AnomalyTUI(App):

    CSS_PATH = "styles.css"
    CALC = Calculator()

    def __init__(self):
        super().__init__()
        self.title = "Anomaly"
        global ApplicationInstance
        ApplicationInstance = self

    def compose(self) -> ComposeResult:
        yield Header()
        self.stack = Stack(AnomalyTUI.CALC)
        self.shortcuts = Shortcuts()
        yield Container(Horizontal(
            self.stack,
            self.shortcuts
        ))

    
    def on_key(self, event: events.Key) -> None:
        # self.query_one(RichLog).write(event)
        if event.character in DIGITS:
            self.stack.push(event.character)
        elif event.key == 'enter':
            self.stack.enter()
        elif event.key == 'backspace':
            self.stack.backspace()
        elif event.key in KEYBINDINGS.keys():
            self.stack.push(event.key)
        elif event.key == 'escape':
            self.stack.clear()
        elif event.key == 'm':
            self.switch_trig_mode()

    def switch_trig_mode(self):
        AnomalyTUI.CALC.trigMode = 'degrees' if AnomalyTUI.CALC.trigMode == 'radians' else 'radians'
        self.stack.trig_label.update(f"{AnomalyTUI.CALC.trigMode}")


if __name__ == "__main__":
    app = AnomalyTUI()
    app.run()