# class Book:
#     def __init__(self, title, author, _is_checked_out):
#         self.title = title
#         self.author = author
#         self._is_checked_out = _is_checked_out


# class Library:
#     def __init__(self, books):
#         self._books = books

#     def add_book(self, book):
#         self._books.append(book)

#     def check_out_book(self, title):
#         books = [book for book in self._books if book.title == title]
#         if books[0]:
#             books[0]._is_checked_out = True
#             return True
#         return False

#     def return_book(self, title):
#         self._books = [book for book in self._books if book.title == title]
#         if title in self._books:
#             title._is_checked_out = False
#             return True
#         return False

#     def list_available_books(self):
#         for book in self._books:
#             if not book._is_checked_out:
#                 print(book.title)
class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out


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
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return True
        return False

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(book.title)

    # def check_out_book(self, title):
    #     for book in self._books:
    #         if book.title == title and not book._is_checked_out:
    #             book._is_checked_out = True
    #             return True
    #     return False

    # def return_book(self, title):
    #     for book in self._books:
    #         if book.title == title and book._is_checked_out:
    #             book._is_checked_out = False
    #             return True
    #     return False

    # def list_available_books(self):
    #     for book in self._books:
    #         if not book._is_checked_out:
    #             print(book.title)
