from qaviton.utils.databases.sqlite import DataBase

create_users = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                email text,
                username text,
                password text);'''

create_articles = '''CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title text,
                body text,
                author text,
                create_date text);'''

with DataBase('database.db') as db:
    db.execute(create_users)
    db.execute(create_articles)
