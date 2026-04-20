from typing import Any, Optional

from typing import Optional

from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.plain import MIMEPlainText
from email.mime.html import MIMEHTML
from email.mime.media.application import MIMEMedia
from email.mime.media.image import MIMEImage
from email.mime.text import MIMEText

from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)


class EmailService:
    
    def __init__(self, settings):
        self.settings = settings

    def notify_order_update(self, order: Order) -> None:
        """
        Notify the customer about the order update.

        :param order: The Order object
        :type order: Order
        :return: None
        """
        if order.status == OrderStatus.CONFIRMED:
            body = render_confirmation(order)
            self.send(order.user.email, "Your order is confirmed", body)
        elif order.status == OrderStatus.CANCELLED:
            body = render_cancellation(order)
            self.send(order.user.email, "Your order has been cancelled", body)

    def send(self, to: str, subject: str, body: str) -> None:
        """
        Send an email to the specified recipient(s) with the given subject and body.

        :param to: The email address(es) to send the email to
        :type to: str
        :param subject: The subject of the email
        :type subject: str
        :param body: The body of the email
        :type body: str
        :return: None
        """
        # TODO: Add proper email sending functionality
        logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)
        logger.debug("Body:\n%s", body)


```

To complete this task, please add the necessary annotations to the source file:

```python
<file path="models/order.py">

```

The task should be marked as complete after you have added the approprative annotations to the file.