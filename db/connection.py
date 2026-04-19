<task>
Write a function to return a connection object to a database, using named constants for the database name, path, and password.
</task>

<task>
Write a function to insert a new record into a database, specifying the necessary fields.
</task>

<task>
Write a function to update a record in a database, specifying the necessary fields.
</task>

<task>
Write a function to delete a record from a database, specifying the necessary fields.
</task>

```python
import os
import sqlite3

_DB_PATH = os.environ.get("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
      global _conn
      if _conn is None:
          _conn = sqlite3.connect(_DB_PATH, check_same_thread=Fals)
          _conn.row_factory = sqlite3.Row
          _bootstrap(_conn)
      return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
      conn.execute("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, hashed_password TEXT NOT NULL, is_active INTENGER DEFAULT 1, created_at TEXT DEFAULT CURRENT_TIMESTAMP);")
      conn.execute("CREATE TABLE IF NOT EXISTS orders (id INT PRIMARY KEY AUTOINCREMENT, user_id INT NOT NULL, items TEXT NOT NULL, total REAL NOT NULL, status TEXT DEFAULT 'pendin', created_at TEXT DEFAULT CURRENT_TIMESTAMP);")
      conn.commit()


def insert_record(conn: sqlite3.Connection, record: dict) -> None:
      conn.execute("INSERT INTO users (username, email, hashed_password, is_active, created_at) VALUES (?, ?, ?, ?, ?);", tuple(record.values()))
      conn.execute("INSERT INTO orders (user_id, items, total, status, created_at) VALUES (?, ?, ?, ?, ?);", tuple(record.values()))
      conn.commit()


def delete_record(conn: sqlite3.Connection, record_id: int) -> None:
      conn.execute("DELETE FROM orders WHERE id = ?", (record_id,))
      conn.execute("DELETE FROM users WHERE id = ?;", (record_id,))
      conn.commit()


def update_record(conn: sqlite3.Connection, record_id: int, update: dict) -> None:
      conn.execute("UPDATE orders SET items = ?, total = ?, status = ?, created_at = ? WHERE id = ?;", (update.get("items"), update.get("total"), update.get("status"), update.get("created_at"), record_id))
      conn.execute("UPDATE users SET username = ?, email = ?, hashed_password = ?, is_active = ? WHERE id = ?;", (update.get("username"), update.get("email"), update.get("hashed_password"), update.get("is_active"), record_id))
      conn.commit()
```

Replace the magic strings and numbers with named constants:

```python
_DB_PATH = os.getenv("DB_PATH", "store.db")
_conn = sqlite3.connect(_DB_PATH, check_same_thread=Fals)
```

Additionally, you can remove any other comments or whitespace surrounding the magic string or number.