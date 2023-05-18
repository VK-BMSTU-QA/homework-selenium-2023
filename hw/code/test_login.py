from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from utils.driver import dvr

class TestLogin(BasePage):
    LOGIN = 'Qwe123@a.a'
    PASSWD = 'Qwe123@a.a'
    CLASS_BUTTON_OPEN_REG_WINDOW = 'modal__login__switch__btn'
    X_BUTTON_OPEN_REG_WINDOW = "/html/body/div/div[1]/div/div/div/div[2]/div/a"
    X_INPUT_EMAIL = "//input[@placeholder='Укажите адрес электронной почты']"
    X_INPUT_PASSWORD = "//input[@placeholder='Введите пароль']"
    X_BUTTON_LOGIN = "//button[contains(text(), 'Войти')]"
    CLASS_WRONG_INPUT = 'modal__input_red_border'
    CLASS_MODAL = 'modal__background'
    URL_PAGE_LOGIN = f'{BasePage.DOMAIN}/login/'
    URL_PAGE_SIGNUP = f'{BasePage.DOMAIN}/signup/'

    def test_redirect_signup(self):
        self.render(self.URL_PAGE_LOGIN)

        btn_login = self.find((By.XPATH, self.X_BUTTON_OPEN_REG_WINDOW), 10)
        btn_login.click()
        pattern = self.URL_PAGE_SIGNUP
        current__url = dvr.get_instance().current_url
        if (pattern != current__url):
            raise Exception("wrong redirect", pattern, current__url)

    def test_invalid_emeil(self):
        self.render(self.URL_PAGE_LOGIN)
        wrong_email = '123456'

        input_email = self.find((By.XPATH, self.X_INPUT_EMAIL))
        input_email.send_keys(wrong_email)
        input_password = self.find((By.XPATH, self.X_INPUT_PASSWORD)).send_keys(self.PASSWD)

        self.find((By.XPATH, self.X_BUTTON_LOGIN)).click()

        is_wrong = self.CLASS_WRONG_INPUT in input_email.get_attribute("class").split()
        if (is_wrong != True):
            raise Exception("wrong check", input_email, wrong_email)

    def test_invalid_password(self):
        self.render(self.URL_PAGE_LOGIN)
        wrong_password = '123456'

        input_email = self.find((By.XPATH, self.X_INPUT_EMAIL)).send_keys(self.LOGIN)
        input_password = self.find((By.XPATH, self.X_INPUT_PASSWORD))
        input_password.send_keys(wrong_password)

        self.find((By.XPATH, self.X_BUTTON_LOGIN)).click()

        is_wrong = self.CLASS_WRONG_INPUT in input_password.get_attribute("class").split()
        if (is_wrong != True):
            raise Exception("wrong check", input_password, input_password)

    def test_correct_login(self):
        self.render(self.URL_PAGE_LOGIN)

        self.find((By.XPATH, self.X_INPUT_EMAIL)).send_keys(self.LOGIN)
        self.find((By.XPATH, self.X_INPUT_PASSWORD)).send_keys(self.PASSWD)

        self.find((By.XPATH, self.X_BUTTON_LOGIN)).click()
        try:
            self.find((By.CLASS, self.CLASS_MODAL))
            raise Exception('unreachable code')
        except:
            None
