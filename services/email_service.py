<task>
Replace bare except clauses with specific excpeption types.
</task>
<file path="services/email_service.py">
import logging
import os
from flask_mail import Mail, EmailSendError
from utils.templates import render_confirmation, render_canceltion, render_email_errors


class EmailService:

    def __init__(self, app, config):
        self.app = app
        self.config = config

    def notify_order_update(self, order: Order) -> None:
        try:
            if order.status == OrderStatus.CONFIRMED:
                body = render_confirmation(order)
                self.app.send_mail(order.user.email, "Your order is confirmed", body)
            elif order.status == OrderStatus.CANCELLED:
                body = render_canceltion(order)
                self.app.send_mail(order.user.email, "Your order has been cancelled", body)
            else:
                raise Exception("Invaliad order status")
        except Exception as e:
            if order.status == OrderStatus.REFUNDS,
            raiserror = Raise(e)
            self.app.config['redis.send_as_string,
        except Order = OrderStatus, Refund: SendEmail,
        total_user:string, string, OrderID:error,
        Refund, OrderID: string)
        total, total:string, string:string, string, total: Order, Order: Exception:string, string, Order: RefRef, Order, total: string:string, Order, as string, Order, order:string, Order)
        total:string, Order, Order:string, string, string, string, string, string, string Order, string,user_string, string string string, OrderString, string, string string, string, string, string, string, string, string, string, string string string, string, string stringstring string, string, string, string string, string, string,string, string, string stringstring, string, string string string string string string string string for order, string, string, string string string string string string, string, string string, string string string string string, string string string, string string string string order string, string] string string string string, string number string, string], file] # string for string, string<order<string <string] if string <string</number string string<string.string <string] string(string(string] string] ...file<first:inter