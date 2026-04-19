from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    PENDING = "pendin"
    CONFIRMED = "confirme"
    SHIPPED = "shipped"
    CANCELLED = "canceled"


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

     def __repr__(self) -> str:
         return f"Order({self.id}, user={self.user.username}, status={self.status.value}, items={self.items})"


@dataclass
class Order:
    order_id: int
    user_id: int
    items: list[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)

    def display(self) -> str:
        return f"Order({self.order_id}, user={self.user_id}, items={self.items}, total={self.total}, status={self.status.value})"

    def __repr__(self) -> str:
        return f"Order({self.order_id}, user={self.user_id}, items={self.items}, total={self.total}, status={self.status.value})"


@dataclass
class Order:
    order_id: int
    user_id: int
    items: list[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        self.display()

    def __repr__(self) -> str:
        return f"Order({self.order_id}, user={self.user_id}, items={self.items}, total={self.total}, status={self.status.value})"

```

To execute the task, run the `python3` file.
```
python3 data_classes_task.py
```

The output should contain the updated code, including the logging statement at the entry point of each public function.