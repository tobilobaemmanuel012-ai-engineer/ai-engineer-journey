
import sqlite3
from pathlib import Path
from datetime import datetime

DATABASE_PATH = Path(__file__).with_name("study_history.db")


def initialize_database():
    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS study_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            study_mode TEXT NOT NULL,
            studied_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_study(topic, study_mode):
    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute(
        """
        INSERT INTO study_history (topic, study_mode, studied_at)
        VALUES (?, ?, ?)
        """,
        (
            topic,
            study_mode,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    connection.commit()
    connection.close()


def get_study_history():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    history = connection.execute(
        """
        SELECT id, topic, study_mode, studied_at
        FROM study_history
        ORDER BY id DESC
        LIMIT 50
        """
    ).fetchall()

    connection.close()
    return history
