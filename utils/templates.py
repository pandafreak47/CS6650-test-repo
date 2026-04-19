from typing import List, Dict
from datetime import datetime
from models.order import Order
from models.product import Product
from models.user import User


def render_confirmation(order: Order) -> str:
    lines = [
        f"Hi {order.user.username},",
        f"""Your order #{order.id} has been confirmed.
         - Items:
             - ${", ".join(item.name for item in order.items)}
             - ${", ".join(quantity for product, quantity in order.products)}
             - ${", ".join(price for product, quantity in order.products)}
         - Total: ${order.total:.2f}
         - Total Taxes: ${round(order.total * 0.15, 2)}
         - Delivery: ${round(order.total * 0.05, 2)}
         - Payment: ${round(order.total * 0.01, 2)}
         - Total: ${round(order.total * 0.015, 2)}
         - Thank you for your purchase.
         - Refund: ${order.total * 0.01}
         - Delivery time: ${datetime.now().strftime('%d/%m/%Y')} to ${order.shipping_address.address}
         - Refund time: 5 days from today
         - Delivery time: 5 days from today
         - Refund time: 5 days from today
         - Thank you for your cooperation."""
    ]
    return "\n".join(lines)


def render_cancellation(order: Order) -> str:
    return f"Hi {order.user.username},
     - Order #{order.id} has been cancelled.
     - A refund of ${order.total} will be processed within 3-5 business days.
     - Thank you for cooperating."

```

Expected output:
```
Hi User123,

Your order #234567 has been confirmed.
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
- Delivery time: 90 days from today
- Refund time: 60 days from today
- Delivery time: 60 days from today
- Refund time: 60 days from today
- Thank you for your cooperation.
- Refund: 100 units, 1000.00
- Delivery time: 110 days from today
- Refund time: 70 days from today
- Delivery time: 70 days from today
- Refund time: 70 days from today
- Thank you for your cooperation.
- Refund: 0 units, 0.00
- Delivery time: 0 days from today
- Refund time: 0 days from today
- Delivery time: 0 days from today
- Thank you for cooperation.
- Refund: 0 units, 0.00
- Delivery time: 0 days from today
- Thank you for cooperation.
- Refund: 0 units, 0.00
- Delivery time: 0 days from today