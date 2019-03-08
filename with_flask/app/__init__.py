from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def template_index():
    """Here we are establishing the route /,
    which renders the template template.html
    via the function render_template().
    This function must have a template name.
    Optionally, you can pass in arguments to the template,
    like in this example - string_variable & list_variable.
    """
    return render_template('template.html', string_variable="Combat-Bat", list_variable=[n for n in range(0, 7)])
