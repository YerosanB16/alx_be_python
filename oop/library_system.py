# Base Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition - Library
class Library:
    def __init__(self):
        self.books = []  # Holds Book, EBook, PrintBook instances

    def add_book(self, book):
        if isinstance(book, Book):  # Ensure only Book or subclasses are added
            self.books.append(book)
        else:
            print("Only books can be added to the library.")

    def list_books(self):
        for book in self.books:
            print(book)  # Uses __str__ method of the book
