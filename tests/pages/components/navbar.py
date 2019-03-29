from tests.pages.components.page import Page
from tests.config.locators import locator


class NavBar(Page):
    def navbar_myflaskapp(self):
        return self.find(locator.navbar_myflaskapp)

    def navbar_Home(self):
        return self.find(locator.navbar_Home)

    def navbar_About(self):
        return self.find(locator.navbar_About)

    def navbar_Articles(self):
        return self.find(locator.navbar_Articles)

    def navbar_Login(self):
        return self.find(locator.navbar_Login)

    def navbar_Register(self):
        return self.find(locator.navbar_Register)
