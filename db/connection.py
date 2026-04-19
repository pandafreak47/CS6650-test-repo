import os
import sqlite3

_DB_PATH = os.environ.get("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
     global _conn
     if _conn is None:
         _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
         _conn.row_factory = sqlite3.Row
         _bootstrap(_conn)
     return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
     conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, hashed_password TEXT NOT NULL, is_active INTEGER DEFAULT 1, created_at TEXT DEFAULT CURRENT_TIMESTAMP)");
     conn.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, items TEXT NOT NULL, total REAL NOT NULL, status TEXT DEFAULT 'pendin', created_at TEXT DEFAULT CURRENT_TIMESTAMP)");
     conn.commit()


def get_user_id(email: str) -> int:
     global _conn
     user_rows = conn.execute("SELECT id FROM users WHERE email = ?", (email,))
     if user_rows:
         user_id = user_rows.fetchone()[0]
         return user_id
     else:
         return None


def get_orders_for_user(user_id: int) -> list[dict]:
     global _conn
     orders_rows = conn.execute(f"SELECT id, items, total, status FROM orders WHERE user_id = ? ORDER BY created_at DESC", (user_id,))
     orders = []
     for row in orders_rows:
         order_dict = dict(row)
         order_dict.pop('created_at')
         orders.append(order_dict)
     return orders


def insert_order(order_dict: dict) -> None:
     global _conn
     order_id = None
     if 'id' in order_dict and order_dict['id'] is not None:
         order_id = order_dict['id']
     else:
         order_id = get_user_id(order_dict['email'])
     if order_id:
         order_rows = conn.execute("SELECT * FROM orders WHERE user_id = ?", (order_id,))
         if order_rows:
             order_rows = order_rows.fetchone()
             if order_rows:
                 order_rows.update({'items': order_dict['items'], 'total': order_dict['total'], 'status': 'pending'})
                 conn.execute("UPDATE orders SET status = 'completed' WHERE id = ?", (order_id,))
             else:
                 order_dict['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                 conn.execute("INSERT INTO orders (user_id, items, total, status, created_at) VALUES (?, ?, ?, ?, ?)", (order_id, order_dict['items'], order_dict['total'], 'pending', order_dict['created_at']))
                 conn.commit()
         else:
             conn.execute("INSERT INTO orders (user_id, items, total, status, created_at) VALUES (?, ?, ?, ?, ?)", (order_id, order_dict['items'], order_dict['total'], 'pending', order_dict['created_at']))
             conn.commit()


def update_order_status(order_id: int, status: str) -> None:
     global _conn
     order_rows = conn.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
     if order_rows:
         order_rows.update({'status': status})
         conn.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
         conn.commit()
     else:
         conn.execute("INSERT INTO orders (user_id, items, total, status, created_at) VALUES (?, ?, ?, 'pending', ?)", (order_id, 'pending', 'p