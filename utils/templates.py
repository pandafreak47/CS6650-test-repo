from typing import Dict, Optional

from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_admin import Admin, BaseAdmin, form, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.helpers import render_field, render_checkbox, render_label, render_error
from models.order import Order


class AdminUsers(Admin):
    users = Admin.get_model('users')
    order_history = Admin.get_model('order_history')

    def configure_admin(self):
        self.add_view(ModelView(self.users), 'users')
        self.add_view(ModelView(self.order_history), 'order_history')


class AdminOrder(Admin):
    users = Admin.get_model('users')
    order = Admin.get_model('order')

    def configure_admin(self):
        self.add_view(ModelView(self.users))
        self.add_view(ModelView(self.order))


class AdminUsersLogin(BaseAdmin):
    @classmethod
    def get_form(cls):
        return AdminUsersLoginForm


class AdminUsersRegister(BaseAdmin):
    @classmethod
    def get_form(cls):
        return AdminUsersRegisterForm


class AdminLogin(LoginManager):
    login_url = '/admin/login'


class AdminLoginForm(form.Form):
    username = form.StringField('Username', [
        validators.Length(min=3, max=30),
        validators.RegularExpression(r'\b[a-zA-Z0-9_-]*\b', message='Only letters, numbers, and underscores are allowed.'),
    ])
    password = form.PasswordField('Password', [
        validators.Length(min=8, max=32),
        validators.RegularExpression(r'\b[a-zA-Z0-9_-]*\b', message='Only letters, numbers, and underscores are allowed.'),
    ])


class AdminRegister(BaseAdmin):
    form = AdminLoginForm


class AdminOrder(Admin):
    users = Admin.get_model('users')
    order = Admin.get_model('order')

    def get_view_function(self, view_name: str) -> function:
        return self.admin_views[view_name]


class AdminOrderForm(form.Form):
    title = form.StringField('Order Title', [
        validators.Length(min=3, max=200),
        validators.RegularExpression(r'\b[a-zA-Z0-9_-]*\b', message='Only letters, numbers, and underscores are allowed.'),
    ])
    total_price = form.NumberField('Total Price', [
        validators.Range(min=0, max=999999, message='Must be a positive integer'),
    ])
    payment_method = form.SelectField('Payment Method', [
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
    ])


class AdminOrderHistory(Admin):
    order = Admin.get_model('order')
    user = Admin.get_model('users')

    def get_view_function(self, view_name: str) -> function:
        return self.admin_views[view_name]


class AdminOrderView(Expose):
    order = Admin.get_model('order')
    user = Admin.get_model('users')

    def get_view_function(self, view_name: str) -> function:
        return self.admin_views[view_name]


class AdminOrderFormHistory(AdminOrderForm):
    id = form.IntegerField(required=True)

    def get_view_function(self, view_name: str) -> function:
        return self.admin_views[view_name]


class AdminOrderHistoryView(Expose):
    order_history = Admin.