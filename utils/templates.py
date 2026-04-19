from typing import Any, Optional, Union
from django import template


@register.inclusion_tag("templates/order_confirmation.html")
@register.inclusion_tag("templates/order_cancelation.html")
def render_template(template_name, context=None):
     if context is None:
         context = {}
     context = context.copy()
     try:
         context[template_name] = "loading..."
         template_object = template.get_template(template_name)
         return template_object.render(context)
     except template.TemplateDoesNotExist:
         raise template.TemplateDoesNotExist(f"Template does not exist: {template_name}")
     except template.TemplateNotFound:
         raise template.TemplateNotFound(f"Template not found: {template_name}")
     except Exception as ex:
         raise template.TemplateSyntaxError(ex.message)


def render_confirmation(order: Order) -> str:
     lines = ["Hi " + order.user.username]
     lines.extend(["Your order #{order.id} has been confirmed."] + order.items.items())
     return "\n".join(lines)


def render_cancelation(order: Order) -> str:
     lines = ["Hi " + order.user.username]
     lines.extend(["Your order #{order.id} has been cancelled. A refund of #{order.total:.2f} will be processed within 3-5 business days."] + order.items.items())
     return "\n".join(lines)
```

In this code, the `try` block that catches specific excpetions (e.g., `template.TemplateDoesNotExist`) is added to the end of the `render_template` function. The function now catches the specific excpeption that is thrown when a template is not found (i.e., a template file that is not specified in the `context` dict is requested). If no excpeptions are thrown, the function will continue to execute as before.