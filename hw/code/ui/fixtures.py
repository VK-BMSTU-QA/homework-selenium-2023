import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def _options(headless=False):
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--incognito")
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-xss-auditor")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-webgl")
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--no-proxy-server')
    options.add_argument("--disable-extensions")
    options.set_capability(
        "goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"}
    )
    options.page_load_strategy = 'normal'

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("window-size=1920x1080")

    return options


def get_driver(browser_name):
    headless = True

    if browser_name == 'chrome':
        browser = webdriver.Chrome(
            service=ChromeService(
                executable_path=ChromeDriverManager().install()),
            options=_options(headless=headless))
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(
            service=FirefoxService(
                executable_path=GeckoDriverManager().install()))
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')

    if headless is True:
        browser.set_window_size(1920, 1080)
    else:
        browser.maximize_window()

    return browser


@pytest.fixture()
def driver(browser_config):
    driver = get_driver(browser_config)
    yield driver
    driver.quit()
