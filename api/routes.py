```python
from http import HTTPStatus
from api.middleware import require_auth, AuthError
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


def _validate_register_body(body: dict) -> None:
    """Validate register request body."""
    if not isinstance(body, dict):
        raise ValueError("Request body must be a JSON object")
    if not body.get("username"):
        raise ValueError("username is required")
    if not body.get("email"):
        raise ValueError("email is required")
    if not body.get("password"):
        raise ValueError("password is required")
    if not isinstance(body["username"], str):
        raise ValueError("username must be a string")
    if not isinstance(body["email"], str):
        raise ValueError("email must be a string")
    if not isinstance(body["password"], str):
        raise ValueError("password must be a string")


def _validate_place_order_body(body: dict) -> None:
    """Validate place order request body."""
    if not isinstance(body, dict):
        raise ValueError("Request body must be a JSON object")
    if "user_id" not in body:
        raise ValueError("user_id is required")
    if "items" not in body:
        raise ValueError("items is required")
    if "total" not in body:
        raise ValueError("total is required")
    if not isinstance(body["user_id"], int) or body["user_id"] <= 0:
        raise ValueError("user_id must be a positive integer")
    if not isinstance(body["items"], list):
        raise ValueError("items must be a list")
    if len(body["items"]) == 0:
        raise ValueError("items list cannot be empty")
    if not isinstance(body["total"], (int, float)):
        raise ValueError("total must be a number")


def _validate_order_id(order_id: int) -> None:
    """Validate order_id parameter."""
    if not isinstance(order_id, int) or order_id <= 0:
        raise ValueError("order_id must be a positive integer")


@route("POST /users/register")
def register(body: dict) -> tuple[int, dict]:
    _validate_register_body(body)
    user = _users.register(body["username"], body["email"], body["password"])
    return HTTPStatus.CREATED, {"id": user.id, "username": user.username}


@route("POST /orders")
@require_auth
def place_order(body: dict, current_user: str = "") -> tuple[int, dict]:
    _validate_place_order_body(body)
    order = _orders.place(body["user_id"], body["items"], body["total"])
    _emails.notify_order_update(order)
    return HTTPStatus.CREATED, {"id": order.id, "status": order.status.value}


@route("GET /orders/{id}")
@require_auth
def get_order(order_id: int, current_user: str = "") -> tuple[int, dict]:
    _validate_order_id(order_id)
    order = _orders.get(order_id)
    return HTTPStatus.OK, {"id": order.id, "status": order.status.value, "total": order.total}


@route("DELETE /orders/{id}")
@require_auth
def cancel_order(order_id: int, current_user: str = "") -> tuple[int, dict]:
    _validate_order_id(order_id)
    order = _orders.cancel(order_id)
    _emails.notify_order_update(order)
    return HTTPStatus.OK, {"id": order.id, "status": order.status.value}
```