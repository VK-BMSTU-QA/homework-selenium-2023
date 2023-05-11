from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class FavouritesLocators(BaseLocators):
    def __init__(self):
        super(FavouritesLocators, self).__init__()

    GET_FAVOURITES_LABEL = (
        By.XPATH, '//label[@class="product-page-header__selection"]'
    )

    GET_FAVOURITES_INPUT = (
        By.ID, 'favourite-opt_cart'
    )
