from ui.locators import locators
from ui.pages.base_page import BasePage
from ui.base_case.base_case import BaseCase
from ui.locators.base_locators import BaseLocators


class CartPage(BasePage):
    paths = BaseLocators().hrefs
    auth_locators = locators.AuthorizeLocators
    favourites_locators = locators.FavouritesLocators
    header_locators = locators.HeaderLocators
    category_phones_locators = locators.CategoryPhonesLocators
    home_locators = locators.HomeLocators
    locators = locators.CartLocators

    def add_product(self):
        self.click(self.locators.EMPTY_CART_MESSAGE_LINK)
        self.click(self.category_phones_locators.BUTTON_ADD_TO_CART)
        self.click(self.header_locators.BUTTON_CART)

    def add_product_after_login(self):
        self.click(self.home_locators.BUTTON_ADD_TO_CART)
        self.click(self.header_locators.BUTTON_CART)

    def get_item_count_price(self):
        item_price = int(self.find(self.locators.ITEM_PRICE).text.split(' ')[0])
        item_count = int(self.find(self.locators.ITEM_COUNT).text)
        return item_price, item_count

    def get_total_price(self):
        return int(self.find(self.locators.TOTAL_PRICE).text.split(' ')[0])

    def get_discount(self):
        return int(self.find(self.locators.DISCOUNT).text.split(' ')[0])

    def get_price_without_discount(self):
        return int(self.find(self.locators.PRICE_WITHOUT_DISCOUNT).text.split(' ')[0])

    def authorize(self):
        self.click(self.header_locators.BUTTON_LOGIN)
        self.send_keys(self.auth_locators.INPUT_EMAIL, BaseCase.EMAIL)
        self.send_keys(self.auth_locators.INPUT_PASSWORD, BaseCase.PASSWORD)
        self.click(self.auth_locators.LOGIN_BUTTON_FORM)
        self.waitUntilVisible(self.home_locators.GET_CATEGORIES_CONTAINER)
