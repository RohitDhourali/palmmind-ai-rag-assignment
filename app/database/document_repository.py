from app.database.database import get_connection


def save_document(
    filename: str,
    file_type: str,
    chunk_strategy: str,
    chunk_count: int,
) -> None:

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO documents
        (
            filename,
            file_type,
            chunk_strategy,
            chunk_count
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            filename,
            file_type,
            chunk_strategy,
            chunk_count,
        ),
    )

    conn.commit()
    conn.close()