import logging
from models.order import Order, OrderStatus
from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)


class EmailService:
    
    def notify_order_update(self, order: Order) -> None:
        if order.status == OrderStatus.CONFIRMED:
            body = render_confirmation(order)
            self._send(order.user.email, "Your order is confirmed", body)
        elif order.status == OrderStatus.CANCELLED:
            body = render_cancellation(order)
            self._send(order.user.email, "Your order has been cancelled", body)

    def _send(self, to: str, subject: str, body: str) -> None:
        logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)

```

2. Run the script with a test task to check that the task completes successfully:

```
python3 task.py email_service notify_order_update Order(user=User(name="John Smith"), id=1)
```

3. Run the script with a task that raises an exception, e.g.:

```
python3 task.py email_service notify_order_update Exception: This is an invalid request.
```

4. Check the output of the script to ensure that the task completes successfully.