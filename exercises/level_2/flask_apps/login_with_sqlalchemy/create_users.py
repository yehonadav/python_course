from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from exercises.level_2.flask_apps.login_with_sqlalchemy.tables import User, Base

engine = create_engine('sqlite:///users.db', echo=True)

# create tables
Base.metadata.create_all(engine)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User(username="admin", password="password")
session.add(user)

user = User(username="python", password="python")
session.add(user)

user = User(username="jumpy", password="python")
session.add(user)

# commit the record the database
session.commit()

session.commit()