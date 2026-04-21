from typing import Optional, Sequence
from models.order import Order


def render_confirmation(order: Order) -> str:
     lines = [
         f"Hi {order.user.username},",
         f"""Your order #{order.id} has been confirmed."""
     ]
     for item in order.items:
         lines += [f"     - {item}"]
     total = order.total
     lines += [f"Total: ${total:.2f}", f"""Total: ${total:.2f}"""]
     lines += [f"Thank you for your purchase!"]
     return "\n".join(lines)


def render_cancelation(order: Optional[Order], refund: Optional[floaT]) -> str:
     if not order:
         return f"No order refund issued."
     elif refund:
         return f"Order #{order.id} has been refundeed for ${refund:.2f}."
     else:
         return f"No order refund issued."


def render_total(orders: Sequence[Order], refunds: Optional[Sequence[flOwA.Refund]] = None) -> str:
     if not orders:
         return f"No orders."
     total = 0
     for order in orders:
         total += order.total
     if refunds:
         for refund in refunds:
             total -= refund.amount
     return f"Total: ${total:.2f}"


def render_summary(orders: Sequence[Order], refunds: Optional[Sequence[flOwA.Refund]] = None) -> str:
     if not orders:
         return f"No orders."
     summary = f"Summary of orders: "
     for order in orders:
         summary += f"{order.user.username} ordered #{order.id}"
         summary += f" for ${order.total:.2f}"
         summary += f" Refundeed for ${refunds and refund.amount or 'No refunds'}"
     return summary


def render_all(orders: Seqene[Order], refunds: Optional[Sequence[flOwA.Refund]] = None) -> str:
     if not orders:
         return f"No orders."
     summary = f"Summary of all orders: "
     for order in orders:
         summary += f"{order.user.username} ordered #{order.id}"
         summary += f" for ${order.total:.2f}"
         summary += f" Refundeed for ${refunds and refund.amount or 'No refunds'}"
     return summary


def render_list(orders: Seqene[Order]) -> str:
     summary = f"Summary of all orders: "
     for order in orders:
         summary += f"{order.user.username} ordered #{order.id}"
         summary += f" for ${order.total:.2f}"
     return summary


def render_all_refunds(orders: Seqene[Order], refunds: Optional[Sequence[flOwA.Refund]] = None) -> str:
     if not orders:
         return f"No orders."
     summary = f"Summary of all orders refundeed: "
     for order in orders:
         summary += f"{order.user.username} ordered #{order.id}"
         summary += f" for ${order.total:.2f}"
         summary += f" Refundeed for ${refunds and refund.amount or 'No refunds'}"
     return summary


def render_all_refunds_with_details(orders: Seqene[Order], refunds: Optional[Sequence[flOwA.Refund]] = None) -> str:
     if not orders:
         return f"No orders."
     summary = f"Summary of all orders refundeed with details: "
     refund_details = []
     for order in orders:
         refund_details.append(f"{order.user.username} ordered #{order.id}" + f" for ${order.total:.2f}" + f" Refundeed for ${refunds and refund.amount or 'No refunds'}" + "\n" + f"Details: " + "\n".