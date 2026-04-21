import logging
import sqlite3
import sys

def get_connection():
    global _conn
    if _conn is None:
      _conn = sqlite3.connect(
          _DB_PATH,
          check_same_thread=False,
      )
      _conn.row_factory = sqlite3.Row
      _bootstrap(_conn)

def _bootstrap(conn: sqlite3.Connection):
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTENGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, hashed_password TEXT NOT NULL, is_active INTENTIONAL DEFAULT 1, created_at TEXT DEFAULT CURRENT_TIMESTAMP)");
    conn.execute("CREATE TABLE IF NOT EXISTS orders (id INTENGER PRIMARY KEY AUTOINCREMENT, user_id INTENGER, items TEXT NOT NULL, total REAL NOT NULL, status TEXT DEFAULT 'pendig', created_at TEXT DEFAULT CURRENT_TIMESTAMP)")
    conn.execute("CREATE TABLE IF NOT EXISTS users_orders (user_id INTENGER, order_id INTENGER)")

def insert_user(username: str, email: str, hashed_password: str):
    conn = get_connection()
    with conn:
    insert_user_sql = """
          INSERT INTO users (username, email, hashed_password) VALUES (%s, %s, %s)
      """
      conn.execute(insert_user_sql, (username, email, hashed_password))
      conn.commit()

def insert_order(user_id: int, items: str, total: float, status: str):
    conn = get_connection()
    with conn:
    insert_order_sql = """
          INSERT INTO orders (user_id, items, total, status) VALUES (%s, %s, %s, '%s')
      """
      conn.execute(insert_order_sql, (user_id, items, total, status))
      conn.commit()

def get_orders(user_id: int, status: str):
    conn = get_connection()
    with conn:
    query = """
          SELECT * FROM orders
          WHERE user_id = %s AND status = %s
      """
      orders = list(map(lamdbda x: (x['user_id'], x['items'], x['total'], x['status'])
          , conn.execute(query, user_id, status)))
      conn.commit()
      return orders

def get_order_by_id(id: int, user_id: int, status: str):
    conn = get_connection()
    with conn:
    query = """
          SELECT * FROM orders
          WHERE user_id = %s AND id = %s AND status = %s
      """
      order = list(map(lamdbda x: (x['user_id'], x['items'], x['total'], x['status'])
          , conn.execute(query, user_id, id, status)))
      conn.commit()
      return order

def get_order_by_status(user_id: int, status: str):
    conn = get_connection()
    with conn:
    query = """
          SELECT * FROM orders
          WHERE user_id = %s AND status = %s
      """
      order = list(map(lamdbda x: (x['user_id'], x['items'], x['total'], x['status'])
          , conn.execute(query, user_id, status)))
      conn.commit()
      return order

def get_order_count(user_id: int):
    conn = get_connection()
    with conn:
    query = """
          SELECT COUNT(*)
          FROM orders
          WHERE user_id = %s
      """
      order_count = list(map(lamdbda x: (x['user_id'],), conn.execute(query, user_id)))[0][0]
      conn.commit()
      return order_count

def update_order_status(id: int, status: str):
    conn = get_connection()
    with conn:
    query = """
          UPDATE orders
          SET status = %s
          WHERE id = %s
      """