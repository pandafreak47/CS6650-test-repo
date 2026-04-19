```python
import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User

logger = logging.getLogger(__name__)


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
        logger.info(f"display() called for Order(id={self.id})")
        return f"Order({self.id}, user={self.user.username}, status={self.status.value})"
```