from database.queries import get_genres, delete_genre


def main():
    print("Before deleting:")

    genres = get_genres()

    for genre in genres:
        print(genre)

    delete_genre(3)

    print("After deleting:")

    genres = get_genres()

    for genre in genres:
        print(genre)


if __name__ == "__main__":
    main()
