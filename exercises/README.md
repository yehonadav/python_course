# Exercises
  
level 0: 
---------
  
just go through them    
  
level 1: 
---------

(1)  Create a program ```name_info.py``` that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year they were born in. 
  
(2)  Create a program ```odd_or_even_numbers.py``` that asks the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message. 
  
  
(3)  Create a program ```list_less_than_5.py```  
use this list:  
```ages = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]```  
Write a program that creates a new list that has all the elements  
less than 5 from ```ages``` list and print out all the elements of the new list.  
  
  
(4)  Create a program ```divider.py```  
that asks the user for a number and then prints out  
a list of all the divisors of that number.  
(If you don’t know what a divisor is,  
it is a number that divides evenly into another number.  
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)  
   
   
(5)  Create a program ```common_list.py```  
that takes two lists:  
```  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]```  
```  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]```  
and returns a list that contains only the elements that  
are common between the lists (without duplicates).  
Make sure your program works on two lists of different sizes.  
  
  
(6)  Create a program ```palindrome.py```  
that asks the user for a string and print out  
whether this string is a palindrome or not.  
(A palindrome is a string that reads the same forwards and backwards.)  
  
  
(7)  Create a program ```bar_mitzva.py```  
use the exercises data:  
```from exercises.data import get_data```  
```data = get_data(10)```  
loop over 10 items and get the first item  
who's age is under 13 & print the item keys  
& values. if none of the items has an age  
less than 13 print a message saying all the  
people are old.  
  
  
(8)  Create a program ```fibonacci_sum.py```  
create a program to summarize the fibonacci sequence.   
  
  
(9)  Create a program ```hobbies_handler.py```  
create a hobbies function with ```name, age, hobby, *optional_hobbies & **other```  
that returns a sentence:
```my name is {name}, my age is {age}.\nI like to {hobby}{optional_hobbies}.{optional_keyword_hobbies}```   
* add ```int``` hint to age argument.  
* add type enforcement to age argument.  
* create a main program condition to call the function:  
  ```if __name__ == "__main__":```  
  and print the result in the main program.  
  
  
(10)  Create a program ```sort_data.py```  
* create a function ```sort_names_with_addresses``` that gets a data argument(exercise data)  
* the function creates a list of sorted names.  
* the function adds addresses to the name list,  
* the function finally returns a sorted list (by name) of tuples  
  with names and lists of addresses.  
output example:  
```[```  
```('Ana Romero', ['8973 Cline Mall\nWest Williamhaven, LA 13926']),```  
```('Anthony Poole', ['3412 Costa Fall Apt. 204\nEast Gerald, VT 13412'])```  
```]```  
  
  
(11)  open ```sort_data.py```  
* create another function called add_random_postal  
  that gets a ```names_with_addresses``` argument(the sorted output of previous function)  
* the function iterates over the list  
  and creates a new list with a third value  
  of every item: a string of 5 random digits.  
* the function return the result.  
  
  
(12)  open ```sort_data.py```  
* create another function called sum_postal_codes  
  that gets a data argument(the output of previous function)  
* the function iterates over the data  
  and sums up the random postal code of each item.  
* the function return the result.  
  
  
(13)  Create a program ```main_sort.py```  
* import ```from exercises.data import get_data```  
* import ```sort_names_with_addresses``` from ```exercises.level_1.sort_data```  
* import ```add_random_postal``` from ```exercises.level_1.sort_data```  
* import ```sum_postal_codes``` from ```exercises.level_1.sort_data```  
* create a main program condition:  
  ```if __name__ == "__main__":```  
