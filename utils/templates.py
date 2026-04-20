import typing

from typing import Any, Optional, Union

from models.order import Order


def render_confirmation(
    order: Order, user: User = None, email: Email = None
) -> str:
     """
     Render a confirmation message for a specific order.

     :param order: The order object.
     :param user: The user who placed the order.
     :param email: The email address of the user.
     :return: The rendered message.
     """
     lines = [
         f"Hi {user.username},",
         f"""Your order #{order.id} has been confirmed.
         """
         f"""Items:
         - {order.items}",
         f"""Total: ${order.total:.2f}",
         f"""Thank you for your purchase!
         """
     ]
     return "\n".join(lines)


def render_cancellation(
    order: Order, user: User = None, email: Email = None
) -> str:
     """
     Render a cancellation message for a specific order.

     :param order: The order object.
     :param user: The user who placed the order.
     :param email: The email address of the user.
     :return: The rendered message.
     """
     return (
         f"Hi {user.username},\n\n"
         f"Your order #{order.id} has been cancelled. A refund of ${order.total:.2f} will be processed within 3-5 business days. "
     )


def render_notification(
    order: Optional[Order], user: User, email: Optional[Email]
) -> str:
     """
     Render a notification message for an order.

     :param order: The order object, if present.
     :param user: The user who placed the order.
     :param email: The email address of the user.
     :return: The rendered message.
     """
     if not order:
         return ""
     return (
         f"Hi {user.username},\n\n"
         f"Your order #{order.id} has been fulfilled. Thank you for your purchase! "
         f"Your order was fulfilled on {order.created.strftime('%Y-%m-%d')}. "
         f"We hope you have a great time with your purchase. "
         f"We recommend you follow the instructions below for delivery or pick-up:\n\n"
         f"Delivery: https://www.example.com/delivery-instructions\n\n"
         f"Pick-up: https://www.example.com/pickup-instructions\n\n"
     )