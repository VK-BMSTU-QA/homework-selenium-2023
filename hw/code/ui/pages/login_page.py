from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage

class LoginPage(BasePage):
    url = 'https://95.163.213.142/'

    def login(self, user, password):
        self.click((By.XPATH, '/html/body/div[1]/div[4]/div'), 15)
        self.find((By.ID, 'login_form__email_login')).send_keys(user)
        self.find((By.ID, 'login_form__password')).send_keys(password)

        self.click((By.ID, 'login_form__submit_button'))

        return MainPage(self.driver)