def test_sanity(app):
    register_button = app.home.assert_home_buttons()
    register_button.click()
    app.wait_until_page_loads()

    user = app.register()


def test_register_error(app):
    register_button = app.home.assert_home_buttons()
    register_button.click()
    app.wait_until_page_loads()

    user = {
        "name": "already exist",
        "email": "already exist",
        "username": "already exist",
        "password": "already exist",
        "re_password": "already exist",
    }
    app.register.with_error(user)