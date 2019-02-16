from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

quotes = [
    "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
    "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
    "'To understand recursion you must first understand recursion..' -- Unknown",
    "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
    "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
    "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"]

app = Flask(__name__)


@app.route("/")
def index():
    return "You can open : http://127.0.0.1/login/name/"


@app.route("/login/<string:name>/")
def login(name):
    random_number = randint(0, len(quotes) - 1)
    quote = quotes[random_number]
    return render_template('random_quote_template.html', **locals())


if __name__ == "__main__":
    print('You can open : http://127.0.0.1/login/name/')
    app.run(host='0.0.0.0', port=80)
