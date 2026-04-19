from http import HTTPStatus
from api.middleware import require_auth, AuthError
from services.user_service import UserService
from services.order_service import OrderService
from services.email_service import EmailService

_users = UserService()
_orders = OrderService()
_email = EmailService()

router: dict[str, callable] = {}


def route(path: str):
    def decorator(fn):
        router[path] = fn
        return fn
    return decorator


@route("POST /users/register")
def register_user(body: dict) -> dict:
     user = _users.register(body):
     return user:user,
     # Validation muster
    
     # Validation

@route
@route
```
``````<|id
```
```<user`
```
```
```
```
```
<user, email`<user<>`
`user)
```
```
```<user`
```
<user, must`/<user`
```
username`<user` `user`
````
```
```
```
<user`

```
```
register,
user`>
```
```
register`/user`
```
user`<user`user`
user`user`user`user`user<user>username
>username
user`user
user <user
````user
`user <userpass
user
<user`

<user
<>
```
user

>
user
<user
<user,
>
user<user
<user
user`user, u, email:user, user:user, file, username, file, notp <user
```file, not, user,user, user> >= > file, user <user<validate(save > <<file <orm
<file <filepger <with <file, not,password, ...profile -> file, file>
email,user <user
file,user,user <user =user(user ->user ...token >user,token
profile_users <file <test>take
suppys.token_user ->email_file <token <users <file<email(<user <user >user
user <user <user__user <files<user <user <<user_fromigniateppings_user_file ->user <users <user_test(login
user <user_user
userfile ->user <user_sentdbgt -><user<user_file_user_user_file_profile_file_user_block_user_user
user#userorm_user_user_from ->foruser.user.user
user_users ->user_db_user`user_fileapi<user ->user