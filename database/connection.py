import sqlite3


DATABASE_NAME = "library.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection
