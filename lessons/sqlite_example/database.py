"""
in this example we want to create a user credentials database with:
user_id & password
logger showing connection logs, DB version, errors during fetching & executing
"""

import sqlite3
from lessons.sqlite_example.log import create as create_logger


class Commands:
    create_users_table = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id text,
            password text
        );
    '''
    add_user = 'INSERT INTO users (user_id, password) VALUES (\'{}\', \'{}\');'
    get_users = 'SELECT user_id, password FROM users;'
    get_user_by_user_id = 'SELECT user_id, password FROM users WHERE user_id = \'{}\';'
    get_user_by_id = 'SELECT user_id, password FROM users WHERE id = \'{}\';'''
    get_last_user = 'SELECT user_id, password FROM users ORDER BY ID DESC LIMIT 1'
    drop_table = 'DROP TABLE IF EXISTS {};'


class DataBase:
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    """

    def __init__(self, db_file, log, commands=None):
        """ database connection """
        try:
            self.log = log
            self.log.info('connecting to database')
            self.connection = sqlite3.connect(db_file)
            self.cursor = self.connection.cursor()
            self.log.info('connection success')
            self.log.info('sqlite3 version {}'.format(sqlite3.version))
            if commands is None:
                commands = Commands
            self.command = commands
        except Exception as e:
            self.log.exception(e)
            raise Exception(e)

    def execute(self, command, *args, **kwargs):
        try:
            return self.cursor.execute(command)
        except Exception as e:
            self.log.exception(e)

    def fetch(self, command=None, *args, **kw):
        if command is not None:
            self.execute(command)
        try:
            return self.cursor.fetchall()
        except Exception as e:
            self.log.exception(e)

    def export_from_table_to_file(self, table, file_name, titles, permission='w'):
        try:
            self.cursor.execute("select * from {}".format(table))
            table_list = self.cursor.fetchall()
            with open(file_name, permission) as f:
                f.write(','.join(titles) + '\n')
                for i in table_list:
                    s = []
                    for a in i:
                        s.append(str(a))
                    f.write(','.join(s) + '\n')
        except Exception as e:
            self.log.exception(e)

    def fetch_log(self, *args, **kw):
        rows = self.fetch(*args, **kw)
        if rows is not None:
            for r in rows:
                self.log.info(r)
            return rows


class DataBaseExtention(DataBase):

    # def get_user_credentials(self, user=None, id=None):
    #     users = self.fetch(self.command.get_users)
    #     if user is not None:
    #         for i in users:
    #             if user in i:
    #                 return i
    #     if id is not None:
    #             return users[id][1:]
    #     return users[-1][1:]
    def get_user_credentials(self, user=None, id=None):
        if user is not None:
            user_credentials = self.fetch(self.command.get_user_by_user_id.format(user))
        elif id is not None:
            user_credentials = self.fetch(self.command.get_user_by_id.format(id))
        else:
            user_credentials = self.fetch(self.command.get_last_user)
        if len(user_credentials) > 0:
            return user_credentials[0]


if "__main__" == __name__:
    import os
    log_file = os.path.dirname(os.path.abspath(__file__)) + '\\log.txt'
    db_file = os.path.dirname(os.path.abspath(__file__)) + '\\db.db'
    log = create_logger(log_file=log_file)
    database = DataBaseExtention(db_file, log)

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # database.execute(database.command.drop_table.format('users'))
    # database.execute(database.command.create_users_table)
    # database.execute(database.command.add_user.format('cs0008', '123123a'))
    # database.execute(database.command.add_user.format('af0006', '123123a'))
    # database.execute(database.command.add_user.format('jh0003', '123123a'))
    # database.execute(database.command.add_user.format('kb0004', '123123a'))
    # database.execute(database.command.add_user.format('op0001', '123123a'))
    # database.execute(database.command.add_user.format('gv0001', '123123a'))
    # database.execute(database.command.add_user.format('pm0001', '123123a'))
    # database.execute(database.command.add_user.format('ps0001', '123123a'))
    # database.execute(database.command.add_user.format('qa0000', '123123a'))
    # user_credentials = database.get_user_credentials(id='14')
    # database.connection.commit()
    # database.connection.close()
    # print(user_credentials)


    # create a simple database with websites table that includes (
    #   url: varchar(1024),
    #   popularity_score: integer,
    #   monthly_visitations: integer
    # )

    # database.command.create_websites_table = '''
    #     CREATE TABLE IF NOT EXISTS websites (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         url TEXT,
    #         popularity_score INTEGER,
    #         monthly_visitations INTEGER
    #     )
    # '''
    # database.command.add_website = 'INSERT INTO websites (url, popularity_score, monthly_visitations) VALUES (\'{}\', \'{}\', \'{}\');'
    # database.execute(database.command.create_websites_table)
    # database.execute(database.command.add_website.format('https://www.google.com', 5, 4000000000))
    # database.execute(database.command.add_website.format('https://www.ynet.com', 3, 5000000))
    # database.execute(database.command.add_website.format('https://www.youtube.com', 6, 1300000000))
    # database.execute(database.command.add_website.format('https://www.python.org', 5, 1000000))

    # database.command.get_site = 'SELECT url, popularity_score, monthly_visitations FROM websites WHERE url = \'{}\';'
    # url, popularity, visitations = database.fetch(database.command.get_site.format('https://www.python.org'))[0]
    #
    # print(url, popularity, visitations)

    database.export_from_table_to_file(
        table='websites',
        file_name='exported.csv',
        titles=('id', 'url', 'popularity_score', 'monthly_visitations')
    )

    # database.connection.commit()
    database.connection.close()
