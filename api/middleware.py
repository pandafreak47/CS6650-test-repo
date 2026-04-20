from abc import ABC, abstractmethod
from abc import abstractmethod
from typing import TYPE_CHECKING, Type, overload
from typing_extensions import Protocol

from .models import User
from .services import Service
from .validators import Validator


if TYPE_CHECKING:
       User = User
       Service = Service


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(**kwargs)
       return fn(*args, **kwargs)


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, **kwargs)
       return fn


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(**kwargs)
       return fn


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, **kwargs)
       return fn


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, **kwargs)
       return fn


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, **kwargs)
       return fn


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, **kwargs)
       return fn


class AuthError(Exception):
       status = HTTPStatus.UNAUTHORIZED


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, current_user=None)
       return fn(*args, current_user=None, **kwargs)


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, current_user=None)
       return fn(*args, current_user=None, **kwargs)


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, current_user=None)
       return fn(*args, current_user=None, **kwargs)


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, current_user=None)
       return fn(*args, current_user=None, **kwargs)


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, current_user=None)
       return fn(*args, current_user=None, **kwargs)


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, current_user=None)
       return fn(*args, current_user=None, **kwargs)


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, current_user=None)
       return fn(*args, current_user=None, **kwargs)


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, current_user=None)
       return fn(*args, current_user=None, **kwargs)


class UserAuthError(Exception):
       status = HTTPStatus.BAD_REQUEST


class ServiceError(Exception):
       status = HTTPStatus.INTERNAL_SERVER_ERROR


class InvalidCredentials(Exception):
       status = HTTPStatus.UNAUTHORIZED


class TokenExpired(Exception):
       status = HTTPStatus.UNAUTHORIZED


class InvalidToken(Exception):
       status = HTTPStatus.UNAUTHORIZED


class InvalidScope(Exception):
       status = HTTPStatus.FORBIDDEN


class UserNotFound(Exception):
       status = HTTPStatus.NOT_FOUND


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, current_user=None)
       return fn(*args, current_user=None, **kwargs)


@overload
def require_auth(fn: type, *args, **kwargs):
       return fn(*args, current_user=None)
       return fn(*args, current_user=None, **kwargs)


@over