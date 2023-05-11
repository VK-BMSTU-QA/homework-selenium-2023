import allure

from ui.fixtures import get_driver
from ui.pages.login_page import LoginPage
from ui.pages.header import Header


class TestLogin():
    driver = get_driver(browser_name='chrome')
    loginPage = LoginPage(driver)
    header = Header(driver)

    @allure.feature('Test Login')
    @allure.story('Login')
    @loginPage.render_decorator
    def test_login(self):
        with allure.step('findLoginPageButton'):
            self.header.findLoginPageButton()

        with allure.step('login'):
            self.loginPage.login()

        with allure.step('findUserPageButton'):
            self.header.findUserPageButton()

        with allure.step('logout'):
            self.header.logout()
