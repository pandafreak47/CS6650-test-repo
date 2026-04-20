<task>
Add docstrings to all public functions and methods.
</task>

<task>
Re-write the target file to complete the task. Output ONLY the file content, nothing else:
<file path="db/connection.py">

<assistant>
from typing import Optional, Dict
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
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
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            is_active INTEGER DEFAULT 1,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            items TEXT NOT NULL,
            total REAL NOT NULL,
            status TEXT DEFAULT 'pendin',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    ''')
    conn.commit()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), unique=True)
    email = Column(String(128))
    hashed_password = Column(String(128))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return '<User {0} {1}>'.format(self.id, self.username)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id, cascade_delete=True, onupdate='CASCADE'), nullable=False)
    items = Column(String(1024), nullable=False)
    total = Column(Real, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __repr__(self) -> str:
        return '<Order {0} {1}>'.format(self.id, self.items)


Base.metadata.create_all(engine)

```

Clean up the code in the `db/connection.py` file, removing any unused code or irrelevant comments.