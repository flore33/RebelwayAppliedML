from Library.file_io import FileIO
from Library.book import Book
from dataclasses import dataclass, field, asdict
from Library.random_number_utils import RandomNumberUtils
import json


@dataclass()
class Library:
    """
    class for library
    add a book to the library
    remove a book from the library
    update a book in the library
    get a book from the library
    """
    dict_books: dict[str, Book] = field(default_factory=dict)


    def add_book(self, book_parm: Book):
        """
        add a book to the library
        """
        self.dict_books[book_parm.id] = book_parm

    def get_book(self, book_id: str):
        """
        get a book from the library
        """
        return self.dict_books.get(book_id)
    
    def remove_book(self, book_id: str):
        """
        remove a book from the library
        """
        removed_book = self.dict_books.pop(book_id, None)

        if removed_book:
            print(f"Book '{removed_book.title}' by {removed_book.author} removed from the library.")
        else:
            print(f"Book with ID '{book_id}' not found in the library.")
    
    def update_book(self, book_id: str, **kwargs):
        old_book = self.dict_books.get(book_id)
        if not old_book:
            print("Book not found.")
            return

        book_data = asdict(old_book)
        for key, value in kwargs.items():
            if key in book_data and key != "id":
                book_data[key] = value

        new_book = Book(**book_data)
        self.dict_books[book_id] = new_book
        print(f"Updated book '{new_book.title}' with price {new_book._price} and quantity {new_book.quantity}")

    def search_book_by_author(self, author_name: str):
        """
        search all books in the library with the author's name

        """
        found_books = [
            book for book in self.dict_books.values()
            if author_name.strip().lower() in book.author.lower()
        ]
        if found_books:
            for book in found_books:
                print(f"ID: {book.id} | Title: {book.title} | Author: {book.author}")
        if not found_books:
            print(f"No books found by author: {author_name}")
        return found_books

    def list_books_by_category(self, category_name: str)->list[Book]:
        """
        List all books in the library by category

        """
        found_books = [
            book for book in self.dict_books.values()
            if category_name.strip().lower() in book.category.lower()
        ]
       
        for book in found_books:
            print(f"ID: {book.id} | Title: {book.title} | Author: {book.author} | Category: {book.category}")
        if not found_books:
            print(f"No books found in the category: {category_name}")
        return found_books

            
    def list_all_books(self)->list[Book]:
        """
        List all books in the library
        """
        for book in self.dict_books.values():
            print(f"ID: {book.id} | Title: {book.title} | Author: {book.author} | Category: {book.category}")
               
        return list(self.dict_books.values())

    def save_library_to_file(self, file_path: str):
        """
        Save the library to a file
        """
        try:
            data_file = FileIO.load_json_files(file_path)
        except (FileNotFoundError, json.JSONDecodeError):
            data_file = {}  # Start fresh if file is missing or empty/invalid

            # Convert Book objects to dictionaries (important for JSON serialization)
        data_file["Books_list"] = {
            book_id: asdict(book) for book_id, book in self.dict_books.items()
        }
        FileIO.save_json_files(data_file, file_path)
        print(f"Library saved to {file_path}")

    def load_library_from_file(self, file_path: str):
        """
        Load the library from a file
        """
        data_file = FileIO.load_json_files(file_path)
        self.dict_books = {book_id: Book(**book_data) for book_id, book_data in data_file.get("Books_list", {}).items()}
        print(f"Library loaded from {file_path}")

    def print_book_details(self, book: Book):
        print(f"ID: {book.id} | Title: {book.title} | Author: {book.author} | Category: {book.category} | Price: {book._price} | Quantity: {book.quantity}")




   
        


# Create a Library instance
#library = Library()

# Create a Book instance
#book1 = Book(title="1984", author="George Orwell", year=1949, category="Fiction", _price=10.0, quantity=1)
#book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960, category="Fiction", _price=15.0, quantity=6)
#book3 = Book(title= "Go set a watchman", author="Harper Lee", year=2015, category="Fiction", _price=32.0, quantity=4)
#book4 = Book(title= "The Great Gatsby", author="F. Scott Fitzgerald", year=1925, category="Fiction", _price=10.0, quantity=1)
#book5 = Book(title= "The Catcher in the Rye", author="J.D. Salinger", year=1951, category="Fiction", _price=10.0, quantity=1)
#book6 = Book(title= "The Lord of the Rings", author="J.R.R. Tolkien", year=1954, category="Fiction", _price=10.0, quantity=1)
#book7 = Book(title= "The Hobbit", author="J.R.R. Tolkien", year=1937, category="Fiction", _price=10.0, quantity=1)
#book8 = Book(title= "The Da Vinci Code", author="Dan Brown", year=2003, category="Fiction", _price=10.0, quantity=1)
#book9 = Book(title= "The Alchemist", author="Paulo Coelho", year=1988, category="Fiction", _price=10.0, quantity=1)
#book10 = Book(title= "The Little Prince", author="Antoine de Saint-Exupéry", year=1943, category="Fiction", _price=10.0, quantity=1)

# Add the book to the library
#library.add_book(book1)
#library.add_book(book2)
#library.add_book(book3)
#library.add_book(book4)
#library.add_book(book5)
# library.add_book(book6)
#library.add_book(book7)
#library.add_book(book8)
#library.add_book(book9)
#library.add_book(book10)

# Confirm it was added
##print("Current books in the library:")

#for book_id, book in library.dict_books.items():
#    print(f"ID: {book_id} | Title: {book.title} | Author: {book.author}")  


#library.remove_book(book1.id)
#print("Book removed from the library:")
#for book_id, book in library.dict_books.items():
#    print(f"ID: {book_id} | Title: {book.title} | Author: {book.author}")  

#library.update_book(book2.id, _price=12.0, quantity=2)
#print("Book updated in the library:")
#for book_id, book in library.dict_books.items():
#    print(f"ID: {book_id} | Title: {book._price} | Author: {book.quantity}")  

#library.search_book_by_author("Harper Lee")
#print("Search book by author:")
#for book_id, book in library.dict_books.items():
#    print(f"ID: {book_id} | Title: {book.title} | Author: {book.author}")  

#library.save_library_to_file("../database_library.json")

#library.load_library_from_file("../database_library.json")











   
