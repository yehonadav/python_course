from tests.pages.components.page import Page
from tests.pages.components.navbar import NavBar
from tests.config.locators import locator


class HomePage(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self.navbar = NavBar(driver)

    def home_login(self):
        return self.find(locator.home_login)

    def home_register(self):
        return self.find(locator.home_register)

    def home_welcome_message(self):
        return self.find(locator.home_welcome_message)

    def home_description(self):
        return self.find(locator.home_description)

    def assert_home_buttons(self):
        self.home_login()
        self.home_description()
        self.home_welcome_message()
        self.home_register()
        self.navbar.navbar_myflaskapp()
        self.navbar.navbar_Home()
        self.navbar.navbar_About()
        self.navbar.navbar_Articles()
        self.navbar.navbar_Login()
        return self.navbar.navbar_Register()
