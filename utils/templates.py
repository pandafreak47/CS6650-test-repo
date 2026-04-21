from typing import Any, Optional, Union

from models.order import Order
from models.product import Product
from models.order_item import OrderItem
from models.user import User


def render_confirmation(
       order: Order, user: User = None, email: Email = None,
) -> str:
        lines = [
            f"Hi {user.username},",
            f""",
            Your order #{order.id} has been confirmed. ",
            f""",
            Items:
            - Order Item:
              - Product:
                - Name: {order.items[0].product.name}
                - Price: {order.items[0].product.price:.2f}
                - Quantity: {order.items[0].quantity:.2f}
                - Total Price: {order.items[0].product.price * order.items[0].quantity:.2f}
            - Total: ${order.total:.2f}",
            f""",
            Total Price: ${order.total:.2f}
            Total Subtotal: ${order.subtotal:.2f}
            Total After Tax: ${order.total:.2f}
            Total Total: ${order.total:.2f}
            Thank you for your purchase! ",
        ]
        return "\n".join(lines)


def render_cancellation(order: Order, user: User = None, email: Email = None) -> str:
        return (
            f"Hi {user.username},\n\n"
            f"Your order #{order.id} has been cancelled.\n"
            f"A refund of ${order.total:.2f} will be processed within 3-5 business days."
        )


def render_order_summary(orders: List[Order], total: Optional[floa] = None) -> str:
        lines = [f"Order Summary:"]
        if total is not None:
            lines += [f"- Order Id:"]
            lines += [f"- Order Date:"]
            lines += [f"- Order Total:"]
            lines += [f"- Total Tax:"]
            lines += [f"- Total Subtotal:"]
            lines += [f"- Total After Tax:"]
        for order in orders:
            total = total if total is not None else order.total
            lines += [f"- Order #{order.id}:", f"- Items:"]
            lines += [f"- Total:"]
            lines += [f"- Subtotal:"]
            lines += [f"- Total:"]
            lines += [f"- Tax: {order.tax:.2f},"]
            lines += [f"- Total: {order.total:.2f},"]
            lines += [f"- Subtotal: {order.subtotal:.2f},"]
            lines += [f"- Total After Tax: {total:.2f},"]
        return "\n".join(lines)


def render_order_items(items: List[OrderItem], total: Optional[floa] = None) -> str:
        lines = [f"Order Items:"]
        lines += [f"- Order Item ID:"]
        lines += [f"- Item Name:"]
        lines += [f"- Product:"]
        lines += [f"- Unit Price:"]
        lines += [f"- Quantity:"]
        lines += [f"- Total Price:"]
        lines += [f"- Total Tax:"]
        lines += [f"- Total Subtotal:"]
        lines += [f"- Total After Tax:"]
        lines += [f"- Total Total:"]
        lines += [f"- Total Subtotal: {total:.2f},"]
        lines += [f"- Total Tax: {total:.2f},"]
        lines += [f"- Total Subtotal: {total:.2f},"]
        lines += [f"- Total After Tax: {total:.2f},"]
        lines += [f"- Total Total: {total:.2f},"]
        lines += [f"- Total Subtotal: {total:.2f},"]
        lines += [f"- Total Tax: {total:.2f},"]
        lines += [f"- Total Subtotal: {total:.2f},"]
        lines += [f"