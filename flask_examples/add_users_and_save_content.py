# login page save new users
# home page -> user content page, save user content
import os
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import jsonify


app = Flask('my app')


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
    if not os.path.exists('users\\'+name):
        open('users\\'+name, 'w').close()
    session['logged_in'] = False
    return login(name)


@app.route('/home', methods=['GET'])
def home(user):
    if not os.path.exists(user): open('users\\'+user, 'w').close()
    with open('users\\'+user) as db: content = db.read()
    return render_template('userhome.html', name=user, content=content)


@app.route('/save_user_content', methods=['POST'])
def save_user_content():
    user = request.form['username']
    content = request.form['content']
    with open('users\\'+user, 'w') as db:
        db.write(content)
    return content


if __name__ == "__main__":
    app.secret_key = '123'
    app.run(host='0.0.0.0', port=80, debug=True)
