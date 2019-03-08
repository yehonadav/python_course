# login page save new users
# home page -> user content page, save user content
# import os
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from qaviton.utils.databases.sqlite import DataBase
from flask_examples.add_users_and_save_content_db_commands import DBCommands

app = Flask('my app')


def get_db():
    return DataBase('db.db', DBCommands)


@app.route('/', methods=['GET'])
def login(user=None):
    if user:
        return home(user)
    if not session.get('logged_in'):
        return render_template('login.html')
    session['logged_in'] = False
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def auth_user():
    name = request.form['username']
    with get_db() as database:
        users = database.execute(database.command.get_user.format(name))
        if len(users) == 0:
            database.execute(database.command.create_user.format(name, ''))
        # if not os.path.exists('users\\'+name):
        #     open('users\\'+name, 'w').close()
        session['logged_in'] = False
        database.commit()
        return login(name)


@app.route('/home', methods=['GET'])
def home(user):
    # if not os.path.exists(user): open('users\\'+user, 'w').close()
    # with open('users\\'+user) as db: content = db.read()
    with get_db() as database:
        users = database.execute(database.command.get_user.format(user))
        content = ''
        if len(users) > 0:
            content = users[0][2]
        else:
            database.execute(database.command.create_user.format(user, ''))
        database.commit()
        return render_template('userhome.html', name=user, content=content)


@app.route('/save_user_content', methods=['POST'])
def save_user_content():
    user = request.form['username']
    content = request.form['content']
    # with open('users\\'+user, 'w') as db:
    #     db.write(content)
    with get_db() as database:
        # users = database.execute(database.command.get_user.format(user))
        # if len(users) > 0:
        #     content = users[0][2]
        database.execute(database.command.update_user_content.format(content, user))
        database.commit()
        return content


if __name__ == "__main__":
    app.secret_key = '123'
    app.run(host='0.0.0.0', port=80, debug=True)
