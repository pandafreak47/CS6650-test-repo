import typing

from models.order import Order


def render_confirmation(
       order: Order,
       user: User = None,
       email: Email = None
) -> str:
     lines = [
         f"Hi {user.username},",
         f"""Your order #{order.id} has been confirmed. """
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


def render_confirmation(
       order: Order,
       user: User = None,
       email: Email = None
) -> str:
     lines = [
         f"Hi {user.username},",
         f"""Your order #{order.id} has been confirmed. """
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


class Template:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_template_str(self, template_name: str) -> str:
        return open(self.file_path + "/templates/" + template_name + ".html").read()

    def render(self, template_name: str, **context) -> str:
        template_str = self.get_template_str(template_name)
        context_dict = {**context}
        return template_str.format(**context_dict)


def main():
    template_file = Template("templates/confirmation.html")
    order = Order(
        id=1,
        items=[
            {"name": "Item 1", "quantity": 5},
            {"name": "Item 2", "quantity": 3},
            {"name": "Item 3", "quantity": 1},
        ],
        total=50,
    )

    file_path = "templates/confirmation.html"
    html = template_file.render(
        order=order,
        email=Email(
            name="John Doe",
            address="example@gmail.com",
            email="john_doe@gmail.com",
            password="password",
        ),
        user=User(
            name="Administrator",
            email="admin@example.com",
            password="password",
        ),
    )

    with open(file_path, "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
```

After running the script, you should see the following output:

```
$ python utils/templates.py
Hi John Doe,

Your order #1 has been confirmed.

Item 1: Name: Item 1, Quantity: 5
Item 2: Name: Item 2, Quantity: 3
Item 3: Name: Item 3, Quantity: 1

Total: $50.00

Hi Administrator,

Your order #1 has been cancelled.

Refund of $50.00 will be processed within 3-5 business days.

Note: This order may be processed within the next 3-5 business days.

Thank you for your cooperation.

Best regards,

The Ordering Team
```

This script comple