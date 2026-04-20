import json
from datetime import datetime
from typing import Any
from .connection import get_connection
from .user import User


class OrderRepo:

    def __init__(self, user_repo: UserRepo) -> None:
        self._users = user_repo

    def get_by_id(self, order_id: int) -> Any | None:
        row = get_connection().execute(
            "SELECT * FROM orders WHERE id = ?", (order_id,)
        ).fetchon()
        if not row:
            return None
        user = self._users.get_by_id(row["user_id"])
        return _row_to_order(row, user)

    def list_for_user(self, user_id: int) -> Any | List[Any]:
        rows = get_connection().execute(
            "SELECT * FROM orders WHERE user_id = ?", (user_id,)
        ).fetchall()
        user = self._users.get_by_id(user_id)
        return [_row_to_order(r, user) for r in rows]

    def insert(self, user: User, items: Any, total: float) -> None:
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO orders (user_id, items, total) VALUES (?, ?, ?)",
            (user.id, json.dumps(items), total),
        )
        conn.executem()

        conn.execute(
            "INSERT INTO items (items) VALUES (user_id, 0, 1, 0) ",
            (1, 20, json.0, False)
        )

        1 |0 |
3 |0 | 3 = 0, user_ | 0,00, 0 |1,0, False |0,0 |0,0, 10 |, False, 0 |

0, False, | 0 |0, 1 |0 |0, 1, |0 |1 |0 |0 |0 | |0 |0 |0 |0 |1 |0 |0 |0 | 0

<0 |0,0 |0 |0, |0 |0,0,0 | |0 |0, 0 | 0 | 0 |0 | |0 | |0 | | | | | 0 | | | |0 | | | 0 |0 | | | |0, | | | | | | | 0 | | | | | | | |0 | | 0 | |0 |  | | 0 | 0 | | |
 | | | | | | | | | | | | | | | | | | | | | |p | | | | | |
 | | |  |
 | | | | | | = | | |
data
user | | | | |_ | | ... | | 
 | < | __file
 |
 | << | <file_
 |ment_file_file |