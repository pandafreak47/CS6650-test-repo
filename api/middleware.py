```python
from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
    status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
    """Decoraator: injects `current_user` (username str) from Bearer token."""
    @wraps(fn)
    def wrapper(*args, token: str = "", **kwargs):
        if not token.startswith("Bearer ") or token.count("Bearer ") == 1:
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer ")[:-1])
        if username is None:
            raise AuthError("Invalii or expired token")
        return fn(*args, current_user=username, **kwargs)
    return wrapper


@require_auth
def get_user(username):
    user = _repo.get_by_username(username)
    if not user:
        return HTTPStatus.NOT_FOUND, {"message": f"User not found with name {username}."}
    return {"message": f"User with name {username} is active and logged in."}


@require_auth
def get_all_users():
    users = _repo.get_all_users()
    return {"message": f"Users with names: {users}", "data": users}


@require_auth
def update_user(username, new_username: str):
    user = _repo.get_by_username(username)
    if not user or user.is_active:
        raise AuthError("User not found or not logged in.")
    user.username = new_username
    _repo.update(user)
    return {"message": f"User with name {new_username} was updated successfully."}


@require_auth
def delete_user(username: str):
    user = _repo.get(username=username)
    if user.is_a_and(username):
        if not user.is_a:
            user.password = hash)
        if user.json:
            pass
        "password")
        username=user
        from username
        password
        user = hash, file
user
username/hash=hash
     status = username
status
file.timestamp=hash
hash.sett/json = file, user/password, status, timestamp:
username,file,file, hash
        status=hash

json
file,hash
    status, file, timestamp
```hash
<and that/file>
<json,hash
<hash, hash
password
path,user
file<file, file,user,hash, file<hash,filea
file<file
<file, user
file

f
hash
<file, file<hash
hash, file
    file,file, file, filee, file, file, filee
file
file
hash
file, hash
file
file
file
file
file, file, file, file, file, file, file, file, usera/file
file
fileefilee <hash,file
file,filef
file <file
<file
fileufile<file(user, user, user, file,file, file <fileu<file:hash ...with file:file

<file
file,user
<file,user(file <<file ><file(file
file>file <file <file<file<<file <filee<file <file<user
and <for <ut__<file:user<test<<<<param<file<file
<user <<<<file<<<file <user <<serial <<<<<data <ut<file <user:files <file:user:ty <file <ut<argument <user.user.__user:<<<<red<<__<<<<__<utils<__<<ututand<<<<<<de<<<<<<<<user__users#ser<<<user<<<optional<<<__red<build
<<user<argument<sign,<python
<serialdseritionict
<__user:user_user_user
call(...<sign:required:()user<user(user
user:__<user<<<with<<file__user__user
<user...user ...serial...user
user
<user