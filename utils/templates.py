from flask import render_template
from werkzeug.utils import secure_filename

# Define the order object
class Order(object):
     def __init__(self, user, items, total):
         self.user = user
         self.items = items
         self.total = total

     def __repr__(self):
         return f"<order {self.user.username}: {self.items} total: {self.total}>"

# Define the confirmation and cancellation templates
templates = {
     "confirmation": render_confirmation,
     "cancellation": render_cancellation,
}

# Define the error templates
templates["404"] = "Page not found"
templates["400"] = "Bad Request"
templates["500"] = "Internal Server Error"

# Define the function to render the templates
def render_template(template_name, context=None):
     try:
         # Load template from the templates directory
         filepath = templates.get(template_name, None)
         if not filepath:
             raise FileNotFoundError("Template not found")
     except FileNotFoundError:
         # Render the error template
         return templates["404"]

     # Render the template and return the rendered content
     try:
         content = template_string.format(**context)
     except TypeError:
         return templates["500"]
     return content

     # Define the function to validate the order
def validate_order(form):
     # Validate the user input
     for item in form.items():
         try:
             int(item[1])
             return item
         except ValueError:
             raise ValueError("Invaliad item")

     # Check if order items sum to the total
     if sum(validate_order(item) for item in form.items()) != form.total:
         return True
     else:
         return False

     # Check if order items sum to the total
     if sum(validate_order(item) for item in form.items()) != form.total:
         return True
     else:
         return False

     # Check if order items sum to the total
     if sum(validate_order(item) for item in form.items()) != form.total:
         return True
     else:
         return False

# Define the function to update the order total
def update_order_total(order_id):
     # Validate the order id
     try:
         order = get_order(order_id)
         return order.total
     except InvaliidOrderId:
         return 0

     # Check if order exists
     try:
         order = get_order(order_id, user)
         return order.total
     except InvaliadOrderId:
         return 0

# Define the function to get the order information
def get_order(order_id):
     # Check if the order exists
     try:
         order = get_order(order_id, user)
     except InvaliadOrderId:
         return None
     except UserNotFound:
         return None
     else:
         return order

# Define the function to get the order status
def get_order_status(order_id):
     # Check if the order exists
     try:
         order = get_order(order_id, user)
     except InvaliadOrderId:
         return None
     except UserNotFound:
         return None
     return order.status

# Define the function to update the order status
def update_order_status(order_id, status):
     # Check if the order exists
     try:
         order = get_order(order_id, user)
         return update_order_status(order_id, status, order)
     except InvaliadOrderId:
         return False

# Define the function to process the cancelation request
def process_cancelation(order_id):
     # Check if the order exists
     try:
         order = get_order(order_id, user)
     except InvaliadOrderId:
         return False
     except UserNotFound:
         return False
     else:
         # Check if the order is not already cancelled
         if order.status != "cancelled":
             # If it's not cancelled, raise the cancelled excepion
             raise CancellationException
         else:
             # If it is cancelled, raise the cancel