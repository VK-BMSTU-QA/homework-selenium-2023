from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage

class LoginPage(BasePage):
    url = 'https://target.my.com/'

    def login(self, user, password):
        self.click((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]'), 15)
        self.find((By.NAME, 'email')).send_keys(user)
        self.find((By.NAME, 'password')).send_keys(password)

        self.click((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[4]/div[1]'))

        return MainPage(self.driver)