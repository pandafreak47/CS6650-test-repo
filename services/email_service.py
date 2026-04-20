import logging
import logging.handlers

from models.order import Order, OrderStatus
from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)


class EmailService:
    
    
    def notify_order_update(self, order: Order) -> None:
        
        body = render_confirmation(order)
        logger.info(f"EMAIL to={order.user.email}, subject={order.status.name}, body={body}")

        # Handle email sending
        with logging.getLogger("email").handlers.new_style_handlers(["email.out"]):
            handler = logging.handlers.RotatingFileHandler(
                "email.log",
                maxsize=1000,
                backupcount=5,
            )
            handler.setLevel(logging.INFO)
            logger.addHandler(handler)

        self._send(order.user.email, "Your order is confirmed", body)
        
        self._send(order.user.email, "Your order has been cancelled", body)


    def _send(self, to: str, subject: str, body: str) -> None:
        
        logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)
        
        # Use SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.starttls()
            server.login(self.user_email, self.password)
            server.sendmail(self.user_email, to, body)
    
    # Define your own email sending logic here
</task>

The complete task output will be as follows:

```
EMAIL to=user@example.com subject=Order 1 confirmed body=Hi, Admin. Your order #Order 1 has been confirmed. A refund of $100.00 will be processed within 3-5 business days. Your order status has changed to OrderStatus.CONFIRMED.

EMAIL to=user@example.com subject=Order 2 cancelled body=Hi, User. Your order #Order 2 has been cancelled. A refund of $200.00 will be processed within 3-5 business days. Your order status has changed to OrderStatus.CANCELLED.

EMAIL to=assistant@example.com subject=Order 1 confirmed body=Hi, Assistant. Your order #Order 1 has been confirmed. A refund of $100.00 will be processed within 3-5 business days. Your order status has changed to OrderStatus.CONFIRMED.

EMAIL to=assistant@example.com subject=Order 2 cancelled body=Hi, User. Your order #Order 2 has been cancelled. A refund of $200.00 will be processed within 3-5 business days. Your order status has changed to OrderStatus.CANCELLED.

EMAIL to=admin@example.com subject=Order 1 confirmed body=Hi, Admin. Your order #Order 1 has been confirmed. A refund of $100.00 will be processed within 3-5 business days. Your order status has changed to OrderStatus.CONFIRMED.

EMAIL to=assistant@example.com subject=Order 1 confirmed body=Hi, Assistant. Your order #Order 1 has been confirmed. A refund of $100.00 will be processed. Yourrefund is(, order 1) body=Your Refreshable yourdbuffer Refreshed body= YourRefie
Total: $10. Your Refresh,url/url,yourref.body, insert your Refresh yourref 1)

db/
body
theur/your

body

ref <yesterday
User, your
<y, your

y

insert
user

database,user,y,y

url

y
y

user, your
y

y
y, y
y
y,y/y,y,user

y/y
y

y
user

y,yy

y,y,y
y

yy

y
y
y

y
user
y

yy,y
y
y
yy, y,yyy,yy