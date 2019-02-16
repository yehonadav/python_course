from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "index route"


@app.route("/login")
def login():
    return "would you like to login?"


@app.route("/logout")
def logout():
    return "you are logged out"


@app.route("/login/<string:name>/")
def user_login(name):
    return name + ' is now logged in'


if __name__ == "__main__":
    app.run()
