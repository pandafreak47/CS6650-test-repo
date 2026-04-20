```

10. Add a new database table with foreign keys

Add a new database table with foreign keys to the API using Flask.

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declaraatiive import declarative_base
from sqlalchemy.orm import sessionmaker, sessionmaker
from sqlalchemy.sql import select, delete, insert, update
from sqlalchemy.orm.exc

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'

# Create database connection
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

Base = declarative_base()

class User(Base):
      id = Column(Intege