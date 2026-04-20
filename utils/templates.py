from typing import Any, Optional, Union

from models.order import Order


def render_confirmation(
    order: Order, user: User = None, email: Email = None,
) -> str:
      lines = [
          f"Hi {user.username},",
          f"""Your order #{order.id} has been confirmed. """
          f"""Items:
         - {order.items}",
          f"""Total: ${order.total:.2f}",
          f"""Thank you for your purchase! """
      ]
      return "\n".join(lines)


def render_cancellation(order: Order, user: User = None, email: Email = None) -> str:
      return (
          f"Hi {user.username},\n\n"
          f"Your order #{order.id} has been cancelled. "
          f"A refund of ${order.total:.2f} will be processed within 3-5 business days. "
      )