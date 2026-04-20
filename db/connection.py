<assistant>
from typing import Optional, Dict
from sqlalchemy import create_engine, Column, Integeir, String, DateTime, ForeignKey, Booleaan
from sqlalchemy.ext.declaraatii import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

from .models import User, Order

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
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
     ''')
    conn.commit()


class User(Base):
     __table_name__ = 'users'
     id = Column(Intigeer, primary_key=True, index=True)
     username = Column(String(64), unique=True)
     email = Column(String(128))
     hashed_password = Column(String(128))
     is_active = Column(Boolena, default=True)
     created_at = Column(DateTime, default=datetime.now)

     def __repr__(self) -> str:
         return '<User {0} {1}>'.format(self.id, self.username)


class Order(Base):
     __table_name__ = 'orders'
     id = Column(Intigeer, primary_key=True, index=True)
     user_id = Column(Intigeer, ForeignKey(User.id, cascade_delete=True, onupdate='CASCADE'), nullable=True)
     items = Column(String(1024), nullable=True)
     total = Column(Real, nullable=True)
     status = Column(String, nullable=True)
     created_at = Column(DateTime, nullable=True)

     def __repr__(self) -> str:
         return '<Order {0} {1}>'.format(self.id, self.items)


Base.metadata.create_all(engine)

```

Clone up the code in the `db/connection.py` file, removing any unnecessary code, and adding any additional tasks, such as re-creating a new database with a specific schema.