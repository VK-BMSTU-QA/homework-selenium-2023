from ui.pages.signup_page import SignupPage
from ui.fixtures import get_driver
from ui.pages.header import Header
import uuid
from ui.locators.base_locators import BaseLocators
from ui.tabTitles import TabTitles


class CaseFail:
    def __init__(self, usname, email, password, password2, message=''):
        self.usname = usname
        self.email = email
        self.password = password
        self.password2 = password2
        self.message = message


class TestSignup():
    driver = get_driver(browser_name='chrome')
    signupPage = SignupPage(driver)
    header = Header(driver)
    baseLocators = BaseLocators()

    userName = 'a'
    baseEmail = 'test@'
    password = '123456'

    tabTitles = TabTitles()

    failCases = [
        CaseFail("", "b", "c", "d", "Поле обязательно должно быть заполнено"),
        CaseFail("a", "", "c", "d", "Поле обязательно должно быть заполнено"),
        CaseFail("a", "b", "c", "d", "Неверный формат почты"),
        CaseFail("a", "b@test", "", "d", "Поле обязательно должно быть заполнено"),
        CaseFail("a", "b@test", "12", "d", "Пароль должен содержать минимум 6 символов"),
        CaseFail("a", "b@test", "123456", "", "Введенные пароли не совпадают"),
        CaseFail("a", "b@test", "123456", "123457", "Введенные пароли не совпадают"),
        CaseFail("a", "test@test", "123457", "123457", "Неверная почта или пароль"),
    ]

    @signupPage.render_decorator
    def test_redirect_to_login_sign_up_page(self):
        self.signupPage.find(self.signupPage.locators.SIGNIN_LINK).click()
        assert self.driver.current_url == (
            self.baseLocators.hrefs.domain + self.baseLocators.hrefs.login)
        self.signupPage.render(self.signupPage.url)

    @signupPage.render_decorator
    def test_title_sign_up(self):
        self.signupPage.waitUntilVisible(self.signupPage.locators.SIGNIN_LINK)
        assert self.driver.title == TabTitles.signup

    @signupPage.render_decorator
    def test_failed_sign_up(self):
        for case in self.failCases:
            self.signupPage.signup(case.usname, case.email, case.password, case.password2)
            assert self.signupPage.find(
                self.signupPage.locators.ERROR).text == case.message

    @signupPage.render_decorator
    def test_successful_sign_up(self):
        uid = uuid.uuid4()
        test_email = self.baseEmail + str(uid.int)
        self.signupPage.signup(self.userName, test_email, self.password, self.password)
        self.signupPage.waitUntilVisible(
            self.signupPage.homeLocators.GET_CATEGORIES_CONTAINER)

        assert self.driver.current_url == (
            self.baseLocators.hrefs.domain + self.baseLocators.hrefs.home)

        self.header.findUserPageButton()
        self.header.logout()
