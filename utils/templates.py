```python
from models.order import Order


def render_confirmation(order: Order) -> str:
    """
    Render an order confirmation message as a formatted string.
    
    Args:
        order: The Order object containing order details and user information.
        
    Returns:
        A formatted confirmation message including order ID, items, and total.
    """
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
    """
    Render an order cancellation message as a formatted string.
    
    Args:
        order: The Order object containing order details and user information.
        
    Returns:
        A formatted cancellation message including order ID and refund information.
    """
    return (
        f"Hi {order.user.username},\n\n"
        f"Your order #{order.id} has been cancelled.\n"
        f"A refund of ${order.total:.2f} will be processed within 3-5 business days.\n"
    )
```