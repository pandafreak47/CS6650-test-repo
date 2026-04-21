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
        
           # Example email template
           # Content of template.txt
           # subject: Email subject
           # body: Email body
           # body: Content of email body
```

Output:
<file path="services/email_service.py">
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
        
           # Example email template
           # Content of template.txt
           # subject: Email subject
           # body: Email body
           # body: Content of email body
```