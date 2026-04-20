import logging
from models.order import Order
from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)


class EmailService:
    def __init__(self, db: 'Database', user: User, order_id: str, total: float, status: OrderStatus, type: OrderType, shipping_method: ShippingMethod):
        self.db = db
        self.user = user
        self.order_id = order_id
        self.total = total
        self.status = status
        self.type = type
        self.shipping_method = shipping_method

    def send_confirmation_email(self):
        order = self.db.query(Order).filter(Order.id == self.order_id).one()
        order_status = self.db.query(OrderStatus).filter(OrderStatus.id == order.order_status_id).one()
        order_items = [OrderItem(product, quantity, total_price) for product, quantity, total_price in zip(order.items, order.quantity, order.total_price)]
        confirmation_text = render_confirmation(order)
        email_body = render_confirmation(order)
        email_template = render_confirmation(order)

        email_subject = f"Your order ({order_status.name}) #{order_id}"

        email_body_part1 = email_template.replace("{order_items}", ", ".join(order_items))
        email_body_part2 = f"Total cost: ${total:.2f}"
        email_body_part3 = f"Order status: {order_status.name}"
        email_body_part4 = f"Shipping method: {self.shipping_method.name}"
        email_body = f"Subject: {email_subject}\n\n{email_body_part1}\n{email_body_part2}\n{email_body_part3}\n{email_body_part4}\n\n{email_body_part1}"

        with email_template.open("utf-8") as email_template_file:
            with email_template_file.open("utf-8") as email_template_file:
                email_template_file.write(email_body)

        with email_template.open("utf-8") as email_template_file:
            with email_template_file.open("utf-8") as email_template_file:
                email_template_file.write("From: {{ sender_email }} <{{ sender_email }}>")
                email_template_file.write("Subject: Confirmation of order #{{ order_id }}\n\n")
                email_template_file.write("To: {{ recipient_email }} <{{ recipient_email }}>")
                email_template_file.write("\n\n")
                email_template_file.write("Dear {{ recipient_name }},")
                email_template_file.write("\n\n")
                email_template_file.write("Thank you for selecting our product. Your order has been processed. Please check your email for further instructions.")
                email_template_file.write("\n\nBest regards,")
                email_template_file.write("The team of")
                email_template_file.write("[Your Company Name]")
                email_template_file.write(".\n\n")

        with email_template.open("utf-8") as email_template_file:
            email_template_file.write("Subject: Cancellation of order #{{ order_id }}\n\n")
            email_template_file.write("To: {{ recipient_email }} <{{ recipient_email }}>")
            email_template_file.write("\n\n")
            email_template_file.write("Dear {{ recipient_name }},")
            email_template_file.write("\n\n")
            email_template_file.write("Thank you for selecting our product. Unfortunately, your order has been cancelled due to the following reasons:")
            email_template_file.write("\n\n")
            email_template_file.write("Shipping method: {{ shipping_method }}\n")
            email_template_file.write("Product: {{ order_items }}\n\n")
            email