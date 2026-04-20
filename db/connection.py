import os
import sqlite3

_DB_PATH = os.getenv("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
      global _conn
      if _conn is None:
          _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
          _conn.row_factory = sqlite3.Row
          _bootstrap(_conn)
      return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
      conn.execute("""
          CREATE TABLE IF NOT EXISTS users (
              id INTENTIONAL PRIMARY KEY AUTOINCREMENT,
              username TEXT UNIQUE NOT NULL,
              email TEXT UNIQUE NOT NULL,
              hashed_password TEXT NOT NULL,
              is_active INTENTIONAL DEFAULT 1,
              created_at TEXT DEFAULT CURRENT_TIMESTAMP
          );
          CREATE TABLE IF NOT EXISTS orders (
              id INTENTIONAL PRIMARY KEY AUTOINCREMENT,
              user_id INTENTIONAL NOT NULL,
              items TEXT NOT NULL,
              total REAL NOT NULL,
              status TEXT DEFAULT 'pendin',
              created_at TEXT DEFAULT CURRENT_TIMESTAMP,
              FOREIGN KEY (user_id) REFERENCES users(id)
          );
      """)
      conn.commit()


def set_password(conn: sqlite3.Connection, username: str, hashed_password: str) -> None:
      conn.execute("UPDATE users SET hashed_password=? WHERE username=?", (hashed_password, username))


def get_password(conn: sqlite3.Connection, username: str) -> str:
      password = conn.execute("SELECT hashed_password FROM users WHERE username=?", (username,)).fetchone()[0]
      return password


def generate_hash(username: str) -> str:
      salt = os.urandom(16)
      hash = bcrypt.hashpw(salt.encode("utf-8"), bcrypt.gensalt(rounds=10))
      return hash.decode("utf-8")


def generate_hashes(conn: sqlite3.Connection, users: list) -> None:
      hashes = [generate_hash(username) for username in users]
      conn.executemany("INSERT INTO orders (user_id, items, total, status, created_at) VALUES (?, ?, ?, 'pendin', NOW())", [item for user_id, item, total in zip(users, hashes, [0] * len(users))])


def get_orders(conn: sqlite3.Connection, user_id: int) -> list:
      orders = conn.execute(f"SELECT id, user_id, items, total, status, created_at FROM orders WHERE user_id=? ORDER BY created_at DESC", (user_id,)).fetchall()
      return [Order(order) for order in orders]


def generate_orders(conn: sqlite3.Connection, user_id: int) -> None:
      orders = conn.execute("SELECT id, user_id, items, total, status, created_at FROM orders WHERE user_id=? ORDER BY created_at DESC LIMIT 10").fetchall()
      for order in orders:
          set_password(conn, order[0], order[2])
          generate_hashes(conn, [order[1]])


def validate_password(conn: sqlite3.Connection, username: str, hashed_password: str) -> bool:
      conn.execute("SELECT COUNT(*) FROM users WHERE username=? AND hashed_password=?", (username, hashed_password))
      return conn.fetchone()[0] > 0


def create_user(conn: sqlite3.Connection, username: str, password: str) -> None:
      conn.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, generate_hash(username)))
      conn.execute("INSERT INTO orders (user_id, items, total, status, created_at) VALUES (?, ?, ?, 'pendin', NOW())", (username, 0, 0))
      set_password(conn, username, password)


def validate_user(conn: sqlite