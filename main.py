from database.queries import (
    get_books_by_genre,
    get_books_by_author,
    get_borrowings_by_user,
    get_popular_genres,
    get_active_users
)


def main():
    print("=== BOOKS BY GENRE ===")

    for item in get_books_by_genre():
        print(item)

    print()

    print("=== BOOKS BY AUTHOR ===")

    for item in get_books_by_author():
        print(item)

    print()

    print("=== BORROWINGS BY USER ===")

    for item in get_borrowings_by_user():
        print(item)

    print()

    print("=== POPULAR GENRES ===")

    for item in get_popular_genres():
        print(item)

    print()

    print("=== ACTIVE USERS ===")

    for item in get_active_users():
        print(item)


if __name__ == "__main__":
    main()
