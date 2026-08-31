from database.queries import (
    add_book,
    get_books,
    get_book_by_id,
    update_book,
    delete_book,
    add_user,
    get_users,
    update_user_email,
    delete_user,
    borrow_book,
    return_book,
    get_borrowing_history,
    get_books_with_genres,
    get_statistics,
    search_books,
    get_books_by_genre,
    get_books_by_author,
    get_borrowings_by_user,
    get_popular_genres,
    get_active_users,
    get_genres,
    add_genre,
    delete_genre,
)


def show_books():
    print("\n=== BOOKS ===")

    books = get_books()

    if not books:
        print("No books found.")
        return

    for book in books:
        status = "Available" if book[5] else "Borrowed"

        print(
            f"ID: {book[0]} | "
            f"{book[1]} | "
            f"Author: {book[2]} | "
            f"Year: {book[3]} | "
            f"Genre ID: {book[4]} | "
            f"{status}"
        )


def add_book_menu():
    print("\n=== ADD BOOK ===")

    title = input("Title: ")
    author = input("Author: ")

    try:
        year = int(input("Year: "))
        genre_id = int(input("Genre ID: "))
    except ValueError:
        print("Invalid number.")
        return

    add_book(title, author, year, genre_id)
    print("Book added successfully.")


def search_book_menu():
    print("\n=== SEARCH BOOK ===")

    text = input("Enter title or author: ")

    books = search_books(text)

    if not books:
        print("No books found.")
        return

    for book in books:
        status = "Available" if book[5] else "Borrowed"

        print(
            f"ID: {book[0]} | "
            f"{book[1]} | "
            f"Author: {book[2]} | "
            f"Year: {book[3]} | "
            f"Genre: {book[4]} | "
            f"{status}"
        )


