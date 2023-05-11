from ui.locators import locators
from ui.pages.base_page import BasePage
from ui.base_case.base_case import BaseCase
from ui.locators.home_locators import HomeLocators
from ui.locators.order_locators import OrderPageLocators


class OrdersPage(BasePage):
    
    home_locators = locators.HomeLocators
    auth_locators = locators.AuthorizeLocators
    header_locators = locators.HeaderLocators

    def __init__(self, driver):
        super(OrdersPage, self).__init__(driver)
        self.locators = OrderPageLocators()
        self.url = self.locators.hrefs.domain + self.locators.hrefs.orders

    def authorize(self, login, passwd):
        self.click(self.header_locators.BUTTON_LOGIN)
        self.send_keys(self.auth_locators.INPUT_EMAIL, login)
        self.send_keys(self.auth_locators.INPUT_PASSWORD, passwd)
        self.click(self.auth_locators.LOGIN_BUTTON_FORM)
        self.waitUntilVisible(self.home_locators.GET_CATEGORIES_CONTAINER)

    def add_product_after_login(self):
        self.click(self.home_locators.BUTTON_ADD_TO_CART)
        self.click(self.header_locators.BUTTON_CART)
