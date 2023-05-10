from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from contextlib import contextmanager

from BasePage import BasePage
import os
import time

class HelperLogin(BasePage):
    def __init__(self, url):
        self.url = url
        self.LOGIN = os.environ.get('LOGIN')
        self.PASSWD = os.environ.get('PASSWORD')
        self.is_registered = False
        self.is_logined = False

    def register(self):
        X_BUTTON_OPEN_MODAL = '/html/body/div/header/a[5]'
        X_BUTTON_OPEN_REG_WINDOW = '/html/body/div/div[1]/div/div/div/div[2]/div/a'
        X_INPUT_NICKNAME = '/html/body/div/div[1]/div/div/div/div[2]/form/div[1]/input'
        X_INPUT_EMAIL = '/html/body/div/div[1]/div/div/div/div[2]/form/div[2]/input'
        X_INPUT_PASSWORD = '/html/body/div/div[1]/div/div/div/div[2]/form/div[3]/input'
        X_INPUT_REPEAT_PASSWORD = '/html/body/div/div[1]/div/div/div/div[2]/form/div[4]/input'
        X_BUTTON_REG = '/html/body/div/div[1]/div/div/div/div[2]/form/button'
        NICKNAME = 'Admin'

        self.render(self.url)
        btn_modal = self.find((By.XPATH, X_BUTTON_OPEN_MODAL), 10)
        btn_modal.click()

        btn_reg = self.find((By.XPATH, X_BUTTON_OPEN_REG_WINDOW), 10)
        btn_reg.click()

        input_nickname = self.find((By.XPATH, X_INPUT_NICKNAME)).send_keys(NICKNAME)
        input_email = self.find((By.XPATH, X_INPUT_EMAIL)).send_keys(self.LOGIN)
        input_password = self.find((By.XPATH, X_INPUT_PASSWORD)).send_keys(self.PASSWD)
        input_repeat_password = self.find((By.XPATH, X_INPUT_REPEAT_PASSWORD)).send_keys(self.PASSWD)

        self.find((By.XPATH, X_BUTTON_REG)).click()

        self.is_registered = True

    def login(self):
        X_BUTTON_OPEN_MODAL = '/html/body/div/header/a[5]'
        X_INPUT_EMAIL = '/html/body/div/div[1]/div/div/div/div[1]/form/div[1]/input'
        X_INPUT_PASSWORD = '/html/body/div/div[1]/div/div/div/div[1]/form/div[2]/input'
        X_BUTTON_LOGIN = '/html/body/div/div[1]/div/div/div/div[1]/form/button'

        self.render(self.url)
        btn_modal = self.find((By.XPATH, X_BUTTON_OPEN_MODAL), 10)
        btn_modal.click()

        input_email = self.find((By.XPATH, X_INPUT_EMAIL)).send_keys(self.LOGIN)
        input_password = self.find((By.XPATH, X_INPUT_PASSWORD)).send_keys(self.PASSWD)

        self.find((By.XPATH, X_BUTTON_LOGIN)).click()
        try:
            err = self.find((By.XPATH, '/html/body/div/div[1]/div/div/div/div[1]/form/div[1]/div'), 2).text
            if err == 'Такой пользователь не зарегистирован':
                self.register()
        except:
            self.is_logined = True

    def logout(self):
        self.del_session()
        # X_PROFILE1 = '/html/body/div/header/div/div[1]/img'
        # X_BUTTON_LOGOUT = '/html/body/div/header/div/div[2]/a[4]'
        # menu = self.find((By.XPATH, X_PROFILE1))
        # actions = ActionChains(self.driver)
        # actions.move_to_element(menu)
        # actions.click_and_hold()
        # actions.perform()
        # self.find((By.XPATH, X_BUTTON_LOGOUT)).click()
