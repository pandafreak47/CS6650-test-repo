<task>
Write a complete email service using Flask and Flask-Mail, handling email notifications for orders.

The email notifications should be sent using the `send_mail()` function of the Flask-Mail extension.

The email content should be validated against the model `Order`, and any email addresses not found in the order will be ignored.

The email notification should also include the recipient's email address, as well as the email subject and body.

The email service should have methods to update the status of a given order, and notify the user by sending an email.

The email service should also have methods to send confirmation emails for orders that have been confirmed, and to send cancellation emails for orders that have been cancelled.

The email service should have methods to send notifications for order updates.

The email service should have methods to send error notifications for email sending errors.

Finally, the email service should be documented with proper docstrings for each method.

```python
import logging
from flask import Flask, render_template, request, send_from_directory
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from models import db, User, Order
from utils.templates import render_confirmation, render_cancellation
from utils.utils import get_recaptcha_secret_key

class EmailService:
    """
    Email service to update status of orders, and notify users.
    """

    def notify_order_update(self, order: Order) -> None:
        """
        Notifies the user by sending an email.
        """
        to = order.user.email
        subject = f"Order {order.id} status updated"
        body = render_confirmation(order)

        # Send email
        message = Message(body)
        message.attachments = [
            (secure_filename("order.pdf"), f"Order {order.id}.pdf")
        ]
        message.attach(order.order_receipt)

        send_from_directory("email", f"order_update_{order.id}.html", message)

    def notify_order_cancelled(self, order: Order) -> None:
        """
        Notifies the user by sending an email.
        """
        to = order.user.email
        subject = f"Order {order.id} cancellation"
        body = render_cancellation(order)

        # Send email
        message = Message(body)
        message.attachments = [
            (secure_filename("order.pdf"), f"Order {order.id}.pdf")
        ]
        message.attach(order.order_receipt)

        send_from_directory("email", f"order_cancelled_{order.id}.html", message)

    def send_confirmation(self, order: Order) -> None:
        """
        Notifies the user by sending an email.
        """
        to = order.user.email
        subject = f"Order {order.id} confirmed"
        body = render_confirmation(order)

        # Send email
        message = Message(body)
        message.attachments = [
            (secure_filename("order.pdf"), f"Order {order.id}.pdf")
        ]
        message.attach(order.order_receipt)

        send_from_directory("email", f"order_confirmed_{order.id}.html", message)

    def send_error(self, error: Exception) -> None:
        """
        Notifies the user by sending an email.
        """
        to = get_recipient(error)
        now = datetime.now()
        message = Message(
        {
            'subject_postfix_message_id='.format(now=now)
        }
        'body="'html|templates.send(body=text=render_confirmation=message_confirmation errorsender_content=",user.html")

from="html"
user=post_content='confirmation="post"
from"
error=confirm=post_confirm_post=confirmation>message=confirm=user_confirm=post">confirm_post_confirm_confirm_post.html=confirm=confirm=confirm_confirm=post=confirm_posting=post_post_file.post_post_postifying_post_post_request_post_post_post_post_file_post_post_post_postorm /post /_