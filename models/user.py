from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    id: int
    username: str
    email: str
    hashed_password: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True

     def display(self) -> str:
         return f"User({self.id}, {self.username})"

class InvalidHashException(Exception):
     def __init__(self, message: str) -> None:
         self.message = message


def generate_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_hash(hashed_password: str, password: str) -> bool:
    return bcrypt.verify(password.encode('utf-8'), hashed_password)


def save_user(user: User) -> None:
    try:
        user.id = next(user.id for _ in range(10))
        user.created_at = datetime.utcnow()
        db.session.add(user)
        db.session.commit()
    except InvalidHashException:
        raise InvalidHashException(f"Invalid password: {password}") from None
    except bcrypt.bscrypt_hash_and_salt_failure:
        raise bcrypt.bscrypt_hash_and_salt_failure from None
    except Exception:
        raise


@save_user
def create_user(username: str, password: str):
    user = User(id=next(user.id for _ in range(10)), username=username, hashed_password=generate_hash(password), created_at=datetime.utcnow())
    db.session.add(user)
    db.session.commit()


@save_user
def update_user(id: int, username: str, password: str):
    user = db.session.query(User).filter(User.id == id).first()
    if user.username != username:
        raise InvalidHashException(f"Invalid username: {username}") from None
    user.hashed_password = generate_hash(password)
    db.session.commit()


@save_user
def delete_user(id: int):
    user = db.session.query(User).filter(User.id == id).first()
    if user is not None:
        db.session.delete(user)
        db.session.commit()
else:
    pass


@save_user
def delete_all_users():
    db.session.query(User).delete()
    db.session.commit()


@save_user
def get_all_users():
    users = db.session.query(User).all()
    return [user.display() for user in users]


@save_user
def get_user(id: int):
    user = db.session.query(User).filter(User.id == id).first()
    return user.display()


@save_user
def get_user_by_username(username: str):
    user = db.session.query(User).filter(User.username == username).first()
    return user.display()


@save_user
def get_users_by_id(ids: [int, list, tuple, set, range, slice]):
    if isinstance(ids, int):
        ids = [ids]
    if isinstance(ids, list):
        ids = tuple(ids)
    if isinstance(ids, tuple) or isinstance(ids, set) or isinstance(ids, range) or isinstance(ids, slice):
        for id in ids:
            try:
                user = db.session.query(User).filter(User.id == id).first()
            except Exception as ex:
                raise ex from None
            return user.display()
    elif isinstance(ids, tuple) and len(ids) == 1:
        for id in ids:
            try:
                user = db.session.query(User).filter(User.id == id).first()
            except Exception as ex:
                raise ex from None
            return user.display()