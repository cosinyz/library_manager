from database.connection import get_connection


def main():
    connection = get_connection()

    print("Database connected successfully!")

    connection.close()


if __name__ == "__main__":
    main()
