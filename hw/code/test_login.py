import time, os

import creds

import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from ui.fixtures import get_driver
from ui.pages.base_page import BasePage, PageNotOpenedExeption, ElementCheckException


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.login_page = LoginPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.refresh()

@pytest.fixture(scope='session')
def credentials():
    script_dir = os.path.dirname(__file__)
    rel_path = "/creds"
    with open(script_dir + rel_path, 'r') as f:
        user = f.readline().strip()
        password = f.readline().strip()

    return user, password


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config['browser'])
    driver.get(config['url'])
    login_page = LoginPage(driver)
    login_page.login(*credentials)
    WebDriverWait(driver, timeout=5).until(lambda d: d.get_cookie('session_id'))
    cookies = driver.get_cookies()
    driver.quit()
    return cookies

class MainPage(BasePage):
    url = 'https://95.163.213.142/'

class LoginPage(BasePage):
    url = 'https://95.163.213.142/'

    def login(self, user, password):
        self.click((By.XPATH, '/html/body/div[1]/div[4]/div'), 15)
        self.find((By.ID, 'login_form__email_login')).send_keys(user)
        self.find((By.ID, 'login_form__password')).send_keys(password)

        self.click((By.XPATH, '//*[@id="login_form__submit_button"]'))

        return MainPage(self.driver)

class TestLogin(BaseCase):
    authorize = False
    
    def test_login(self, credentials):
        page = LoginPage(self.driver)
        page.login(*credentials)
