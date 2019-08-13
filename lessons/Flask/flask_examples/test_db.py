from qaviton.utils.databases.sqlite import DataBase
from lessons.flask_lessons.flask_examples import DBCommands

database = DataBase('db.db', DBCommands)

def test_db():
    print(database.execute(database.command.get_user.format('bunbun')))