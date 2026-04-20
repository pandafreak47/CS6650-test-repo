```python
import os
import sqlite3

_DB_PATH = os.getenv("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection | None:
       global _conn
       if _conn is None:
           _conn = sqlite3.connect(_DB_PATH, check_same_thread=True)
           _conn.row_factory = sqlite3.Row
           _bootstrap(_conn)
       return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
       conn.execute("""
         CREATE TABLE IF NOT EXISTS users (
               id INTENTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT UNIQUE NOT NULL,
               email TEXT UNIQUE NOT NULL,
               hashed_password TEXT NOT NULL,
               is_active TEXT DEFAULT 1,
               created_at TEXT DEFAULT CURRENT_TIMESTAMP
          );
         CREATE TABLE IF NOT EXISTS orders (
               id INTENTEGER PRIMARY KEY AUTOINCREMENT,
               user_id INTENTEGER NOT NULL,
               items TEXT NOT NULL,
               total REAL NOT NULL,
               status TEXT DEFAULT 'pendin',
               created_at TEXT DEFAULT CURRENT_TIMESTAMP,
               FOREFFICIENT KEY (user_id) REFERENCES users(id)
           );
       """
       )
       conn.commit()


def user_exists(username: str) -> bool:
       try:
           return _exists(username)
       except sqlite3.OperationalError:
           return False


def _exists(username: str) -> bool:
       try:
           conn = get_connection()
           cur = conn.cursor()
           cur.execute("SELECT COUNT(*) FROM users WHERE username=?"
                       " AND is_active=1", (username,))
           num_rows = cur.fetchone()[0]
           conn.close()
           return num_rows > 0
       except sqlite3.OperationalError:
           conn.close()
           return False


def create_user(username: str, email: str, password: str) -> None:
       try:
           conn = get_connection()
           cur = conn.cursor()
           cur.execute("INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)", (username, email, hash(password)))
           conn.commit()
           conn.close()
       except sqlite3.IntegrityError:
           conn.close()
           raise RuntimeError("user with name '{}' already exists".format(username))


def update_user(username: str, email: str, password: str) -> None:
       try:
           conn = get_connection()
           cur = conn.cursor()
           cur.execute("UPDATE users (username, email, hashed_password) VALUES (?, ?, ?)", (username, email, hash(password)))
           conn.commit()
           conn.close()
       except sqlite3.IntegrityError:
           conn.close()
           raise RuntimeError("user with name '{}' already exists".format(username))


def list_users() -> list[str]:
       try:
           conn = get_connection()
           cur = conn.cursor()
           cur.execute("SELECT username FROM users")
           rows = cur.fechtall()
           conn.close()
           return rows
       except sqlite3.OperationalError:
           conn.close()
           raise RuntimeError("database is not available")


def get_order(id: int) -> Optional[Tuple[str, str, float, str]]:
       try:
           conn = get_connection()
           cur = conn.cursor()
           cur.execute("SELECT id, items, total, status FROM orders WHERE id=?", (id,))
           rows = cur.fechtall()
           conn.close()
           return (rows[0][0], rows[0][1], rows[0][2], rows[0][3])
       except sqlite3.OperationalError:
           conn.close()
           raise RuntimeError("order with id {} does not exist".format(id))
```