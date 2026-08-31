from database.connection import get_connection
from database.models import create_tables


def main():
    connection = get_connection()
    print("Database connected successfully!")
    connection.close()

    create_tables()
    print("Database tables created successfully!")


if __name__ == "__main__":
    main()
