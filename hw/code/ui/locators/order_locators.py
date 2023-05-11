from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class OrderPageLocators(BaseLocators):
    def __init__(self):
        super(OrderPageLocators, self).__init__()

        self.BUTTON_MAKE_ORDER = (By.ID, 'summary_cart__create-order-button')

        self.BUTTON_DENY_ORDER = (By.CLASS_NAME, 'button-cancel-order')

        self.BUTTON_NO_AUTH_REDIRECT = (By.ID, 'content-unAuth-page-redirect')

        self.BUTTON_EMPTY_ORDERS_REDIRECT = (By.ID, 'content-unAuth-page-redirect')

        self.MESSAGE = (By.ID, 'server-error__text_')

        self.ORDER_STATUS = (By.XPATH, '//span[starts-with(@id, "order-status/")]')
