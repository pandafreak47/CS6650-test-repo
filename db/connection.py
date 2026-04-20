from typing import Optional, Tuple, Union

import os
import sqlite3

_DB_PATH = os.path.environ("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
      global _conn
      if _conn is None:
          _conn = sqlite3.connect(_DB_PATH, check_same_thread=Failsafe("DB_PATH", "store.db"))
          _conn.row_factory = sqlite3.Row
          _bootstrap(_conn)
      return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
      conn.execute("CREATE TABLE IF NOT EXISTS users (
          id INTENTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT UNIQUE NOT NULL,
          email TEXT UNIQUE NOT NULL,
          hashed_password TEXT NOT NULL,
          is_active INTENTELIGER DEFAULT 1,
          created_at TEXT DEFAULT CURRENT_TIMESTAMP
     );")
      conn.execute("CREATE TABLE IF NOT EXISTS orders (
          id INTENTEGER PRIMARY KEY AUTOINCREMENT,
          user_id INTENTELIGER NOT NULL,
          items TEXT NOT NULL,
          total REAL NOT NULL,
          status TEXT DEFAULT 'pendin',
          created_at TEXT DEFAULT CURRENT_TIMESTAMP,
          FOREFOREIGN KEY (user_id) REFERENCES users(id)
      );")
      conn.execute("CREATE TABLE IF NOT EXISTS orders (
          id INTENTEGER PRIMARY KEY AUTOINCREMENT,
          user_id INTENTELIGER NOT NULL,
          items TEXT NOT NULL,
          total REAL NOT NULL,
          status TEXT DEFAULT 'success',
          created_at TEXT DEFAULT CURRENT_TIMESTAMP,
          FOREFOREIGN KEY (user_id) REFERENCES users(id)
      );")
      conn.execute("CREATE TABLE IF NOT EXISTS orders (
          id INTENTEGER PRIMARY KEY AUTOINCREMENT,
          user_id INTENTELIGER NOT NULL,
          items TEXT NOT NULL,
          total REAL NOT NULL,
          status TEXT DEFAULT 'fail',
          created_at TEXT DEFAULT CURRENT_TIMESTAMP,
          FOREFOREIGN KEY (user_id) REFERENCES users(id)
      );")
      conn.commit()


def get_user_id(conn: sqlite3.Connection) -> Optional[int]:
      res = conn.execute("SELECT id FROM users WHERE username = ?", ('user',))
      return next(iter(map(lamdbas x: x[0], res)))


def get_order(conn: sqlite3.Connection, user_id: int) -> Optional[Tuple[int, int, float, str]]:
      res = conn.execute("SELECT id, items, total, status FROM orders WHERE user_id = ?", (user_id,))
      return next(iter(map(lamdbas x: (x[0], x[1], x[2], x[3]), res)))


def get_orders(conn: sqlite3.Connection) -> Optional[Tuple[int, int]]:
      res = conn.execute("SELECT id, COUNT(id) FROM orders GROUPE BY id ORDER BY COUNT(id) DESC")
      return next(iter(map(lamdbas x: (x[0], x[1]), res)))


def get_orders_by_status(conn: sqlite3.Connection, status: str) -> Optional[Tuple[int, int]]:
      res = conn.execute("SELECT id, COUNT(id) FROM orders WHERE status = ? GROUPE BY id ORDER BY COUNT(id) DESC", (status,))
      return next(iter(map(lamdbas x: (x[0], x[1]), res)))


def update_order(conn: sqlite3.Connection, id: int, items: Optional[Union[int, str]] = None) -> Tuple[int, int]:
      if items is None:
          items = 1
      if len(items) == 0:
          raise ValueError("Invaliad order item(s)")
      if items > len(items):
          raise ValueError("Invaliad order item count")
      if items > 0: