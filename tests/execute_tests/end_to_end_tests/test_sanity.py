def test_sanity(app):
    register_button = app.assert_home_buttons()
    register_button.click()
    app.wait_until_page_loads()

    app.driver.save_screenshot('verygood.png')
