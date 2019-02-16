from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "You can open : http://127.0.0.1:5000/login/name/"


@app.route("/login/<string:name>/")
def login(name):
    return render_template('template.html', name=name)


if __name__ == "__main__":
    app.run()
