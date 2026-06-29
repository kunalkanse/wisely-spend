import sqlite3
from datetime import datetime
from pathlib import Path

from werkzeug.security import generate_password_hash

DB_PATH = Path(__file__).resolve().parent.parent / "expense_tracker.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    with get_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                name          TEXT NOT NULL,
                email         TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at    TEXT DEFAULT (datetime('now'))
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL REFERENCES users(id),
                amount      REAL NOT NULL,
                category    TEXT NOT NULL,
                date        TEXT NOT NULL,
                description TEXT,
                created_at  TEXT DEFAULT (datetime('now'))
            )
            """
        )


def seed_db():
    with get_db() as conn:
        existing = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        if existing > 0:
            return

        cursor = conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            ("Demo User", "demo@spendly.com", generate_password_hash("demo123")),
        )
        user_id = cursor.lastrowid

        today = datetime.now()
        month_prefix = today.strftime("%Y-%m")

        def d(day):
            return f"{month_prefix}-{day:02d}"

        expenses = [
            (user_id, 250.00, "Food",          d(2),  "Lunch at office canteen"),
            (user_id, 480.50, "Food",          d(15), "Groceries from BigBasket"),
            (user_id, 120.00, "Transport",     d(4),  "Auto-rickshaw to work"),
            (user_id, 1899.00, "Bills",        d(7),  "Electricity bill"),
            (user_id, 650.00, "Health",        d(9),  "Pharmacy — monthly meds"),
            (user_id, 499.00, "Entertainment", d(12), "Movie tickets"),
            (user_id, 2399.00, "Shopping",     d(18), "New running shoes"),
            (user_id, 150.00, "Other",         d(20), "Birthday gift card"),
        ]
        conn.executemany(
            """
            INSERT INTO expenses (user_id, amount, category, date, description)
            VALUES (?, ?, ?, ?, ?)
            """,
            expenses,
        )
