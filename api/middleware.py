```
from typing import Any, Optional
from flask_restful import Resource, reqparse
from werkzeug.exceptions import BadRequest, Forbidden
from api.utils import db, hashuser, validuser
from api.auth import auth
from api.user_repo import UserRepo

class User(Resource):
    @hashuser
    def get(self, username: str):
        user = db.session.query(UserRepo).get(username)
        if not user:
            return BadRequest(f"User not found: {username}")
        return user

    @validuser
    def put(self, username: str):
        user = db.session.query(UserRepo).get(username)
        if not user:
            return BadRequest(f"User not found: {username}")
        user.update({"password": hashuser(user.password)})
        db.session.commit()
        return user

    @validuser
    def delete(self, username: str):
        user = db.session.query(UserRepo).get(username)
        if not user:
            return BadRequest(f"User not found: {username}")
        db.session.delete(user)
        db.session.commit()
        return None

    @hashuser
    def post(self, username: str):
        user = db.session.query(UserRepo).get(username)
        if not user:
            db.session.add(UserRepo(username, hashuser(user.password)))
            db.session.commit()
            return user
        else:
            return BadRequest(f"User already exists: {username}")

    @validuser
    def delete_password(self, username: str):
        user = db.session.query(UserRepo).get(username)
        if not user:
            return BadRequest(f"User not found: {username}")
        user.password = hashuser(user.password)
        db.session.commit()
        return None
```

</task>

The output will contain the updated file content.