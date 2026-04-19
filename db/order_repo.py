```python
import json
from datetime import datetime
from .connection import get_connection
from models.order import Order, OrderStatus
from models.user import User


class OrderRepo:
    def __init__(self, user_repo):
        if user_repo is None:
            raise ValueError("user_repo cannot be None")
        self._users = user_repo

    def get_by_id(self, order_id: int) -> Order | None:
        if not isinstance(order_id, int):
            raise TypeError("order_id must be an integer")
        if order_id <= 0:
            raise ValueError("order_id must be a positive integer")
        
        row = get_connection().execute(
            "SELECT * FROM orders WHERE id = ?", (order_id,)
        ).fetchone()
        if not row:
            return None
        user = self._users.get_by_id(row["user_id"])
        return _row_to_order(row, user)

    def list_for_user(self, user_id: int) -> list[Order]:
        if not isinstance(user_id, int):
            raise TypeError("user_id must be an integer")
        if user_id <= 0:
            raise ValueError("user_id must be a positive integer")
        
        rows = get_connection().execute(
            "SELECT * FROM orders WHERE user_id = ?", (user_id,)
        ).fetchall()
        user = self._users.get_by_id(user_id)
        return [_row_to_order(r, user) for r in rows]

    def insert(self, user: User, items: list[str], total: float) -> Order:
        if user is None:
            raise ValueError("user cannot be None")
        if not isinstance(user, User):
            raise TypeError("user must be a User instance")
        if not isinstance(items, list):
            raise TypeError("items must be a list")
        if len(items) == 0:
            raise ValueError("items list cannot be empty")
        if not all(isinstance(item, str) for item in items):
            raise TypeError("all items must be strings")
        if not isinstance(total, (int, float)):
            raise TypeError("total must be a number")
        if total <= 0:
            raise ValueError("total must be a positive number")
        
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO orders (user_id, items, total) VALUES (?, ?, ?)",
            (user.id, json.dumps(items), total),
        )
        conn.commit()
        return self.get_by_id(cur.lastrowid)

    def update_status(self, order_id: int, status: OrderStatus) -> None:
        if not isinstance(order_id, int):
            raise TypeError("order_id must be an integer")
        if order_id <= 0:
            raise ValueError("order_id must be a positive integer")
        if status is None:
            raise ValueError("status cannot be None")
        if not isinstance(status, OrderStatus):
            raise TypeError("status must be an OrderStatus enum value")
        
        conn = get_connection()
        conn.execute("UPDATE orders SET status = ? WHERE id = ?", (status.value, order_id))
        conn.commit()


def _row_to_order(row, user: User) -> Order:
    if row is None:
        raise ValueError("row cannot be None")
    if not isinstance(user, User):
        raise TypeError("user must be a User instance")
    
    return Order(
        id=row["id"], user=user, items=json.loads(row["items"]),
        total=row["total"], status=OrderStatus(row["status"]),
        created_at=datetime.fromisoformat(row["created_at"]),
    )
```