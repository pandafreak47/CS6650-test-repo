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


# Define your functions as static methods with the same name and return type.
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


# Define the logging statement at the entry point of the public functions.
def log_message(msg: str, level: str = "INFO") -> None:
      logger.info(msg)


# Define the logging statement at the exit point of the public functions.
def log_message_exit(msg: str, level: str = "INFO") -> None:
      logger.warning(msg)


# Define the logging statement at the entry point of each public function.
# This will only include the file name.
def log_message_entry(msg: str, level: str = "INFO") -> None:
      logger.info(f"Entry point: {msg}")


# Define the logging statement at the exit point of each public function.
# This will only include the file name.
def log_message_exit_entry(msg: str, level: str = "INFO") -> None:
      logger.warning(f"Exit point: {msg}")


# Define the logging statement at the end of each public function.
def log_message_end(msg: str, level: str = "INFO") -> None:
      logger.info(f"End of function: {msg}")


# Define the logging statement at the beginning of each public function.
def log_message_begin(msg: str, level: str = "INFO") -> None:
      logger.info(f"Beginning of function: {msg}")


# Define the logging statement at the end of each public function.
def log_message_end_begin(msg: str, level: str = "INFO") -> None:
      logger.info(f"Ending of function: {msg}")


# Define the logging statement at the beginning of each public function.
def log_message_begin_begin(msg: str, level: str = "INFO") -> None:
      logger.info(f"Beginning of function: {msg}")


# Define the logging statement at the end of each public function.
def log_message_end_begin_end(msg: str, level: str = "INFO") -> None:
      logger.info(f"Ending of function: {msg}")


# Define the logging statement at the beginning of each public function.
def log_message_begin_end(msg: str, level: str = "INFO") -> None:
      logger.info(f"Beginning of function: {msg}")


# Define the logging statement at the end of each public function.
def log_message_end_begin_end(msg: str, level: str = "