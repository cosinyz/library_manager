from database.connection import get_connection


def add_genre(name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO genres (name) VALUES (?)",
        (name,)
    )

    connection.commit()
    connection.close()


def get_genres():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, name FROM genres")
    genres = cursor.fetchall()

    connection.close()

    return genres


def delete_genre(genre_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM genres WHERE id = ?",
        (genre_id,)
    )

    connection.commit()
    connection.close()


def add_book(title, author, year, genre_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO books (title, author, year, genre_id)
        VALUES (?, ?, ?, ?)
        """,
        (title, author, year, genre_id)
    )

    connection.commit()
    connection.close()


def get_books():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, title, author, year, genre_id, is_available
        FROM books
        """
    )

    books = cursor.fetchall()

    connection.close()

    return books


def get_book_by_id(book_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, title, author, year, genre_id, is_available
        FROM books
        WHERE id = ?
        """,
        (book_id,)
    )

    book = cursor.fetchone()

    connection.close()

    return book


def update_book(book_id, title, author, year, genre_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE books
        SET title = ?, author = ?, year = ?, genre_id = ?
        WHERE id = ?
        """,
        (title, author, year, genre_id, book_id)
    )

    connection.commit()
    connection.close()


def delete_book(book_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )

    connection.commit()
    connection.close()


def get_available_books():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, title, author, year, genre_id, is_available
        FROM books
        WHERE is_available = 1
        """
    )

    books = cursor.fetchall()

    connection.close()

    return books


def add_user(name, email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users (name, email)
        VALUES (?, ?)
        """,
        (name, email)
    )

    connection.commit()
    connection.close()


def get_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, email
        FROM users
        """
    )

    users = cursor.fetchall()

    connection.close()

    return users


def update_user_email(user_id, email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET email = ?
        WHERE id = ?
        """,
        (email, user_id)
    )

    connection.commit()
    connection.close()


def delete_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )

    connection.commit()
    connection.close()