* get 30 different data items  
* use sort_names_with_addresses  
* use add_random_postal  
* use sum_postal_codes  
* print the results  
  
  
(14)  Create a file ```number_generator.py```  
* import the random module  
* create a numbers function with a range argument  
* add a while range > 0 loop to the function.  
* yeild a random number(0-10,000) in the loop  
* subtract 1 from range in the loop  
* finish the loop and write a return to break the function  
* congrats! you created a generator. test it with  
```for n in numbers(200): print(n)```  
  
  
(15)  Create a file ```even_numbers.py```  
use the number generator from previous exercise(range=40)  
create a list that has only even numbers in it.  
* if list length > 10 raise an exeption stating that the list has exceeded its limit.  
* create a special MaxLengthException for the exercise.  
  
  
(16)  Create a file ```rock_paper_scissors.py```  
create a rock paper scissors game.  
* use the getpass module(doesn't run well with pycharm)  
https://stackoverflow.com/questions/40007802/getpass-getpass-function-in-python-not-working
  
  
(17)  Create a file ```guess_game.py```  
* Generate a random number between 0 and 10  
* Ask the user to guess the number,  
* then tell them whether they guessed too low,  
  too high, or exactly right.   
* Keep the game going until the user types “exit”
* Keep track of  answer + low/high/exact guesses  
  the user has taken in each round,  
  and when the game ends, print this out.  
* use functions & run the game from the main condition.  
  
(18)  Create a file ```zero_division.py```
* create a function ```create_numbers``` that returns a list of  
  random numbers with a random length between 0-9  
* create a function ```avg``` that takes the list of ```create_numbers``` and returns an average number  
* create a function ```print_average``` that takes the list of ```create_numbers``` and try to print the average  
* if ```print_average``` fail with ```ZeroDivisionError``` or ```TypeError``` it will print  
  the error and return it.  
* make a main program to call ```print_average``` until failure.  
  
(19)  Create a file ```type_error.py```
* use and import functions from ```zero_division.py```  
* create a function ```randomly_stringify_list_items```
* make a main program to:  
  create random list of numbers  
  randomly stringify some numbers  
  ```print_average``` until failure.  
  
(20)  Create a file ```quadratic.py```
* create a ```QuadError```  exception  
* create a function ```calculate_quadratic_equation```  
  ```ax² + bx + c = 0``` to find x1, x2 using the ```math``` module  
  ![quadratic](https://github.com/yehonadav/python_course/blob/master/exercises/images/quadratic.JPG?raw=true)  
  raise a ```QuadError``` if the equation is not quadratic(a=0) or has no real roots(b²-4ac<0)  
* make a main program to:  
  solve & print results of -> 5x² + 7x = 15  
  solve & print results of -> 6x² + 11x - 35 = 0  
  solve & print results of -> 2x² - 4x - 2 = 0  
  solve & print results of -> 2x² - 64 = 0  
  solve & print results of -> -12x² + 13x = 0  
  try to solve -> 6x² + 11x - 35 = 0
  in case of ```QuadError``` solve -> 11x + 50 = 0
  
(21)  Create a file ```calculator.py```  
* create a ```Calculator```  class  with ```a, b``` arguments  
* create ```display``` method to print the numbers and the last result  
* create ```add``` method to calculate ```a+b```  
* create ```sub``` method to calculate ```a-b```  
* make sure the result is shared between all calculators  
* test the calculators(level 2)  
  
(22)  Create a file ```inherit.py```  
* use ```time``` & ```datetime``` modules  
* create ```Time``` class with ```get_time``` to get a time signature  
* create ```Date``` class with ```get_date``` to get a date signature  
* inherit ```Time``` class from in ```Date``` class  
* create a main program condition:  
  ```if __name__ == "__main__":```  
  use both classes and their available methods  
  
(23)  Create a file ```athlete.py```  
* create ```Athlete``` class with ```name, power, speed, endurance, weight``` arguments  
* create ```Sprinter``` and inherit ```Athlete```  
  boots the ```Sprinter``` parameters as such:  
```  
power *= 2, speed += 1, endurance -= 3  
if endurance < 1: endurance = 1
```  
* create a ```run``` method like so in ```Sprinter```:  
```
    def run(self, distance):
        endurance = 1 + distance/self.endurance
        sleep((self.weight*distance)/(self.power*(self.speed**2)+endurance))
        return self.name
```
  
(25)  Create a file ```timer.py```  
* create ```Measurement``` class with ```date``` & ```run_time```  
  
(26)  in ```timer.py```  
* import ```Date```  from exercise 22  
* create ```Timer``` class & inherit ```Date```  
* create ```__init__``` method with ```f, *args, **kwargs``` arguments  
* save the arguments as such:
```
    self.operation = f
    self.args = args
    self.kwargs = kwargs
    self.last_measurement = Measurement()
```  
* create a ```start``` method  
  to measure time & date,  
  run an operation with its arguments  
  & return the operation result  
  
(27)  in ```timer.py```  
* create a main program condition:  
  ```if __name__ == "__main__":```  
* use these imports: 
```
    from random import randint
    from exercises.level_1.oop.athlete import Sprinter
    from exercises.data import get_data

```
* create ```winner```, ```distance```, ```athletes``` variables  
* loop over the athletes and create sprinters  
* use Timer to measure each sprinter running ```distance```   
* sort the winner  
* print a message with:  
  the date of the competition,  
  winner name, the distance,  
  the winner run time  
  
(27)  in ```timer.py``` class ```Timer```  
* add doc string explaining the Timer API
* add a hint typing for ```f``` argument hinting it is a function (callable)  
    
(29)  Create ```Hello World``` flask app 
  
(30)  Create a flask app with 4 routes  
    
(31)  Create a flask app with port 80(http protocol) and open your app to other devices  
  
(32)  Create a flask app with a styled page using html  
  
(33)  Create a flask app  
* serve an html template  
* the route will receive a name argument and pass it to the template  

(34)  Create a ```staticfiles``` flask app with route that receives a page name and renders a template by that name.  

(35)  Create a simple login flask app  
![flask_login](https://github.com/yehonadav/python_course/blob/master/exercises/images/flask_login.JPG?raw=true)  

(36)  Create a simple form flask app with validations  
![flask_form](https://github.com/yehonadav/python_course/blob/master/exercises/images/flask_form.JPG?raw=true)  
  
Jinja Templating:  
Right out of the box, Flask includes the powerful [Jinja](http://jinja.pocoo.org/docs/) templating language. It's modeled after Django templates (but it renders much faster) and, although, Flask does not force you to use any templating language, it assumes that you'll be using Jinja since it does come pre-installed.

For those who have not been exposed to a templating language before, such languages essentially contain variables as well as some programming logic, which when evaluated (or rendered into HTML) is replaced with **actual** values. The variables and/or logic are placed between tags or delimiters. For example, Jinja templates use `{% ... %}` for expressions or logic (like for loops), while `{{ ... }}` are used for outputting the results to the end user. The latter tag, when rendered, is replaced with a value or values, and are seen by the end user.

> Jinja Templates are just .html files. By convention they live in the "/templates" directory in a Flask project.
  
(37)  using jinja2 create a simple hello world template  
  
(38)  Create a file ```simple_message.py```, using jinja2 render a template with a message from user input  
  
(39)  using jinja2 create a simple for loop template  
   
(40)  Create a flask app using jinja2:  
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
  
(41)  in your ```with_flask``` app:  
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
  
(42)  in your ```with_flask``` app:  
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
  
(43)  in ```with_flask``` app:  
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
  
(44) in ```with_flask``` app:  
* add a *home* route:  
![jinja_flask_home](https://github.com/yehonadav/python_course/blob/master/exercises/images/jinja_flask_home.png?raw=true)  
  
(45) create ```hobbies.py```  
* add these lines of code:  
```
from exercises.data import get_data
from statistics import median
import random

users = get_data(2000)  
```
* create a list of hobbies  
* create a second list of different hobbies  
* create a __main__ = __name__ condition  

(46) in ```hobbies.py```:  
* create and run a function that extract users and measure their average age  
* create and run a function that extract users and find the most common name  
* create and run a function that extract users and measure their median  
  
(47) in ```hobbies.py```:  
* create and run a function that adds a random hobby to users  
  
* create and run a function to count the hobbies and print their count  
  
* create and run a function that adds a second hobby from the same hobby pool,  
  if the hobbies are the same, randomly change one of the hobbies  
  to a new random hobby from a second hobby pool  
  
* create and run a function to count the hobbies from the second hobby pool  
  and print their count  
  
(48) create ```loopers.py```:  
* import these:  
```python
import time
from exercises.data import get_data
from exercises.level_1.hobbies import add_random_hobby, add_second_hobby, hobbies, hobbies2
```  
  
* create a ```if "__main__" = __name__``` condition  
  
* create 2000 users in your main  
  
(49) in ```loopers.py```:  
* create and run a function named ```get_addresses```  
  the function receive ```(users, start=0, stop=50)``` parameters,  
  iterates through users and return a list of user addresses  
  starting with the starting point up to the stop point.  
  
(50) in ```loopers.py```:  
* create and run a function named ```count_address_numbers```  
  the function receive ```(user_addresses)``` parameter,  
  and holds a counter dictionary & most_counted_address_number parameters  
```python
def count_address_numbers(user_addresses):
    address_number = user_addresses[0].split(' ', 1)[0]
    counter = {address_number: 0}
    most_counted_address_number = address_number
```  

* use the function to iterate through users  
* in each iteration get the first word of the address  
* if the word is not a number continue(ignore that iteration)  
* if the word is in ```counter``` increment counter
* otherwise add the word to the counter with a value of 1
* each time you increment ```counter``` check if the word has beed counted more than the ```most_counted_address_number```  
* if a new word has been counted the most, update ```most_counted_address_number```  
* print the most counted word and how many times it has been counted.  
  
(51) in ```loopers.py```:  
* create and run a function named ```encounter_name_twice```  
  the function receive ```(users)``` parameter,  
  iterates with a while loop through users until it encounters a user name twice  
* use the function to print the name you encountered twice  
  
(52) in ```loopers.py```:  
* create and run a function named ```sum_index30```  
  the function receive ```(users)``` parameter, and  
  iterate users until their age sum is bigger than the current iteration index by 30 fold or more  
* use the function to print the users age summary and index  
    
(53) in ```loopers.py```:  
* create and run a function named ```name_and_address20```  
  the function receive ```(users)``` parameter, and  
  iterate users until it finds a name and address with a combined length bigger than 20 characters  
* use the function to print the combined name+address length, if found  
  
(54) in ```loopers.py```:  
* create and run a function named ```assert_names```  
  the function receive ```(users)``` parameter, and  
  iterate users and assert their name length is between 2-20 characters long  
* if you encounter an AssertionError, make sure your main can handle it  
  
(55) in ```loopers.py```:  
* create and run a function named ```assert_ages```  
  the function receive ```(users)``` parameter, and  
  iterate users and assert their age is between 0-120 characters long  
* if you encounter an AssertionError, make sure your main can handle it  
  
(56) in ```loopers.py```:  
* create and run a function named ```assert_user_hobby```  
  the function receive ```(users)``` parameter  
* use ```hobbies``` & ```hobbies2``` to create ```all_hobbies``` a list containing all hobbies   
* iterate users and assert their hobby is in ```all_hobbies```  
* also assert users second hobby is in ```all_hobbies```
* make sure to run  
```python
add_random_hobby(users)
add_second_hobby(users)
```  
  in your main, before calling ```assert_user_hobby(users)```  
* inject an invalid hobby to a user  
* if you encounter an AssertionError, make sure your main can handle it  
* if the invalid injection failed make sure to raise an exception, with an ```expectation failed: ..``` message  
  
(57) in ```loopers.py```:  
* create a function named ```get_user_uptime```  
  the function receive ```(user)``` parameter, and  
  uses the user's 'created' key to pull an epoc time value, 
  it then measures the current time and subtract the created time to get the user uptime value.  
  if the 'created' key does not exist the caller should handle a KeyError exception.  
  
(58) in ```loopers.py```:  
* create and run a function named ```print_users_avg_uptime```  
  the function receive ```(users)``` parameter, and  
  print the users average uptime  
  
(59) in ```loopers.py```:  
* create and run a function named ```find_equal_neighbor_age```  
  the function receive ```(users)``` parameter, and  
  iterate the users, if 2 neighboring users have the same age  
  a message with their name and age is printed before the function returns  
  
(60) in ```loopers.py```:  
* create and run a function named ```create_more_users```  
  the function receive ```(users)``` parameter, and  
  loops for ~2 seconds, while looping the function creates users
  in sets of 10 and adds them to the main users list  
  before checking the loop condition for the next iteration  
  after the creation process is done, a message telling  
  how many users were added is printed  
  
(61) create ```simple_regex.py```:  
* import these:  
```python
import re
from regEx.data import sentences, data as regex_text
from exercises.data import create_user, get_data, get_data_as_text, transform_data_to_text
from exercises.level_1.hobbies import add_random_hobby, add_second_hobby
```
* create a ```__name__ == "__main__"``` condition  
* join all sentences into 1 string
* create a user  
* create 20 users from get data and add a hobby to each user  
* create another 10 users and add a hobby and a second hobby to each user  
* transform all created users into text  
* create another 30 users as text  
* combine all the data into 1 string  
    
(62) in ```simple_regex.py```:  
* create a function called find_matches which receives a regex and string parameters  
* the function must return a list of matches for the regex  

(63) in ```simple_regex.py``` in combined_data text  
print the number of matches for b-x + F-W or whitespace 0 times or more + 2-6  

(64) in ```simple_regex.py``` in user text  
print the number of matches for exclusion any of these characters acegijlnprtvxz    

(65) in ```simple_regex.py``` in user text  
print the number of matches for any none word character or any of IDAN  
  
(66) in ```simple_regex.py``` in user text  
print the number of matches for a/b/c + any character  
  
(67) in ```simple_regex.py``` in user text  
print the number of matches for any 5 characters  
  
(68) in ```simple_regex.py``` in users20 text  
print the number of matches for all numbers  
  
(69) in ```simple_regex.py``` in users30 text  
Search the string to see if it starts with "name" and ends with "a number adn a white-space"  
print the result  
  
(70) in ```simple_regex.py``` in regex_text text  
print the number of matches of 'to'  
  
(71) in ```simple_regex.py``` in user text  
print 0 matches if no match was found for 'zombie'  
  
(72) in ```simple_regex.py``` in regex_text text  
Search for the first white-space character in the string  
print the result  
  
(73) in ```simple_regex.py``` in users20 text  
Make a search that returns no match  
print the result  
  
(74) in ```simple_regex.py``` in user text  
Split at each white-space character  
print the number of matches  
  
(75) in ```simple_regex.py``` in user text  
Split the string only at the first occurrence of a white-space  
print the number of matches  
  
(76) in ```simple_regex.py``` in user text  
replace every white-space character with tab  
  
(77) in ```simple_regex.py``` in user text  
replace the first 2 occurrences of a white-space to _  
  
(78) in ```simple_regex.py``` in regex_text text  
Do a search that will return a Match Object  
The Match object has properties and methods  
used to retrieve information about the search, and the result:  
  .span() returns a tuple containing the start-, and end positions of the match.  
  .string returns the string passed into the function  
  .group() returns the part of the string where there was a match  
print the match regex, string(text) size, span and value(match group)  
  
(79) in ```simple_regex.py``` in users10 text  
print the position (start- and end-position) of the first match occurrence.  
The regular expression looks for any words that starts with a "na"  
  
(80) in ```simple_regex.py``` in regex_text text  
print the value of the first match match.  
The regular expression looks for any words that starts with an "S"  
  
(81) in ```simple_regex.py``` in regex_text text  
print the value of the first match.  
The regular expression looks for any words that starts with an "S"  
whats wrong here? make an error handler  
  
(82) in ```simple_regex.py``` in combined_data text  
print any word that starts with ar  
  
(83) in ```simple_regex.py``` in combined_data text  
print all matches of any characters with 2 following occurrences  
  
(84) in ```simple_regex.py``` in sentences text  
print the starting 2 characters of the sentence  
  
(85) in ```simple_regex.py``` in sentences text  
print the final 10 characters of the sentence  
  
(86) in ```simple_regex.py``` in sentences text  
print the number of matches for the following 3 a-z A-Z characters after each white-space  
  
(87) in ```simple_regex.py``` in combined_data text  
print the number of matches for all valid ip octets(0-255)  
  
(88) in ```simple_regex.py``` in users30 text  
print the number of matches for any single character except \n  
  
(89) in ```simple_regex.py``` in users30 text  
print the number of matches for all `.` occurrences  
  
(90) in ```simple_regex.py``` in combined_data text  
print the number of matches for all website occurrences  
  
(91) in ```simple_regex.py``` in combined_data text  
print the number of matches for all email occurrences  
  
(92) in ```simple_regex.py``` in users30 text  
print set of the matches for all user names  
  
(93) in ```simple_regex.py``` in users20 text  
print set of the matches for all users first hobbies  
  
(94) in ```simple_regex.py``` in users10 text  
print set of the matches for all user hobbies  
  
(95) in ```simple_regex.py``` in combined_data text  
print set of all ip occurrences  
  
level 2:  
---------
  
(1)  Create a file ```fibonacci.py```  
* create a main program condition:  
  ```if __name__ == "__main__":```   
* create a fibonacci_sequence function
* print the result of the first 10 items of the sequence  
* create a fibonacci_generator function  
* create a fibonacci_iterator function  
* iterate over fibonacci_iterator and print  
  the result from 5  to 89.  
  
(2)  Create a file ```assert_program_is_done.py```  
* create a ```UserQuit``` exception  
* create a ```ask_user``` function with a question  
  argument. try to ask the question using ```input```  
  and expect an ```y,n,q```  answer.  
  raise a UserQuit exception if an ```EOFError```  
  is encountered or if the user pressed "Q/q/quit/QUIT"  
  if the user pressed "Y/YES/N/NO/y/yes/n/no"  
  return the uppercased first character the user pressed.  
  for anything else recurse the ```ask_user``` function  
* create a ```assert_program_is_done``` function  
  use the ```time``` module to measure how long it  
  took the user to answer. if a UserQuit error rises  
  print a message stating that the user quit before  
  assertion was completed, else: check if the answer is 'Y'  
  print the time it took the user to answer, if the answer  
  is 'N' print ```'better luck next time'```  
  finally print ```'assertion is done'```  
* call ```assert_program_is_done```  
  
(3)  Create a file ```first_recurring_char.py```    
* create a function to find the first recurring char in a string.  
* make it performance worthy!  
  
(4)  Create a file ```required_keyword_positionals.py```    
* create a function that accepts only keyword arguments  
* you can't use ```**kwargs``` or its variants  
* arguments can't have default values  
* the function must print all local variables
* make it in 1 line of code. - what's cool about this function?
  
(5)  Create a simple address book application,  
to store, search, modify & delete records containing:  
name, address, email & phone number (level 2+)  
* you must use a class called ```AddressBook```  
* use the pickle module as a database  
  
(6)  Create a progress bar using ```sys``` & ```time``` modules  
![progressbar1](https://github.com/yehonadav/python_course/blob/master/exercises/images/progressbar.JPG?raw=true)  
  
(7)  Create a file ```best_sum_and_ratio.py``` (level 2++)  
* import:  
```
import random  
from exercises.level_2.overloaded_function import expon, results
```  
* create & run a function to try and run expon with None  
  and run it again with a str/int(randomly) with a random value: 0-4.  
  in case of failure run expon with a list of 2 random values: 0-4, 2-3.  
* create a ```create_results``` function  
  it will run this loop:  
```
    while res_sum > stop:
        print("sum {} > {}".format(res_sum, stop))
        ...
        # we can wrap this into a function
        expon(random.randint(0, 1025))
        expon(random.randint(0, 1025) * 0.001)
        expon([random.randint(1, 101) * 68 / 47 * random.randint(1, 3) for _ in range(random.randint(0, 25))])

        stop = len(results)
        # we can wrap this into a function
        if stop > ...:
            before = start - n
            if before < 1:
                before = 1
            for i in range(before, stop):
                if results[i] > 1:
                    results[i] = 1/results[i]
                    
        # should be able to reach +5000 results
        n = int(str((n+1)*...*(n+1)).split('.')[0])+1
        res_sum = sum(results)
        ...
    print("sum {} < {}\n\n\n".format(res_sum, stop))
```  
  res_sum: expon results summary  
  stop: expon results length  
  results: expon results  
  n: a counter starting from 0  
  start: expon results length  
  ...: fill your own code    
* create a ```find_best_sum_and_ratio``` function  
  inside the function: create a SUM class with ```sum, len, ratio``` attributes  
  find the point in time where the summary of the results was the highest  
  find the point in time where the ratio summary:length of results was the highest  
  print them.

(8)  Create a file ```users.py```  
* create exceptions: ```LowCreditsError, LowStockError, MissingItemError```  
* create ```User``` class:  
```
class User:
    users = {}

    def __init__(self, name, password, credit):
        self.name = name
        self.password = password
        self.credit = credit
        self.items = {}
    
    ...
```
* create ```login, logout, buy, sell, create``` methods:  
login/logout need to compare passwords and return True/None
buy/sell will add/subtract items and change user credit, use exceptions accordingly  
create is a classmethod to create users and add them to the users by their names:
```
class User:
    users = {} # right here
```  
  
(9)  Create a test for ```users.py```  
  
(10)  Create a simple game using pyxel  
  
(11)  Build a fill-in-the-blanks quiz game.  
Your quiz will prompt a user with a sentence  
containing several blanks. The user should then be asked to fill in each blank appropriately to complete the sentence.  
  
(12)  create a tic tac toe game  
  
(13)  Create a simple pie, bar & line charts flask app with using Chart.min.js  
![flask_pie_chart](https://github.com/yehonadav/python_course/blob/master/exercises/images/flask_pie_chart.JPG?raw=true)  
![flask_line_chart](https://github.com/yehonadav/python_course/blob/master/exercises/images/flask_line_chart.JPG?raw=true)  
![flask_bar_chart](https://github.com/yehonadav/python_course/blob/master/exercises/images/flask_bar_chart.JPG?raw=true)  
  
(14)  Create a simple login flask app with sqlite database & 3 users using sqlalchemy  
  
  
level 3:  
---------
  
(1)  create a black jack game  
  
(2)  Build a randomly generated Python space game.  
With traveling, trading, mining, resource management, battles and storyline events  
along with saving the users data to that of an output file.  
  
(3)  Create a snake game using the pygame module  
![Snake](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/sanke.JPG?raw=true)  
* Create a python package ```snake```  
![Snake package](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/snake_package.JPG?raw=true)  
* create a ```__main__.py``` file for the package  
  and import a Play class to run the game.  
* create a play.py file with a Play class.  
  the Play class should contain a ```run```,```restart``` & ```start```  
  methods to run the game, go back to the menu & start the menu.  
  an ```__init__``` method should also be defined with some variables:  
  self.menu: to include the menu object.  
  self.game: to include the running game object.  
  self.screenX & self.screenY: to set the screen size of the game.  
  after setting the variables the init method should call the start method.  
* import a Game & StartMenu classes from the snake package.
* create a game.py & menu.py file to import from.  
* in the StartMenu class create a start & exit buttons
  for calling sys.exit() or proceeding to choose a game size.
![menu](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/menu.JPG?raw=true)  
* have a choose_size method with ```Small Normal Big``` buttons  
  to set the snake & apple sizes and proceeding to choose a difficulty level.
![choose size](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/choose_size.JPG?raw=true)  
* have a choose_difficulty method with ```Easy Normal Hard Expert``` buttons  
  to set the snake moving speed and proceeding to run the game.  
![choose difficulty](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/choose_difficulty.JPG?raw=true)  
* use these methods to run the game from the menu:  
```    
    def easy(self):
        self.game.run(0.25, self.size)

    def normal(self):
        self.game.run(0.5, self.size)

    def hard(self):
        self.game.run(1, self.size)

    def expert(self):
        self.game.run(2, self.size)
```  
* create a mainloop method to run events in the menu.  
* create a resources package, add snake.py & apple.py  
  and create a Snake & Apple classes.  
* go to the ```game.py``` file, import the Snake & Apple classes  
* create a Game class
* use the ```__init__``` method to set the screen
* create an over method to show the score, go back to the menu or exit the program  
![game over](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/game_over.JPG?raw=true)  
* create a loop method that will:  
  fill the screen ```self.screen.fill((30, 40, 100))```  
  update the snake object ```self.snake.update()```  
  check snake for collisions  
  check for apples  
  update image positions of snake & apple  
  check for key events  
good luck!  
  
level 4:  
---------
    
![game over](https://github.com/yehonadav/python_course/blob/master/exercises/images/coming_soon.png?raw=true)  
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  