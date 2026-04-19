```
from db.user_repo import UserRepo
from models.user import User
from utils.validators import validate_email, validate_username, validate_order_items
from utils.auth import hash_password

_repo = UserRepo()

class UserService:

    def register(self, username: str, email: str, password: str) -> User:
        validate_username(username)
        validate_email(email)

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")

        hashed = hash_password(password)
        return _repo.insert(username, email, hashed)

    def get(self, user_id: int) -> User:
        user = _repo.get_by_id(user_id)
        if not user:
            raise LookupError("User does not exist")
        return user

    def deactivate(self, user_id: int) -> None:
        self.get(user_id).deactivate()

```
</task>
<filepath>
services/user_service.py
```
<user_repo.py">
```
```
```
```
```
```
```
```
""")
```
```
```
`user_user`
```
```
```
user_user`
```
`
```
```
```
`
<utils/db/user`
```
<utils/user`
```
`<user`")
"<user_user"
"ass/user"
```
```
<user>
""
```
```
```
```
```
``````
`user`
```
``` ````````````user```
````````` ``` ``` ``` `
`````` ````````` ``` ``` ``` ``` ``` ``` ``` ``` ``` ``````
```````
``` ``` ``` ``` `````` ``` ``` `user
<user``` ``` ``` ``` `userbase
````<file/userbeattenay <valids<<user``` ```<<<user
```
```````````
```user
```
````````````````<user `user`)``` `````````user````````
```user__task and <user`user
```<file<user``` ````````````user````````` ``` `user```` ```file```""file>file"><file>file_user.file`:``````````````<file:file`user`,<<```file```<file<file```<````````````````````````file><file>`file>>`task`````````<file>`files