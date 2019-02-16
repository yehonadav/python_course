from flask import Flask, render_template, flash, request
from wtforms import Form, StringField, validators
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class SignUpForm(Form):
    name = StringField('Name:', validators=[validators.DataRequired()])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Length(min=6, max=35)])
    password = StringField('Password:', validators=[validators.DataRequired(), validators.Length(min=3, max=35)])
 
 
@app.route("/", methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm(request.form)
 
    if request.method == 'POST':
        name = request.form['name']
        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('hello.html', form=form)


if __name__ == "__main__":
    app.run()
