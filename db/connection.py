```python
import os
import sqlite3

# Configuration constants
DEFAULT_DB_NAME = "store.db"
DB_PATH_ENV_VAR = "DB_PATH"

# Database constants
CHECK_SAME_THREAD = False
DEFAULT_ACTIVE_STATUS = 1
DEFAULT_ORDER_STATUS = "pending"
CURRENT_TIMESTAMP = "CURRENT_TIMESTAMP"

# Table names
USERS_TABLE = "users"
ORDERS_TABLE = "orders"

# Users table columns
USERS_ID_COL = "id"
USERS_USERNAME_COL = "username"
USERS_EMAIL_COL = "email"
USERS_HASHED_PASSWORD_COL = "hashed_password"
USERS_IS_ACTIVE_COL = "is_active"
USERS_CREATED_AT_COL = "created_at"

# Orders table columns
ORDERS_ID_COL = "id"
ORDERS_USER_ID_COL = "user_id"
ORDERS_ITEMS_COL = "items"
ORDERS_TOTAL_COL = "total"
ORDERS_STATUS_COL = "status"
ORDERS_CREATED_AT_COL = "created_at"

# Column constraints
COLUMN_PRIMARY_KEY = "INTEGER PRIMARY KEY AUTOINCREMENT"
COLUMN_TEXT_UNIQUE_NOT_NULL = "TEXT UNIQUE NOT NULL"
COLUMN_TEXT_NOT_NULL = "TEXT NOT NULL"
COLUMN_TEXT_DEFAULT = "TEXT DEFAULT"
COLUMN_REAL_NOT_NULL = "REAL NOT NULL"
COLUMN_INTEGER_NOT_NULL = "INTEGER NOT NULL"
COLUMN_INTEGER_DEFAULT = "INTEGER DEFAULT"

# Initialize connection
_DB_PATH = os.environ.get(DB_PATH_ENV_VAR, DEFAULT_DB_NAME)
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(_DB_PATH, check_same_thread=CHECK_SAME_THREAD)
        _conn.row_factory = sqlite3.Row
        _bootstrap(_conn)
    return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
    conn.executescript(f"""
        CREATE TABLE IF NOT EXISTS {USERS_TABLE} (
            {USERS_ID_COL} {COLUMN_PRIMARY_KEY},
            {USERS_USERNAME_COL} {COLUMN_TEXT_UNIQUE_NOT_NULL},
            {USERS_EMAIL_COL} {COLUMN_TEXT_UNIQUE_NOT_NULL},
            {USERS_HASHED_PASSWORD_COL} {COLUMN_TEXT_NOT_NULL},
            {USERS_IS_ACTIVE_COL} {COLUMN_INTEGER_DEFAULT} {DEFAULT_ACTIVE_STATUS},
            {USERS_CREATED_AT_COL} {COLUMN_TEXT_DEFAULT} {CURRENT_TIMESTAMP}
        );
        CREATE TABLE IF NOT EXISTS {ORDERS_TABLE} (
            {ORDERS_ID_COL} {COLUMN_PRIMARY_KEY},
            {ORDERS_USER_ID_COL} {COLUMN_INTEGER_NOT_NULL},
            {ORDERS_ITEMS_COL} {COLUMN_TEXT_NOT_NULL},
            {ORDERS_TOTAL_COL} {COLUMN_REAL_NOT_NULL},
            {ORDERS_STATUS_COL} {COLUMN_TEXT_DEFAULT} '{DEFAULT_ORDER_STATUS}',
            {ORDERS_CREATED_AT_COL} {COLUMN_TEXT_DEFAULT} {CURRENT_TIMESTAMP},
            FOREIGN KEY ({ORDERS_USER_ID_COL}) REFERENCES {USERS_TABLE}({USERS_ID_COL})
        );
    """)
    conn.commit()
```