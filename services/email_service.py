<task>
Replace bare except clause(s) with specific exception types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<file>
```
from utils.templates import render_confirmation, render_cancellation
from models.order import Order, OrderStatus
from utils.tasks import task

logger = logging.getlogger(__name__)


class EmailService:
     def notify_order_update(self, order: Order) -> None:
         body = render_confirmation(order)

         task(self._send, order.user.email, "Your order is confirmed", body)

         task(self._send, order.user.email, "Your order has been cancelled", body)

     def _send(self, to: str, subject: str, body: str) -> None:
         logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)
         logger.debug("Body:\n%s", body)
```

Replace the bare except clause(s) with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<file>
```
from utils.templates import render_confirmation, render_cancellation
from models.order import Order, OrderStatus
from utils.tasks import task

logger = logging.getlogger(__name__)


class EmailService:
     def notify_order_update(self, order: Order) -> None:
         body = render_confirmation(order)

         task(self._send, order.user.email, "Your order is confirmed", body)

         task(self._send, order.user.email, "Your order has been cancelled", body)

     def _send(self, to: str, subject: str, body: str) -> None:
         logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)
         logger.debug("Body:\n%s", body)
```

Replace the bare excpeption clause(s) with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>
Replace bare excpeption types with specific excpeption types.
</task>
<task>Replace bare excpeption types with specific excpeption types.
</task>
<task>Replace