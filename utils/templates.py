from typing import Any, Optional, Union

from models.order import Order


def render_confirmation(
      order: Order,
      user: User = None,
      email: Email = None,
) -> str:
     lines = [
         f"Hi {user.username},",
         f"""Your order #{order.id} has been confirmed. """
     ]
     for item in order.items:
         lines.append(f"- {item}")
     lines.append("Total: ${order.total:.2f}")
     return "\n".join(lines)


def render_cancellation(
      order: Order,
      user: User = None,
      email: Email = None
) -> str:
     lines = [f"Hi {user.username}, "]
     lines.append("Your order #{order.id} has been cancelled. "
         f"A refund of ${order.total:.2f} will be processed within 3-5 business days.")
     return "\n".join(lines)


def render_order_details(order: Order) -> str:
     lines = []
     lines.append(f"Order ID: {order.id}")
     lines.append(f"Order Date: {order.date_created:Y-m-d}")
     lines.append(f"Shipped To: {order.shipping_address}")
     lines.append(f"Shipped By: {order.shipping_company}")
     lines.append(f"Shipped To: {order.shipment_address}")
     lines.append(f"Shipped By: {order.shipment_company}")
     lines.append(f"Total Cost: ${order.total:.2f}")
     return "\n".join(lines)


def render_order_summary(orders: List[Order]) -> str:
     lines = []
     for order in orders:
         lines.append(f"Order ID: {order.id}")
         lines.append(f"Order Date: {order.date_created:Y-m-d}")
         lines.append(f"Shipped To: {order.shipping_address}")
         lines.append(f"Shipped By: {order.shipping_company}")
         lines.append(f"Shipped To: {order.shipment_address}")
         lines.append(f"Shipped By: {order.shipment_company}")
         lines.append(f"Total Cost: ${order.total:.2f}")
         lines.append(f"Total Order Quantity: {len(order.items)}")
     return "\n".join(lines)


def render_confirm_email(
      order: Order,
      user: User = None,
      email: Email = None
) -> str:
     lines = [f"Hi {user.username},", f"""Your order #{order.id} has been confirmed. """
     ]
     for item in order.items:
         lines.append(f"- {item}")
     lines.append("Total: ${order.total:.2f}")
     lines.append("Order Confirmation")
     lines.append(f"Your order was successfully placed. Please check your email for tracking information.")
     lines.append(f"Thanks for your order!")
     lines.append(f"If you have any questions or concerns, please contact us at {order.email_address}")
     lines.append(f"Best regards,")
     lines.append(f"The Order Team")
     lines.append(f"Order ID: {order.id}")
     lines.append(f"Order Date: {order.date_created:Y-m-d}")
     lines.append(f"Shipped To: {order.shipping_address}")
     lines.append(f"Shipped By: {order.shipping_company}")
     lines.append(f"Shipped To: {order.shipment_address}")
     lines.append(f"Shipped By: {order.shipment_company}")
     lines.append(f"Total Cost: ${order.total:.2f}")
     lines.append(f"Total Order Quantity: {len(order.items)}")
     lines.append("If you received this email, please ignore it.")
     lines.append("If you have any questions or concerns, please contact us at "
         f"{order.