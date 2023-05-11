from selenium.webdriver.common.by import By
from ui.hrefs import Hrefs


class BaseLocators():
    def __init__(self):
        self.hrefs = Hrefs()

        self.HEADER_ERROR_MESSAGE = (By.ID, 'header_error-message')

    def GET_BY_TEXT(self, text):
        return (
            By.XPATH, f'//*[contains(text(), "{text}")]'
        )
