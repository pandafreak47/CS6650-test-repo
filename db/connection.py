```python
import os
import sqlite3
from typing import Optional

_DB_PATH = os.environ.get("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
    """Get or create the database connection with validation."""
    global _conn
    if _conn is None:
        _validate_db_path(_DB_PATH)
        _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
        _conn.row_factory = sqlite3.Row
        _bootstrap(_conn)
    return _conn


def _validate_db_path(db_path: str) -> None:
    """Validate the database path."""
    if not isinstance(db_path, str):
        raise TypeError("Database path must be a string")
    if not db_path:
        raise ValueError("Database path cannot be empty")
    if len(db_path) > 255:
        raise ValueError("Database path is too long")
    if any(char in db_path for char in ['\x00']):
        raise ValueError("Database path contains invalid characters")


def _bootstrap(conn: sqlite3.Connection) -> None:
    """Bootstrap the database with required tables."""
    if not isinstance(conn, sqlite3.Connection):
        raise TypeError("conn must be a sqlite3.Connection instance")
    
    try:
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
                status TEXT DEFAULT 'pending',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        """)
        conn.commit()
    except sqlite3.Error as e:
        raise RuntimeError(f"Failed to bootstrap database: {e}") from e
```