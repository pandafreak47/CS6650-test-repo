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
    Represents a customer order.
    
    Attributes:
        id: Unique identifier for the order.
        user: The User who placed the order.
        items: List of item names in the order.
        total: Total price of the order.
        status: Current status of the order.
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
        Generate a string representation of the order.
        
        Returns:
            A formatted string containing the order ID, username, and status.
        """
        return f"Order({self.id}, user={self.user.username}, status={self.status.value})"
```