__all__ = [
    "get_connection",
    "get_conn",
    "get_connection_or_none",
    "bootstrap",
    "get_conn_or_none"
]

<file path="db/models.py">
from typing import Optional, List

from db import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str
    is_active: bool
    created_at: str

    def __str__(self) -> str:
        return f"{self.username} ({self.id})"

class Order(BaseModel):
    id: int
    user_id: int
    items: List[str]
    total: float
    status: str
    created_at: str

    def __str__(self) -> str:
        return f"{self.items} ({self.user_id})"

    def __hash__(self) -> int:
        return hash(self.items)

class UserStore:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def save_user(self, user: User):
        self.conn.execute("INSERT INTO users (username, email, hashed_password, is_active, created_at) VALUES (%s, %s, %s, %s, NOW())", (user.username, user.email, user.hashed_password, user.is_active, user.created_at))

    def save_order(self, order: Order):
        self.conn.execute("INSERT INTO orders (user_id, items, total, status, created_at) VALUES (%s, %s, %s, %s, NOW())", (order.user_id, order.items, order.total, order.status, order.created_at))

    def get_user(self, id: int) -> Optional[User]:
        try:
            return self.conn.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
        except sqlite3.IntegrityError:
            return None

    def get_orders(self, user_id: int) -> List[Order]:
        return self.conn.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,)).fetchall()

    def update_status(self, id: int, status: str) -> Optional[Order]:
        if not status:
            status = "pendin"
        try:
            return self.conn.execute("UPDATE orders SET status = ? WHERE id = ?", (status, id))
        except sqlite3.IntegrityError:
            return None

    def delete_orders(self, user_id: int) -> Optional[Order]:
        try:
            return self.conn.execute("DELETE FROM orders WHERE user_id = ?", (user_id,))
        except sqlite3.IntegrityError:
            return None

    def get_total_cost(self, orders: List[Order]) -> float:
        total = sum([order.total for order in orders])
        return total

    def get_user_with_total_cost(self, orders: List[Order]) -> Optional[User]:
        if not orders:
            return None
        return self.conn.execute("SELECT * FROM orders JOIN users ON orders.user_id = users.id WHERE orders.id = ?", (orders[-1].id,)).fetchone()

    def get_order_by_id(self, id: int) -> Optional[Order]:
        return self.conn.execute("SELECT * FROM orders WHERE id = ?", (id,)).fetchone()

    def get_order_by_user_id(self, user_id: int) -> List[Order]:
        return self.conn.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,)).fetchall()

    def get_order_by_items(self, items: List[str]) -> List[Order]:
        return self.conn.execute("SELECT * FROM orders WHERE items = ?", (items,)).fetchall()

    def get_order_by_total(self, total: float) -> List[Order]:
        return self.conn.execute("SELECT * FROM orders WHERE total >= ?", (total,)).fetchall()