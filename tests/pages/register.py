from qaviton.utils.random_util import create_random, random_number
from tests.pages.components.page import Page
from tests.pages.components.navbar import NavBar
from tests.config.locators import locator


class RegisterPage(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self.navbar = NavBar(driver)

    def register_name(self):
        return self.find(locator.register_name)

    def register_email(self):
        return self.find(locator.register_email)

    def register_username(self):
        return self.find(locator.register_username)

    def register_password(self):
        return self.find(locator.register_password)

    def register_re_password(self):
        return self.find(locator.register_re_password)

    def register_submit(self):
        return self.find(locator.register_submit)

    def __call__(self):
        user = {
            "name": create_random.string(length=random_number(3, 30)),
            "email": create_random.string(length=random_number(3, 30)),
            "username": create_random.string(length=random_number(3, 30)),
            "password": create_random.string(length=random_number(3, 30)),
            "re_password": create_random.string(length=random_number(3, 30)),
        }
        self.register_name().send_keys(user['name'])
        self.register_email().send_keys(user['email'])
        self.register_username().send_keys(user['username'])
        self.register_password().send_keys(user['password'])
        self.register_re_password().send_keys(user['re_password'])
        self.register_submit().click()
        self.wait_until_page_loads()
        return user

    def with_error(self, user, error_message="user already exist"):
        self.register_name().send_keys(user['name'])
        self.register_email().send_keys(user['email'])
        self.register_username().send_keys(user['username'])
        self.register_password().send_keys(user['password'])
        self.register_re_password().send_keys(user['re_password'])
        self.register_submit().click()
        self.wait_until_page_loads()
        self.find(locator.text(error_message))
        return user
