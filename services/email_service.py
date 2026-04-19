import logging
from typing import Any
from models.order import Order
from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)


class EmailService:
    
    def __init__(self, client: Any) -> None:
        self.client = client

    def notify_order_update(self, order: Order) -> None:
        if self.validate_order(order, OrderStatus.CONFIRMED):
            body = render_confirmation(order)
            self.client.send_email(order.user.email, "Your order is confirmed", body)
        elif self.validate_order(order, OrderStatus.CANCELLED):
            body = render_cancellation(order)
            self.client.send_email(order.user.email, "Your order has been cancelled", body)

    def _send(self, to: str, subject: str, body: str) -> None:
        logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)

    def validate_order(self, order: Order, expected_status: OrderStatus) -> bool:
        return order.status == expected_status