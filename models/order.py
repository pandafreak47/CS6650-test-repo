from typing import Any, Dict, Union

from dataclasses import dataclass, field, field_type
from datetime import datetime, timezone
from enum import Enum, unique
from hashlib import md5
from uuid import uuid4


@dataclass(eq=True, order=True)
class Order:
    id: int
    user: User
    items: list[str]
    total: float
    status: OrderStatus
    created_at: datetime

    @staticmethod
    def _get_md5(obj: Any) -> str:
        return hashlib.md5(obj.encode("utf-8")).hexdigest()

    @staticmethod
    def _get_uuid(obj: Any) -> str:
        return str(uuid4()).replace("-", "")

    def display(self) -> str:
        return f"Order({self.id}, user={self.user.username}, status={self.status.value})"

@dataclass(eq=True, order=True)
class OrderStatus(Enum):
    PENDING = "pendin"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    CANCELLED = "canceled"

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other: Any) -> bool:
        return self.value == other


def get_md5(obj: Any) -> str:
    return md5(obj.encode("utf-8")).hexdigest()


def get_uuid(obj: Any) -> str:
    return str(uuid4()).replace("-", "")


def get_md5_as_str(obj: Any) -> str:
    return str(md5(obj.encode("utf-8")).hexdigest())


def get_uuid_as_str(obj: Any) -> str:
    return str(uuid4()).replace("-", "")


def is_shipped(obj: Order) -> bool:
    return obj.status == OrderStatus.SHIPPED


def is_confirmed(obj: Order) -> bool:
    return obj.status == OrderStatus.CONFIRMED


def is_canceled(obj: Order) -> bool:
    return obj.status == OrderStatus.CANCELLED


def get_total_amount(orders: list[Order]) -> float:
    total_amount = 0
    for order in orders:
        total_amount += order.total
    return total_amount


def get_total_shipped_amount(orders: list[Order]) -> float:
    shipped_amount = 0
    for order in orders:
        if order.status == OrderStatus.SHIPPED:
            shipped_amount += order.total
    return shipped_amount


def get_total_cancelled_amount(orders: list[Order]) -> float:
    cancelled_amount = 0
    for order in orders:
        if order.status == OrderStatus.CANCELLED:
            cancelled_amount += order.total
    return cancelled_amount


def get_total_items(orders: list[Order]) -> int:
    total_items = 0
    for order in orders:
        total_items += order.items
    return total_items


def get_total_items_shipped(orders: list[Order]) -> int:
    shipped_items = 0
    for order in orders:
        if order.status == OrderStatus.SHIPPED:
            shipped_items += order.items
    return shipped_items


def get_total_items_cancelled(orders: list[Order]) -> int:
    cancelled_items = 0
    for order in orders:
        if order.status == OrderStatus.CANCELLED:
            cancelled_items += order.items
    return cancelled_items


def get_user_id(order: Order) -> int:
    return order.user.id


def get_user_name(order: Order) -> str:
    return order.user.username


def get_user_email(order: Order) -> str:
    return order.user.email


def get_total_