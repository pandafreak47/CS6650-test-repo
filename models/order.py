```python
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


# Default order status constant
DEFAULT_ORDER_STATUS = OrderStatus.PENDING

# Display format constants
ORDER_DISPLAY_FORMAT = "Order({id}, user={user}, status={status})"

# Field name constants for display formatting
DISPLAY_FORMAT_ID_KEY = "id"
DISPLAY_FORMAT_USER_KEY = "user"
DISPLAY_FORMAT_STATUS_KEY = "status"


@dataclass
class Order:
    id: int
    user: User
    items: list[str]
    total: float
    status: OrderStatus = field(default_factory=lambda: DEFAULT_ORDER_STATUS)
    created_at: datetime = field(default_factory=datetime.utcnow)

    def display(self) -> str:
        return ORDER_DISPLAY_FORMAT.format(
            **{
                DISPLAY_FORMAT_ID_KEY: self.id,
                DISPLAY_FORMAT_USER_KEY: self.user.username,
                DISPLAY_FORMAT_STATUS_KEY: self.status.value
            }
        )
```