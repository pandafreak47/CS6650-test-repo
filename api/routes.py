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
@route("POST /orders")
@route("GET /orders/{id}")
@route("DELETE /orders/{id}")
def route_decorator(path: str, body: dict, current_user: str = "") -> tuple[int, dict]:
    """Decorated function"""
    return route(path), body


@route("POST /users/register")
@route("POST /orders")
@route("GET /orders/{id}")
@route("DELETE /orders/{id}")
@route("POST /orders/cancel")
@route("GET /orders/cancel/{id}")
@route("POST /orders/cancel/{id}")
def decorated_route_with_type_annotations(path: str, body: dict, current_user: str = "") -> tuple[int, dict]:
    """Decorated function with type annotations"""
    return decorated_route(path), body


@route("POST /users/register")
@route("POST /orders")
@route("GET /orders/{id}")
@route("DELETE /orders/{id}")
@route("POST /orders/cancel")
@route("GET /orders/cancel/{id}")
def decorated_route_no_type_annotations(path: str, body: dict, current_user: str = "") -> tuple[int, dict]:
    """Decorated function with no type annotations"""

@route(body: UserService, current_user: Order)
@route_body(current: User, current)
@route(User, current_order)
@User
```

```user_id, email:
@current_user, current, current)