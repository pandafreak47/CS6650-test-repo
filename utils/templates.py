from django.template import Context, Template
from models.order import Order

def render_confirmation(order: Order) -> str:
        lines = [
            f"Hi {order.user.username},",
            f"""Your order #{order.id} has been confirmed.
             - Items:
               - {order.items}
             - Total: ${order.total:.2f}
             Thank you for your purchase!
           """
        ]
        return "\n".join(lines)

def render_cancellation(order: Order) -> str:
        lines = [
            f"Hi {order.user.username},",
            f"""Your order #{order.id} has been cancelled.
             - A refund of ${order.total:.2f} will be processed within 3-5 business days.
             Thank you for your purchase!
           """
        ]
        return "\n".join(lines)


# Define the logging statement at the beginning of each public function.
def log_message_begin_begin_begin_end_begin_end(msg: str, level: str = "INFO") -> None:
        logger.info(f"Beginning of function: {msg}")


# Define the logging statement at the end of each public function.
def log_message_end_begin_end_begin_begin_end(msg: str, level: str = "INFO") -> None:
        logger.info(f"Ending of function: {msg}")


# Define the logging statement at the beginning of each public function.
def log_message_begin_end_begin_begin_end_begin_end_end(msg: str, level: str = "INFO") -> None:
        logger.info(f"Beginning of function: {msg}")


# Define the logging statement at the end of each public function.
def log_message_end_begin_end_begin_end_begin_end(msg: str, level: str = "INFO") -> None:
        logger.info(f"Ending of function: {msg}")


# Define the logging statement at the beginning of each public function.
def log_message_begin_end_begin_begin_end_begin_end_end(msg: str, level: str = "INFO") -> None:
        logger.info(f"Beginning of function: {msg}")


# Define the logging statement at the end of each public function.
def log_message_end_begin_end_begin_end_end(msg: str, level: str = "INFO") -> None:
        logger.info(f"Ending of function: {msg}")


# Define the logging statement at the beginning of each public function.
def log_message_begin_end_begin(msg: str, level: str = "INFO") -> None:
        logger.info(f"Beginning of function: {msg}")


# Define the logging statement at the end of each public function.
def log_message_end_begin(msg: str, level: str = "INFO") -> None:
        logger.info(f"End of function: {msg}")


# Define the logging statement at the beginning of each public function.
def log_message_begin(msg: str, level: str = "INFO") -> None:
        logger.info(f"Beginning of function: {msg}")


# Define the logging statement at the end of each public function.
def log_message_end(msg: str, level: str = "INFO") -> None:
        logger.info(f"End of function: {msg}")


# Define the logging statement at the beginning of each public function.
def log_message_begin_begin_end(msg: str, level: str = "INFO") -> None:
        logger.info(f"Beginning of function: {msg}")


# Define the logging statement at the end of each public function.
def log_message_begin_end(msg: str, level: str = "INFO") -> None:
        logger.info(f"End of function: {msg}")


# Define the logging statement at the beginning of each public function.
def log_message_begin_end_begin_end_end(msg: str, level: str = "INFO") -> None:
        logger.info(f"Beginning of function: {msg}")


# Define the logging statement at the end of each public function.
def