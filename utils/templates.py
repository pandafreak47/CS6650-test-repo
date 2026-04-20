from pathlib import Path
from typing import Dict, List, Optional

from flask import flash, request, redirect, render_template, session, url_for, send_file
from werkzeug.utils import secure_filename

from .models import db, User, Order, Product, Category, OrderItem, ItemType, OrderStatus, OrderType, ShippingMethod

class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return f"<user {self.username}>"

    def __eq__(self, other: User) -> bool:
        return self.username == other.username

    def __hash__(self) -> int:
        return hash(self.username)

    def __str__(self) -> str:
        return self.username


class Order:
    def __init__(self, user: User, order_id: str, total: float, status: OrderStatus, type: OrderType):
        self.user = user
        self.order_id = order_id
        self.total = total
        self.status = status
        self.type = type

    def __repr__(self) -> str:
        return f"<order {self.user.username} ({self.order_id})>"

    def __eq__(self, other: Order) -> bool:
        return self.user == other.user and self.order_id == other.order_id

    def __hash__(self) -> int:
        return hash((self.user.username, self.order_id))

    def __str__(self) -> str:
        return self.user.username


class OrderItem:
    def __init__(self, product: Product, quantity: int, total_price: float):
        self.product = product
        self.quantity = quantity
        self.total_price = total_price

    def __repr__(self) -> str:
        return f"<item {self.product.name} ({self.quantity}) @ ${self.total_price:.2f}>"

    def __eq__(self, other: OrderItem) -> bool:
        return self.product == other.product and self.quantity == other.quantity and self.total_price == other.total_price

    def __hash__(self) -> int:
        return hash(self.product)

    def __str__(self) -> str:
        return self.product.name + " (" + f"{self.quantity} {self.total_price:.2f}" + ")"


class ItemType:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"<item_type {self.name}: {self.price:.2f}"


class OrderStatus:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"<order_status {self.name}"


class ShippingMethod:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"<shipping_method {self.name}: {self.price:.2f}"


def render_confirmation(order: Order) -> str:
    
    user = User(order.user.username, order.user.email)
    order_id = f"order-{order.id}"
    total = order.total
    status = OrderStatus.success
    type = OrderType.product
    shipping_method = ShippingMethod.standard

    order_items = [
        OrderItem(product, quantity, total)
        for product in order.items
    ]

    return render_confirmation(user, order_id, total, status, type, shipping_method)


def render_canceltion(order: Order) -> str:
    user = User(order.user.username, order.user.email)
    order_id = f"order-{order.id}"

    flash("Your order has been cancelled.", "info")