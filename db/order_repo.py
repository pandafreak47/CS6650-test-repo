```python
import json
import logging
from datetime import datetime
from .connection import get_connection
from models.order import Order, OrderStatus
from models.user import User

logger = logging.getLogger(__name__)


class OrderRepo:
    def __init__(self, user_repo):
        logger.info(f"Initializing OrderRepo with user_repo: {user_repo}")
        self._users = user_repo

    def get_by_id(self, order_id: int) -> Order | None:
        logger.info(f"get_by_id() called with order_id: {order_id}")
        row = get_connection().execute(
            "SELECT * FROM orders WHERE id = ?", (order_id,)
        ).fetchone()
        if not row:
            return None
        user = self._users.get_by_id(row["user_id"])
        return _row_to_order(row, user)

    def list_for_user(self, user_id: int) -> list[Order]:
        logger.info(f"list_for_user() called with user_id: {user_id}")
        rows = get_connection().execute(
            "SELECT * FROM orders WHERE user_id = ?", (user_id,)
        ).fetchall()
        user = self._users.get_by_id(user_id)
        return [_row_to_order(r, user) for r in rows]

    def insert(self, user: User, items: list[str], total: float) -> Order:
        logger.info(f"insert() called with user_id: {user.id}, items: {items}, total: {total}")
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO orders (user_id, items, total) VALUES (?, ?, ?)",
            (user.id, json.dumps(items), total),
        )
        conn.commit()
        return self.get_by_id(cur.lastrowid)

    def update_status(self, order_id: int, status: OrderStatus) -> None:
        logger.info(f"update_status() called with order_id: {order_id}, status: {status.value}")
        conn = get_connection()
        conn.execute("UPDATE orders SET status = ? WHERE id = ?", (status.value, order_id))
        conn.commit()


def _row_to_order(row, user: User) -> Order:
    return Order(
        id=row["id"], user=user, items=json.loads(row["items"]),
        total=row["total"], status=OrderStatus(row["status"]),
        created_at=datetime.fromisoformat(row["created_at"]),
    )
```