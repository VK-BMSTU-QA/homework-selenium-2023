from contextlib import contextmanager
import allure
import pytest
from _pytest.fixtures import FixtureRequest
import os
import shutil
import sys
import time
import random

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Driver import dvr

class BasePage(object):
    driver = dvr.get_instance()

    def render(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    # def navigate(self, url):
    #     self.driver.navigate().to(url)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def wait_hide(self, locator, timeout=None):
        return self.wait(timeout).until(EC.invisibility_of_element_located(locator))


    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def del_session(self):
        return self.driver.delete_all_cookies()
