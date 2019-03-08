from qaviton.utils.databases.sqlite import DataBase
from flask_examples.add_users_and_save_content_db_commands import DBCommands

database = DataBase('db.db', DBCommands)

def test_db():
    print(database.execute(database.command.get_user.format('bunbun')))