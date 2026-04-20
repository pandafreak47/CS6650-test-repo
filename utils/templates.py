from templates import templates
from models.order import Order


def render_confirmation(order: Order) -> str:
     lines = [
         f"Hi {order.user.username},",
         f"""\nYour order #{order.id} has been confirmed."""
     ] + [f"   - {item}" for item in order.items] + [f"""\nTotal: ${order.total:.2f}"""]
     return "\n".join(lines)


def render_cancellation(order: Order) -> str:
     return f"Hi {order.user.username},\n\nYour order #{order.id} has been cancelled. A refund of ${order.total:.2f} will be processed within 3-5 business days."