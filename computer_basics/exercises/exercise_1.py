"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b = Book("1984", "George Orwell")
print(b.title)  # Output: 1984

"""
"""
class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book(title='{self.title}')"

b = Book("1984")
print(b)  # Output: Book(title='1984')
"""
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __repr__(self):
        return f"Movie(title='{self.title}', director='{self.director}', year={self.year})"

    def __eq__(self, other):
        return (
            isinstance(other, Movie) and
            self.title == other.title and
            self.director == other.director and
            self.year == other.year
        )

# Try it out
movie1 = Movie("Inception", "Christopher Nolan", 2010)
movie2 = Movie("Inception", "Christopher Nolan", 2010)
movie3 = Movie("Tenet", "Christopher Nolan", 2020)

print(movie1)               # Uses __repr__
print(movie1 == movie2)     # Uses __eq__ → True
print(movie1 == movie3)     # Uses __eq__ → False
