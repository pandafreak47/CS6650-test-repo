```python
from django.template import Context, loader

from django.http import HttpResponse
from django.template.loader import render_to_string

from models.order import Order

def render_confirmation(order: Order) -> str:
    """
    Renders an HTML template for confirming an order.
    """
    lines = [
        f"Hi {order.user.username},",
        f""",
        f"Your order #{order.id} has been confirmed. ",
        f""",
        f"Items:"
    ] + [f"     - {item}" for item in order.items] + [
        f""",
        f"Total: ${order.total:.2f}",
        f""",
        f"Thank you for your purchase! ",
    ]
    return "\n".join(lines)

def render_cancellation(order: Order) -> str:
    """
    Renders an HTML template for canceling an order.
    """
    return (
        f"Hi {order.user.username},\n\nYour order #{order.id} has been cancelled. ",
        f""",
        f"A refund of ${order.total:.2f} will be processed within 3-5 business days. ",
        f"Thanks for your cooperation.",
    )
```