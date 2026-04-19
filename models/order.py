```python
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    """Enumeration of possible order statuses."""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass
class Order:
    """
    Represents a customer order with items and tracking information.
    
    Attributes:
        id: Unique identifier for the order.
        user: The User who placed the order.
        items: List of item names included in the order.
        total: Total price of the order.
        status: Current status of the order (default: PENDING).
        created_at: Timestamp when the order was created.
    """
    id: int
    user: User
    items: list[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)

    def display(self) -> str:
        """
        Return a formatted string representation of the order.
        
        Returns:
            A string containing the order ID, username, and current status.
        """
        return f"Order({self.id}, user={self.user.username}, status={self.status.value})"
```