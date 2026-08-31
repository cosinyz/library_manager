from database.queries import get_books, delete_book


def main():
    print("Before deleting:")

    books = get_books()

    for book in books:
        print(book)

    delete_book(2)

    print()
    print("After deleting:")

    books = get_books()

    for book in books:
        print(book)


if __name__ == "__main__":
    main()
