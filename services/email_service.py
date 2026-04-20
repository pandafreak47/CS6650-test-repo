import logging
from models.order import Order, OrderStatus
from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)


class EmailService:
     """Simulate sending transactional emails (logs to stdout in dev)."""

     def notify_order_update(self, order: Order) -> None:
         """Validate order status and send email accordingly."""
         if order.status == OrderStatus.CONFIRMED:
             body = render_confirmation(order)
             self._send(order.user.email, "Your order is confirmed", body)
         elif order.status == OrderStatus.CANCELLED:
             body = render_cancellation(order)
             self._send(order.user.email, "Your order has been cancelled", body)

     def _send(self, to: str, subject: str, body: str) -> None:
         """Validate user email and send email to it."""
         if to and subject and body:
             logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)
             logger.debug("Body:\n%s", body)