def update_book_menu():
    print("\n=== UPDATE BOOK ===")

    try:
        book_id = int(input("Book ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    book = get_book_by_id(book_id)

    if book is None:
        print("Book not found.")
        return

    print(f"Current title: {book[1]}")
    print(f"Current author: {book[2]}")
    print(f"Current year: {book[3]}")
    print(f"Current genre ID: {book[4]}")

    title = input("New title: ")
    author = input("New author: ")

    try:
        year = int(input("New year: "))
        genre_id = int(input("New genre ID: "))
    except ValueError:
        print("Invalid number.")
        return

    update_book(
        book_id,
        title,
        author,
        year,
        genre_id
    )

    print("Book updated successfully.")


def delete_book_menu():
    print("\n=== DELETE BOOK ===")

    try:
        book_id = int(input("Book ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    book = get_book_by_id(book_id)

    if book is None:
        print("Book not found.")
        return

    delete_book(book_id)

    print("Book deleted successfully.")


def show_users():
    print("\n=== USERS ===")

    users = get_users()

    if not users:
        print("No users found.")
        return

    for user in users:
        print(
            f"ID: {user[0]} | "
            f"Name: {user[1]} | "
            f"Email: {user[2]}"
        )


def add_user_menu():
    print("\n=== ADD USER ===")

    name = input("Name: ")
    email = input("Email: ")

    add_user(name, email)

    print("User added successfully.")


def delete_user_menu():
    print("\n=== DELETE USER ===")

    try:
        user_id = int(input("User ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    delete_user(user_id)

    print("User deleted successfully.")


def update_user_menu():
    print("\n=== UPDATE USER ===")

    try:
        user_id = int(input("User ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    email = input("New email: ")

    update_user_email(user_id, email)

    print("Email updated successfully.")


def borrow_book_menu():
    print("\n=== BORROW BOOK ===")

    try:
        book_id = int(input("Book ID: "))
        user_id = int(input("User ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    borrow_book(book_id, user_id)


def return_book_menu():
    print("\n=== RETURN BOOK ===")

    try:
        book_id = int(input("Book ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    return_book(book_id)


def show_history():
    print("\n=== BORROWING HISTORY ===")

    history = get_borrowing_history()

    if not history:
        print("No borrowing history.")
        return

    for item in history:
        print(
            f"Book: {item[0]} | "
            f"User: {item[1]} | "
            f"Borrowed: {item[2]} | "
            f"Returned: {item[3]}"
        )


def show_statistics():
    print("\n=== STATISTICS ===")

    statistics = get_statistics()

    print(f"Books: {statistics['books_count']}")
    print(f"Users: {statistics['users_count']}")
    print(f"Average publication year: {statistics['average_year']}")
    print(f"Oldest publication year: {statistics['oldest_year']}")
    print(f"Newest publication year: {statistics['newest_year']}")
    print(f"Borrowings: {statistics['borrowings_count']}")
    print(f"Sum of publication years: {statistics['years_sum']}")

    print("\n=== BOOKS BY GENRE ===")

    for item in get_books_by_genre():
        print(f"{item[0]} -> {item[1]}")

    print("\n=== BOOKS BY AUTHOR ===")

    for item in get_books_by_author():
        print(f"{item[0]} -> {item[1]}")

    print("\n=== BORROWINGS BY USER ===")

    for item in get_borrowings_by_user():
        print(f"{item[0]} -> {item[1]}")

    print("\n=== POPULAR GENRES ===")

    popular_genres = get_popular_genres()

    if popular_genres:
        for item in popular_genres:
            print(f"{item[0]} -> {item[1]}")
    else:
        print("No popular genres.")

    print("\n=== ACTIVE USERS ===")

    active_users = get_active_users()

    if active_users:
        for item in active_users:
            print(f"{item[0]} -> {item[1]}")
    else:
        print("No active users.")


def show_book_details():
    print("\n=== BOOK DETAILS ===")

    try:
        book_id = int(input("Book ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    book = get_book_by_id(book_id)

    if book is None:
        print("Book not found.")
        return

    status = "Available" if book[5] else "Borrowed"

    print(f"ID: {book[0]}")
    print(f"Title: {book[1]}")
    print(f"Author: {book[2]}")
    print(f"Year: {book[3]}")
    print(f"Genre ID: {book[4]}")
    print(f"Status: {status}")


def add_genre_menu():
    print("\n=== ADD GENRE ===")

    name = input("Genre name: ")

    add_genre(name)

    print("Genre added successfully.")


def show_genres():
    print("\n=== GENRES ===")

    genres = get_genres()

    if not genres:
        print("No genres found.")
        return

    for genre in genres:
        print(f"{genre[0]}. {genre[1]}")


def delete_genre_menu():
    print("\n=== DELETE GENRE ===")

    try:
        genre_id = int(input("Genre ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    delete_genre(genre_id)

    print("Genre deleted successfully.")


def show_join_data():
    print("\n=== BOOKS WITH AUTHORS AND GENRES ===")

    books = get_books_with_genres()

    if not books:
        print("No data.")
        return

    for book in books:
        print(
            f"Book: {book[0]} | "
            f"Author: {book[1]} | "
            f"Genre: {book[2]}"
        )


def main():
    while True:
        print()
        print("=== LIBRARY MANAGER ===")
        print()
        print("1. Add book")
        print("2. Show books")
        print("3. Find book")
        print("4. Update book")
        print("5. Delete book")
        print()
        print("6. Add user")
        print("7. Show users")
        print("8. Delete user")
        print("9. Update user email")
        print()
        print("10. Borrow book")
        print("11. Return book")
        print("12. Borrowing history")
        print()
        print("13. Statistics")
        print("14. Book details")
        print()
        print("15. Add genre")
        print("16. Show genres")
        print("17. Delete genre")
        print("18. Books with authors and genres")
        print()
        print("0. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_book_menu()

        elif choice == "2":
            show_books()

        elif choice == "3":
            search_book_menu()

        elif choice == "4":
            update_book_menu()

        elif choice == "5":
            delete_book_menu()

        elif choice == "6":
            add_user_menu()

        elif choice == "7":
            show_users()

        elif choice == "8":
            delete_user_menu()

        elif choice == "9":
            update_user_menu()

        elif choice == "10":
            borrow_book_menu()

        elif choice == "11":
            return_book_menu()

        elif choice == "12":
            show_history()

        elif choice == "13":
            show_statistics()

        elif choice == "14":
            show_book_details()

        elif choice == "15":
            add_genre_menu()

        elif choice == "16":
            show_genres()

        elif choice == "17":
            delete_genre_menu()

        elif choice == "18":
            show_join_data()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
