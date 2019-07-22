# Flask Exercises  
  
  
(1)  Create ```Hello World``` flask app 
  
(2)  Create a flask app with 4 routes  
    
(3)  Create a flask app with port 80(http protocol) and open your app to other devices  
  
(4)  Create a flask app with a styled page using html  
  
(5)  Create a flask app  
* serve an html template  
* the route will receive a name argument and pass it to the template  

(6)  Create a ```staticfiles``` flask app with route that receives a page name and renders a template by that name.  

(7)  Create a simple login flask app  
![flask_login](https://github.com/yehonadav/python_course/blob/master/exercises/images/flask_login.JPG?raw=true)  

(8)  Create a simple form flask app with validations  
![flask_form](https://github.com/yehonadav/python_course/blob/master/exercises/images/flask_form.JPG?raw=true)  
  
Jinja Templating:  
Right out of the box, Flask includes the powerful [Jinja](http://jinja.pocoo.org/docs/) templating language. It's modeled after Django templates (but it renders much faster) and, although, Flask does not force you to use any templating language, it assumes that you'll be using Jinja since it does come pre-installed.

For those who have not been exposed to a templating language before, such languages essentially contain variables as well as some programming logic, which when evaluated (or rendered into HTML) is replaced with **actual** values. The variables and/or logic are placed between tags or delimiters. For example, Jinja templates use `{% ... %}` for expressions or logic (like for loops), while `{{ ... }}` are used for outputting the results to the end user. The latter tag, when rendered, is replaced with a value or values, and are seen by the end user.

> Jinja Templates are just .html files. By convention they live in the "/templates" directory in a Flask project.
  
(9)  using jinja2 create a simple hello world template  
  
(10)  Create a file ```simple_message.py```, using jinja2 render a template with a message from user input  
  
(11)  using jinja2 create a simple for loop template  
   
(12)  Create a flask app using jinja2:  
* the following project structure:  
  ```sh
  with_flask
      ├── __init__.py
      ├── requirements.txt
      ├── run.py
      └── app
           ├── __init__.py
           └── templates
                 ├── layout.html
                 ├── macros.html
                 └── template.html
  ```
* use these requirements:  
```
Flask==1.0.2
Jinja2==2.10
MarkupSafe==1.0
Werkzeug==0.14.1
itsdangerous==0.24
wsgiref==0.1.2
```    
* create & activate a virtualenv  
* install the requirements  
* add the following code to ```with_flask/app/templates/template.html```:  
```html
  <!DOCTYPE html>
  <html>
    <head>
      <title>Flask With Jinja Example</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
      <style type="text/css">
        .container {
          max-width: 1000px;
          padding-top: 100px;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <p>
        It's worth noting that Jinja only supports a few control structures - 
        if-statements & for-loops are the two primary structures. 
        The syntax is similar to Python, differing in that no colon is required 
        and that termination of the block is done using an endif or endfor 
        instead of by whitespace. You can also complete the logic within your controller 
        or views and then pass each value to the template using the template tags. 
        However, it is much easier to perform such logic within the templates themselves.
        </p>
        <p>string variable: {{string_variable}}</p>
        <p>list index 0 value: {{list_variable[0]}}</p>
        <p>Loop through the list:</p>
        <ul>
          {% for n in wrong_list %}
          <li>{{n}}</li>
          {% endfor %}
        </ul>
        <br>
        <h4>Inheritance</h4>
        <p>
        Templates usually take advantage of <a href="http://jinja.pocoo.org/docs/templates/#template-inheritance">inheritance<a/>, 
        which includes a single base template that defines the basic structure 
        of all subsequent child templates. 
        You use the tags `extends` and `block` to implement inheritance.

        The use case for this is simple: as your application grows, 
        and you continue adding new templates, you will need to keep common code 
        (like a HTML navigation bar, Javascript libraries, CSS stylesheets, and so forth) in sync, 
        which can be a lot of work. 
        Using inheritance, we can move those common pieces to a parent template 
        so that we can create or edit such code one and all child templates will inherent such code.
        </p>
      </div>
      <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
      <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
    </body>
  </html>
```  
* fix the broken html code  
* add the following code to ```with_flask/app/__init__.py```:  
```
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
```  
* add the following code to ```with_flask/run.py```:  
```
from with_flask.app import app


if __name__ == '__main__':
    app.run(debug=True)

```    
* run the app    
  
(13)  in your ```with_flask``` app:  
* add the following code to ```with_flask/app/templates/layout.html```:  
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Flask With Jinja Example</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <style type="text/css">
      .container {
        max-width: 1000px;
        padding-top: 100px;
      }
      h2 {color: red;}
    </style>
  </head>
  <body>
    <div class="container">
      <h2>Before-Block: This is the layout. block templates are inside:</h2>
      <br>
      {% block content %}{% endblock %}
      <br>
      <h2>After-Block: This is the layout. block templates are inside:</h2>
      <!--
        The block defines a block (or area) that child templates can fill in.
        Further, this just informs the templating engine that a child template may override
        the block of the template.

        Think of these as placeholders to be filled in by code from the child template(s).
       -->
    </div>
    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
  </body>
</html>
```
*  Update the *template.html*:  
  ```html
  {% extends "layout.html" %}
  {% block content %}
    <!--
        The `extends` informs the templating engine that this template 
        "extends" another template, layout.html. This establishes the link between the templates.
     -->
    <h3>In-Block-Start: This is a block template nesting inside the layout</h3>
    <br>
    <p> ..prev content.. </p>
    <h3>In-Block-End: This is a block template nesting inside the layout</h3>
  {% endblock %}
  ```  
* run the app:  
![jinja_nesting_template](https://github.com/yehonadav/python_course/blob/master/exercises/images/jinja_nesting_template.JPG?raw=true)  
  
(14)  in your ```with_flask``` app:  
* Add a navigation bar: the following code to your layout, just after the opening <body> tag:
```html
  <nav class="navbar navbar-inverse" role="navigation">
    <div class="container-fluid">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="http://jinja.pocoo.org/">Jinja</a>
      </div>

      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
          <li class="active"><a href="#">Link</a></li>
          <li><a href="#">Link</a></li>
        </ul>
        <form class="navbar-form navbar-left" role="search">
          <div class="form-group">
            <input type="text" class="form-control" placeholder="Search">
          </div>
          <button type="submit" class="btn btn-default">Go</button>
        </form>
        <ul class="nav navbar-nav navbar-right">
          <li><a href="#">Link</a></li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Profile <b class="caret"></b></a>
            <ul class="dropdown-menu">
              <li><a href="#">Manage</a></li>
              <li><a href="#">Account</a></li>
              <li><a href="#">Help</a></li>
              <li class="divider"></li>
              <li><a href="#">Sign Out</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
```  
Now every single child template that extends from the layout, will have the same navigation bar.  
Write once, use anywhere.  
* Add a footer block to the layout template at the end of ```<div class="container">```:  
```html
<div class="footer">
  {% block footer %}
    Watch! This will be added to my base and child templates using the super powerful super block!
    <br>
    <br>
  {% endblock %}
</div>
```  
* Add the [super block](http://jinja.pocoo.org/docs/templates/#super-blocks) - `{{ super() }}` block to *template.html*:  
```html
  ...
  <h3>In-Block-End: This is a block template nesting inside the layout</h3>
  {% block footer %} <!-- add this line -->
  {{super()}} <!-- add this line -->
  {% endblock %} <!-- add this line -->
{% endblock %}
```  
* run the app:  
![jinja_flask_with_navbar_and_footers](https://github.com/yehonadav/python_course/blob/master/exercises/images/jinja_flask_with_navbar_and_footers.JPG?raw=true)  
  
(15)  in ```with_flask``` app:  
The super block is used for common code  
that both the parent and child templates share,  
such as the <title> where both templates share part of the title,  
then you would just need to pass in the other part. Or for a heading. For example:  
  
  **Parent**

  ```html
  {% block heading %}
    <h1>{% block page %}{% endblock %} - Flask Super Example</h1>
  {% endblock %}
  ```

  **Child**

  ```html
  {% block page %}Home{% endblock %}
  {% block heading %}
    {{ super() }}
  {% endblock %}
  ```  
add these and run the app:  
* make sure to send a title parameter in the ```template_index``` route under ```app/__init__.py```  
* *layout.html*:
```html
<!DOCTYPE html>
<html>
  <head>
    {% block head %}
      <title>{% block title %}{% endblock %} - Flask With Jinja Example</title>
    {% endblock %}
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <style type="text/css">
      .container {
        max-width: 1000px;
        padding-top: 100px;
      }
      h2 {color: red;}
    </style>
  </head>
  <body>
    <nav class="navbar navbar-inverse" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="http://jinja.pocoo.org/">Jinja</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
          </ul>
          <form class="navbar-form navbar-left" role="search">
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Search">
            </div>
            <button type="submit" class="btn btn-default">Go</button>
          </form>
          <ul class="nav navbar-nav navbar-right">
            <li><a href="#">Link</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Profile <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#">Manage</a></li>
                <li><a href="#">Account</a></li>
                <li><a href="#">Help</a></li>
                <li class="divider"></li>
                <li><a href="#">Sign Out</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="container">
      {% block heading %}
        <h1>
          {% block page %}{% endblock %} - Flask With Jinja Example
        </h1>
      {% endblock %}
      
      <h2>Before-Block: This is the layout. block templates are inside:</h2>
      <br>
      {% block content %}{% endblock %}
      <br>
      <h2>After-Block: This is the layout. block templates are inside:</h2>
      <!--
        The block defines a block (or area) that child templates can fill in.
        Further, this just informs the templating engine that a child template may override
        the block of the template.

        Think of these as placeholders to be filled in by code from the child template(s).
       -->

      <br>
      <div class="footer" style="color: green">
        {% block footer %}
          This will be added to the layout and child templates using `super` block!
          <br>
          <br>
          <br>
        {% endblock %}
      </div>
    </div>

    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
  </body>
</html>
```  
* *template.html*:  
```html
{% extends "layout.html" %}

{% block title %}
  {{title}}
{% endblock %}

{% block head %}
  {{ super() }}
{% endblock %}

{% block page %}
  {{title}}
{% endblock %}

{% block heading %}
  {{ super() }}
{% endblock %}

{% block content %}
  <h3>In-Block-Start: This is a block template nesting inside the layout</h3>
  <br>
  <!--
    the `extends` informs the templating engine that this template
    "extends" another template, layout.html. This establishes the link between the templates.
  -->
  <p>
    It's worth noting that Jinja only supports a few control structures -
    if-statements & for-loops are the two primary structures.
    The syntax is similar to Python, differing in that no colon is required
    and that termination of the block is done using an endif or endfor
    instead of by whitespace. You can also complete the logic within your controller
    or views and then pass each value to the template using the template tags.
    However, it is much easier to perform such logic within the templates themselves.
  </p>
  <p>string variable: {{string_variable}}</p>
  <p>list index 0 value: {{list_variable[0]}}</p>
  <p>Loop through the list:</p>
  <ul>
    {% for n in list_variable %}
    <li>{{n}}</li>
    {% endfor %}
  </ul>
  <br>
  <h4>Inheritance</h4>
  <p>
    Templates usually take advantage of <a href="http://jinja.pocoo.org/docs/templates/#template-inheritance">inheritance</a>,
    which includes a single base template that defines the basic structure
    of all subsequent child templates.
    You use the tags `extends` and `block` to implement inheritance.

    The use case for this is simple: as your application grows,
    and you continue adding new templates, you will need to keep common code
    (like a HTML navigation bar, Javascript libraries, CSS stylesheets, and so forth) in sync,
    which can be a lot of work.
    Using inheritance, we can move those common pieces to a parent template
    so that we can create or edit such code one and all child templates will inherent such code.
  </p>

  <h3>In-Block-End: This is a block template nesting inside the layout</h3>
  {% block footer %}
  {{super()}}
  {% endblock %}
{% endblock %}
```  
  
(16) in ```with_flask``` app:  
* add a *home* route:  
![jinja_flask_home](https://github.com/yehonadav/python_course/blob/master/exercises/images/jinja_flask_home.png?raw=true)  
  
  
  
more exercises:  
---------   
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  