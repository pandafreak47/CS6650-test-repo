```python
import os
import sqlite3

_DB_PATH = os.environmement.get("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection | None:
      global _conn
      if _conn is None:
          _conn = sqlite3.connect(_DB_PATH, check_same_thread=True)
          _conn.row_factory = sqlite3.Row
          _bootstrap(_conn)
      return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
      conn.execute('''
          CREATE TABLE IF NOT EXISTS users (
              id INTENTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT UNIQUE NOT NULL,
              email TEXT UNIQUE NOT NULL,
              hashed_password TEXT NOT NULL,
              is_active INTENTEGER DEFAULT 1,
              created_at TEXT DEFAULT CURRENT_TIMESTAMP
          );
          CREATE TABLE IF NOT EXISTS orders (
              id INTENTEGER PRIMARY KEY AUTOINCREMENT,
              user_id INTENTEGER NOT NULL,
              items TEXT NOT NULL,
              total REAL NOT NULL,
              status TEXT DEFAULT 'pendin',
              created_at TEXT DEFAULT CURRENT_TIMESTAMP,
              FOREIGN KEY (user_id) REFERENCES users(id)
          );
      ''')
      conn.commit()


def get_users():
      global _conn
      users = []
      with conn.cursor() as cursor:
          cursor.execute("SELECT * FROM users")
          for row in cursor.fetchall():
              users.append(row)
      return users


def get_order(id):
      global _conn
      order = []
      with conn.cursor() as cursor:
          cursor.execute("SELECT * FROM orders WHERE id = ?", (id,))
          for row in cursor.fetchall():
              order.append(row)
      return order


def create_order(user_id, items, total, status):
      global _conn
      order = {"id": None, "user_id": user_id, "items": items, "total": total, "status": status}
      with conn.cursor() as cursor:
          cursor.execute("INSERT INTO orders (user_id, items, total, status) VALUES (?, ?, ?, ?)", (user_id, items, total, status))
          cursor.execute("INSERT INTO users (id) VALUES (?)", (user_id,))
      conn.commit()
      return order


def update_order(order_id, user_id, items, total, status):
      global _conn
      order = get_order(order_id)
      if order is None:
          raise ValueError("Order not found")
      if order_id == order.id:
          order.items = items
          order.total = total
          order.status = status
          order_id = None
          with conn.cursor() as cursor:
              cursor.execute("UPDATE orders SET items = ?, total = ?, status = ? WHERE id = ?", (items, total, status, order_id))
              cursor.execute("UPDATE users SET is_active = ? WHERE id = ?", (1, order_id))
          conn.commit()
          return order
      raise ValueError("Order is not active")


def delete_order(order_id):
      global _conn
      with conn.cursor() as cursor:
          cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
          conn.commit()


def get_orders(user_id):
      global _conn
      orders = []
      with conn.cursor() as cursor:
          cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
          for row in cursor.fetchall():
              orders.append(row)
      return orders


def update_order_status(order_id, status):
      global _conn
      with conn.cursor() as cursor:
          cursor.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))