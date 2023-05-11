import time

from selenium.webdriver.remote.webelement import WebElement
import urllib.parse as urlparse
from ui.locators import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ui.locators.base_locators import BaseLocators


class PageNotOpenedExeption(Exception):
    pass


class StaleTimeoutExeption(Exception):
    pass


class BasePage(object):

    baseLocators = BaseLocators()
    default_timeout = 15
    mini_timeout = 3
    locators = locators.BasePageLocators()
    PATH = ""

    def is_opened(self, url, timeout=default_timeout):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == url:
                return True

        raise PageNotOpenedExeption(
            f'{url} did not open in {timeout} sec,' +
            f'current url {self.driver.current_url}')

    def __init__(self, driver, url=""):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.BASE_URL = url

    def open(self, timeout=default_timeout):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
        self.is_opened(url, timeout)

    def render(self, url):
        self.driver.get(url)

    def render_page(self):
        self.render(self.url)
        self.is_opened(self.url)

    def render_decorator(self, func):
        def wrapper(newSelf):
            self.render_page()
            func(newSelf)
        return wrapper

    def wait(self, timeout=5):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=10):
        self.waitUntilVisible(locator)
        return self.wait(timeout + self.mini_timeout).until(
            EC.presence_of_element_located(locator))

    def scrollToLocator(self, locator):
        element = self.driver.find_element(locator[0], locator[1])
        self.actions.scroll_to_element(element).perform()
        self.scrollByAmount(int(element.size['height']))

    def scrollByAmount(self, amount):
        self.actions.scroll_by_amount(0, amount).perform()

    def hover(self, element):
        self.actions.move_to_element(element).perform()

    def waitUntilVisible(self, selector, timeout=5):
        self.wait(timeout).until(EC.presence_of_element_located(selector))

    def waitUntilInvisible(self, selector, timeout=5):
        self.wait(timeout).until(EC.invisibility_of_element_located(selector))

    def checkErrorMessage(self, errorMessage):
        errorMessageElement = self.find(
            self.baseLocators.HEADER_ERROR_MESSAGE)

        self.waitUntilVisible(self.baseLocators.HEADER_ERROR_MESSAGE, 1)
        assert errorMessage in errorMessageElement.get_attribute('innerText')

        self.waitUntilInvisible(self.baseLocators.HEADER_ERROR_MESSAGE, 6)

    def getTabTitle(self):
        return self.driver.title.strip()

    def getInnerText(self, selector, timeout=mini_timeout):
        return self.find(selector, timeout).get_attribute('innerText').strip()

    def getHref(self, selector, timeout=mini_timeout):
        return self.find(selector, timeout).get_attribute('href')

    def getSrc(self, selector, timeout=mini_timeout):
        return self.find(selector, timeout).get_attribute('src')

    def waitUntilClickableElement(self, selector, timeout=5):
        self.wait(timeout).until(EC.element_to_be_clickable(selector))

    def checkPhoto(self, selector):
        photoURL = self.getSrc(selector)

        self.render(photoURL)

        self.is_opened(photoURL)

    def is_url(self, path):
        return EC.url_matches(urlparse.urljoin(self.BASE_URL, path))

    def click(self, locator, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            elem = self.wait_to_be_clickable(
                locator, timeout - (time.time() - started))
            elem.click()
            return elem

        raise StaleTimeoutExeption(
            f"{locator} did not clickable or have been throwing" +
            f"StaleElementReferenceExceptions in {timeout} sec," +
            " current url {self.driver.current_url}")

    def send_keys(self, locator, keys, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            elem = self.wait_to_be_clickable(
                locator, timeout - (time.time() - started))
            elem.clear()
            elem.send_keys(keys)
            return elem

        raise StaleTimeoutExeption(
            f"{locator} did not clickable or have been throwing" +
            f" StaleElementReferenceExceptions in {timeout} sec," +
            " current url {self.driver.current_url}")

    def wait_to_be_clickable(self, locator, timeout=default_timeout):
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    def get_attribute(self, locator, attribute, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            content = self.find(locator).get_attribute(attribute)
            return content

        raise StaleTimeoutExeption(
            f"{locator} did not clickable or have been throwing" +
            f"StaleElementReferenceExceptions in {timeout} sec," +
            f" current url {self.driver.current_url}")

    def get_text(self, locator, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            content = self.find(locator).getText()
            return content

        raise StaleTimeoutExeption(
            f"{locator} did not clickable or have been throwing" +
            f"StaleElementReferenceExceptions in {timeout} sec," +
            f" current url {self.driver.current_url}")

    def refresh(self, timeout=default_timeout):
        self.driver.refresh()
