class Library:
    def __init__(self):
        self.__books = []
        self.__users = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book_id):
        self.__books = [
            book for book in self.__books
            if book.id != book_id
        ]

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, user_id):
        self.__users = [
            user for user in self.__users
            if user.id != user_id
        ]

    def get_books(self):
        return self.__books.copy()

    def get_users(self):
        return self.__users.copy()

    def find_book(self, title):
        for book in self.__books:
            if title.lower() in book.title.lower():
                return book

        return None

    def get_available_books(self):
        return [
            book for book in self.__books
            if book.check_availability()
        ]

    def borrow_book(self, user_id, book_id):
        user = next(
            (user for user in self.__users if user.id == user_id),
            None
        )

        book = next(
            (book for book in self.__books if book.id == book_id),
            None
        )

        if user is None:
            print("User not found.")
            return

        if book is None:
            print("Book not found.")
            return

        user.borrow_book(book)

    def return_book(self, user_id, book_id):
        user = next(
            (user for user in self.__users if user.id == user_id),
            None
        )

        book = next(
            (book for book in self.__books if book.id == book_id),
            None
        )

        if user is None:
            print("User not found.")
            return

        if book is None:
            print("Book not found.")
            return

        user.return_book(book)

    def get_statistics(self):
        total_books = len(self.__books)
        total_users = len(self.__users)

        available_books = len(self.get_available_books())
        borrowed_books = total_books - available_books

        return {
            "books": total_books,
            "users": total_users,
            "available_books": available_books,
            "borrowed_books": borrowed_books
        }

    def __len__(self):
        return len(self.__books)
