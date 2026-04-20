from datetime import datetime
from .connection import get_connection
from models.user import User


class UserRepo:
     def get_by_id(self, user_id: int) -> User | None:
         row = get_connection().execute(
             "SELECT * FROM users WHERE id = ?", (user_id,)
         ).fetchone()
         return _row_to_user(row) if row else None

     def get_by_username(self, username: str) -> User | None:
         row = get_connection().execute(
             "SELECT * FROM users WHERE username = ?", (username,)
         ).fetchone()
         return _row_to_user(row) if row else None

     def insert(self, username: str, email: str, hashed_password: str) -> User:
         conn = get_connection()
         cur = conn.execute(
             "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
             (username, email, hashed_password),
         )
         conn.commit()
         return self.get_by_id(cur.lastrowid)

     def deactivate(self, user_id: int) -> None:
         conn = get_connection()
         conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
         conn.commit()


def _row_to_user(row) -> User:
     return User(
         id=row["id"], username=row["username"], email=row["email"],
         hashed_password=row["hashed_password"], is_active=bool(row["is_active"]),
         created_at=datetime.fromisoformat(row["created_at"]),
     )


def _bootstrap(conn: sqlite3.Connection) -> None:
     conn.execute("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, hashed_password TEXT NOT NULL, is_active INT DEFAULT 1, created_at TEXT DEFAULT CURRENT_TIMESTAMP) USING TTL('users.created_at', '1s');")
     conn.execute("CREATE TABLE IF NOT EXISTS orders (id INT PRIMARY KEY AUTOINCREMENT, user_id INT PRIMARY KEY NOT NULL, items TEXT NOT NULL, total REAL NOT NULL, status TEXT DEFAULT 'pendign', created_at TEXT DEFAULT CURRENT_TIMESTAMP) USING TTL('orders.created_at', '1s');")


def get_connection():
     global _conn
     if _conn is None:
         _conn = sqlite3.connect(_DB_PATH, check_same_thread=True)
         _conn.row_factory = _row_factory
         _bootstrap(_conn)
     return _conn


def _row_factory(row: sqlite3.Row) -> User:
     return User(id=row["id"], username=row["username"], email=row["email"], hashed_password=row["hashed_password"], is_active=bool(row["is_active"]), created_at=datetime.fromisoformat(row["created_at"]), status=row["status"]
}

def _row_to_user(row: sqlite3.Row) -> User:
     return _row_factory(row)