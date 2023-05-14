from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver import dvr


class BasePage(object):
    driver = dvr.get_instance()

    def render(self, url):
        self.driver.maximize_window()
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def wait_hide(self, locator, timeout=None):
        return self.wait(timeout).until(EC.invisibility_of_element_located(locator))

    def find(self, locator, timeout=None):
        if timeout is None:
            timeout = 10
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def del_session(self):
        return self.driver.delete_all_cookies()
