from dataclasses import dataclass

@dataclass
class Item():
    name: str
    description: str = None
    price: float = None
    tax: float = None