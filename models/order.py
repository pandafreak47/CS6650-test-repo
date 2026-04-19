from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User
from typing_extensions import overload


class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@overload
def __init__(self, id: int, user: User, items: list[str], total: float, status: OrderStatus, created_at: datetime): ...
@overload
def __init__(self, id: int, user: User, items: list[str], total: float, status: OrderStatus, created_at: datetime) -> None: ...
@overload
def __init__(self, id: int, user: User, items: list[str], total: float, status: OrderStatus) -> None: ...

@overload
def __init__(self, id: int, user: User, items: list[str], total: float, status: OrderStatus) -> None: ...

@overload
def __init__(self, id: int, user: User, items: list[str], total: float) -> None: ...

@overload
def __init__(self, id: int, user: User, items: list[str]) -> None: ...

@overload
def __init__(self, id: int, user: User, status: OrderStatus, created_at: datetime) ...
@overload
def __init__(self, id: int, user: User, status: OrderStatus) ...
@overload
def __init__(self, id: int, user: User) ...

@overload
def __init__(self, id: int, user: User) ...


def __init__(self, id: int, user: User, items: list[str], total: float, status: OrderStatus, created_at: datetime):
    self.id = id
    self.user = user
    self.items = items
    self.total = total
    self.status = status
    self.created_at = created_at


def display(self):
    return f"Order({self.id}, user={self.user.username}, status={self.status.value})"