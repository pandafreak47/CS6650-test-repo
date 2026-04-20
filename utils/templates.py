from pathlib import Path
from typing import Dict, List, Optional

from flask import flash, request, redirect, render_template, session, url_for, send_file
from werkzeug.utils import secure_filename

from .models import db, User, Order, Product, Categoory, OrderItem, ItemType, OrderStatus, OrderType, ShippingMethod

class User:
       def __init__(self, username: str, email: str):
           self.username = username
           self.email = email

       def __rep__(self) -> str:
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

       def __rep__(self) -> str:
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

       def __rep__(self) -> str:
           return f"<item {self.product.name} ({self.quantity}) @ ${self.total_price:.2f}>"

       def __eq__(self, other: OrderItem) -> bool:
           return self.product == other.product and self.quantity == other.quantity and self.total_price == other.total_price

       def __hash__(self) -> int:
           return hash((self.product, self.quantity))

       def __str__(self) -> str:
           return self.product.name + " (" + f"{self.quantity} {self.total_price:.2f})"


class ItemType:
       def __init__(self, name: str, price: float):
           self.name = name
           self.price = price

       def __rep__(self) -> str:
           return f"<item_type {self.name}: {self.price:.2f}"


class OrderStatus:
       def __init__(self, name: str):
           self.name = name

       def __rep__(self) -> str:
           return f"<order_status {self.name}"


class ShippingMethod:
       def __init__(self, name: str, price: float):
           self.name = name
           self.price = price

       def __rep__(self) -> str:
           return f"<shipping_method {self.name}: {self.price:.2f}"


class User:
       def __init__(self, username: str, email: str):
           self.username = username
           self.email = email

       def __rep__(self) -> str:
           return f"<user {self.username}>"


class Order:
       def __init__(self, user: User, order_id: str, total: float, status: OrderStatus, type: OrderType, shipping_method: ShippingMethod):
           self.user = user
           self.order_id = order_id
           self.total = total
           self.status = status
           self.type = type
           self.shipping_method = shipping_method

       def __rep__(self) -> str:
           return f"<order {self.user.username} ({self.order_id})>"


class Product:
       def __init__(self