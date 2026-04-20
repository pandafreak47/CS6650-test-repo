from typing import Optional

from models.order import Order


def render_confirmation(order: Order, user: User) -> str:
    lines = [
        f"Hi {order.user.username},",
        f"""Your order #{order.id} has been confirmed."""
    ]
    if order.total:
        lines += [f"Total: ${order.total:.2f}"]
    if user.name:
        lines += ["Items:", "   - {item}" for item in order.items]
    total = f"Total: ${order.total:.2f}"
    lines += [f"Total: ${total}", "Thank you for your purchase!", f"A refund of ${order.total:.2f} will be processed within 3-5 business days. - {user.name}", f"Refund #{order.id}", f"If you need to cancel the order, please contact us at {user.email}."]
    return "\n".join(lines)


def render_cancelled(order: Order, user: User) -> str:
    return (
        f"Hi {order.user.username},\n\n"
        f"Your order #{order.id} has been cancelled."
        f"A refund of ${order.total:.2f} will be processed within 3-5 business days. - {user.name}",
        f"Refund #{order.id}",
        f"If you need to cancel the order, please contact us at {user.email}."
    )