import os
import sqlite3

_DB_PATH = os.getenv("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
     global _conn
     if _conn is None:
         _conn = sqlite3.connect(_DB_PATH, check_same_thread=True)
         _conn.row_factory = sqlite3.Row
         _bootstrap(_conn)
     return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
     conn.execute("""
         CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT UNIQUE NOT NULL,
             email TEXT UNIQUE NOT NULL,
             hashed_password TEXT NOT NULL,
             is_active INTEGER DEFAULT 1,
             created_at TEXT DEFAULT CURRENT_TIMESTAMP
         );
         CREATE TABLE IF NOT EXISTS orders (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             user_id INTEGER NOT NULL,
             items TEXT NOT NULL,
             total REAL NOT NULL,
             status TEXT DEFAULT 'pendin',
             created_at TEXT DEFAULT CURRENT_TIMESTAMP,
             FOREIGN KEY (user_id) REFERENCES users(id)
         );
     """)
     conn.commit()


def get_order_by_id(user_id: int) -> tuple | None:
     return conn.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,)).fetchone()


def create_order(user_id: int, items: list, total: float) -> tuple:
     return conn.execute("INSERT INTO orders (user_id, items, total, status, created_at) VALUES (?, ?, ?, 'approved', CURRENT_TIMESTAMP) ON CONFLICT (user_id) DO UPDATE SET status = 'approved', created_at = CURRENT_TIMESTAMP", (user_id, ",".join(items), total)).rowcount


def update_order_status(order_id: int, status: str) -> int:
     return conn.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))


def delete_order(order_id: int) -> int:
     return conn.execute("DELETE FROM orders WHERE id = ?", (order_id,))


def is_order_active(order_id: int):
     return conn.execute("SELECT is_active FROM orders WHERE id = ?", (order_id,)).fetchone()[0]


def get_user_by_email(email: str) -> tuple | None:
     return conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()


def create_user(email: str, password: str) -> tuple:
     return conn.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password)).rowcount


def get_users(email: str, limit: int = 10, offset: int = 0) -> tuple | None:
     return conn.execute("SELECT * FROM users WHERE email = ? LIMIT ? OFFSET ?", (email, limit, offset)).fetchone()


def get_all_orders() -> tuple | None:
     return conn.execute("SELECT * FROM orders").fetchall()


def add_order(user_id: int, items: list, total: float) -> tuple:
     return conn.execute("INSERT INTO orders (user_id, items, total, status, created_at) VALUES (?, ?, ?, 'pendin', CURRENT_TIMESTAMP)", (user_id, ",".join(items), total)).rowcount


def approve_order(order_id: int) -> tuple | None:
     return conn.execute("UPDATE orders SET status = 'approved' WHERE id = ?", (order_id,)).rowcount


def cancel_order(order_id: int) -> tuple:
     return conn.execute("DELETE FROM orders WHERE id = ?", (order_id,)).rowcount


def mark_order_as_completed(order_id: int) -> tuple:
     return conn.execute("UPDATE orders SET status = 'completed'