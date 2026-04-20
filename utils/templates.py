from typing import Optional, Sequence
from models.order import Order


def render_confirmation(order: Order) -> str:
       lines = [
           f"Hi {order.user.username},",
           f""
       ]
       for item in order.items:
           lines += [f"     - {item}"]
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