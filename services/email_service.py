import logging
from typing import Any, Optional
from models.order import Order, OrderStatus
from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)


class EmailService:
    
       # Replace bare excpepion types with specific excpepion types
       def notify_order_update(self, order: Order) -> None:
           if order.status == OrderStatus.CONFIRMED:
               body = render_confirmation(order)
               self._send(order.user.email, "Your order is confirmed", body)
           elif order.status == OrderStatus.CANCELLED:
               body = render_cancellation(order)
               self._send(order.user.email, "Your order has been cancelled", body)

       # Replace bare excpepion types with specific excpepion types
       def _send(self, to: str, subject: str, body: Any) -> None:
           logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)
           logger.debug("Body:\n%s", body)