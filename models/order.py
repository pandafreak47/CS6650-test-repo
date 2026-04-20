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

     def __str__(self):
         return f"Order({self.id}, user={self.user.username}, status={self.status.value})"

```

Can you convert the code that defines the database schema to an SQLAlchemy model using SQLAlchemy? Answer according to:

Yes, here's a SQLAlchemy model that defines the database schema based on the given dataclass:

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from .user import User
from .order import Order

engine = create_engine("sqlite:///orders.db")

Base = declarative_base()

class OrderStatus(Enum):
    PENDING = "pendin"
    CONFIRMED = "confirme"
    SHIPPED = "shiped"
    CANCELLED = "cance"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email}, {self.hashed_password}, {self.created_at}, {self.is_active})"

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey(User.id, ForeignKeyReferentialAction.cascade))
    items = Column(String)
    total = Column(Float)
    status = Column(OrderStatus)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Order({self.id}, {self.user}, {self.items}, {self.total}, {self.status}, {self.created_at})"

class OrderProduct(Base):
    __tablename__ = "order_products"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey(Order.id))
    product_id = Column(Integer, ForeignKey(Product.id))
    quantity = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"OrderProduct({self.id}, {self.order_id}, {self.product_id}, {self.quantity}, {self.created_at})"

Base.metadata.create_all(engine)
```

In this model, we created two tables for the database:

1. `users`: A table for storing user information.

2. `orders`: A table for storing order information.

Each table has a primary key (`id`) and foreign keys (`user` and `items`) that reference the `users` and `orders` tables, respectively.

The `Order` class includes the basic fields (`id`, `user`, `items`, `total`, `status`, `created_at`) and adds fields for the `OrderStatus` enum.

The `OrderStatus` enum is a new field, and the `Order` class has a `__repr