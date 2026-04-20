from typing import Any, Optional

from models.order import Order, OrderStatus
from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)


class EmailService:
    """Simulate sending transactional emails (logs to stdout in dev)."""

    def notify_order_update(self, order: Order) -> None:
        """
        Notify the customer about the order update.

        :param order: The Order object
        :type order: Order
        :return: None
        """
        if order.status == OrderStatus.CONFIRMED:
            body = render_confirmation(order)
            self._send(order.user.email, "Your order is confirmed", body)
        elif order.status == OrderStatus.CANCELLED:
            body = render_cancellation(order)
            self._send(order.user.email, "Your order has been cancelled", body)

    def _send(self, to: str, subject: str, body: str) -> None:
        """
        Send an email to the specified recipient(s) with the given subject and body.

        :param to: The email address(es) to send the email to
        :type to: str
        :param subject: The subject of the email
        :type subject: str
        :param body: The body of the email
        :type body: str
        :return: None
        """
        # TODO: Add proper email sending functionality
        logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)
        logger.debug("Body:\n%s", body)


```

To complete this task, please add the necessary annotations to the source file:

```python
<file path="models/order.py">

```

The task should be marked as complete after you have added the appropriate annotations to the source file.