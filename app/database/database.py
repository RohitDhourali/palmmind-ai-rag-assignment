import sqlite3
from pathlib import Path

DB_PATH = Path("documents.db")


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)


def initialize_database() -> None:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            file_type TEXT NOT NULL,
            chunk_strategy TEXT NOT NULL,
            chunk_count INTEGER NOT NULL,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()