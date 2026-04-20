import os
import sqlite3

_DB_PATH = os.environ.get("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
     global _conn
     if _conn is None:
         _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
         _conn.row_factory = sqlite3.Row
         _bootstrap(_conn)
     return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
     conn.executescript("""
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


def insert_user(username: str, email: str, hashed_password: str):
     """
     Insert a new user into the database.
     """
     conn = get_connection()
     conn.execute("""
         INSERT INTO users (username, email, hashed_password)
         VALUES (?, ?, ?)
         ON CONFLICT (username) DO UPDATE SET email = ?, hashed_password = ?
         """, (username, email, hashed_password))
     conn.commit()


def get_user(username: str):
     """
     Get a specific user from the database by their username.
     """
     conn = get_connection()
     row = conn.execute("""
         SELECT * FROM users WHERE username = ?
         """, (username,)).fetchone()
     if row is None:
         raise ValueError(f"User not found: {username}")
     return row


def get_orders(user_id: int):
     """
     Get all orders for a specific user.
     """
     conn = get_connection()
     rows = conn.execute(
         """
         SELECT * FROM orders WHERE user_id = ?
         """, (user_id,)
     ).fetchall()
     if not rows:
         raise ValueError("No orders found for user")
     return rows


def update_user(user_id: int, username: str, email: str, hashed_password: str):
     """
     Update a user in the database.
     """
     conn = get_connection()
     conn.execute("""
         UPDATE users SET username = ?, email = ?, hashed_password = ?
         WHERE id = ?
         """, (username, email, hashed_password, user_id))
     conn.commit()


def delete_user(user_id: int):
     """
     Delete a user from the database.
     """
     conn = get_connection()
     conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
     conn.commit()


def get_file_path(db_path: str):
     """
     Get the path to the specified database file.
     """
     db_path = os.path.abspath(db_path)
     if not os.path.isfile(db_path):
         raise ValueError(f"Database file not found: {db_path}")
     return db_path


def create_db(db_path: str):
     """
     Create a new database file.
     """
     conn = sqlite3.connect(get_file_path(db_path))
     conn.commit()
     conn.close()


def bootstrap():
     """
     Bootstrap the database.
     """
     create_db(db_path)
     get_connection().execute("PRAGMA foreign_keys = ON")
     get_connection().execute("