```python
# Example file: templates.py
from typing import List


def render_confirmation(order: List[Order]) -> str:
        lines = [
            f"Hi {order[0].user.username},",
            f"""Your order #{order[0].id} has been confirmed."""
        ] + [f"      - {item}" for item in order[0].items] + [
            f"""Total: ${order[0].total:.2f}"""
        ] + [f"""Thank you for your purchase! """]
        return "\n".join(lines)


def render_cancellation(order: List[Order]) -> str:
        lines = [
            f"Hi {order[0].user.username},",
            f"""Your order #{order[0].id} has been cancelled."""
        ] + [f"      - {item}" for item in order[0].items] + [
            f"""A refund of ${order[0].total:.2f} will be processed within 3-5 business days."""
        ] + [f"Your order was cancelled successfully."]
        return "\n".join(lines)
```

Explaionaion:
- Replace bare excpeption clause with specific excpeption type.
- Move the error-hand