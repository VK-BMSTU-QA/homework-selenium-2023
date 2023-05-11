from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class HeaderLocators(BaseLocators):

    def __init__(self):
        super(HeaderLocators, self).__init__()

        self.OPEN_LOGIN_PAGE_BUTTON = (
            By.XPATH, f'//div[@class="header__profile"]/a[@href="{self.hrefs.login}"]')

        self.OPEN_USER_PAGE_BUTTON = (
            By.XPATH, f'//div[@class="header__profile"]/a[@href="{self.hrefs.user}"]')

        self.OPEN_CART_PAGE_BUTTON = (
            By.XPATH, f'//div[@class="header__card"]/a[@href="{self.hrefs.cart}"]')

        self.OPEN_FAVOURITES_PAGE_BUTTON = (
            By.XPATH, '//div[@class="header__favourites"]/a[@href=' +
            f'"{self.hrefs.userFavorites}"]')

        self.OPEN_ORDERS_PAGE_BUTTON = (
            By.XPATH, f'//div[@class="header__order"]/a[@href="{self.hrefs.orders}"]')

        self.SIGN_OUT_POP_UP = (
            By.XPATH, '//div[@class="profile__pop-up"]'
        )

        self.SIGN_OUT_BUTTON_POP_UP = (
            By.XPATH, f'//div[@class="profile__pop-up/a[@href="{self.hrefs.logout}"]"]'
        )

        self.OPEN_CATEGORY_SELECTOR_BUTTON = (By.ID, 'header__button-catalog')

        self.GET_CATEGORIES_CONTAINER = (
            By.XPATH, '//div[@id="header__dropdown__content"]')

        self.GET_LOGO = (By.XPATH, '//div[@class="header__logotip"]/a')

    def CATEGORY_SELECTOR_MENU(self, index): return (
        By.XPATH, f'//div[@id="header__dropdown__content"]/a[{index}]')
