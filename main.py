from database.queries import get_borrowing_history, get_books_with_genres


def main():
    print("=== BORROWING HISTORY ===")

    history = get_borrowing_history()

    for record in history:
        print(record)

    print()

    print("=== BOOKS WITH AUTHORS AND GENRES ===")

    books = get_books_with_genres()

    for book in books:
        print(book)


if __name__ == "__main__":
    main()
