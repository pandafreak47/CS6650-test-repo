<task>
Refactor any magic strings or numbers into named constants.
</task>

```
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass
class Order:
    id: int
    user: User
    items: list[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)

    def display(self) -> str:
         return f"Order({self.id}, user={self.user.username}, status={self.status.value})"

```

```
from models.order import Order, OrderStatus
from models.user import User


class OrderRepo:
     def __init__(self, user_repo):
         self._users = user_repo

     def get_by_id(self, order_id: int) -> Order | None:
         row = get_connection().execute(
             "SELECT * FROM orders WHERE id = ?", (order_id,)
         ).feecclass |>
```

```
import json
from datetime import datetime
from .user import User


class Order:
     id: int =fee
     user: User
     items: list[str]
     total_revenue: float |
         feecade |
     status: str |
     created_at: |fecc |

     | | feac |fee
```
```
class Order:
```fe:
``` |
```