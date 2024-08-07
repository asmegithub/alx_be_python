
class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out

    def isCheckedOut(self):
        return self._is_checked_out

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return True
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.isCheckedOut():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(book.title)
