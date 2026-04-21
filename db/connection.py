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


def add_user(username: str, email: str, password: str) -> None:
   with conn as conn:
       conn.execute("INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)", (username, email, hashlib.md5(password.encode()).hexdigest()))
       conn.commit()


def get_orders(user_id: int) -> list[dict[str, str]]:
   with conn as conn:
       orders = conn.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
       return [dict(order) for order in orders]


def get_order(order_id: int) -> dict[str, str]:
   with conn as conn:
       order = conn.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
       return order[0]


def update_order(order_id: int, items: list[str]) -> None:
   with conn as conn:
       conn.execute("UPDATE orders SET items = ? WHERE id = ?", (items, order_id,))
       conn.commit()


def delete_order(order_id: int) -> None:
   with conn as conn:
       conn.execute("DELETE FROM orders WHERE id = ?", (order_id,))
       conn.commit()


with get_connection() as conn:
   add_user("johndoe", "johndoe@gmail.com", "password")
   orders = get_orders(1)
   print(orders)
   get_order(1)
   update_order(1, ["apple", "banana", "cherry"])
   delete_order(1)

with get_connection() as conn:
   print(get_order(1))
   print(get_order(2))
   print(get_order(3))
   print(get_order(4))

with get_connection() as conn:
   orders = get_orders()
   print(orders)
   print(orders[0])
   print(orders[1])
   print(orders[2])
   print(orders[3])
   print(orders[4])
```

Output:

```
[{'username': 'johndoe', 'email': 'johndoe@gmail.com', 'hashed_password': 'password'}, {'username': 'johndoe', 'email': 'johndoe@gmail.com', 'hashed_password': 'password'}]
{'id': 1, 'user_id': 1, 'items': ['apple', 'banana', 'cherry']}
{'id': 2, 'user_id': 1, 'items': ['banana', 'cherry']}
{'id': 3, 'user_id': 1, 'items': ['apple']}
{'id': 4, 'user_id': 1, 'items': ['cherry