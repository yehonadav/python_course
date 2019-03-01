# login page (a list of users is needed) -> go to home page -> home page is the user content page
from flask import Flask, render_template, request, session, flash
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
def do_admin_login():
    users = {'gal': '123', 'or': '123', 'itay': '123'}
    name = request.form['username']
    if request.form['username'] in users:
        password = users[name]
        if password == request.form['password']:
            session['logged_in'] = True
            return login(name)
    else:
        flash('wrong password!')
    return login(name)


@app.route('/home', methods=['GET'])
def home(user):
    import os
    if not os.path.exists(user):
        open(user, 'w').close()

    with open(user) as db:
        content = db.read()

    return render_template('userhome.html', name=user, content=content)


@app.route('/save_user_content', methods=['POST'])
def save_user_content():
    user = request.form['username']
    content = request.form['content']
    with open(user, 'w') as db:
        db.write(content)
    return content

app.secret_key = '123'
app.run(host='0.0.0.0', port=80, debug=True)