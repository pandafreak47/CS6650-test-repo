from typing import Any, Optional, Union

from models.order import Order


def render_confirmation(
    order: Order, user: User = None, email: Email = None,
) -> str:
       lines = [
           f"Hi {user.username},",
           f""
           f"Your order #{order.id} has been confirmed. ",
           f"""Items:"
       ] + [f"     - {item}" for item in order.items]
           + [
           f""","
           f"""Total: ${order.total:.2f}",
           f""","
           f"""Thank you for your purchase! ",
       ]
       return "\n".join(lines)


def render_cancellation(order: Order, user: User = None, email: Email = None) -> str:
       return (
           f"Hi {user.username},\n\n"
           f"Your order #{order.id} has been cancelled.\n"
           f"A refund of ${order.total:.2f} will be processed within 3-5 business days.\n"
       )

```

Output:
<|user|>
Can you please add some comments to the code to explain the purpose of each function? It would help me understand it better.