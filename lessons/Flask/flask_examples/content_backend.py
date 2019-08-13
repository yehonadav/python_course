# login page save new users
# home page -> user content page, save user content
import os
from flask import Flask
from flask import request
from flask import jsonify


app = Flask('my app')


@app.route('/save_user_content', methods=['POST'])
def save_user_content():
    user = request.form['username']
    content = request.form['content']
    with open('users\\'+user, 'w') as db:
        db.write(content)
    return content


@app.route('/users', methods=['GET'])
def users():
    users = []
    for i in os.walk('users'):
        users = i[2]
        break
    return jsonify(users)


@app.route('/<username>/get_content', methods=['GET'])
def get_content(username):
    if os.path.exists('users\\'+username):
        with open('users\\'+username) as f:
            content = f.read()
        return content
    return 'no content', 404


@app.route('/<username>/add_content', methods=['POST'])
def add_content(username):
    if os.path.exists('users\\'+username):
        content = request.form['content']
        with open('users\\'+username, 'a') as f:
            f.write(content)
        return ''
    return 'user not found', 404


if __name__ == "__main__":
    app.secret_key = '123'
    app.run(host='0.0.0.0', port=80, debug=True)
