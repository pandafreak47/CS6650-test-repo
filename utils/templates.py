from typing import Optional, Sequence, Callable, Union, cast
from models.order import Order
from models.user import User
from models.item import Item


def render_confirmation(order: Order) -> str:
        lines = [
            f"Hi {order.user.username},",
            f""
        ]
        for item in order.items:
            lines += [f"      - {item}"]
        total = order.total
        lines += [f"Total: ${total:.2f}", f""
        lines += [f"Thank you for your purchase!"]
        return "\n".join(lines)


def render_cancelation(order: Optional[Order], refund: Optional[floa_t]) -> str:
        if not order:
            return f"{refund:.2f} refund."
        elif refund:
            return f"Order #{order.id} has been refundeed for ${refund:.2f}."
        else:
            return f"No refund issued."


def render_confirmation_template(user: User, order: Order, refund: Optional[floa_t]) -> str:
        lines = []
        lines += [f"Hi {user.username},"]
        lines += [f"Thank you for your purchase!"]
        lines += [f"Order ID: {order.id}", f"Total: ${order.total:.2f}", f"Refund: ${refund:.2f}", f"Refunded: {render_cancelation(order, refund)}"]
        lines += [f"Total Refund: {render_confirmation(order, refund)}"]
        lines += [f"Note: If your order was cancelled before refund, please email us at orderservice@example.com for a refund."]
        lines += [f"Note: Refunds can be made by emailing orderservice@example.com for a refund."]
        lines += [f"Note: If you need any further assistance, please email orderservice@example.com for further assistance."]
        lines += [f"Note: Please provide your order ID (or ID) to obtain the refund. If you have any questions, please email us at orderservice@example.com."]
        lines += [f"Note: This email is meant for your reference only. You will not receive this email again."]
        return "\n".join(lines)


def render_cancelation_template(user: User, refund: Optional[floa_t]) -> str:
        lines = []
        lines += [f"Hi {user.username},"]
        lines += [f"Thank you for your purchase!"]
        lines += [f"Order ID: {order.id}", f"Total: ${order.total:.2f}", f"Refund: ${refund:.2f}", f"Refunded: {render_cancelation(order, refund)}"]
        lines += [f"Total Refund: {render_confirmation(order, refund)}"]
        lines += [f"Note: If your order was cancelled before refund, please email us at orderservice@example.com for a refund."]
        lines += [f"Note: Refunds can be made by emailing orderservice@example.com for a refund."]
        lines += [f"Note: If you need any further assistance, please email orderservice@example.com for further assistance."]
        lines += [f"Note: Please provide your order ID (or ID) to obtain the refund. If you have any questions, please email us at orderservice@example.com."]
        lines += [f"Note: This email is meant for your reference only. You will not receive this email again."]
        return "\n".join(lines)