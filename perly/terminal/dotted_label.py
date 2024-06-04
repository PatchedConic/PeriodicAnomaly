from textual.widgets import Label
from textual.events import Resize
from textual.reactive import Reactive

class DottedLabel(Label):
    # text: Reactive[str] = Reactive("")
    # key: Reactive[str] = Reactive("")

    def __init__(self, text: str, key: str, width: int):
        super().__init__()
        self.text = text
        self.key = key
        # width = self.parent.size.width
        available_space = width - len(self.text) - len(self.key)
        num_periods = max(0, available_space)
        periods = "." * num_periods
        self.update(f"{self.text}{periods}{self.key}")


    # def render(self) -> str:
    #     width = self.size.width
    #     available_space = width - len(self.text) - len(self.key)
    #     num_periods = max(0, available_space)
    #     periods = "." * num_periods
    #     return f"{self.text}{periods}{self.key}"

    # async def on_resize(self, event: Resize) -> None:
    #     self.refresh()