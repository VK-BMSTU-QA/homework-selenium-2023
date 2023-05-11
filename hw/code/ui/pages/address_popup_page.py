from ui.locators import locators
from ui.pages.base_page import BasePage
from ui.base_case.base_case import BaseCase
from ui.locators.base_locators import BaseLocators


class AddressPopupPage(BasePage):
    paths = BaseLocators().hrefs
    cart_locators = locators.CartLocators
    header_locators = locators.HeaderLocators
    category_phones_locators = locators.CategoryPhonesLocators
    auth_locators = locators.AuthorizeLocators
    home_locators = locators.HomeLocators
    popup_locators = locators.PopupLocators
    locators = locators.AddressPopupLocators

    def add_product(self):
        self.click(self.cart_locators.EMPTY_CART_MESSAGE_LINK)
        self.click(self.category_phones_locators.BUTTON_ADD_TO_CART)
        self.click(self.header_locators.BUTTON_CART)

    def add_product_after_login(self):
        self.click(self.home_locators.BUTTON_ADD_TO_CART)
        self.click(self.header_locators.BUTTON_CART)

    def authorize(self):
        self.click(self.header_locators.BUTTON_LOGIN)
        self.send_keys(self.auth_locators.INPUT_EMAIL, BaseCase.EMAIL)
        self.send_keys(self.auth_locators.INPUT_PASSWORD, BaseCase.PASSWORD)
        self.click(self.auth_locators.LOGIN_BUTTON_FORM)
        self.waitUntilVisible(self.home_locators.GET_CATEGORIES_CONTAINER)
