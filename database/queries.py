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
