from dataclasses import dataclass

@dataclass
class Token:
    type: str
    value: float = None