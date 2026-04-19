from models.order import Order


def render_confirmation(order: Order) -> str:
     lines = [
         f"Hi {order.user.username},",
         f"""
         Your order #{order.id} has been confirmed.
         """
     ] + [f"   - {item}" for item in order.items] + [
         f"""
         Total: ${order.total:.2f}"""
     ] + [f"""
         Thank you for your purchase!
         """]
     return "\n".join(lines)


def render_cancellation(order: Order) -> str:
     lines = [
         f"Hi {order.user.username},",
         f"""
         Your order #{order.id} has been cancelled.
         A refund of ${order.total:.2f} will be processed within 3-5 business days.
         """
     ] + [f"   - {item}" for item in order.items] + [
         f"""
         Your order was canceled successfully.
         """
     ]
     return "\n".join(lines)

```

Explanation:
- Replace the bare excpeption clauses with specific excpeption types:
- `raise Exception('Something went wrong')` → `raise Exception(f'Something went wrong')`
- `try: ... except Exception as e:` → `try: ... except Exception as e: ... raise e`

- Rearrange the code to put the error handling logic between the `def` function and its `render_confirmation` and `render_cancellation` calls:
- Move the `try...except` block to the beginning of the file, inside a new `try...except` block.
- Move the error-handling code inside the `try...except` block, and catch the specific excpeption types.
- Rename the `exception_handler` function to `handle_errors`.

- Replace `f"""Hi {order.user.username},` with `f"Hi {order.user.username},"`, as the format is already fixed for the message.
- Replace `f"""Your order #{order.id} has been confirmed. """ with `f"Your order #{order.id} has been confirmed."`, to avoid extra whitespace.
- Replace `f"""Your order #{order.id} has been confirmed. """` with `f"Your order #{order.id} has been confirmed. ", as it's an empty string.
- Replace `f"""Total: ${order.total:.2f}"""` with `f"Total: ${order.total:.2f}"`, to avoid extra whitespace.
- Replace `f"""Your order #{order.id} has been confirmed. """` with `f"Your order #{order.id} has been confirmed. ", as it's an empty string.
- Replace `f"""Thank you for your purchase! """` with `f"Thank you for your purchase! ", as it's an empty string.

```python
# Example file: templates.py
from typing import List


def render_confirmation(order: List[Order]) -> str:
     lines = [
         f"Hi {order[0].user.username},",
         f"""Your order #{order[0].id} has been confirmed.
         """
     ] + [f"   - {item}" for item in order[0].items] + [
         f"""Total: ${order[0].total:.2f}"""
     ] + [f"""Thank you for your purchase! """]
     return "\n".join(lines)


def render_cancellation(order: List[Order]) -> str:
     lines = [
         f"Hi {order[0].user.username},",
         f"""Your order #{order[0].id} has been cancelled.
         A refund of ${order[0].total:.2f} will be processed within 3-5 business days.
         """
     ] + [f"   - {item}" for item in order[0].items] + [
         f"""Your order was canceled successfully.
         """
     ]
     return "\n".join(lines)

```

Explanation:
- Rename the `handle_errors` function to `handle_errors`.
- Move the code handling errors between the `try` and `except` blocks.
- Move the error-hand