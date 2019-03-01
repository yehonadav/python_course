import json
from flask import Flask, render_template, request


app = Flask('simple login app')


@app.route('/home', methods=['GET'])
def home(message=''):
    return render_template('login_or_register.html', message=message)


@app.route('/register', methods=['POST'])
def register():
    # get username & password from request
    username = request.form['username']
    password = request.form['password']

    # compare with database
    with open('users.json') as f:
        users = json.load(f)
    if username in users:
        return home(message='user already exist')

    # add to database if not exist
    users[username] = {'password': password}
    with open('users.json', 'w') as f:
        json.dump(users, f)

    # return response
    return home(message='register success')


@app.route('/login', methods=['POST'])
def login():
    # get username & password from request
    username = request.form['username']
    password = request.form['password']

    # compare with database
    with open('users.json') as f:
        users = json.load(f)
    if username not in users:
        return home(message='user not found')
    if password != users[username]['password']:
        return home(message='wrong password')
    return render_template('random_quote_template.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
