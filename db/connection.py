```python
import os
import sqlite3

# Constants
DEFAULT_DB_NAME = "store.db"
DB_PATH_ENV_VAR = "DB_PATH"
DEFAULT_USER_ACTIVE_STATUS = 1
DEFAULT_ORDER_STATUS = "pending"

_DB_PATH = os.environ.get(DB_PATH_ENV_VAR, DEFAULT_DB_NAME)
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
        _conn.row_factory = sqlite3.Row
        _bootstrap(_conn)
    return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
    conn.executescript(f"""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            is_active INTEGER DEFAULT {DEFAULT_USER_ACTIVE_STATUS},
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            items TEXT NOT NULL,
            total REAL NOT NULL,
            status TEXT DEFAULT '{DEFAULT_ORDER_STATUS}',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)
    conn.commit()
```