from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class FooterLocators(BaseLocators):
    def __init__(self):
        super(FooterLocators, self).__init__()

    GET_LOGO = (
        By.XPATH, '//div[@class="footer__grid"]/div/a' +
        '/img[@class="footer__logo logo-reazon"]'
    )
