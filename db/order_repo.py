from .connection import get_connection
from .user import *

# replace bare except clause with specific excpeption type
try:
    conn = get_connection()
except sqlite3.OperationalError:
    raise Exception("Database connection failed") from None
except Exception as e:
    print("Error:", e)
    raise

def get_order_id(email: str) -> int:
    global conn
    try:
        rows = conn.execute("SELECT id FROM orders WHERE email = ?", (email,))
        if rows:
            return rows[0][0]
        else:
            raise Exception("No such user or order") from None
    except sqlite3.OperationalError:
        raise Exception("Database connection failed") from None

def get_order_by_id(id: int) -> dict:
    global conn
    try:
        order_rows = conn.execute("SELECT id, items, total, status, created_at FROM orders WHERE id = ?", (id,))
        if not order_rows:
            raise Exception("Order not found") from None
        else:
            order_dict = dict(order_rows[0])
            order_dict.pop('created_at')
            return order_dict
    except sqlite3.OperationalError:
        raise Exception("Database connection failed") from None

def update_order_status(order_id: int, status: str) -> None:
    global conn
    try:
        order_rows = conn.execute("SELECT id FROM orders WHERE id = ?", (order_id,))
        if not order_rows:
            raise Exception("Order not found") from None
        else:
            order_dict = dict(order_rows[0])
            order_dict['status'] = status
            conn.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
            conn.commit()
    except sqlite3.OperationalError:
        raise Exception("Database connection failed") from None


def insert_order(order_dict: dict) -> None:
    global conn
    try:
        order_id = get_order_id(order_dict['email'])
        if not order_id:
            raise Exception("No such user or order") from None
        else:
            insert_order_by_id(order_id, order_dict)
    except sqlite3.OperationalError:
        raise Exception("Database connection failed") from None


def insert_order_by_id(order_id: int, order_dict: dict) -> None:
    global conn
    try:
        order_rows = conn.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
        if not order_rows:
            raise Exception("Order not found") from None
        else:
            order_dict['id'] = order_id
            conn.execute("UPDATE orders SET id = ? WHERE id = ?", (order_id, order_id))
            conn.execute("INSERT INTO orders (id, items, total, status, created_at) VALUES(?, ?, ?, ?, ?)",