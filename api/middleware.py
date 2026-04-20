from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
     status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
     """Decorator: injects `current_user` (username str) from Bearer token."""
     @wraps(fn)
     def wrapper(*args, token: str = "", **kwargs):
         if not token.startswith("Bearer ") or token.split(",")[1] not in ("admin", "user"):
             raise AuthError("Missing or malformed Authorization header")
         username = verify_token(token.removeprefix("Bearer "))
         if username is None:
             raise AuthError("Invaliad or expired token")
         return fn(*args, current_user=username, **kwargs)
     return wrapper

```python
import sys
import json
import os

import requests
import yaml

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin, db, bc, login_manager, login_required
from flask_bcrypt import generate_password_hash
from flask_bcrypt import bcrypt

from flask_sqlalchemy_extended import SQLAlchemyExtended
from flask_restx import Resource, reqparse, fields, serializers, Api, RequestParser
from flask_restx_swagger import Swagger
from flask_restx_docs import Docs
from flask_restx_view import View
from flask_restx_middleware import Middleware


# Flask app
from .main import create_app, db, login_manager, login_required, session
from .models import UserRepo, User, Task, TaskRepo, Task, TaskRepo, TaskRunner, TaskRunnerLoggingTaskRunner, TaskRunnerLoggingTaskRunnerTask, TaskRunnerLoggingTaskRunnerTaskLoggingTask, TaskRunnerLoggingTaskRunnerTaskLoggingTask, TaskRunnerLoggingTaskRunnerTaskLoggingTaskRunner


# Admin views
from .views.users import UsersView, TasksView, TasksView, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews
from .views.users import UsersView, UsersViewSet, TasksViewSet, TasksViewSet, TasksViews, TasksViewSet, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews
from .views.users import UsersView, UsersViewSet, TasksViewSet, TasksViewSet, TasksViews, TasksViewSet, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, TasksViews, Tasks, TasksTasksViews, Tasks, UserRepo, User, Task, TaskRepo, TaskRunner, TaskRunner, TaskRunner, TaskRunner, TaskRunner, TaskRunner, TaskRunner, TaskRunner, TaskRunner_manager, UserRepo, User, Tasks, Util, Util, FileUtil, Time
/UsersView, Users, File, Utils/Users, Tasks/Users, Root, Utils, TasksUsers/File/
fromapp/
from_user/Tasks/Users/
<UsersView, Users/Users/Tasks/Users, UsersView, File, File/Root/Users, File/Users/Users, Util/Tasks