class User:
    def __init__(self, user_id, name, email, password):
        self.id = user_id
        self.name = name
        self.email = email
        self.__password = password
        self.__books = []

    def get_info(self):
        return f"User #{self.id}: {self.name} | {self.email}"

    def get_permissions(self):
        return ["borrow", "return"]

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            return True

        return False

    def borrow_book(self, book):
        if book.check_availability():
            self.__books.append(book)
            book.is_available = False
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print("Book is not available.")

    def return_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
            book.is_available = True
            print(f"{self.name} returned '{book.title}'.")
        else:
            print("This user does not have this book.")

    @property
    def books(self):
        return self.__books.copy()

    def __str__(self):
        return self.get_info()
