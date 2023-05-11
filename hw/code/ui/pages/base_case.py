import pytest 
from _pytest.fixtures import FixtureRequest

from selenium.webdriver.support.wait import WebDriverWait

from ui.fixtures import get_driver
from ui.pages.login_page import LoginPage

import creds

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
    return creds.email, creds.password


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