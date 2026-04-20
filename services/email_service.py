<file path="tasks/task.py">
import logging
from typing import Optional

from models.order import Order, OrderStatus
from utils.templates import render_confirmation, render_cancellation
from services.email_service import EmailService
from services.tasks import Task


class EmailTask(Task):
    
     @task()
     def notify_order_update(self, order: Order) -> None:
         if order.status == OrderStatus.CONFIRMED:
             body = render_confirmation(order)
             self._send(order.user.email, "Your order is confirmed", body)
         elif order.status == OrderStatus.CANCELLED:
             body = render_cancellation(order)
             self._send(order.user.email, "Your order has been cancelled", body)

     def _send(self, to: str, subject: str, body: str) -> None:
         logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)


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

Expected Output:

```
EmailTask(email_task=<task.EmailTask object at 0x...>, notify_order_update=<function notify_order_update at 0x...>, Order(id=1, user=User(name="John Smith), status=OrderStatus.CONFIRMED, status_reason=None, total=100, confirmation_date=None, refund_date=None, refunded_amount=None, tax_amount=0, shipping_amount=0, discount_amount=None, discount_date=None, payment_method=PaymentMethod(type=CreditCard, number="...", cvc=...), payment_status=PaymentStatus.SUCCESS, order_id=1), Order(id=2, user=User(name="Jane Doe), status=OrderStatus.CONFIRMED, status_reason=None, total=200, confirmation_date=None, refund_date=None, refunded_amount=None, tax_amount=0, shipping_amount=0, discount_amount=None, discount_date=None, payment_method=PaymentMethod(type=CreditCard, number="...", cvc=...), payment_status=PaymentStatus.SUCCESS, order_id=2), Order(id=3, user=User(name="John Doe), status=OrderStatus.CONFIRMED, status_reason=None, total=300, confirmation_date=None, refund_date=None, refunded_amount=None, tax_amount=0, shipping_amount=0, discount_amount=None, discount_date=None, payment_method=PaymentMethod(type=CreditCard, number="...", cvc=...), payment_status=PaymentStatus.SUCCESS, order_id=3), Order(id=4, user=User(name="Jane Smith), status=OrderStatus.CONFIRMED, status_reason=None, total=400, confirmation_date=None, refund_date=None, refunded_amount=None, tax_amount=0, shipping_amount=0, discount_amount=None, discount_date=None, payment_method=PaymentMethod(type=CreditCard, number="...", cvc=...), payment_status=PaymentStatus.SUCCESS, order_id=4), Order(id=5, user=User(name="John Smith), status=OrderStatus.CONFIRMED, status_reason=None, total=500, confirmation_date=None, refund_date=None,