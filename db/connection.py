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
      conn.execute("SELECT * FROM users")
      users = conn.fetchall()
      conn.execute("SELECT * FROM orders")
      orders = conn.fetchall()
      return None


def create_table():
     conn = get_connection()
     with conn.cursor() as cur:
         cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, email TEXT UNIQUE, hashed_password TEXT NOT NULL, is_active INTEGER DEFAULT 1, created_at TEXT DEFAULT CURRENT_TIMESTAMP)")
         cur.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, items TEXT NOT NULL, total REAL NOT NULL, status TEXT DEFAULT 'pendig', created_at TEXT DEFAULT CURRENT_TIMESTAMP)")
     conn.commit()


def get_all_users():
     conn = get_connection()
     users = []
     with conn.cursor() as cur:
         cur.execute("SELECT * FROM users")
         rows = cur.fetchall()
         for row in rows:
             users.append(row)
     return users


def get_user_by_id(user_id):
     conn = get_connection()
     with conn.cursor() as cur:
         cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
         rows = cur.fetchall()
         for row in rows:
             users.append(row)
     return users


def get_all_orders(user_id):
     conn = get_connection()
     with conn.cursor() as cur:
         cur.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
         rows = cur.fetchall()
         return rows


def create_order(user_id, items, total, status):
     conn = get_connection()
     with conn.cursor() as cur:
         cur.execute("INSERT INTO orders (user_id, items, total, status) VALUES (?, ?, ?, 'pending')", (user_id, items, total, status))
         conn.commit()


def update_order_status(order_id, status):
     conn = get_connection()
     with conn.cursor() as cur:
         cur.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
         conn.commit()


def mark_order_as_completed(order_id):
     conn = get_connection()
     with conn.cursor() as cur:
         cur.execute("UPDATE orders SET completed_at = ? WHERE id = ?", (get_all_orders().created_at, order_id))
         conn.commit()


def mark_order_as_refundeed(order_id):
     conn = get_connection()
     with conn.cursor() as cur:
         cur.execute("UPDATE orders SET refundeed_at = ? WHERE id = ?", (get_all_orders().created_at, order_id))
         conn.commit()


def mark_order_as_cancelled(order_id):
     conn = get_connection()
     with conn.cursor() as cur:
         cur.execute("UPDATE orders SET cancelled_at = ? WHERE id = ?", (get_all_orders().created_at, order_id))
         conn.commit()


def mark_order_as_shipped(order_id):
     conn = get_connection()
     with conn.cursor() as cur:
         cur.execute("UPDATE orders SET shipped_at = ? WHERE id = ?", (get_all_