class OrderRepo:
     def __init__(self, user_repo):
         self._users = user_repo

     def get_by_id(self, order_id: int) -> Order | None:
         row = get_connection().execute(
             "SELECT * FROM orders WHERE id = ?", (order_id,)
         ).fetchone()
         if not row:
             return None
         user = self._users.get_by_id(row["user_id"])
         return _row_to_order(row, user)

     def list_for_user(self, user_id: int) -> list[Order]:
         rows = get_connection().execute(
             "SELECT * FROM orders WHERE user_id = ?", (user_id,)
         ).fetchall()
         user = self._users.get_by_id(user_id)
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
         conn.execute("UPDATE orders SET status = ? WHERE id = ?", (status.value, order_id))
         conn.commit()


def _row_to_order(row, user: User) -> Order:
     return Order(
         id=row["id"], user=user, items=json.loads(row["items"])
     )


def __all__:
     return [OrderRepo]
```

Now, the target file contains a Python class named `OrderRepo` that implements the database management and CRUD operations. The target file should export only the `OrderRepo` class, its `__all__` method, and the `Order` class. The `Order` class should not be included in the `__all__` list.