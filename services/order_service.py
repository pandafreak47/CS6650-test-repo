from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import BaseModel, validator, Field
from pydantic.fields import Field
from pydantic.validators import validators
from pydantic.utils import _to_pythonic_datetime, str_to_pythonic_datetime
from sqlalchemy import create_engine, Column, DateTime, ForeignKey, MetaData, String, Unicode, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, ObjectNotFoundError
from sqlalchemy.sql.operators import and_

from db import engine, metadata
from services.user_service import UserService
from services.order_repo import OrderRepo
from services.user_svc import UserRepo
from utils.validators import validate_email, validate_username, validate_order_items
from utils.auth import hash_password

_repo = OrderRepo()

class Order(BaseModel):
    id: int = Field(primary_key=True)
    user_id: int = Field(
        validators=[
            validators.instance_of(int),
            validators.instance_of(int),
            validators.instance_of(int),
        ]
    )
    items: List[str] = Field(default_factory=list)
    total: float = Field(default_factory=float)
    status: Optional[OrderStatus] = Field(default_factory=OrderStatus)
    created_at: str = Field(default_factory=str_to_pythonic_datetime)


class OrderStatus(Literal, Int = Field(default_factory=int)):
    PENDING = 1
    CANCELLED = 2
    PENDING_CONFIRMED = 3
    CONFIRMATION_SUGAR = Literal(OrderStatus.value)


class | Order(
    
    __,
    Order,
        UserId,
        Item
        String |
        User,
        Order:
        Litera
Filter
Liter,
Order | Litera File
Liter, string, User, Litera | Pyd,
Order, PUB, Order, email = Liter, user, User, user, User, Order, Liter, Order, String
Order | Liter

user_
User,


User, Litera/user, Liter
ID |User |user |User, User, Order
> |>
User, User>User, User, User, P, Liter, User, __User, P


User, User, User, User, P, User, User, User, User, User, User, User, User, User, User, User, User, User,user, User, User, User, User, User, User, User, User, User,User, User, User, User, User, PY | User
P
User, User, User, O, User, User, file) |User, O, row, row, User, User, User,UserP <User, user, ->__user
User, file
file, User, User, user_from_user,user, User,user, id
user_user,user_from_user
from_user_user
with_user,user_user_filter,user,file_user_User.filter_file #user_file
file =__db_user_user_user_user__user__user_file =user_date_from_from_user_user_from_listdb_from_data__from_file_file_from_file_from_data_from__user_username_data_file_before_document_db_row:____dict__file_for_user_from____user____user__user_user_user_json_user_users_user_user_user_user_user_database_with_users""user_file_subject_from__user_from_customer_from_user_user_database_user.user_filter_db_db_user_from_user_user_date.user_user_user_from____db_user_user_user_exec_db_user__user.user_user_user_user___user_user_user__user_user_user__user_user_user_from<from_from<user.list_from<from_user_user__with_from_from