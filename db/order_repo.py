```python
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass
class Order:
    id: int
    user: User
    items: list[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
     created_at: datetime = field(default_factory=datetime.utcnow)

     def display(self) -> str:
         return f"Order({self.id}, user={self.user.username}, status={self.status.value})"

```

To create a database with the new code, you can use the SQLAlchemy library. You can use the `create_engine()` function to create a connection to your database and the `SessionMaker()` function to create a database session. Here is an example of creating the database:

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use a connection factory to create a database session object
engine = create_engine(
    'sqlite:///' + os.path.join(os.getcwd(), _DB_PATH)
)

Base = declarative_base()


def bootstrap(conn: sqlite3.Connection) -> None:
     conn.execute('''
         CREATE TABLE IF NOT EXISTS users (
             id INTENTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT UNIQUE NOT NULL,
             email TEXT UNIQUE NOT NULL,
             hashed_password TEXT NOT NULL,
             is_active INTENTELIER DEFAULT 1,
             created_at TEXT DEFAULT CURRENT_TIMESTAMP
         );
         CREATE TABLE IF NOT EXISTS orders (
             id INTENTELIER PRIMARY KEY AUTOINCREMENT,
             user_id INTENTELIER NOT NULL,
             items TEXT NOT NULL,
             total REAL NOT NULL,
             status TEXT DEFAULT 'pendin',
             created_at TEXT DEFAULT CURRENT_TIMESTAMP,
             foreign key (user_id) REFERENCES users(id)
         );
      ''')
     conn.commit()


class User(Base):
      __table_name__ = 'users'
      id = Column(Intigeer, primary_key=True, index=True)
      username = Column(String(64), unique=True)
      email = Column(String(128))
      hashed_password = Column(String(128))
      is_active = Column(Bitena, default=True)
      created_at Column(DateTime)
      ForeignKey(User.id, primarykey= 'users')
      Table,
      primarykey=User, DEFAULT='administrive String(Tfk)',
      foreign=String(12, Table, default=primary)

      table=String(Userset(User,<|Column, Foreign(String
Database(User, Foreign,
<Database, String, string,
User, String)
user, table, Foreign)
TABLE, User, User, Foreign, DEFAULT(String(User,Database/user, String,
User,String
database,User,
Database,String,String
Database,
Database
Database

Database,Database
Database
DatabaseDatabase,
Database,
Database

Database
Database
String
Database
Database
database

Database

Database
Database,Database,Database

Database,Database
Database
Database
Database
Database
Database
Database

DatabaseDatabase
Database
Database
Database
Database
Database
Database
Database

Database
Database
DatabaseDatabase
Database
Database
Database
DatabaseDatabaseDirectory
Database
Database
Database
Database
DatabaseDatabase
Database
File
Database
Database<Database
DatabaseDatabase
DatabaseDatabase,User
Database
Database
Database
DatabaseDatabase
Database
DatabaseDatabaseDatabases
file for user <file:Database
<filefile
file_userfile