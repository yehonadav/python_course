from lessons.flask_lessons.flask_app.create_db import create
from qaviton.utils import path


db = path.of(__file__)('../../flask_app/database.db')
create(db)
