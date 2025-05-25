# import libraries
from dataclasses import dataclass, field
from Library.random_number_utils import RandomNumberUtils

#set module with behabior arguments
@dataclass(frozen=True, order=True, slots=True)
class Book:
    """
    class for book
    """
    title: str
    author: str
    year: int
    category: str
    _price: float = 0.0
    quantity: int = field(default=1)
    id: str = field(default_factory=RandomNumberUtils.generate_random_id)

    @property
    def price(self):
        return round(self._price,2)
    
    @property
    def search_string(self):
        return f"({self.title} {self.author})"


    
#book = Book(title="1984", author="George Orwell", year=1949, category="Fiction", _price=10.0, quantity=1, id="FGHJKL")
#print(book.price)
#print(book.search_string)
#print(book.id)


