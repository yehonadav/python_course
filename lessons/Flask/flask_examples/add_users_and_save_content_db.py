from qaviton.utils.databases.sqlite import DataBase
from lessons.flask_lessons.flask_examples import DBCommands

DBCommands.drop_users_table = 'DROP TABLE IF EXISTS users;'
DBCommands.create_users_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT, 
        content TEXT
      );
'''

database = DataBase('db.db', DBCommands)

database.execute(database.command.drop_users_table)
database.execute(database.command.create_users_table)
