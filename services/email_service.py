<file path="utils/templates.py">
```python
import logging
from django.conf import settings
from django.template import Context, Template
from django.template.loader import get_template


def _render_template(template_path, context_data=None):
    """Render a template from the given path and context data."""
    template_data = context_data or {}
    template = get_template(template_path)
    return template.render(template_data)


def notify_order_update(order: Order) -> None:
    """Validate order status and send email accordingly."""
    if order.status == OrderStatus.CONFIRMED:
        body = _render_template(settings.EMAIL_CONFIRMATION, {'order': order})
        email = get_template('utils/templates.html').render(
            Context({'body': body, 'order': order})
        )
        logger.info("EMAIL to=%s subject=%r body=%r", order.user.email, email, body)
        # email to user
    elif order.status == OrderStatus.CANCELLED:
        body = _render_template(settings.EMAIL_CANCELATION, {'order': order})
        email = get_template('utils/templates.html').render(
            Context({'body': body, 'order': order})
        )
        logger.info("EMAIL to=%s subject=%r body=%r", order.user.email, email, body)
        # email to user
```