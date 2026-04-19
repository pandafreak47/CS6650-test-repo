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
     conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, email TEXT, hashed_password TEXT, is_active INTEGER DEFAULT 1, created_at TEXT)")
     conn.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, items TEXT NOT NULL, total REAL DEFAULT 0, status TEXT DEFAULT 'pendin', created_at TEXT)")
     conn.commit()


def __all__:
    return ["get_connection", "get_conn", "get_connection_or_none", "bootstrap", "get_conn_or_none"]