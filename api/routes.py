```python
import logging
from http import HTTPStatus
from api.middleware import require_auth, AuthError
from services.user_service import UserService
from services.order_service import OrderService
from services.email_service import EmailService

logger = logging.getLogger(__name__)

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
    logger.info("POST /users/register - user registration attempt")
    user = _users.register(body["username"], body["email"], body["password"])
    return HTTPStatus.CREATED, {"id": user.id, "username": user.username}


@route("POST /orders")
@require_auth
def place_order(body: dict, current_user: str = "") -> tuple[int, dict]:
    logger.info("POST /orders - placing order for user_id=%s by %s", body.get("user_id"), current_user)
    order = _orders.place(body["user_id"], body["items"], body["total"])
    _emails.notify_order_update(order)
    return HTTPStatus.CREATED, {"id": order.id, "status": order.status.value}


@route("GET /orders/{id}")
@require_auth
def get_order(order_id: int, current_user: str = "") -> tuple[int, dict]:
    logger.info("GET /orders/%s - retrieving order by %s", order_id, current_user)
    order = _orders.get(order_id)
    return HTTPStatus.OK, {"id": order.id, "status": order.status.value, "total": order.total}


@route("DELETE /orders/{id}")
@require_auth
def cancel_order(order_id: int, current_user: str = "") -> tuple[int, dict]:
    logger.info("DELETE /orders/%s - cancelling order by %s", order_id, current_user)
    order = _orders.cancel(order_id)
    _emails.notify_order_update(order)
    return HTTPStatus.OK, {"id": order.id, "status": order.status.value}
```