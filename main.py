from database.queries import search_books


def main():
    print("=== SEARCH RESULTS ===")

    books = search_books("Python")

    for book in books:
        print(book)


if __name__ == "__main__":
    main()
