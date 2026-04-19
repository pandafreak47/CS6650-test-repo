```python
from models.order import Order


def render_confirmation(order: Order) -> str:
    if not isinstance(order, Order):
        raise TypeError("order must be an instance of Order")
    if order.user is None:
        raise ValueError("order.user cannot be None")
    if order.id is None:
        raise ValueError("order.id cannot be None")
    if order.items is None:
        raise ValueError("order.items cannot be None")
    if order.total is None:
        raise ValueError("order.total cannot be None")
    
    lines = [
        f"Hi {order.user.username},",
        f"",
        f"Your order #{order.id} has been confirmed.",
        f"",
        f"Items:",
    ] + [f"  - {item}" for item in order.items] + [
        f"",
        f"Total: ${order.total:.2f}",
        f"",
        f"Thank you for your purchase!",
    ]
    return "\n".join(lines)


def render_cancellation(order: Order) -> str:
    if not isinstance(order, Order):
        raise TypeError("order must be an instance of Order")
    if order.user is None:
        raise ValueError("order.user cannot be None")
    if order.id is None:
        raise ValueError("order.id cannot be None")
    if order.total is None:
        raise ValueError("order.total cannot be None")
    
    return (
        f"Hi {order.user.username},\n\n"
        f"Your order #{order.id} has been cancelled.\n"
        f"A refund of ${order.total:.2f} will be processed within 3-5 business days.\n"
    )
```