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

# HTTP Methods
HTTP_POST = "POST"
HTTP_GET = "GET"
HTTP_DELETE = "DELETE"

# Route paths
REGISTER_USER_PATH = f"{HTTP_POST} /users/register"
PLACE_ORDER_PATH = f"{HTTP_POST} /orders"
GET_ORDER_PATH = f"{HTTP_GET} /orders/{{id}}"
CANCEL_ORDER_PATH = f"{HTTP_DELETE} /orders/{{id}}"

# Request body keys
USERNAME_KEY = "username"
EMAIL_KEY = "email"
PASSWORD_KEY = "password"
USER_ID_KEY = "user_id"
ITEMS_KEY = "items"
TOTAL_KEY = "total"

# Response body keys
ID_KEY = "id"
STATUS_KEY = "status"

# HTTP Status Codes
STATUS_CREATED = HTTPStatus.CREATED
STATUS_OK = HTTPStatus.OK

# Default values
DEFAULT_CURRENT_USER = ""


def route(path: str):
    def decorator(fn):
        router[path] = fn
        return fn
    return decorator


@route(REGISTER_USER_PATH)
def register(body: dict) -> tuple[int, dict]:
    user = _users.register(body[USERNAME_KEY], body[EMAIL_KEY], body[PASSWORD_KEY])
    return STATUS_CREATED, {ID_KEY: user.id, USERNAME_KEY: user.username}


@route(PLACE_ORDER_PATH)
@require_auth
def place_order(body: dict, current_user: str = DEFAULT_CURRENT_USER) -> tuple[int, dict]:
    order = _orders.place(body[USER_ID_KEY], body[ITEMS_KEY], body[TOTAL_KEY])
    _emails.notify_order_update(order)
    return STATUS_CREATED, {ID_KEY: order.id, STATUS_KEY: order.status.value}


@route(GET_ORDER_PATH)
@require_auth
def get_order(order_id: int, current_user: str = DEFAULT_CURRENT_USER) -> tuple[int, dict]:
    order = _orders.get(order_id)
    return STATUS_OK, {ID_KEY: order.id, STATUS_KEY: order.status.value, TOTAL_KEY: order.total}


@route(CANCEL_ORDER_PATH)
@require_auth
def cancel_order(order_id: int, current_user: str = DEFAULT_CURRENT_USER) -> tuple[int, dict]:
    order = _orders.cancel(order_id)
    _emails.notify_order_update(order)
    return STATUS_OK, {ID_KEY: order.id, STATUS_KEY: order.status.value}
```