import os
import time

from selenium.webdriver.common.by import By

from base_page import BasePage
from const import DOMAIN


class HelperAuth(BasePage):
    CLASS_BUTTON_OPEN_MODAL = 'header__login__btn'
    CLASS_BUTTON_OPEN_REG_WINDOW = 'modal__login__switch__btn'
    X_INPUT_NICKNAME = "//input[@placeholder='Введите имя пользователя']"
    X_INPUT_EMAIL = "//input[@placeholder='Укажите адрес электронной почты']"
    X_INPUT_PASSWORD = "//input[@placeholder='Введите пароль']"
    X_INPUT_REPEAT_PASSWORD = "//input[@placeholder='Подтвердите пароль']"
    X_BUTTON_REG = "//button[contains(text(), 'Зарегистрироваться')]"
    X_BUTTON_LOGIN = "//button[contains(text(), 'Войти')]"

    def __init__(self, domain):
        self.DOMAIN = domain

        self.NICKNAME = 'Admin'

        self.LOGIN = os.environ.get("LOGIN")  # 'HW3testname@gmail.com'
        if self.LOGIN is None:
            self.LOGIN = "HW3testname@gmail.com"

        self.PASSWD = os.environ.get("PASSWORD")  # 'HW3testname'
        if self.PASSWD is None:
            self.PASSWD = "HW3testname"

        self.IS_REGISTERED = False
        self.IS_LOGIN = False

    def register(self):
        time.sleep(1);
        self.render(self.DOMAIN)
        btn_modal = self.find((By.CLASS_NAME, self.CLASS_BUTTON_OPEN_MODAL), 10)
        btn_modal.click()

        self.find((By.CLASS_NAME, self.CLASS_BUTTON_OPEN_REG_WINDOW), 10).click()

        self.find((By.XPATH, self.X_INPUT_NICKNAME)).send_keys(self.NICKNAME)
        self.find((By.XPATH, self.X_INPUT_EMAIL)).send_keys(self.LOGIN)
        self.find((By.XPATH, self.X_INPUT_PASSWORD)).send_keys(self.PASSWD)
        self.find((By.XPATH, self.X_INPUT_REPEAT_PASSWORD)).send_keys(self.PASSWD)

        self.find((By.XPATH, self.X_BUTTON_REG)).click()

        self.IS_REGISTERED = True

    def login(self):
        if self.IS_LOGIN:
            return

        self.render(self.DOMAIN)
        self.find((By.CLASS_NAME, self.CLASS_BUTTON_OPEN_MODAL), 10).click()

        self.find((By.XPATH, self.X_INPUT_EMAIL)).send_keys(self.LOGIN)

        self.find((By.XPATH, self.X_INPUT_PASSWORD)).send_keys(self.PASSWD)

        self.find((By.XPATH, self.X_BUTTON_LOGIN)).click()
        try:
            err = self.find((By.XPATH, '/html/body/div/div[1]/div/div/div/div[1]/form/div[1]/div'), 2).text
            if err == 'Такой пользователь не зарегистирован':
                self.register()
        except:
            self.IS_LOGIN = True

    def logout(self):
        self.del_session()


helper = HelperAuth(DOMAIN)


def needed_auth(method):
    def wrapper(*args, **kwargs):
        helper.login()
        return method(*args, **kwargs)

    return wrapper
