import pytest
from ui.pages.card_popup_page import CardPopupPage
from ui.base_case.base_case import BaseCase
from ui.locators.base_locators import BaseLocators


class TestCardPopup(BaseCase):
    paths = BaseLocators().hrefs
    popUpHeader = 'Мои карты'

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver):
        self.driver = driver
        self.page = CardPopupPage(driver, self.path.domain + self.path.cart)

    def test_open_card_popup(self):
        self.page.authorize()
        self.page.add_product_after_login()
        self.page.click(self.page.cart_locators.BUTTON_EDIT_CARD)
        assert self.page.find(self.page.popup_locators.POPUP).is_displayed()
        assert self.page.find(
            self.page.popup_locators.POPUP_HEADER).text == self.popUpHeader

    def test_add_card_button(self):
        self.page.authorize()
        self.page.add_product_after_login()
        self.page.click(self.page.cart_locators.BUTTON_EDIT_CARD)
        self.page.click(self.page.popup_locators.ADD_BUTTON_IN_POPUP)
        assert self.page.is_url(self.paths.user)

    def test_cancel_button(self):
        self.page.authorize()
        self.page.add_product_after_login()
        self.page.click(self.page.cart_locators.BUTTON_EDIT_CARD)
        self.page.click(self.page.popup_locators.BUTTON_CANCEL)
        assert not self.page.find(self.page.popup_locators.POPUP).is_displayed()

    def test_apply_button(self):
        self.page.authorize()
        self.page.add_product_after_login()
        self.page.click(self.page.cart_locators.BUTTON_EDIT_CARD)
        self.page.click(self.page.popup_locators.BUTTON_APPLY)
        assert not self.page.find(self.page.popup_locators.POPUP).is_displayed()

    def test_select_card(self):
        self.page.authorize()
        self.page.add_product_after_login()
        self.page.click(self.page.cart_locators.BUTTON_EDIT_CARD)
        select_card = self.page.find(self.page.locators.CARD).get_attribute('value')
        self.page.click(self.page.locators.CARD)
        self.page.click(self.page.popup_locators.BUTTON_APPLY)
        assert self.page.find(self.page.cart_locators.SELECT_CARD).text == select_card
