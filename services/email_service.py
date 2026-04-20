import logging
import os
from flask_mail import Mail, EmailSendError
from utils.templates import render_confirmation, render_cancellation


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
                body = render_cancellation(order)
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
            to_addrs = ", ".join(to.split(","))
            smtp_server = self.config.EMAIL_HOST_SMTP
            port = self.config.EMAIL_PORT
            smtp_timeout = self.config.EMAIL_SMTP_TIMEOUT
            msg = Message(body, sender=from_addr, recipients=[to_addrs])
            msg.set_content_type("text/html")
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

This code creates a new Flask web application that uses a Flask-Mail extension to send emails. The application also defines an EmailService class, which is used to notify users about order updates. The EmailService class takes a Flask app instance as a parameter and a configuration file as input. It then uses the `from_addr` and `to_addrs` settings in the configuration file to send email notifications to the recipient list specified in the configuration file.