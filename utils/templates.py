```python
from models.order import Order


def _validate_order_for_confirmation(order: Order) -> None:
    """Validate order object for confirmation rendering."""
    if not isinstance(order, Order):
        raise TypeError("order must be an instance of Order")
    if order.user is None:
        raise ValueError("order.user cannot be None")
    if order.id is None:
        raise ValueError("order.id cannot be None")
    if order.items is None:
        raise ValueError("order.items cannot be None")
    if not order.items:
        raise ValueError("order.items cannot be empty")
    if order.total is None:
        raise ValueError("order.total cannot be None")
    if order.total < 0:
        raise ValueError("order.total cannot be negative")


def _validate_order_for_cancellation(order: Order) -> None:
    """Validate order object for cancellation rendering."""
    if not isinstance(order, Order):
        raise TypeError("order must be an instance of Order")
    if order.user is None:
        raise ValueError("order.user cannot be None")
    if order.id is None:
        raise ValueError("order.id cannot be None")
    if order.total is None:
        raise ValueError("order.total cannot be None")
    if order.total < 0:
        raise ValueError("order.total cannot be negative")


def render_confirmation(order: Order) -> str:
    """Render an order confirmation message.
    
    Args:
        order: An Order instance to render confirmation for.
        
    Returns:
        A formatted confirmation message string.
        
    Raises:
        TypeError: If order is not an instance of Order.
        ValueError: If order is missing required fields or has invalid values.
    """
    _validate_order_for_confirmation(order)
    
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
    """Render an order cancellation message.
    
    Args:
        order: An Order instance to render cancellation for.
        
    Returns:
        A formatted cancellation message string.
        
    Raises:
        TypeError: If order is not an instance of Order.
        ValueError: If order is missing required fields or has invalid values.
    """
    _validate_order_for_cancellation(order)
    
    return (
        f"Hi {order.user.username},\n\n"
        f"Your order #{order.id} has been cancelled.\n"
        f"A refund of ${order.total:.2f} will be processed within 3-5 business days.\n"
    )
```