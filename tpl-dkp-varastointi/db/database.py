import sqlite3
from pathlib import Path

DB_PATH = Path("sqlite_books.db")


def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def add_data(books_dict):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for title, info in books_dict.items():
        cursor.execute(
            "INSERT OR IGNORE INTO books (title, author, pages) VALUES (?, ?, ?)",
            (title, info["author"], info["pages"]),
        )
    conn.commit()
    conn.close()


def query_data(limit):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT title, author, pages
        FROM books
        ORDER BY pages DESC
        LIMIT ?
        """,
        (limit,),
    )
    rows = cursor.fetchall()
    conn.close()
    return rows