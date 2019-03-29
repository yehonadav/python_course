from qaviton.locator import Locator


class locator(Locator):
    home_login = ("xpath", "//*[@class='btn btn-success btn-lg']")
    home_register = ("xpath", "//*[@class='btn btn-primary btn-lg']")
    home_welcome_message = ('text', 'Welcome To FlaskApp')
    home_description = ('text', 'This application is built on the Python Flask framework')

    navbar_myflaskapp = ("text", "MyFlaskApp")
    navbar_Home = ("text", "Home")
    navbar_About = ('text', 'About')
    navbar_Articles = ('text', 'Articles')
    navbar_Login = ('xpath', "//*[@id='navbar']//*[text()='Login']")
    navbar_Register = ('xpath', "//*[@id='navbar']//*[text()='Register']")

    register_name = ('id', 'name')
    register_email = ('id', 'email')
    register_username = ('id', 'username')
    register_password = ('id', 'password')
    register_re_password = ('id', 'confirm')
    register_submit = ('type', 'submit')
