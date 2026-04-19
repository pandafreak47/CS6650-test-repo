import json
from datetime import datetime
from typing import Optional
from .connection import get_connection
from .models import Order, OrderStatus


class OrderRepo:
    def __init__(self, user_repo: UserRepo) -> None:
        self.user_repo = user_repo

    def get_by_id(self, order_id: int) -> Optional[Order]:
        row = get_connection().execute(
            "SELECT * FROM orders WHERE id = ?", (order_id,)
        ).fetchone()
        return row and _row_to_order(row)

    def list_for_user(self, user_id: int) -> list[Order]:
        rows = get_connection().execute(
            "SELECT * FROM orders WHERE user_id = ?", (user_id,)
        ).fetchall()
        user = self.user_repo.get_by_id(user_id)
        return [_row_to_order(r, user) for r in rows]

    def insert(self, user: User, items: list[str], total: float) -> Order:
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO orders (user_id, items, total) VALUES (?, ?, ?)",
            (user.id, json.dumps(items), total),
        )
        conn.commit()
        return self.get_by_id(cur.lastrowid)

    def update_status(self, order_id: int, status: OrderStatus) -> None:
        conn = get_connection()
        conn.execute(
            "UPDATE orders SET status = ? WHERE id = ?", (status.value, order_id)
        )
        conn.commit()


def _row_to_order(row, user: User) -> Order:
    return Order(
        id=row["id"], user=user, items=json.loads(row["items"]),
        total=row["total"], status=OrderStatus(row["status"]),
        created_at=datetime.fromisoformat(row["created_at"]),
    )

```

Example Output:
```
[
    {
        "id": 1,
        "user": {
            "id": 1,
            "username": "John Doe",
            "email": "john.doe@example.com",
            "hashed_password": "123456"
        },
        "items": [
            "Chocolate Cake",
            "Spinach and Feta Salad",
            "Peach Crumble"
        ],
        "total": 35.99,
        "status": {
            "value": "shipped",
            "timestamp": "2021-01-01T00:00:00Z"
        }
    },
    {
        "id": 2,
        "user": {
            "id": 2,
            "username": "Jane Doe",
            "email": "jane.doe@example.com",
            "hashed_password": "123456"
        },
        "items": [
            "Beef Tacos",
            "Fruit and Yogurt Parfait",
            "Chai Latte"
        ],
        "total": 18.99,
        "status": {
            "value": "canceled",
            "timestamp": "2021-02-01T00:00:00Z"
        }
    }
]