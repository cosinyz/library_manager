from models.book import Book
from models.user import User
from models.admin import Admin
from services.library_service import Library


def main():
    library = Library()

    book1 = Book(
        1,
        "Python Basics",
        "John Smith",
        2024,
        "Programming"
    )

    book2 = Book(
        2,
        "Harry Potter",
        "J.K. Rowling",
        1997,
        "Fantasy"
    )

    user = User(
        1,
        "Ali",
        "ali@example.com",
        "12345"
    )

    admin = Admin(
        2,
        "Admin",
        "admin@example.com",
        "admin123"
    )

    library.add_book(book1)
    library.add_book(book2)

    library.add_user(user)
    library.add_user(admin)

    print("=== LIBRARY BOOKS ===")

    for book in library.get_books():
        print(book)

    print()
    print("=== LIBRARY USERS ===")

    for person in library.get_users():
        print(person)

    print()
    print("=== STATISTICS ===")
    print(library.get_statistics())

    print()
    print("=== BORROW BOOK ===")

    library.borrow_book(1, 1)

    print()
    print("Available books:")

    for book in library.get_available_books():
        print(book)

    print()
    print("=== RETURN BOOK ===")

    library.return_book(1, 1)

    print()
    print("Available books:")

    for book in library.get_available_books():
        print(book)

    print()
    print("=== SEARCH ===")

    result = library.find_book("Python")

    if result:
        print(result)

    print()
    print("Total books:", len(library))


if __name__ == "__main__":
    main()
