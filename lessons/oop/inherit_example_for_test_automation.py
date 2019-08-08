class Page:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def wait_until_page_is_ready(self):
        pass

    def find(self, locator, timeout=30):
        return self.driver.find_element(locator, timeout)

    def click(self, locator, timeout=30):
        element = self.driver.click(locator, timeout)
        self.wait_until_page_is_ready()
        return element


class AboutPage(Page):
    def get_news(self):
        return self.find(('test-id', 'news')).text

    def go_to_login(self):
        self.click(('test-id', 'login'))
        self.find(('test-id', 'login-page'))


class LoginPage(Page):
    def __call__(self):
        pass


class App:
    def __init__(self, driver):
        self.login = LoginPage(driver, 'www.login.com')
        self.about = AboutPage(driver, 'www.about.com')


def test_sanity(app: App):
    app.about.get_news()
    app.about.go_to_login()
    app.login()

