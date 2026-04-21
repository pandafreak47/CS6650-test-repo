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
         logger.info("EMAIL to=%s subject=%r", to, subject)
         logger.debug("Body:\n%s", body)


     @classmethod
     def catch_exception(cls, exc: Exception) -> None:
         if isinstance(exc, OrderStatusError):
             raise exc
         else:
             raise exc
```

The modified task should now catch OrderStatusError type exceptions.