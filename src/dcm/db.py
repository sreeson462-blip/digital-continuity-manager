import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DB_PATH = PROJECT_ROOT / "data" / "dcm.db"


def connect():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = connect()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            category    TEXT NOT NULL,
            owner       TEXT NOT NULL,
            location    TEXT NOT NULL,
            file_format TEXT,
            criticality INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()
def add_asset(name, category, owner, location, file_format, criticality):
    conn = connect()
    conn.execute(
        "INSERT INTO assets (name, category, owner, location, file_format, criticality) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (name, category, owner, location, file_format, criticality),
    )
    conn.commit()
    conn.close()


def list_assets():
    conn = connect()
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM assets ORDER BY criticality DESC, name").fetchall()
    conn.close()
    return rows

