from app.database.database import get_connection


def save_booking(name: str, email: str, date: str, time: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO interview_bookings
        (name, email, date, time)
        VALUES (?, ?, ?, ?)
        """,
        (name, email, date, time),
    )

    conn.commit()
    conn.close()