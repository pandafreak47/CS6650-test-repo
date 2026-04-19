```python
import logging
from models.order import Order, OrderStatus
from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)

# Email subject constants
CONFIRMATION_SUBJECT = "Your order is confirmed"
CANCELLATION_SUBJECT = "Your order has been cancelled"


class EmailService:
    """Simulates sending transactional emails (logs to stdout in dev)."""

    def notify_order_update(self, order: Order) -> None:
        if order.status == OrderStatus.CONFIRMED:
            body = render_confirmation(order)
            self._send(order.user.email, CONFIRMATION_SUBJECT, body)
        elif order.status == OrderStatus.CANCELLED:
            body = render_cancellation(order)
            self._send(order.user.email, CANCELLATION_SUBJECT, body)

    def _send(self, to: str, subject: str, body: str) -> None:
        logger.info("EMAIL to=%s subject=%r", to, subject)
        logger.debug("Body:\n%s", body)
```