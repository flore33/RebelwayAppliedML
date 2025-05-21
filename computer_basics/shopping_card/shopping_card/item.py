from dataclasses import dataclass, field
from shopping_card.random_number_utils import RandomNumberUtils

@dataclass(frozen=True, order=True, slots=True)
class Item:
    """
    class for item
    """
    name: str
    type: str
    _price: float = 0.0
    quantity: int = field(default=1)
    id: str = field(default_factory=RandomNumberUtils.generate_random_id)

    @property
    def price(self):
        return round(self._price,2)
    
    @property
    def search_string(self):
        return f"({self.name} {self.type})"
        