import pytest
import os

from ui.locators.base_locators import BaseLocators
from ui.pages.base_page import BasePage

from dotenv import load_dotenv
load_dotenv()


class BaseCase:
    EMAIL = os.getenv('EMAIL_CART')
    PASSWORD = os.getenv('PASSWORD_CART')
    EMAIL_PROFILE = os.getenv('LOGIN_PROFILE')
    PASSWORD_PROFILE = os.getenv('PWD_PROFILE')
    path = BaseLocators().hrefs

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver):
        self.driver = driver
        self.page = BasePage(driver, self.path.domain + self.path.home)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.page.open()
