import Library.library_script as library_script 
import Library.book as book
import Library.file_io as file_io   
import unittest

class TestLibraryScript(unittest.TestCase):

    def setUp(self):
        self.library = library_script.Library()
        self.book = book.Book(id="KWEFGD", title="1984", author="George Orwell", year=1949, category="Fiction", _price=9.999, quantity=1)
        self.file_io = file_io.FileIO()

    def test_add_book(self):
        self.library.add_book(self.book)
        self.assertEqual(self.library.dict_books[self.book.id], self.book)

    def test_get_book(self):
        self.library.add_book(self.book)
        self.assertEqual(self.library.get_book(self.book.id), self.book)

    def test_remove_book(self):
        self.library.add_book(self.book)
        self.library.remove_book(self.book.id)
        self.assertEqual(self.library.get_book(self.book.id), None)

    def test_update_book(self):
        self.library.add_book(self.book)
        self.library.get_book(self.book.id)
        self.library.update_book(self.book.id, _price=10.0, quantity=2)
        self.assertEqual(self.library.get_book(self.book.id).price, 10.0)
        self.assertEqual(self.library.get_book(self.book.id).quantity, 2)

    def test_search_book_by_author(self):
        self.library.add_book(self.book)
        self.library.search_book_by_author(self.book.author)
        self.assertEqual(self.library.search_book_by_author(self.book.author), [self.book])

    def test_list_books_by_category(self):
        self.library.add_book(self.book)
        self.library.list_books_by_category(self.book.category)
        self.assertEqual(self.library.list_books_by_category(self.book.category), [self.book])

    def test_list_all_books(self):
        self.library.add_book(self.book)
        self.library.list_all_books()
        self.assertEqual(self.library.list_all_books(), [self.book])

    def test_save_library_to_file(self):
        self.library.add_book(self.book)
        try:
            self.library.save_library_to_file("test_database_library.json")
        except Exception as e:
            self.fail(f"Error saving library to file: {e}")

    def test_load_library_from_file(self):
        self.library.add_book(self.book)
        try:
            self.library.load_library_from_file("test_database_library.json")
        except Exception as e:
            self.fail(f"Error loading library from file: {e}")

    

   


    

		




    

    
   