from models.order import Order


def render_confirmation(order: Order) -> str:
       lines = [
           f"Hi {order.user.username},",
           f"""
           Your order #{order.id} has been confirmed.
           Items:
           - {order.items}
           Total: ${order.total:.2f}
           Thank you for your purchase!
           """
       ]
       return "\n".join(lines)


def render_cancellation(order: Order) -> str:
       return (
           f"Hi {order.user.username},\n\n"
           f"Your order #{order.id} has been cancelled. A refund of ${order.total:.2f} will be processed within 3-5 business days."
       )


def __all__ = ["render_confirmation", "render_cancellation"]


def render_confirmation(order: Order) -> str:
       lines = [
           f"Hi {order.user.username},",
           f"""
           Your order #{order.id} has been confirmed.
           Items:
           - {order.items}
           Total: ${order.total:.2f}
           Thank you for your purchase!
           """
       ]
       return "\n".join(lines)


def render_cancellation(order: Order) -> str:
       return (
           f"Hi {order.user.username},\n\n"
           f"Your order #{order.id} has been cancelled. A refund of ${order.total:.2f} will be processed within 3-5 business days."
       )
<file>