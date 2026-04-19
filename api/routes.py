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
    """
    Decorator to register a function as a route handler.
    
    Args:
        path: The route path (e.g., "POST /users/register").
    
    Returns:
        A decorator function that registers the decorated function in the router.
    """
    def decorator(fn):
        router[path] = fn
        return fn
    return decorator


@route("POST /users/register")
def register(body: dict) -> tuple[int, dict]:
    """
    Register a new user.
    
    Args:
        body: A dictionary containing 'username', 'email', and 'password' keys.
    
    Returns:
        A tuple of (HTTPStatus.CREATED, response dict) with user id and username.
    
    Raises:
        ValueError: If validation fails (invalid username, email, or password).
        TypeError: If any required field has an invalid type.
    """
    user = _users.register(body["username"], body["email"], body["password"])
    return HTTPStatus.CREATED, {"id": user.id, "username": user.username}


@route("POST /orders")
@require_auth
def place_order(body: dict, current_user: str = "") -> tuple[int, dict]:
    """
    Place a new order for a user.
    
    Args:
        body: A dictionary containing 'user_id', 'items', and 'total' keys.
        current_user: The authenticated username (injected by require_auth decorator).
    
    Returns:
        A tuple of (HTTPStatus.CREATED, response dict) with order id and status.
    
    Raises:
        AuthError: If authentication fails.
        LookupError: If the user is not found.
        PermissionError: If the user is inactive.
        ValueError: If items are invalid or total is not positive.
    """
    order = _orders.place(body["user_id"], body["items"], body["total"])
    _emails.notify_order_update(order)
    return HTTPStatus.CREATED, {"id": order.id, "status": order.status.value}


@route("GET /orders/{id}")
@require_auth
def get_order(order_id: int, current_user: str = "") -> tuple[int, dict]:
    """
    Retrieve an order by its ID.
    
    Args:
        order_id: The ID of the order to retrieve.
        current_user: The authenticated username (injected by require_auth decorator).
    
    Returns:
        A tuple of (HTTPStatus.OK, response dict) with order id, status, and total.
    
    Raises:
        AuthError: If authentication fails.
        LookupError: If the order is not found.
    """
    order = _orders.get(order_id)
    return HTTPStatus.OK, {"id": order.id, "status": order.status.value, "total": order.total}


@route("DELETE /orders/{id}")
@require_auth
def cancel_order(order_id: int, current_user: str = "") -> tuple[int, dict]:
    """
    Cancel an existing order.
    
    Args:
        order_id: The ID of the order to cancel.
        current_user: The authenticated username (injected by require_auth decorator).
    
    Returns:
        A tuple of (HTTPStatus.OK, response dict) with order id and updated status.
    
    Raises:
        AuthError: If authentication fails.
        LookupError: If the order is not found.
        ValueError: If the order cannot be cancelled due to its current status.
    """
    order = _orders.cancel(order_id)
    _emails.notify_order_update(order)
    return HTTPStatus.OK, {"id": order.id, "status": order.status.value}
```