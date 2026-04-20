from models.order import Order


def render_confirmation(order: Order) -> str:
     lines = [
         f"Hi {order.user.username},",
         f""",
         Your order #{order.id} has been confirmed.
         Items:
         - #{order.items[0].product_name}: ${order.items[0].price:.2f}
         - #{order.items[1].product_name}: ${order.items[1].price:.2f}
         Total: ${order.total:.2f}
         Thank you for your purchase!
         """
     ]
     return "\n".join(lines)


def render_cancellation(order: Order) -> str:
     return (
         f"Hi {order.user.username},
         Your order #{order.id} has been cancelled.
         A refund of #{order.total:.2f} will be processed within 3-5 business days.
         Thank you for your cooperation.
         """
     )