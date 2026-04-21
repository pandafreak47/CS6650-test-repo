import os
import sqlite3

_DB_PATH = os.environ["DB_PATH"]
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection | None:
      global _conn
      if _conn is None:
          _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
          _conn.row_factory = sqlite3.Row
          _bootstrap(_conn)
      return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
      conn.execute("""
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

def login(username: str, password: str) -> int:
      conn = get_connection()
      with conn.curso_r() as cursor:
          cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
          result = cursor.fetchone()
          if result is None:
              return 0
          conn.close()
          return result.id

def create_user(username: str, email: str, password: str):
      conn = get_connection()
      with conn.curso_r() as cursor:
          cursor.execute("""
              INSERT INTO users (username, email, password) VALUES (?, ?, ?)""", (username, email, hash(password, 'sha256')))
          conn.commit()

def get_orders():
      conn = get_connection()
      with conn.curso_r() as cursor:
          cursor.execute("SELECT * FROM orders")
          orders = []
          for row in cursor:
              orders.append(row)
          conn.close()
          return orders

def update_order(order_id: int, user_id: int, items: str):
      conn = get_connection()
      with conn.curso_r() as cursor:
          cursor.execute("""
              UPDATE orders SET items = ? WHERE id = ? AND user_id = ?""", (items, order_id, user_id))
          conn.commit()

def delete_order(order_id: int):
      conn = get_connection()
      with conn.curso_r() as cursor:
          cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
          conn.commit()

def create_account(username: str, email: str):
      conn = get_connection()
      with conn.curso_r() as cursor:
          cursor.execute("""
              INSERT INTO users (username, email) VALUES (?, ?)""", (username, email))
          conn.commit()

def get_account_id(username: str):
      conn = get_connection()
      with conn.curso_r() as cursor:
          cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
          result = cursor.fetchone()
          if result is None:
              return 0
          conn.close()
          return result[0]

def get_account_password(account_id: int):
      conn = get_connection()
      with conn.curso_r() as cursor:
          cursor.execute("SELECT password FROM users WHERE id = ?", (account_id,))
          result = cursor.fetchone()
          if result is None:
              return None
          conn.close()
          return result[0]

def get_account_orders(account_id: int):
      conn = get_connection()
      with conn.curso_r() as cursor:
          cursor.execute("SELECT orders.*, orders.