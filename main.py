Exports only the public API.

import json
from services.user_service import UserService
from services.order_service import OrderService
from services.email_service import EmailService

_users = UserService()
_orders = OrderService()
_emails = EmailService()

router: dict[str, callable] = {}


def route(path: str):
     def decorator(fn):
         router[path] = fn
         return fn
     return decorator


@route("POST /users/register")
def register(body: dict) -> tuple[int, dict]:
     user = _users.register(body["username"], body["email"], body["password"])
     return HTTPStatus.CREATED, {"id": user.id, "username": user.username}


@route("POST /orders")
@require_auth
def place_order(body: dict, current_user: str = "") -> tuple[int, dict]:
     order = _orders.place(body["user_id"], body["items"], body["total"])
     _emails.notify_order_update(order)
     return HTTPStatus.CREATED, {"id": order.id, "status": order.status.value}


@route("GET /orders/{id}")
@require_auth
def get_order(order_id: int, current_user: str = "") -> tuple[int, dict]:
     order = _orders.get(order_id)
     return HTTPStatus.OK, {"id": order.id, "status": order.status.value, "total": order.total}


@route("DELETE /orders/{id}")
@require_auth
def cancel_order(order_id: int, current_user: str = "") -> tuple[int, dict]:
     order = _orders.cancel(order_id)
     _emails.notify_order_update(order)
     return HTTPStatus.OK, {"id": order.id, "status": order.status.value}


@route("GET /users")
def get_users():
     return json.dumps(_users)


@route("GET /orders")
def get_orders():
     return json.dumps(_orders)


@route("GET /orders/{id}")
def get_order(id: int):
     order = _orders.get(id)
     return json.dumps(order)


@route("PUT /orders/{id}")
def modify_order(id: int, body: dict):
     order = _orders.get(id)
     order.set(body)
     return json.dumps(order)


@route("DELETE /orders/{id}")
def cancel_order(id: int):
     order = _orders.cancel(id)
     return json.dumps(order)


@route("POST /orders/shipping")
def add_shipping(id: int, shipping_address: dict):
     order = _orders.get(id)
     order.shipping = shipping_address
     return json.dumps(order)


@route("GET /shipping")
def get_shipping(id: int):
     order = _orders.get(id)
     return json.dumps(order.shipping)


@route("POST /orders/payment")
def add_payment(id: int, payment_method: str, amount: float):
     order = _orders.get(id)
     order.payment = payment_method, amount
     return json.dumps(order)


@route("GET /payments")
def get_payments(id: int):
     order = _orders.get(id)
     return json.dumps(order.payments)


@route("POST /orders/{id}/complete")
def complete_order(id: int):
     order = _orders.get(id)
     order.complete()
     return json.dumps(order)


@route("GET /users/orders")
def get_orders_for_user(username: str):
     users = _users.get_users()
     for user in users:
         orders = [order for order in _orders.get_orders(user.id)]
         orders.sort(key=lambda o: o.total)
         yield json.dumps({"