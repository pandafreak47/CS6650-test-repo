import logging
import os
from pathlib import Path

from models.order import Order, OrderStatus
from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)


class EmailService:
    """Simulate sending transactional emails (logs to stdout in dev)."""

    def notify_order_update(self, order: Order) -> None:
        if order.status == OrderStatus.CONFIRMED:
            body = render_confirmation(order)
            os.system(f"python {os.path.join(os.path.dirname(__file__), 'services', 'email_service.py')} " f"--user {order.user.username} --subject 'Your order is confirmed' --body '{body}'")
        elif order.status == OrderStatus.CANCELLED:
            body = render_cancellation(order)
            os.system(f"python {os.path.join(os.path.dirname(__file__), 'services', 'email_service.py')} " f"--user {order.user.username} --subject 'Your order has been cancelled' --body '{body}'")

    @classmethod
    def _send(cls, to: str, subject: str, body: str) -> None:
        logger.info("EMAIL to=%s subject=%r", to, subject)
        logger.debug("Body:\n%s", body)

    def __init__(self, user_dir: Path, email_server: str, email_from: str, email_from_name: str) -> None:
        self.user_dir = user_dir
        self.email_server = email_server
        self.email_from = email_from
        self.email_from_name = email_from_name

    def __call__(self, order: Order) -> None:
        body = render_confirmation(order)
        os.system(f"python {os.path.join(os.path.dirname(__file__), 'services', 'email_service.py')} --user {order.user.username} --subject 'Your order is confirmed' --body '{body}'")
        body = render_cancellation(order)
        os.system(f"python {os.path.join(os.path.dirname(__file__), 'services', 'email_service.py')} --user {order.user.username} --subject 'Your order has been cancelled' --body '{body}'")