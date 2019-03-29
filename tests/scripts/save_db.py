from qaviton.utils import path
import os
import datetime


db = path.of(__file__)('../../flask_app/database.db')
os.rename(
    db,
    db + '.' +
    str(datetime.datetime.utcnow())
    .replace(" ", "-")
    .replace(":", "")
)
