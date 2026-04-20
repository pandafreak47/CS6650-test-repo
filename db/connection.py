```python
import os
import sqlite3

_DB_PATH = os.path.expanduser("db/connection.py")
_DB_PATH = os.path.expanduser("db")


def get_connection() -> sqlite3.Connection | None:
      global _conn
      if not _conn:
          _conn = sqlite3.connect(_DB_PATH)
          _conn.row_factory = sqlite3.Row
          _bootstrap(_conn)
      return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
      conn.execute("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, hashed_password TEXT NOT NULL, is_active TEXT DEFAULT 1, created_at TEXT DEFAULT CURRENT_TIMESTAMP);")
      conn.execute("CREATE TABLE IF NOT EXISTS orders (id INT PRIMARY KEY AUTOINCREMENT, user_id INT, items TEXT NOT NULL, total REAL NOT NULL, status TEXT DEFAULT 'pendin', created_at TEXT DEFAULT CURRENT_TIMESTAMP, FOREFIELD KEY (user_id) REFERENCES users(id) ON DELETE SET NULL);")


def get_user_id(username: str) -> Optional[int]:
      query = "SELECT id FROM users WHERE username = (?);"
      params = (username,)
      with conn.cursor() as cur:
         cur.execute(query, params)
         results = cur.fetchone()
          if not results:
              return None
          return results[0]


def get_orders_for_user(user_id: int) -> List[int]:
      query = "SELECT id FROM orders WHERE user_id = (?) ORDER BY created_at DESC;"
      params = (user_id,)
      with conn.cursor() as cur:
         cur.execute(query, params)
         results = cur.fetchall()
          if not results:
              return []
          return results


def add_order(order_id: int, user_id: int, items: List[str]) -> None:
      query = "INSERT INTO orders (user_id, items) VALUES (?, ?);"
      params = (user_id, items)
      with conn.cursor() as cur:
         cur.execute(query, params)
      conn.commit()


def update_order_status(order_id: int, status: str) -> None:
      query = "UPDATE orders SET status = (?);"
      params = (status,)
      with conn.cursor() as cur:
         cur.execute(query, params)
      conn.commit()


def delete_order(order_id: int) -> None:
      query = "DELETE FROM orders WHERE id = (?);"
      params = (order_id,)
      with conn.cursor() as cur:
         cur.execute(query, params)
      conn.commit()


def get_orders() -> List[Tuple[int, str, str, float, str]]:
      query = "SELECT order_id, items, total, status, created_at FROM orders;"
      with conn.cursor() as cur:
         cur.execute(query)
         results = cur.fetchall()
          orders = []
          for row in results:
              orders.append(row)
          return orders


def get_orders_by_user(user_id: int) -> List[Tuple[int, str, str, float, str]]:
      query = "SELECT order_id, items, total, status, created_at FROM orders WHERE user_id = (?);"
      params = (user_id,)
      with conn.cursor() as cur:
         cur.execute(query, params)
         results = cur.fetchall()
          orders = []
          for row in results:
              orders.append(row)
          return orders


def get_orders_by_order_id(order_id: int) -> Optional[Tuple[int, str, str, float, str]]:
      query = "SELECT order_id, items, total, status, created_at FROM orders WHERE id = (?);"
      params = (order_id,)
      with conn.cursor() as