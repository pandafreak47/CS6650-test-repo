import typing


def render_confirmation(order: typing.Tuple[str, ...]) -> typing.List[str]:
     lines = [
         f"Hi {order[0]},",
         f""",
         f""",
         f"Your order #{order[1] has been confirmed."
         f""",
         f""",
         Items:"
     ] + [f"   - {item}" for item in order[2]] + [
         f""",
         Total: ${order[3] :.2f}
         Thank you for your purchase!"
     ]
     return "\n".join(lines)


def render_cancellation(order: typing.Tuple[str, ...]) -> typing.List[str]:
     return (
         f"Hi {order[0]},
         Your order #{order[1] has been cancelled."
         f""",
         A refund of ${order[2] :.2f} will be processed within 3-5 business days."
     )