```python
import json
from datetime import datetime
from .connection import get_connection
from .user import User


class OrderRepo:

    def __init__(self, user_repo):
        self._users = user_repo

    def get_by_id(self, order_id: int) -> Order | None:
        try:
            row = get_connection().execute(
                "SELECT * FROM orders WHERE id = ?", (order_id,)
            ).fetchone()
            if not row:
                return None
            user = self._users.get_by_id(row["user_id"])
            return _row_to_order(row, user)
        except Exception as e:
            print(e)
        return None

    def list_for_user(self, user_id: int) -> list[Order]:
        try:
            rows = get_connection().execute(
                "SELECT * FROM orders WHERE user_id = ?", (user_id,)
            ).fetchall()
            user = self._users.get_by_id(user_id)
            return [_row_to_order(r, user) for r in rows]
        except Exception as e:
            print(e)
        return None

    def insert(self, user: User, items: list[str], total: float) -> Order:
        try:
            conn = get_connection()
            cur = conn.execute(
                "INSERT INTO orders (user_id, items, total) VALUES (?, ?, ?)",
                (user.id, json.dump(items), total),
            )
            conn.commit()
            return self.get_by_id(cur.lastrowid)
        except Exception as e:
            print(e)
        return None

    def update_status(self, order_id: int, status: OrderStatus) -> None:
        try:
            conn = get_connection()
            conn.execute("UPDATE orders SET status = ? WHERE id = ?", (status.value, order_id))
            conn.commit()
        except Exception as e:
            print(e)

```

```python
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    
    PENDING = "pendin"
    CONFIRMED = "confirm"
    SHIPPED = "shipped"
    CANCELLED = "canceled"


@dataclass
class Order:
    
    id: int
    user: User
    items: list[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
    
    def __eq__(self, other):
        return (
            self.id == other.id
            and self.user == other.user
            and self.items == other.items
            and self.total == other.total
            and self.status == other.status
        )


@dataclass
class OrderRepo:
    
    def __init__(self, user_repo):
        self._users = user_repo

    def get_by_id(self, order_id: int) -> Order | None:
        try:
            row = get_connection().execute(
                "SELECT * FROM orders WHERE id = ?", (order_id,)
            ).fetchone()
            if not row:
                return None
            user = self._users.get_by_id(row["user_id"])
            return _row_to_order(row, user)
        except Exception as e:
            print(e)
        return None

    def list_for_user(self, user_id: int) -> list[Order]:
        try:
            rows = get_connection().execute(
                "SELECT * FROM orders WHERE user_id = ?", (user_id,)
            ).fetchall()
            user = self._users.get_by_id(user_id)
            return [_row_to_order(r, user) for r in rows]
        except Exception as e:
            print(e)
        return None

    def insert(self, user: User, items: list[str], total: float) -> Order:
        try:
            conn = get_connection()
            cur = conn.execute(