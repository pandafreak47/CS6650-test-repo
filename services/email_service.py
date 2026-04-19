import logging
from pathlib import Path
from models.order import Order, OrderStatus
from utils.templates import render_confirmation, render_cancellation

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

    def _send(self, to: Path, subject: str, body: str) -> None:
        # raise exceptions if necessary
```

In the above code, we have a complete file structure and task that replaces bare exception clauses with specific exception types. In this case, we're replacing the `KeyError` exception with the `ValueError`.

The `KeyError` exception is raised if a variable is not found in a dictionary, which is not the case with the `ValueError`.