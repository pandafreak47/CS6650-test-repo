```python
from http import HTTPStatus
from api.middleware import require_auth, AuthError
from services.user_service import UserService
from services.order_service import OrderService
from services.email_service import EmailService

# Constants
ROUTE_REGISTER = "POST /users/register"
ROUTE_PLACE_ORDER = "POST /orders"
ROUTE_GET_ORDER = "GET /orders/{id}"
ROUTE_CANCEL_ORDER = "DELETE /orders/{id}"

BODY_KEY_USERNAME = "username"
BODY_KEY_EMAIL = "email"
BODY_KEY_PASSWORD = "password"
BODY_KEY_USER_ID = "user_id"
BODY_KEY_ITEMS = "items"
BODY_KEY_TOTAL = "total"

RESPONSE_KEY_ID = "id"
RESPONSE_KEY_USERNAME = "username"
RESPONSE_KEY_STATUS = "status"
RESPONSE_KEY_TOTAL = "total"

DEFAULT_CURRENT_USER = ""

_users = UserService()
_orders = OrderService()
_emails = EmailService()

router: dict[str, callable] = {}


def route(path: str):
    def decorator(fn):
        router[path] = fn
        return fn
    return decorator


@route(ROUTE_REGISTER)
def register(body: dict) -> tuple[int, dict]:
    user = _users.register(
        body[BODY_KEY_USERNAME],
        body[BODY_KEY_EMAIL],
        body[BODY_KEY_PASSWORD]
    )
    return HTTPStatus.CREATED, {
        RESPONSE_KEY_ID: user.id,
        RESPONSE_KEY_USERNAME: user.username
    }


@route(ROUTE_PLACE_ORDER)
@require_auth
def place_order(body: dict, current_user: str = DEFAULT_CURRENT_USER) -> tuple[int, dict]:
    order = _orders.place(
        body[BODY_KEY_USER_ID],
        body[BODY_KEY_ITEMS],
        body[BODY_KEY_TOTAL]
    )
    _emails.notify_order_update(order)
    return HTTPStatus.CREATED, {
        RESPONSE_KEY_ID: order.id,
        RESPONSE_KEY_STATUS: order.status.value
    }


@route(ROUTE_GET_ORDER)
@require_auth
def get_order(order_id: int, current_user: str = DEFAULT_CURRENT_USER) -> tuple[int, dict]:
    order = _orders.get(order_id)
    return HTTPStatus.OK, {
        RESPONSE_KEY_ID: order.id,
        RESPONSE_KEY_STATUS: order.status.value,
        RESPONSE_KEY_TOTAL: order.total
    }


@route(ROUTE_CANCEL_ORDER)
@require_auth
def cancel_order(order_id: int, current_user: str = DEFAULT_CURRENT_USER) -> tuple[int, dict]:
    order = _orders.cancel(order_id)
    _emails.notify_order_update(order)
    return HTTPStatus.OK, {
        RESPONSE_KEY_ID: order.id,
        RESPONSE_KEY_STATUS: order.status.value
    }
```