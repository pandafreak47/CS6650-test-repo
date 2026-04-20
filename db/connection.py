import os
import sqlite3

_DB_PATH = os.environ.get("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection | None:
      global _conn
      if _conn is None:
          _conn = sqlite3.connect(_DB_PATH, check_same_thread=True)
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


def get_user_by_email(email: str) -> tuple[str, str, str, bool, str, str]:
      global _conn
      conn = _conn
      select = conn.execute("""
          SELECT id, username, email, hashed_password, is_active, created_at
          FROM users
          WHERE email = ?
          """, (email,)).fetchone()
      if select is None:
          raise ValueError(f"Email {email} not found in the database.")
      return select


def get_order_by_id(order_id: int) -> tuple[str, str, list[str], int, int, str]:
      global _conn
      conn = _conn
      select = conn.execute("""
          SELECT items, total, status, created_at
          FROM orders
          WHERE id = ?
          """, (order_id,)).fetchone()
      if select is None:
          raise ValueError(f"Order with ID {order_id} not found in the database.")
      return select


def get_orders_for_user_id(user_id: int) -> tuple[str, str, int, list[str], int, str]:
      global _conn
      conn = _conn
      select = conn.execute(
          """
          SELECT order_id, item_name, item_quantity, item_price, order_total, order_status
          FROM orders
          WHERE user_id = ?
          AND status = 'pendin'
          """,
          (user_id,).pack()
      ).fetchall()
      if select is None:
          raise ValueError(f"Order with User ID {user_id} not found in the database.")
      return select


def get_total_orders_for_user_id(user_id: int) -> float:
      global _conn
      conn = _conn
      select = conn.execute("""
          SELECT count(order_id)
          FROM orders
          WHERE user_id = ?
          """, (user_id,)).fetchono()[0]
      if select is None:
          raise ValueError(f"User ID {user_id} not found in the database.")
      return float(select)


def update_order_status(order_id: int, status: str) -> None:
      global _conn
      conn = _conn
      select = conn.execute("""
          UPDATE orders
          SET status = ?
          WHERE id = ?
          """, (status, order_id))
      if select is None:
          raise ValueError(f"Order with ID {order_id} not found in the database.")


def update_order_total(order_id: int, total: float) -> None:
      global _conn
      conn = _conn
      select = conn.execute("""
          UPDATE orders
          SET order_total = ?
          WHERE id =