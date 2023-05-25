from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from locators.pageLoginLocators import SelectorsLogin
from utils.driver import dvr


class PageLogin(BasePage): 
    def render_page(self):
        self.render(SelectorsLogin.URL_PAGE_LOGIN)

    def action_login(self, login, password):
        input_email = self.find_group((By.CLASS_NAME, SelectorsLogin.CLASS_NAME_MODAL_INPUT))[SelectorsLogin.EMAIL_INPUT]
        input_email.send_keys(login)

        input_password = self.find_group((By.CLASS_NAME, SelectorsLogin.CLASS_NAME_MODAL_INPUT))[SelectorsLogin.PASSWORD_INPUT]
        input_password.send_keys(password)

        self.find((By.CLASS_NAME, SelectorsLogin.CLASS_NAME_BUTTON_LOGIN)).click()

        return input_email, input_password

    def move_to_signup(self):
        btn_reg = self.find((By.XPATH, SelectorsLogin.X_BUTTON_OPEN_REG_WINDOW))
        btn_reg.click()
        current__url = dvr.get_instance().current_url

        return current__url
    
