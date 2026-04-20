from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from os import environ
from api.routes import router
from api.middleware import AuthError

_users = UserService()
_orders = OrderService()
_email_service = EmailService()

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
     _email_service.notify_order_update(order)
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
     _email_service.notify_order_update(order)
     return HTTPStatus.OK, {"id": order.id, "status": order.status.value}


@route("GET /users/{username}")
@require_auth
def get_user(username: str, current_user: str = "") -> tuple[str, dict]:
     try:
         user = _users.get(username)
     except ValueError:
         return HTTPStatus.BAD_REQUEST, {"error": "Invalid username"}
     return HTTPStatus.OK, {"id": user.id, "username": user.username, "email": user.email}


@route("GET /orders/{id}")
@require_auth
def get_order_by_id(order_id: int, current_user: str = "") -> tuple[int, dict]:
     order = _orders.get(order_id)
     return HTTPStatus.OK, {"id": order.id, "status": order.status.value, "total": order.total}


@route("POST /orders/{id}/confirm")
@require_auth
def confirm_order(order_id: int, current_user: str = "") -> tuple[str, dict]:
     order = _orders.get(order_id)
     if order is None or order.status.value is None:
         return HTTPStatus.UNEMPTY, {}
     order.confirm()
     return HTTPStatus.NO_CONTENT, {"id": order.id}

     return


@route("GET", "DELETE", "/orders/{id}".replace("users/{username:id}")
     @POST)
     @DELETE)
     GET /users/{username:username}/{"orders/{email}")
     {"GET /username/order" {username/order /user / /users username/get/get/user/ GET /users/POST/{users/email/users/ /email/GET /order"username/confirm" / {username/email/ / email/confirm/email/ / /username/ / / / / / / /server/ // /username/ / / /middle/user / / /username/ /username/users/username/server/ / / /user/ / / / /user / /user / //username

/ / / / / / / / /user / / / / / / / / / / / / / / / / / / / /user / / / / / / / / / / /username / / / / / / / / / / /username / / /username