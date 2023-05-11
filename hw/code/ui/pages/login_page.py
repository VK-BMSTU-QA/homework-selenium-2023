from ui.pages.base_page import BasePage
from ui.locators.locators import ProfileLocators
from ui.base_case.base_case import BaseCase
from ui.locators.login_locators import LoginPageLocators
from ui.locators.home_locators import HomeLocators
from ui.pages.header import Header

import os


class LoginPage(BasePage):
    email = os.getenv('LOGIN_DEFAULT')
    pwd = os.getenv('PWD_DEFAULT')
    userName = 'Sheesh'

    homeLocators = HomeLocators()
    profileLocators = ProfileLocators()

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.locators = LoginPageLocators()
        self.url = self.locators.hrefs.domain + self.locators.hrefs.login
        self.header = Header(driver)

    def login(self):
        self.loginData(self.email, self.pwd)

        self.waitUntilVisible(self.homeLocators.GET_CATEGORIES_CONTAINER)

    def loginData(self, email, passwd):
        email_field = self.find(
            self.locators.EMAIL_INPUT_LOGIN_PAGE)

        pwd_field = self.find(
            self.locators.PASSWORD_INPUT_LOGIN_PAGE)

        pwd_field.send_keys(passwd)

        self.find(self.locators.SIGN_IN_BUTTON_LOGIN_PAGE).click()

        email_field.clear()
        email_field.send_keys(email)

        pwd_field = self.find(
            self.locators.PASSWORD_INPUT_LOGIN_PAGE)
        pwd_field.clear()
        pwd_field.send_keys(passwd)

        self.find(self.locators.SIGN_IN_BUTTON_LOGIN_PAGE).click()

    def loginProfile(self):
        self.header.findLoginPageButton().click()

        self.loginData(BaseCase.EMAIL_PROFILE, BaseCase.PASSWORD_PROFILE)

        self.header.findUserPageButton().click()

        self.waitUntilVisible(self.profileLocators.USER_AVATAR)
