import pytest

from ui.fixtures import get_driver
from ui.pages.base_case import BaseCase, cookies, credentials
from ui.pages.login_page import LoginPage


class TestLogin(BaseCase):
    authorize = False
    
    def test_login(self, credentials):
        page = LoginPage(self.driver)
        page.login(*credentials)
