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
```

Expected output:
```
Hi User123,

Your order #23456 has been confirmed.
- Items:
    - Product 1: 10 items, 1000 units, 10000000000.00
    - Product 2: 20 items, 2000 units, 20000000000.00
    - Total: 3000 units, 30000000000.00
- Total: 3000 units, 30000000000.00
- Total Taxes: 100 units, 1000.00
- Delivery: 10 units, 100.00
- Payment: 100 units, 1000.00
- Total: 110 units, 1100.00
- Thank you for your purchase.
- Refund: 300 units, 3000.00
- Delivery time: 7 days from today
- Refund time: 14 days from today
- Delivery time: 14 days from today
- Refund time: 14 days from today
- Thank you for your cooperation.
- Refund: 200 units, 2000.00
- Delivery time: 10 days from today
- Refund time: 60 days from today
- Delivery time: 60 days from today
- Refund time: 60 days from today
- Thank you for your cooperation.
- Refund: 100 units, 1000.00
- Delivery time: 15 days from today
- Refund time: 70 days from today
- Delivery time: 70 days from today
- Refund time: 70 days from today
- Thank you for your cooperation.
- Refund: 0 units, 0.00
- Delivery time: 0 days from today
- Refund time: 0.00
- Deliver date: today from today
- Refund date: total_price= 100 units,10000
- order_total=1000_00.00 from total=0.0
- Dearer:00.00_total=00.00 total_0,00 total_0 total_00 total_total_00 total_total000,0 total_00 total_0,00_0 total_0_total_0,00
from_000
0000000000000000o000o00o >o0oo>0oooo0o0o00o00oo0oooo0ooo:o,0oo<oooooooooo0ooooo",o oido_o <oooooo",0oooooiedpiere