from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from locators.pageSignupLocators import SelectorsSignup
from utils.driver import dvr


class SignupPage(BasePage):
    def render_page(self):
        self.render(SelectorsSignup.URL_PAGE_SIGNUP)

    def action_registration(self, nickname, login, password, repeat_password):
        input_nickname = self.find_group((By.CLASS_NAME, SelectorsSignup.CLASS_NAME_MODAL_INPUT))[SelectorsSignup.NICKNAME_INPUT]
        input_nickname.send_keys(nickname)

        input_email = self.find_group((By.CLASS_NAME, SelectorsSignup.CLASS_NAME_MODAL_INPUT))[SelectorsSignup.EMAIL_INPUT]
        input_email.send_keys(login)

        input_password = self.find_group((By.CLASS_NAME, SelectorsSignup.CLASS_NAME_MODAL_INPUT))[SelectorsSignup.PASSWORD_INPUT]
        input_password.send_keys(password)

        input_repeat_password = self.find_group((By.CLASS_NAME, SelectorsSignup.CLASS_NAME_MODAL_INPUT))[SelectorsSignup.REPEAT_PASSWORD_INPUT]
        input_repeat_password.send_keys(repeat_password)

        self.find((By.CLASS_NAME, SelectorsSignup.CLASS_NAME_BUTTON_REG)).click()

        return input_nickname, input_email, input_password, input_repeat_password

    def get_error_massage(self):
        return self.find((By.CLASS_NAME, SelectorsSignup.CLASS_NAME_ALREADY_REGISTER)).text

    def move_to_login(self):
        btn_login = self.find((By.CLASS_NAME, SelectorsSignup.CLASS_BUTTON_OPEN_LOGIN_WINDOW))
        btn_login.click()
        current__url = dvr.get_instance().current_url

        return current__url
