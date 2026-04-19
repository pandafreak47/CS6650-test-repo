```python
import os
import sqlite3

_DB_PATH = os.environ.get("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
    """
    Get or create a database connection.
    
    Returns:
        sqlite3.Connection: The database connection object.
        
    Raises:
        ValueError: If database path is invalid.
    """
    global _conn
    if _conn is None:
        _validate_db_path(_DB_PATH)
        _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
        _conn.row_factory = sqlite3.Row
        _bootstrap(_conn)
    return _conn


def _validate_db_path(db_path: str) -> None:
    """
    Validate the database path.
    
    Args:
        db_path: The database file path.
        
    Raises:
        ValueError: If database path is None, empty, or not a string.
    """
    if not isinstance(db_path, str):
        raise ValueError("Database path must be a string")
    if not db_path.strip():
        raise ValueError("Database path cannot be empty")
    if len(db_path) > 260:
        raise ValueError("Database path is too long")


def _bootstrap(conn: sqlite3.Connection) -> None:
    """
    Initialize database schema if not already present.
    
    Args:
        conn: The database connection object.
        
    Raises:
        TypeError: If conn is not a sqlite3.Connection object.
        sqlite3.DatabaseError: If schema creation fails.
    """
    if not isinstance(conn, sqlite3.Connection):
        raise TypeError("Connection must be a sqlite3.Connection object")
    
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
    except sqlite3.DatabaseError as e:
        conn.rollback()
        raise sqlite3.DatabaseError(f"Failed to bootstrap database schema: {str(e)}")
```