class EmailService:
       """Simulate sending transactional emails (logs to stdout in dev)."""

       def notify_order_update(self, order: Order) -> None:
           if order.status == OrderStatus.CONFIRMED:
               body = render_confirmation(order)
               self._send(order.user.email, "Your order is confirmed", body)
           elif order.status == OrderStatus.CANCELLED:
               body = render_cancellation(order)
               self._send(order.user.email, "Your order has been cancelled", body)

       def _send(self, to: str, subject: str, body: str) -> None:
           logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)
           logger.debug("Body:\n%s", body)