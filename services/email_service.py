from utils.templates import render_confirmation, render_cancellation
from email_service import EmailService

logger = logging.getLogger(__name__)


class EmailService:

    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_pass):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_pass = smtp_pass

    def notify_order_update(self, order: Order) -> None:
        if order.status == OrderStatus.CONFIRMED:
            body = render_confirmation(order)
            self.smtp_send(body)
        elif order.status == OrderStatus.CANCELLED:
            body = render_cancellation(order)
            self.smtp_send(body)
        logger.debug("EMAIL to=%s subject=%r", order.user.email, order.subject)

    def smtp_send(self, message) -> None:
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp:
                smtp.starttls()
                smtp.login(self.smtp_user, self.smtp_pass)
                smtp.sendmail(self.smtp_user, self.smtp_user, message)
        except smtplib.smtplib.SMTPServerAccepted as e:
            logger.error("EMAIL could not be sent to %s: %s", self.smtp_server, e)
```

Output:
<|assistant|>
```python
import logging
from utils.templates import render_confirmation, render_cancellation
from email_service import EmailService

logger = logging.getLogger(__name__)


class EmailService:

    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_pass):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_pass = smtp_pass

    def notify_order_update(self, order: Order) -> None:
        if order.status == OrderStatus.CONFIRMED:
            body = render_confirmation(order)
            self.smtp_send(body)
        elif order.status == OrderStatus.CANCELLED:
            body = render_cancellation(order)
            self.smtp_send(body)
        logger.debug("EMAIL to=%s subject=%r", order.user.email, order.subject)

    def smtp_send(self, message) -> None:
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp:
                smtp.starttls()
                smtp.login(self.smtp_user, self.smtp_pass)
                smtp.sendmail(self.smtp_user, self.smtp_user, message)
        except smtplib.smtplib.SMTPServerAccepted as e:
            logger.error("EMAIL could not be sent to %s: %s", self.smtp_server, e)
```