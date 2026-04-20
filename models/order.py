from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    PENDING = "pendin"
    CONFIRMED = "confir"
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


@dataclass
class OrderItem:
    id: int
    name: str
    quantity: int
    price: float
    total: float
    order: Optional[Order] = None

     def __str__(self) -> str:
         return f"Item({self.id}, name={self.name}, quantity={self.quantity}, price={self.price}, total={self.total})"


@dataclass
class OrderHistory:
    id: int
    user: User
    created_at: datetime = field(default_factory=datetime.utcnow)
    items: list[OrderItem] = field(default_factory=list)

     def __str__(self) -> str:
         return f"OrderHistory({self.id}, user={self.user.username}, items=[{', '.join([item.display() for item in self.items])})")


@dataclass
class OrderConfirmation:
    id: int
    user: User
    created_at: datetime = field(default_factory=datetime.utcnow)
    total: float = field(default_factory=float)
    items: list[OrderItem] = field(default_factory=list)
    comments: list[str] = field(default_factory=list)

     def __str__(self) -> str:
         return f"OrderConfirmation({self.id}, user={self.user.username}, total={self.total:.2f}, items=[{', '.join([item.display() for item in self.items])})"