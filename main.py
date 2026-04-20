from api.routes import router
from api.middleware import AuthError

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
def get_users() -> tuple[int, dict[str, dict]]:
     return HTTPStatus.OK, {"users": {}}


@route("POST /users")
def create_user(body: dict) -> tuple[int, dict]:
     user = _users.create(**body)
     _emails.notify_user_register(user)
     return HTTPStatus.CREATED, {"id": user.id}


@route("POST /orders")
def create_order(body: dict) -> tuple[int, dict]:
     order = _orders.create(**body)
     _emails.notify_order_update(order)
     return HTTPStatus.CREATED, {"id": order.id}


@route("POST /orders/track")
@require_auth
def track_order(body: dict) -> tuple[int, dict]:
     order = _orders.track(body["order_id"])
     return HTTPStatus.OK, {"id": order.id}


@route("POST /orders/resend")
def resend_order(body: dict) -> tuple[int, dict]:
     order_id = body["order_id"]
     order = _orders.get(order_id)
     _orders.resend(order)
     return HTTPStatus.OK, {"id": order_id}


@route("GET /orders")
def get_orders(body: dict) -> tuple[str, dict]:
     return json.load(body)

```

```
```
@route("POST /orders")
```