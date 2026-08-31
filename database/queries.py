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


from datetime import datetime

def borrow_book(book_id, user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, is_available FROM books WHERE id = ?",
        (book_id,)
    )

    book = cursor.fetchone()

    if book is None:
        connection.close()
        print("Book not found.")
        return

    if book[1] == 0:
        connection.close()
        print("Book is already borrowed.")
        return

    cursor.execute(
        "SELECT id FROM users WHERE id = ?",
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        connection.close()
        print("User not found.")
        return

    borrow_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        INSERT INTO borrowings (book_id, user_id, borrow_date)
        VALUES (?, ?, ?)
        """,
        (book_id, user_id, borrow_date)
    )

    cursor.execute(
        """
        UPDATE books
        SET is_available = 0
        WHERE id = ?
        """,
        (book_id,)
    )

    connection.commit()
    connection.close()

    print("Book borrowed successfully.")


def return_book(book_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id
        FROM borrowings
        WHERE book_id = ? AND return_date IS NULL
        """,
        (book_id,)
    )

    borrowing = cursor.fetchone()

    if borrowing is None:
        connection.close()
        print("Active borrowing not found.")
        return

    return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        UPDATE borrowings
        SET return_date = ?
        WHERE id = ?
        """,
        (return_date, borrowing[0])
    )

    cursor.execute(
        """
        UPDATE books
        SET is_available = 1
        WHERE id = ?
        """,
        (book_id,)
    )

    connection.commit()
    connection.close()

    print("Book returned successfully.")


def get_borrowing_history():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            books.title,
            users.name,
            borrowings.borrow_date,
            borrowings.return_date
        FROM borrowings
        INNER JOIN books ON borrowings.book_id = books.id
        INNER JOIN users ON borrowings.user_id = users.id
        ORDER BY borrowings.borrow_date
        """
    )

    history = cursor.fetchall()

    connection.close()

    return history


def get_books_with_genres():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            books.title,
            books.author,
            genres.name
        FROM books
        INNER JOIN genres ON books.genre_id = genres.id
        ORDER BY books.title
        """
    )

    books = cursor.fetchall()

    connection.close()

    return books


def get_statistics():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    books_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM users")
    users_count = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(year) FROM books")
    average_year = cursor.fetchone()[0]

    cursor.execute("SELECT MIN(year) FROM books")
    oldest_year = cursor.fetchone()[0]

    cursor.execute("SELECT MAX(year) FROM books")
    newest_year = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM borrowings")
    borrowings_count = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(year) FROM books")
    years_sum = cursor.fetchone()[0]

    connection.close()

    return {
        "books_count": books_count,
        "users_count": users_count,
        "average_year": average_year,
        "oldest_year": oldest_year,
        "newest_year": newest_year,
        "borrowings_count": borrowings_count,
        "years_sum": years_sum
    }


def get_books_by_genre():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT genres.name, COUNT(books.id)
        FROM books
        INNER JOIN genres ON books.genre_id = genres.id
        GROUP BY genres.name
        ORDER BY COUNT(books.id) DESC
        """
    )

    result = cursor.fetchall()

    connection.close()

    return result


def get_books_by_author():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT author, COUNT(id)
        FROM books
        GROUP BY author
        ORDER BY COUNT(id) DESC
        """
    )

    result = cursor.fetchall()

    connection.close()

    return result


def get_borrowings_by_user():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT users.name, COUNT(borrowings.id)
        FROM users
        INNER JOIN borrowings ON users.id = borrowings.user_id
        GROUP BY users.name
        ORDER BY COUNT(borrowings.id) DESC
        """
    )

    result = cursor.fetchall()

    connection.close()

    return result


def get_popular_genres():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT genres.name, COUNT(books.id)
        FROM books
        INNER JOIN genres ON books.genre_id = genres.id
        GROUP BY genres.name
        HAVING COUNT(books.id) > 5
        """
    )

    result = cursor.fetchall()

    connection.close()

    return result


def get_active_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT users.name, COUNT(borrowings.id)
        FROM users
        INNER JOIN borrowings ON users.id = borrowings.user_id
        GROUP BY users.name
        HAVING COUNT(borrowings.id) > 3
        """
    )

    result = cursor.fetchall()

    connection.close()

    return result


