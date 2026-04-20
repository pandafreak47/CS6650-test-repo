<file path="api/routes.py">
from http import HTTPStatus
from api.middleware import AuthError
from services.user_service import UserService
from services.order_service import OrderService
from services.email_service import EmailService

_users = UserService()
_orders = OrderService()
_email = EmailService()

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
     _email.notify_order_update(order)
     return HTTPStatus.OK, {"id": order.id, "status": order.status.value}


@route("GET /users/{username}")
@require_auth
def get_user(username: str, current_user: str = "") -> tuple[int, dict]:
     user = _users.get(username)
     return HTTPStatus.OK, {"id": user.id, "username": user.username, "email": user.email}


@route("GET /orders/{username}")
@require_auth
def get_orders(username: str, current_user: str = "") -> tuple[int, dict]:
     orders = _orders.get_orders(username)
     return HTTPStatus.OK, {"orders": orders}


@route("GET /orders/{username}/{id}")
@require_auth
def get_order(username: str, id: int, current_user: str = "") -> tuple[int, dict]:
     order = _orders.get(id)
     return HTTPStatus.OK, {"id": order.id, "status": order.status.value, "total": order.total}


@route("POST /orders/place")
@require_auth
def place_order(body: dict, current_user: str = "") -> tuple[int, dict]:
     order = _orders.place(body)
     return HTTPStatus.CREATED, {"id": order.id, "id": order.id, "status": place.value()}


@route("POST /orders")
@requiReq("username")
def route/GET("order/place")

```
<username/user.py>"username")
<service/
username"/"username"
     username/api/post": GET/username" /orders/place/order/"POST/username/"
    place/place/"username/username/service/username/username"
username/" / 1:id"
/username/service/service/ / / GET/service/service/service/service / / / /service/username / / /service /server /user, /username/username /user/user/user/ //username/user / / / /username/user / /username/user/service //user/
//user /service /service / / / /username/username / /service / / / / / /user /service / / / /user / / / / / /user /service / / /service / /user /service / /user / /