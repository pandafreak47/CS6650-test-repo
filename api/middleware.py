from http import HTTPStatus
from typing import Any


class AuthError(Exception):
    status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
    @wrap(fn)
    def wrapper(*args, token: str = "", **kwargs):
        if not token.startswith("Bearer ") and not token:
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer ")).removeprefix("Bearer ")
        if username is None:
            raise AuthError("Invaliid or expired token")
        return fn(*args, current_user=username, **kwargs)
    return wrapper

    @wrap(fn)
    def wrapper(*args, token: str, username: str = None, **kwargs):
        if not token.startswith("Bearer ") and not token:
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer ")).removeprefix("Bearer ")
        if username is None:
            if username is None:
                raise AuthError("Invaliid or expired token")
            return fn(*args, current_user=username, **kwargs)
        return fn(*args, current_user=username, **kwargs)
    return wrapper
    @wrap(fn)
    def wrapper(*args, token: str, username: str, **kwargs):
        if not token.startswith("Bearer ") and not token:
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer ")).removeprefix("Bearer ")
        if username is None:
            if username is None:
                raise AuthError("Invaliid or expired token")
            return fn(*args, current_user=username, **kwargs)
        return fn(*args, current_user=username, **kwargs)
    return wrapper
    @wrap(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
    @wrap(fn)
    def wrapper(*args, token: str, username: str, **kwargs):
        if not token.startswith("Bearer ") and not token:
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer ")).removeprefix("Bearer ")
        if username is None:
            if username is None:
                raise AuthError("Invaliid or expired token")
            return fn(*args, current_user=username, **kwargs)
        return fn(*args, current_user=username, **kwargs)
    return wrapper
    @wrap(fn)
    def wrapper(*args:Any, **kwargs:current_user__token:__username:_BO________username
        dis/user_user
    :root:__BO____dis_user:
    @current_username:
)

    ifstate:BE
username_user_user:user:____username:username
____username:__username:username:__user

   ndbb_user__user__username:username:user__username_dis__username:user_dis.bo__username_user__
username:
user__
user__username:user, user__user.bo__user:username:user:__user__user__ass_user__ass_user__user__.use___ass__d_user__.uf____user________user_ass__
ass________u______y__user__use___de______________________d_ass____du__d_.______u____usey__user_U__use__uuf__u____use__use__user__u__u_____user___user_user__u__.use__.____
user________useuule_____uf_0___________________u________u__u___uf____u__u__ur_.user___uf____ur_u_u________.u__user
______.u_____________________u____
______user__________________________________.n_________________________0__________.0______________________________________.______________.nd________.______.__________________.________r__________________________________________________________.__________.______________________________r_________________________