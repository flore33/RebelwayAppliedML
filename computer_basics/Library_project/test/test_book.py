import unittest
from Library.book import Book
from Library.random_number_utils import RandomNumberUtils


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book(id="KWEFGD", title="1984", author="George Orwell", year=1949, category="Fiction", _price=9.999, quantity=1)

    def test_book_creation(self):
        self.assertEqual(self.book.id, "KWEFGD")
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.author, "George Orwell")
        self.assertEqual(self.book.year, 1949)
        self.assertEqual(self.book.category, "Fiction")
        self.assertEqual(self.book._price, 9.999)
        self.assertEqual(self.book.quantity, 1)

    def test_book_price(self):
        self.assertEqual(self.book._price, 9.999)

    def test_book_search_string(self):
        self.assertEqual(self.book.search_string, "(1984 George Orwell)")

    def test_book_id(self): 
        self.assertIsInstance(self.book.id, str)
        self.assertEqual(len(self.book.id), 6)
        self.assertTrue(self.book.id.isupper())
    
    def test_price_rounding(self):
        self.assertEqual(self.book.price, 10.00)

  
