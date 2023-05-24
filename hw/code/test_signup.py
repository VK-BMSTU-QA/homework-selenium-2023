from selenium.webdriver.common.by import By
import unittest

from utils.base_page import BasePage
from utils.driver import dvr


class SignupPageParams:
    URL_PAGE_LOGIN = 'login'
    URL_PAGE_SIGNUP = '/signup/'

    CLASS_BUTTON_OPEN_LOGIN_WINDOW = 'modal__login__switch__btn'
    CLASS_NAME_MODAL_INPUT = 'js-modal__input'
    NICKNAME_INPUT = 0
    EMAIL_INPUT = 1
    PASSWORD_INPUT = 2
    REPEAT_PASSWORD_INPUT = 3
    CLASS_NAME_BUTTON_REG = "modal__input__button-auth"
    CLASS_NAME_ALREADY_REGISTER = "js-modal__input__error"
    CLASS_WRONG_INPUT = 'modal__input_red_border'


class PageSignup(BasePage):
    def start(self):
        self.render(SignupPageParams.URL_PAGE_SIGNUP)

    def action_registration(self, nickname, login, password, repeat_password):
        input_nickname = self.find_group((By.CLASS_NAME, SignupPageParams.CLASS_NAME_MODAL_INPUT))[SignupPageParams.NICKNAME_INPUT]
        input_nickname.send_keys(nickname)

        input_email = self.find_group((By.CLASS_NAME, SignupPageParams.CLASS_NAME_MODAL_INPUT))[SignupPageParams.EMAIL_INPUT]
        input_email.send_keys(login)

        input_password = self.find_group((By.CLASS_NAME, SignupPageParams.CLASS_NAME_MODAL_INPUT))[SignupPageParams.PASSWORD_INPUT]
        input_password.send_keys(password)

        input_repeat_password = self.find_group((By.CLASS_NAME, SignupPageParams.CLASS_NAME_MODAL_INPUT))[SignupPageParams.REPEAT_PASSWORD_INPUT]
        input_repeat_password.send_keys(repeat_password)

        self.find((By.CLASS_NAME, SignupPageParams.CLASS_NAME_BUTTON_REG)).click()

        return input_nickname, input_email, input_password, input_repeat_password

    def get_error_massage(self):
        return self.find((By.CLASS_NAME, SignupPageParams.CLASS_NAME_ALREADY_REGISTER)).text

    def move_to_login(self):
        btn_login = self.find((By.CLASS_NAME, SignupPageParams.CLASS_BUTTON_OPEN_LOGIN_WINDOW))
        btn_login.click()
        current__url = dvr.get_instance().current_url

        return current__url


class TestSignup(unittest.TestCase, PageSignup):
    LOGIN = 'Qwe123@a.a'
    PASSWD = 'Qwe123@a.a'
    NICKNAME = 'Admin'

    EXPECTED_ERROR = "Пользователь с таким email уже зарегистрирован", "wrong register msg"
    EXPECTED_LOGIN = "login"

    def test_redirect_login(self):
        self.start()

        actual_position = self.move_to_login()

        self.assertIn(self.EXPECTED_LOGIN, actual_position, "wrong redirect")

    def test_short_nick(self):
        self.start()

        short_nick = '123'

        input_nickname, _, _, _ = self.action_registration(short_nick, self.LOGIN, self.PASSWD, self.PASSWD)

        is_wrong = SignupPageParams.CLASS_WRONG_INPUT in input_nickname.get_attribute("class").split()
        self.assertTrue(is_wrong, "wrong check")

    def test_invalid_email(self):
        self.start()

        wrong_email = '123456'

        _, input_email, _, _ = self.action_registration(self.NICKNAME, wrong_email, self.PASSWD, self.PASSWD)

        is_wrong = SignupPageParams.CLASS_WRONG_INPUT in input_email.get_attribute("class").split()
        self.assertTrue(is_wrong, "wrong check")

    def test_invalid_password(self):
        self.start()

        wrong_password = 'abcds'

        _, _, input_password, _ = self.action_registration(self.NICKNAME, self.LOGIN, wrong_password, wrong_password)

        is_wrong_input_password = SignupPageParams.CLASS_WRONG_INPUT in input_password.get_attribute("class").split()
        is_wrong_input_repeat_password = SignupPageParams.CLASS_WRONG_INPUT in input_password.get_attribute("class").split()

        self.assertTrue(is_wrong_input_password or is_wrong_input_repeat_password, "wrong check")

    def test_such_user_exist(self):
        self.start()

        self.action_registration(self.NICKNAME, self.LOGIN, self.PASSWD, self.PASSWD)

        msg_already_register = self.get_error_massage()

        self.assertIn(msg_already_register, self.EXPECTED_ERROR)
