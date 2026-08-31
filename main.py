from database.queries import return_book, get_available_books


def main():
    print("Available books before returning:")

    books = get_available_books()

    for book in books:
        print(book)

    print()

    return_book(1)

    print()

    print("Available books after returning:")

    books = get_available_books()

    for book in books:
        print(book)


if __name__ == "__main__":
    main()
