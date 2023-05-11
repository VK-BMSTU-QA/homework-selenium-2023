from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class SignupPageLocators(BaseLocators):
    def __init__(self):
        super(SignupPageLocators, self).__init__()

    USERNAME_INPUT_SIGNUP_PAGE = (By.NAME, 'username')

    EMAIL_INPUT_SIGNUP_PAGE = (By.NAME, 'email')

    PASSWORD_INPUT_SIGNUP_PAGE = (By.NAME, 'password')

    REPEAT_PASSWORD_INPUT_SIGNUP_PAGE = (By.NAME, 'repeatPassword')

    SIGN_UP_BUTTON_SIGNUP_PAGE = (By.ID, 'submit-result')

    ERROR = (By.ID, 'error-text')

    SIGNIN_LINK = (By.LINK_TEXT, 'Войти')
