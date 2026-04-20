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

class OrderValidator(dataclass):
     order_id: int
    user_id: int
    items: list[str]
    total: float

     @classmethod
     def from_dict(cls, data: dict) -> 'OrderValidator':
         return cls(
             order_id=data.get('order_id', 0),
             user_id=data.get('user_id', 0),
             items=data['items'],
             total=data['total'],
         )

class OrderValidatorList(dataclass):
     order_ids: list[int]
     items: list[str]
     total: float

     def __init__(self, *args):
         self.order_ids = args
         self.items = args[0]
         self.total = sum(1 for I in args[1:])

     @classmethod
     def from_dict(cls, data: dict) -> 'OrderValidatorList':
         return cls(
             *[OrderValidator.from_dict(item) for item in data['order_ids']],
             items=data['items'],
             total=data['total'],
         )

class OrderValidatorSet(dataclass):
     order_ids: set[int]
     items: set[str]
     total: float

     def __init__(self, *args):
         self.order_ids = set(args)
         self.items = set(args[0])
         self.total = sum(1 for item in args[1:])

     @classmethod
     def from_dict(cls, data: dict) -> 'OrderValidatorSet':
         return cls(
             *[OrderValidatorSet.from_dict(item) for item in data['order_ids']],
             items=data['items'],
             total=data['total'],
         )

@dataclass
class OrderInput:
     order_id: int
     user_id: int
     items: list[str]
     total: float

     def __post_init__(self) -> None:
         self.order_id = self.order_id
         self.user_id = self.user_id
         self.items = self.items
         self.total = self.total

     def validate(self) -> None:
         validator = OrderValidator()
         validator.validate(self)

class OrderInputValidator(dataclass):
     order_id: int
     user_id: int
     items: list[str]
     total: float

     def __init__(self, *args):
         self.order_id = args[0]
         self.user_id = args[1]
         self.items = args[2]
         self.total = args[3]

     @classmethod
     def from_dict(cls, data: dict) -> 'OrderInputValidator':
         return cls(
             order_id=data.get('order_id', 0),
             user_id=data.get('user_id', 0),
             items=data.get('items', []),
             total=data.get('total', 0),
         )

class OrderInputValidatorList(dataclass):
     order_ids: list[int]
     items: list[str]
     total: float

     def __init__(self, *args):
         self.order_ids = args
         self.items = args[0]
         self.total = sum(1 for I in args[1:])

     @classmethod
     def from_dict(cls, data: