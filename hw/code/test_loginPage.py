from ui.pages.login_page import LoginPage
from ui.fixtures import get_driver
from ui.pages.header import Header
from ui.locators.base_locators import BaseLocators
from ui.tabTitles import TabTitles
import os


class Case:
    def __init__(self, email, password, message=''):
        self.email = email
        self.password = password
        self.message = message


class TestLogin():
    driver = get_driver(browser_name='chrome')
    loginPage = LoginPage(driver)
    header = Header(driver)
    baseLocators = BaseLocators()
    tabTitles = TabTitles()

    failCases = [
        Case("", "b", "Поле обязательно должно быть заполнено"),
        Case("a", "b", "Неверный формат почты"),
        Case("a@a", "", "Поле обязательно должно быть заполнено"),
        Case("a@a", "123", "Пароль должен содержать минимум 6 символов"),
        Case("test@test", "123123", "Неверная почта или пароль")
    ]

    @loginPage.render_decorator
    def test_title(self):
        assert self.driver.title == self.tabTitles.login

    @loginPage.render_decorator
    def test_redirect(self):
        self.loginPage.find(self.loginPage.locators.SIGNUP_LINK).click()
        assert self.driver.current_url == (
            self.baseLocators.hrefs.domain + self.baseLocators.hrefs.signup)
        self.loginPage.render(self.loginPage.url)

    @loginPage.render_decorator
    def test_fail(self):
        for case in self.failCases:
            self.loginPage.loginData(case.email, case.password)
            assert self.loginPage.find(self.loginPage.locators.ERROR).text == case.message

    @loginPage.render_decorator
    def test_ok(self):
        self.loginPage.loginData(os.getenv('LOGIN_AUTH'), os.getenv('PWD_AUTH'))
        self.loginPage.waitUntilVisible(
            self.loginPage.homeLocators.GET_CATEGORIES_CONTAINER)
        assert self.driver.current_url == (
            self.baseLocators.hrefs.domain + self.baseLocators.hrefs.home)
        self.header.findUserPageButton()
        self.header.logout()
