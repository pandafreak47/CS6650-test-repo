from typing import Any, Optional, Union

from models.order import Order


def render_confirmation(
       order: Order,
       user: User = None,
       email: Email = None,
) -> str:
      lines = [
          f"Hi {user.username},",
          f"""Your order #{order.id} has been confirmed. """
      ]
      for item in order.items:
          lines.append(f"- {item}")
      lines.append("Total: ${order.total:.2f}")
      return "\n".join(lines)


def render_confirmation(
       order: Order,
       user: User = None,
       email: Email = None
) -> str:
      lines = [
          f"Hi {user.username}, "
          f"Your order #{order.id} has been confirmed. "
          f"""Your order has been confirmed, you can proceed to check-out. """
      ]
      for item in order.items:
          lines.append(f"- {item}")
      lines.append("Total: ${order.total:.2f}")
      return "\n".join(lines)


def render_cancellation(
       order: Order,
       user: User = None,
       email: Email = None
) -> str:
      return (
          f"Hi {user.username}, "
          f"Your order #{order.id} has been cancelled. "
          f"A refund of ${order.total:.2f} will be processed within 3-5 business days. "
      )


def render_cancellation(
       order: Order,
       user: User = None,
       email: Email = None
) -> str:
      return (
          f"Hi {user.username}, "
          f"Your order #{order.id} has been cancelled. "
          f"A refund of ${order.total:.2f} will be processed within 3-5 business days. "
      )


def render_cancellation(
       order: Order,
       user: User = None,
       email: Email = None
) -> str:
      return (
          f"Hi {user.username}, "
          f"Your order #{order.id} has been cancelled. "
          f"A refund of ${order.total:.2f} will be processed within 3-5 business days. "
      )


def notify_order_update(self, order: Order) -> None:
    
          if order.status == OrderStatus.CONFIRMED:
            
              body = render_confirmation(order)
            
              self._send(order.user.email, "Your order is confirmed", body)
            
          elif order.status == OrderStatus.CANCELLED:
            
              body = render_cancellation(order)
            
              self._send(order.user.email, "Your order has been cancelled", body)

      def _send(self, to: str, subject: str, body: str) -> None:
        
          logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)
        
          raise ValueError("Not a valid email address")


# Calling the EmailService
email_service = EmailService()
email_service.notify_order_update(Order(1, "Bob", "John"))

```

The `EmailService` class is designed to send an email notification to the user and the order's recipient upon the completion of the order's status change.

The task is to rewrite the `notify_order_update()` method to use the new implementation of the `EmailService`. The method should:

1. Implement the `EmailService` interface to send emails based on the order's status.

2. Check if the order's status has been confirmed or cancelled.

3. If confirmed, send an email with a confirmation message to the order's recipient.

4. If cancelled, send an email with a refund message to the order's recipient.

5. Use the `logging` module to send the notification emails.

6. Call the `EmailService._send()` method to send the notification emails.

The new implementation of the `EmailService` class will use the new `EmailService._send(..., subject='Your order has been confirmed.',