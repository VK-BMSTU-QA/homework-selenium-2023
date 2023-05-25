import os

from selenium.webdriver.common.by import By

from utils.base_page import BasePage


class HelperAuth(BasePage):
    CLASS_BUTTON_OPEN_MODAL = 'header__login__btn'
    CLASS_BUTTON_OPEN_REG_WINDOW = 'modal__login__switch__btn'
    CLASS_NAME_BUTTON_REG = "modal__input__button-auth"
    CLASS_NAME_BUTTON_LOGIN = "modal__input__button-auth"

    CLASS_NAME_NO_USER = 'js-modal__input__error'
    CLASS_NAME_MODAL_INPUT = 'js-modal__input'
    NICKNAME_INPUT = 0
    EMAIL_INPUT = 1
    PASSWORD_INPUT = 2
    REPEAT_PASSWORD_INPUT = 3

    EMAIL_INPUT_LOGIN = 0
    PASSWORD_INPUT_LOGIN = 1

    def __init__(self):
        self.NICKNAME = os.environ.get("NICKNAME")

        self.LOGIN = os.environ.get("LOGIN")

        self.PASSWD = os.environ.get("PASSWORD")

        self.IS_REGISTERED = False
        self.IS_LOGIN = False

    def register(self):
        self.render(f'/signup/')

        input_nickname = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.NICKNAME_INPUT]
        input_nickname.send_keys(self.NICKNAME)
        input_email = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.EMAIL_INPUT]
        input_email.send_keys(self.LOGIN)
        input_password = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.PASSWORD_INPUT]
        input_password.send_keys(self.PASSWD)
        input_repeat_password = self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.REPEAT_PASSWORD_INPUT]
        input_repeat_password.send_keys(self.PASSWD)

        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REG)).click()

        self.IS_REGISTERED = True
        self.IS_LOGIN = True

    def login(self):
        if self.IS_LOGIN:
            return

        self.render('/')
        self.find((By.CLASS_NAME, self.CLASS_BUTTON_OPEN_MODAL), 10).click()

        self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.EMAIL_INPUT_LOGIN].send_keys(self.LOGIN)

        self.find_group((By.CLASS_NAME, self.CLASS_NAME_MODAL_INPUT))[self.PASSWORD_INPUT_LOGIN].send_keys(self.PASSWD)

        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_LOGIN)).click()
        try:
            err = self.find((By.CLASS_NAME, self.CLASS_NAME_NO_USER), 4).text
            if err == 'Такой пользователь не зарегистирован':
                self.register()
        except:
            self.IS_LOGIN = True

    def logout(self):
        self.del_session()


helper = HelperAuth()


def needed_auth(method):
    def wrapper(*args, **kwargs):
        helper.login()
        return method(*args, **kwargs)

    return wrapper
