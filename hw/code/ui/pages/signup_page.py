from ui.pages.base_page import BasePage
from ui.locators.signup_locators import SignupPageLocators
from ui.locators.home_locators import HomeLocators


class SignupPage(BasePage):

    homeLocators = HomeLocators()

    def __init__(self, driver):
        super(SignupPage, self).__init__(driver)
        self.locators = SignupPageLocators()
        self.url = self.locators.hrefs.domain + self.locators.hrefs.signup

    def signup(self, usname, email, passwd, passwd2):
        usname_field = self.find(self.locators.USERNAME_INPUT_SIGNUP_PAGE)
        usname_field.clear()
        usname_field.send_keys(usname)

        email_field = self.find(self.locators.EMAIL_INPUT_SIGNUP_PAGE)
        email_field.clear()
        email_field.send_keys(email)

        pwd_field = self.find(self.locators.PASSWORD_INPUT_SIGNUP_PAGE)
        pwd_field.clear()
        pwd_field.send_keys(passwd)

        pwd2_field = self.find(self.locators.REPEAT_PASSWORD_INPUT_SIGNUP_PAGE)
        pwd2_field.clear()
        pwd2_field.send_keys(passwd2)

        self.find(self.locators.SIGN_UP_BUTTON_SIGNUP_PAGE).click()
