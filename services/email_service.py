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

To complete the task, ensure that the code is formatted in a consistent style, with appropriate indentation, comments, and variable names. Ensure that the code is well-documented and follows the appropriate coding standards, including following best practices for naming conventions, variable and function naming, and indentation and spacing guidelines.