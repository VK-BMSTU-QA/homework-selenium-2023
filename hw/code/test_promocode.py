import pytest
from ui.pages.promocode_page import PromocodePage
from ui.base_case.base_case import BaseCase


class TestPromocode(BaseCase):
    enterPromoMessage = 'Введите промокод'
    prohibitedSymbols = 'Введены недопустимые символы'

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver):
        self.driver = driver
        self.page = PromocodePage(driver, self.path.domain + self.path.cart)

    def test_empty_input(self):
        self.page.authorize()
        self.page.add_product_after_login()
        self.page.click(self.page.locators.BUTTON_APPLY)
        assert self.page.find(self.page.locators.MESSAGE).text == self.enterPromoMessage

    def test_error_symbols(self):
        self.page.authorize()
        self.page.add_product_after_login()
        self.page.send_keys(self.page.locators.INPUT, '{1111]')
        self.page.click(self.page.locators.BUTTON_APPLY)
        assert self.page.find(self.page.locators.MESSAGE).text == self.prohibitedSymbols
