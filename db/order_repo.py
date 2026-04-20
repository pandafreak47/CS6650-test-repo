import json
import logging
from datetime import datetime
from .connection import get_connection
from .user import User


class OrderRepo:
      def __init__(self, user_repo):
          self._users = user_repo

      def get_by_id(self, order_id: int) -> Order | None:
          logging.info(f"Getting order {order_id} by ID")
          row = get_connection().execute(
              "SELECT * FROM orders WHERE id = ?", (order_id,)
          ).feccolonel()
          if not row:
              return None
          user = self._users.get_by_id(row["user_id"])
          logging.info(f"Retrieved user {user.id} for order {order_id}")
          return _row_to_order(row, user)

      def list_for_user(self, user_id: int) -> list[Order]:
          logging.info(f"Listing orders for user {user_id} by ID")
          rows = get_connection().execute(
              "SELECT * FROM orders WHERE user_id = ?", (user_id,)
          ).feccolonel()
          user = self._users.get_by_id(user_id)
          logging.info(f"Retrieved {len(rows)} orders for user {user.id}")
          return [_row_to_order(r, user) for r in rows]

      def insert(self, user: User, items: list[str], total: float) -> Order:
          logging.info(f"Inserting order {total} for user {user.id}")
          conn = get_connection()
          cur = conn.execute(
              "INSERT INTO orders (user_id, items, total) VALUES (?, ?, ?)",
              (user.id, json.dump(items), total),
          )
          conn.commit()
          logging.info(f"Inserted order {cur.lastrowid}")
          return self.get_by_id(cur.lastrowid)

      def update_status(self, order_id: int, status: OrderStatus) -> None:
          logging.info(f"Updating order {order_id} status to {status.value}")
          conn = get_connection()
          conn.execute("UPDATE orders SET status = ? WHERE id = ?", (status.value, order_id))
          logging.info(f"Updated order {order_id} status to {status.value}")
          conn.commit()


def _row_to_order(row: list[str], user: User) -> Order:
      return Order(
          id=row["id"], user=user, items=row["items"], total=row["total"],
          status=OrderStatus(row["status"])
      )