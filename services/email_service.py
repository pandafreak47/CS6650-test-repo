```python
import logging
from models.order import Order, OrderStatus
from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)


class EmailService:
    """Simulates sending transactional emails (logs to stdout in dev)."""

    def notify_order_update(self, order: Order) -> None:
        """
        Send an email notification based on the current status of an order.

        Args:
            order: The Order object whose status has been updated.

        Returns:
            None
        """
        if order.status == OrderStatus.CONFIRMED:
            body = render_confirmation(order)
            self._send(order.user.email, "Your order is confirmed", body)
        elif order.status == OrderStatus.CANCELLED:
            body = render_cancellation(order)
            self._send(order.user.email, "Your order has been cancelled", body)

    def _send(self, to: str, subject: str, body: str) -> None:
        """
        Send an email with the given recipient, subject, and body.

        Args:
            to: The email address of the recipient.
            subject: The subject line of the email.
            body: The body content of the email.

        Returns:
            None
        """
        logger.info("EMAIL to=%s subject=%r", to, subject)
        logger.debug("Body:\n%s", body)
```