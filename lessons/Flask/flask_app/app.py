from flask import Flask, render_template, flash, redirect, url_for, session, request
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask import g
import datetime
from lessons.flask_lessons.flask_app.database import DataBase


app = Flask(__name__)

DATABASE_URI = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = DataBase(DATABASE_URI)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Index
@app.route('/')
def index():
    return render_template('home.html')


# About
@app.route('/about')
def about():
    return render_template('about.html')


# Articles
@app.route('/articles')
def articles():
    # Create cursor
    db = get_db()

    # Get articles
    articles = db.execute("SELECT * FROM articles")

    if len(articles) > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('articles.html', msg=msg)


# Single Article
@app.route('/article/<string:id>/')
def article(id):
    # Create cursor
    db = get_db()

    # Get article
    articles = db.execute("SELECT * FROM articles WHERE id = '{}';".format(id))
    return render_template('article.html', article=articles[0])


# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        db = get_db()

        # Execute query
        db.execute("INSERT INTO users(name, email, username, password) VALUES('{}', '{}', '{}', '{}');"
                   .format(name, email, username, password))  # what if username already exist???

        # Commit to DB
        get_db().commit()  # is this ok ?

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        db = get_db()

        # Get user by username
        result = db.execute("SELECT * FROM users WHERE username = '{}';".format(username))

        if len(result) > 0:
            # Get stored hash
            password = result[0][4]

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))

    return wrap


# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    # Create cursor
    db = get_db()

    # Get user articles
    articles = db.execute("SELECT * FROM articles;")  # what is missing in this query??

    if len(articles) > 0:
        return render_template('dashboard.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('dashboard.html', msg=msg)


# Article Form Class
class ArticleForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])


# Add Article
@app.route('/add_article', methods=['GET', 'POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        # Create Cursor
        db = get_db()

        # Execute
        db.execute("INSERT INTO articles(title, body, author, create_date) VALUES('{}', '{}', '{}', '{}');"
                   .format(title, body, session['username'], datetime.datetime.now()))

        # Commit to DB
        db.commit()

        flash('Article Created', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_article.html', form=form)


# Edit Article
@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    # Create cursor
    db = get_db()

    # Get article by id
    article = db.execute("SELECT * FROM articles WHERE id = '{}';".format(id))[0]

    db.close()  # is this necessary?

    # Get form
    form = ArticleForm(request.form)

    # Populate article form fields
    form.title.data = article[1]
    form.body.data = article[2]

    if request.method == 'POST' and form.validate():
        title = request.form[1]
        body = request.form[2]

        # Create Cursor
        db = get_db()

        app.logger.info(title)  # what's this??

        # Execute
        db.execute("UPDATE articles SET title='{}', body='{}' WHERE id='{}';".format(title, body, id))

        # Commit to DB
        db.commit()

        flash('Article Updated', 'success')
        return redirect(url_for('dashboard'))

    return render_template('edit_article.html', form=form)


# Delete Article
@app.route('/delete_article/<string:id>', methods=['POST'])
@is_logged_in
def delete_article(id):
    # get database connection
    db = get_db()

    # execute deletion
    db.execute("DELETE FROM articles WHERE id = '{}';".format(id))

    # commit to DB
    db.commit()

    flash('Article Deleted', 'success')
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
