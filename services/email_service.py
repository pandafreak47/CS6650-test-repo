<file path="utils/templates.py">
<file path="tasks/task.py">
```
# Example file: tasks/task.py
from typing import Any

from django.core.mail import send_mail
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext as _


class EmailService(object):
    def notify_order_update(self, order: Any) -> None:
        logger = getattr(self, "logger", None)
        if isinstance(order, Order):
            logger.info("EMAIL to=%s subject=%s body=%s", order.user.email, order.status.name, order.body)
        else:
            raise ImproperlyConfigured(_("Expecting Order instance, got %s", type(order)))

        body = render_confirmation(order)
        subject = _("Your %s has been confirmed", order.status.name)

        send_mail(
            "Welcome to our shop!",
            subject,
            settings.SERVER_EMAIL,
            ["your@email.com"],
            fail_silently=False,
        )

        logger.info("EMAIL to=%s subject=%s body=%s", order.user.email, order.status.name, body)

    def notify_order_cancelled(self, order: Any) -> None:
        logger = getattr(self, "logger", None)
        if isinstance(order, Order):
            logger.info("EMAIL to=%s subject=%s body=%s", order.user.email, order.status.name, order.body)
        else:
            raise ImproperlyConfigured(_("Expecting Order instance, got %s", type(order)))

        body = render_cancellation(order)
        subject = _("Your %s has been cancelled", order.status.name)

        send_mail(
            "Your order has been canceled.",
            subject,
            settings.SERVER_EMAIL,
            ["your@email.com"],
            fail_silently=False,
        )

        logger.info("EMAIL to=%s subject=%s body=%s", order.user.email, order.status.name, body)
```

Recode the template files:
<file path="utils/templates.py">
<file path="tasks/task.py">
```
# Example file: tasks/task.py
from django.core.mail import send_mail
from django.core.exceptions import ImproperlyConfigured


class EmailService(object):
    def notify_order_update(self, order: Any) -> None:
        logger = getattr(self, "logger", None)
        if isinstance(order, Order):
            logger.info("EMAIL to=%s subject=%s body=%s", order.user.email, order.status.name, order.body)
        else:
            raise ImproperlyConfigured(_("Expecting Order instance, got %s", type(order)))

        body = render_confirmation(order)
        subject = _("Your %s has been confirmed", order.status.name)

        send_mail(
            "Welcome to our shop!",
            subject,
            settings.SERVER_EMAIL,
            ["your@email.com"],
            fail_silently=False,
        )

        logger.info("EMAIL to=%s subject=%s body=%s", order.user.email, order.status.name, body)

    def notify_order_cancelled(self, order: Any) -> None:
        logger = getattr(self, "logger", None)
        if isinstance(order, Order):
            logger.info("EMAIL to=%s subject=%s body=%s", order.user.email, order.status.name, order.body)
        else:
            raiseimproperlyconfigured.render_cancelled"
        subject=%s" %s
        subject, message="Your order %s has been cancelled."
        subject, body", cancelled."user",sender/yourself.py>.pybody").send"subject.py"
        "order=y.subject, "user"y.pyleditor"
        """y, "y", "user", "user>.py>".y".csvy>user>.user".py""y