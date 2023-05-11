from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from contextlib import contextmanager

from BasePage import BasePage
import os
import time

class HelperLogin(BasePage):
    CLASS_BUTTON_OPEN_MODAL = 'header__login__btn'
    CLASS_BUTTON_OPEN_REG_WINDOW = 'modal__login__switch__btn'
    X_INPUT_NICKNAME = "//input[@placeholder='Введите имя пользователя']"
    X_INPUT_EMAIL = "//input[@placeholder='Укажите адрес электронной почты']"
    X_INPUT_PASSWORD = "//input[@placeholder='Введите пароль']"
    X_INPUT_REPEAT_PASSWORD = "//input[@placeholder='Подтвердите пароль']"
    X_BUTTON_REG = "//button[contains(text(), 'Зарегистрироваться')]"
    X_BUTTON_LOGIN = "//button[contains(text(), 'Войти')]"

    def __init__(self, url):
        self.url = url
        self.LOGIN = 'HW3testname@gmail.com' #os.environ.get('LOGIN')
        self.PASSWD = 'HW3testname' #os.environ.get('PASSWORD')
        self.is_registered = False
        self.is_logined = False

    def register(self):
       
        NICKNAME = 'Admin'

        self.render(self.url)
        btn_modal = self.find((By.CLASS_NAME, self.CLASS_BUTTON_OPEN_MODAL), 10)
        btn_modal.click()

        btn_reg = self.find((By.CLASS_NAME, self.CLASS_BUTTON_OPEN_REG_WINDOW), 10)
        btn_reg.click()

        input_nickname = self.find((By.XPATH, self.X_INPUT_NICKNAME)).send_keys(NICKNAME)
        input_email = self.find((By.XPATH, self.X_INPUT_EMAIL)).send_keys(self.LOGIN)
        input_password = self.find((By.XPATH, self.X_INPUT_PASSWORD)).send_keys(self.PASSWD)
        input_repeat_password = self.find((By.XPATH, self.X_INPUT_REPEAT_PASSWORD)).send_keys(self.PASSWD)

        self.find((By.XPATH, self.X_BUTTON_REG)).click()

        self.is_registered = True

    def login(self):
        self.render(self.url)
        btn_modal = self.find((By.CLASS_NAME, self.CLASS_BUTTON_OPEN_MODAL), 10)
        btn_modal.click()

        input_email = self.find((By.XPATH, self.X_INPUT_EMAIL))
        input_email.send_keys(self.LOGIN)
        input_password = self.find((By.XPATH, self.X_INPUT_PASSWORD)).send_keys(self.PASSWD)

        self.find((By.XPATH, self.X_BUTTON_LOGIN)).click()
        try:
            err = self.find((By.XPATH, '/html/body/div/div[1]/div/div/div/div[1]/form/div[1]/div'), 2).text
            if err == 'Такой пользователь не зарегистирован':
                self.register()
        except:
            self.is_logined = True

    def logout(self):
        self.del_session()
