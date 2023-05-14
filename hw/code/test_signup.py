from selenium.webdriver.common.by import By

from base_page import BasePage
from driver import dvr
from const import *

class TestSignup(BasePage):
    LOGIN = 'Qwe123@a.a'
    PASSWD = 'Qwe123@a.a'
    CLASS_BUTTON_OPEN_LOGIN_WINDOW = 'modal__login__switch__btn'
    CLASS_NAME_MODAL_INPUT = 'js-modal__input'
    NICKNAME_INPUT = 0
    EMAIL_INPUT = 1
    PASSWORD_INPUT = 2
    REPEAT_PASSWORD_INPUT = 3
    CLASS_NAME_BUTTON_REG = "modal__input__button-auth"
    CLASS_NAME_ALREADY_REGISTER = "js-modal__input__error"
    CLASS_WRONG_INPUT = 'modal__input_red_border'
    NICKNAME = 'Admin'
    URL_PAGE_LOGIN = f'{DOMAIN}/login/'
    URL_PAGE_SIGNUP = f'{DOMAIN}/signup/'

    def test_redirect_login(self):
        self.render(self.URL_PAGE_SIGNUP)

        btn_login = self.find((By.CLASS_NAME, self.CLASS_BUTTON_OPEN_LOGIN_WINDOW), 10)
        btn_login.click()
        pattern = self.URL_PAGE_LOGIN
        current__url = dvr.get_instance().current_url
        if (pattern != current__url):
            raise Exception("wrong redirect", pattern, current__url)

    def test_short_nick(self):
        self.render(self.URL_PAGE_SIGNUP)
        short_nick = '123'

        input_nickname = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.NICKNAME_INPUT]
        input_nickname.send_keys(short_nick)
        input_email = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.EMAIL_INPUT]
        input_email.send_keys(self.LOGIN)
        input_password = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.PASSWORD_INPUT]
        input_password.send_keys(self.PASSWD)
        input_repeat_password = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.REPEAT_PASSWORD_INPUT]
        input_repeat_password.send_keys(self.PASSWD)

        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REG)).click()

        is_wrong = self.CLASS_WRONG_INPUT in input_nickname.get_attribute("class").split()
        if (is_wrong != True):
            raise Exception("wrong check", input_nickname, short_nick)

    def test_invalid_emeil(self):
        self.render(self.URL_PAGE_SIGNUP)
        wrong_email = '123456'

        input_nickname = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.NICKNAME_INPUT]
        input_nickname.send_keys(self.NICKNAME)
        input_email = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.EMAIL_INPUT]
        input_email.send_keys(wrong_email)
        input_password = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.PASSWORD_INPUT]
        input_password.send_keys(self.PASSWD)
        input_repeat_password = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.REPEAT_PASSWORD_INPUT]
        input_repeat_password.send_keys(self.PASSWD)

        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REG)).click()

        is_wrong = self.CLASS_WRONG_INPUT in input_email.get_attribute("class").split()
        if (is_wrong != True):
            raise Exception("wrong check", input_email, wrong_email)

    def test_invalid_password(self):
        self.render(self.URL_PAGE_SIGNUP)
        wrong_password = 'abcds'

        input_nickname = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.NICKNAME_INPUT]
        input_nickname.send_keys(self.NICKNAME)
        input_email = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.EMAIL_INPUT]
        input_email.send_keys(self.LOGIN)
        input_password = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.PASSWORD_INPUT]
        input_password.send_keys(wrong_password)
        input_repeat_password = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.REPEAT_PASSWORD_INPUT]
        input_repeat_password.send_keys(wrong_password)

        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REG)).click()

        is_wrong_input_password = self.CLASS_WRONG_INPUT in input_password.get_attribute("class").split()
        is_wrong_input_repeat_password = self.CLASS_WRONG_INPUT in input_password.get_attribute("class").split()
        if (is_wrong_input_password != True or is_wrong_input_repeat_password != True):
            raise Exception("wrong check", input_password, wrong_password)

    def test_correct_register(self):
        self.render(self.URL_PAGE_SIGNUP)

        input_nickname = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.NICKNAME_INPUT]
        input_nickname.send_keys(self.NICKNAME)
        input_email = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.EMAIL_INPUT]
        input_email.send_keys(self.LOGIN)
        input_password = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.PASSWORD_INPUT]
        input_password.send_keys(self.PASSWD)
        input_repeat_password = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.REPEAT_PASSWORD_INPUT]
        input_repeat_password.send_keys(self.PASSWD)


        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REG)).click()
        msg_already_register = self.find((By.CLASS_NAME, self.CLASS_NAME_ALREADY_REGISTER)).text
        if (msg_already_register != "Пользователь с таким email уже зарегистрирован"):
            raise Exception("wrong register msg", msg_already_register,
                            "Пользователь с таким email уже зарегистрирован")
