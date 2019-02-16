from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello</h1><div>Hello</div><h3><strong>Hello</strong></h3>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
