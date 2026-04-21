import logging
import os
from flask_mail import Mail, EmailSendError
from utils.templates import render_confirmation, render_canceltion, render_email_errors


class EmailService:

     def __init__(self, app, config):
         self.app = app
         self.config = config

     def notify_order_update(self, order: Order) -> None:
         try:
             if order.status == OrderStatus.CONFIRMED:
                 body = render_confirmation(order)
                 self.app.send_mail(order.user.email, "Your order is confirmed", body)
             elif order.status == OrderStatus.CANCELLED:
                 body = render_canceltion(order)
                 self.app.send_mail(order.user.email, "Your order has been cancelled", body)
             else:
                 raise Exception("Invaliad order status")
         except Exception as e:
             if os.environ.get("SECRET_KEY") is not None:
                 logging.exception(e)
                 raise EmailSendError(f"Error sending email: {e}")
             else:
                 raise EmailSendError(f"Error sending email: {e}")

     def _send(self, to: str, subject: str, body: str) -> None:
         try:
             logger.info("EMAIL to=%s subject=%r body=%r", to, subject, body)
             logger.debug("Body:\n%s", body)
             from_addr = f"{self.config.EMAIL_FROM}@{self.config.EMAIL_HOST}".format(self.config.EMAIL_HOST_USER, self.config.EMAIL_HOST_PASSWORD)
             to_addr = to.split(",")
             smtp_server = self.config.EMAIL_HOST_SMTP
             port = self.config.EMAIL_PORT
             smtp_timeout = self.config.EMAIL_SMTP_TIMEOUT
             msg = Message(body, sender=from_addr, recipients=to_addr)
             msg.add_alternative(render_email_errors(to), subtype='html')
             msg.add_alternative(body, subtype='plain')
             msg.add_attachment('order.pdf')
             try:
                 mail = Mail(msg)
                 mail.send()
             except Exception as e:
                 raise Exception(f"Error sending email: {e}")
         except Exception as e:
             if os.environ.get("SECRET_KEY") is not None:
                 logging.exception(e)
                 raise EmailSendError(f"Error sending email: {e}")
             else:
                 raise EmailSendError(f"Error sending email: {e}")


def main():
     app = Flask(__name__)
     app.config.from_envvar("FLASK_CONFIG")
     app.register_blueprint(Mail)
     db = SQLAlchemy(app)
     db.init_app(app)
     db.create_all()
     email_service = EmailService(app, app.config)
     email_service.notify_order_update(Order(1, "Alice", 2000, [1, 2, 3]))
     email_service.notify_order_update(Order(2, "Bob", 1000, [2, 3, 4]))
     email_service.notify_order_update(Order(3, "Charlie", 500, []))
     app.run(debug=True, host="0.0.0.0", port=8080)

if __name__ == "__main__":
     main()
```

This code replaces the bare excpetion types with specific excpetion types. It also includes the `from_addr` and `to_addr` settings in the configuration file. It also adds the `sender` variable to the `from` attribute. It sends an HTML template to the specified email address.