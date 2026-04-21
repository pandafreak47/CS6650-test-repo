from typing import Any, Optional, Union

from models.order import Order


def render_confirmation(
      order: Order, user: User = None, email: Email = None,
) -> str:
       lines = [
           f"Hi {user.username},",
           f"",
           f"Your order #{order.id} has been confirmed. ",
           f""",
           f"Items:"
      ] + [f"     - {item}" for item in order.items]
           + [
           f""",
           Total: ${order.total:.2f}",
           f""",
           Thank you for your purchase! ",
       ]
       return "\n".join(lines)


def render_cancellation(order: Order, user: User = None, email: Email = None) -> str:
       return (
           f"Hi {user.username},\n\n"
           f"Your order #{order.id} has been cancelled.\n"
           f"A refund of ${order.total:.2f} will be processed within 3-5 business days.\n"
       )


def render_order_summary(orders: List[Order], total: Optional[float] = None) -> str:
       lines = [f"Order Summary:", f"- Order Id:", "- Order Date:", "- Order Total:"]
       if total is not None:
           lines += [f"- Total:", f"- Order Total:", f"- Total Tax:", f"- Total Subtotal:", f"- Total After Tax:"]
       for order in orders:
           total = total if total is not None else order.total
           lines += [f"- Order #{order.id}:", f"- Items:", "- Total:", f"- Subtotal:", f"- Total:", f"- Tax:", f"- Total:"]
           lines[-1] += f"- {order.total:.2f}"
           lines[-1] += f"- {order.tax:.2f}"
           lines[-1] += f"- {order.total:.2f}"
           lines[-1] += f"- {order.subtotal:.2f}"
           lines[-1] += f"- {order.total:.2f}"
           lines[-1] += f"- Tax: {order.tax:.2f},"
           lines[-1] += f"- Total: {order.total:.2f},"
           lines[-1] += f"- Subtotal: {order.subtotal:.2f},"
           lines[-1] += f"- Total After Tax: {total:.2f},"
       return "\n".join(lines)


def render_order_status(orders: List[Order], total: Optional[float] = None) -> str:
       lines = [f"Order Status:", f"- Order Id:", "- Order Date:", "- Order Status:", "- Order Total:"]
       if total is not None:
           lines += [f"- Total:", f"- Order Total:", f"- Total Tax:", f"- Total Subtotal:", f"- Total After Tax:"]
       for order in orders:
           total = total if total is not None else order.total
           lines += [f"- Order #{order.id}:", f"- Items:", "- Total:", f"- Subtotal:", f"- Total:", f"- Tax:", f"- Total:"]
           lines[-1] += f"- {order.total:.2f}"
           lines[-1] += f"- {order.tax:.2f}"
           lines[-1] += f"- {order.total:.2f}"
           lines[-1] += f"- {order.subtotal:.2f}"
           lines[-1] += f"- {order.total:.2f}"
           lines[-1] += f"- Tax: {order.tax:.2f},"
           lines[-1] += f"- Total: {order.total:.2f},"
           lines[-1] += f"- Subtotal: {order.subtotal:.2f},"
           lines[-1] += f"- Total After Tax: {total:.2f},"
       return "\n".join(lines)


def render_order_items(items: List