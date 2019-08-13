from qaviton.utils.databases.sqlite import DataBase

create_users = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                email text,
                username text,
                password text);'''  # username should be UNIQUE

create_articles = '''CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title text,
                body text,
                author text,
                create_date text);'''

def create(db_path):
    with DataBase(db_path) as db:
        db.execute(create_users)
        db.execute(create_articles)


if __name__ == "__main__":
    create('database.db')