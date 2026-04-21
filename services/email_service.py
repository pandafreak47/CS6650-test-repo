import logging
from models.order import Order, OrderStatus
from utils.templates import render_confirmation, render_cancellation
from email_service import EmailService

logger = logging.getLogger(__name__)


class EmailService:
      """Simulate sending transactional emails (logs to stdout in dev)."""

      def notify_order_update(self, order: Order) -> None:
          if order.status == OrderStatus.CONFIRMED:
              body = render_confirmation(order)
              self._send(order.user.email, "Your order is confirmed", body)
          elif order.status == OrderStatus.CANCELLED:
              body = render_cancellation(order)
              self._send(order.user.email, "Your order has been cancelled", body)
          logger.debug("EMAIL to=%s subject=%r", order.user.email, order.subject)

      def _send(self, to: str, subject: str, body: str) -> None:
          logger.info("EMAIL to=%s subject=%r", to, subject)
          logger.debug("Body:\n%s", body)
```

Output:
<|user|>
Can you please add some comments to the code explaining how the `EmailService` class works? I want to understand the logic behind it better.