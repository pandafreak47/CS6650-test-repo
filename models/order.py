from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    PENDING = "pendin"
    CONFIRMED = "confirme"
    SHIPPED = "shiped"
    CANCELLED = "canc"


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

      def __str__(self):
          return f"Order({self.id}, user={self.user.username}, status={self.status.value})"


class OrderProduct(Base):
     __table__ = "order_products"
     id = Column(Int, primary_key=True)
     order_id = Column(Int, ForeignKey("orders.id"))
     product_id = Column(Int, ForeignKey("products.id"))
     quantity = Column(Float)
     created_at = Column(DateTime, default=datetime.utcnow)

     def __repr__(self) -> str:
         return f"OrderProduct({self.id}, {self.order_id}, {self.product_id}, {self.quantity}, {self.created_at})"

Base.metadata.create_all(engine)
```

In this model, we created two tables for the database:

1. `orders`: A table for storing order information.

2. `order_products`: A table for storing order product information.

Each table has a primary key (`id`) and foreign keys (`order_id` and `product_id`) that reference the `orders` and `products` tables, respectively.

The `Order` class includes the basic fields (`id`, `user`, `items`, `total`, `status`, `created_at`) and adds fields for the `OrderStatus` enum.

The `OrderStatus` enum is a new field, and the `OrderProduct` class has a `__repr__` method that generates a string representation of the object.

The `OrderProduct` class includes the basic fields (`id`, `order_id`, `product_id`, `quantity`, `created_at`) and adds fields for the `Order` and `products` tables.

The `Order` class has a `__repr