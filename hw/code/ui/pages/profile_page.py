from ui.pages.base_page import BasePage
from ui.locators.locators import ProfileLocators
from ui.locators.locators import BasePageLocators
from ui.pages.login_page import LoginPage
import time


class ProfilePage(BasePage):
    locators = ProfileLocators
    PATH = 'user'

    def login(self):
        LoginPage.login(self)
        self.click(BasePageLocators.USER_BUTTON)

    def logout(self):
        self.click(BasePageLocators.USER_BUTTON)
        self.click(BasePageLocators.LOGOUT_BUTTON)
        self.refresh()

    def change_password(self, ex, new):
        self.click(ProfileLocators.CHANGE_PASSWORD_BUTTON)
        input = self.find(ProfileLocators.CURRENT_PASSWORD_INPUT)
        input.send_keys(ex)
        input = self.find(ProfileLocators.NEW_PASSWORD_INPUT)
        input.send_keys(new)
        input = self.find(ProfileLocators.REPEAT_PASSWORD_INPUT)
        input.send_keys(new)
        self.click(ProfileLocators.USER_INFO_POPUP_APPLY_BUTTON)
