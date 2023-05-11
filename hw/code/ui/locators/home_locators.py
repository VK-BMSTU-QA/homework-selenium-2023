
from ui.locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By


class HomeLocators(BaseLocators):
    def __init__(self):
        super(HomeLocators, self).__init__()

    def CATEGORY_SELECTOR_MENU(self, index):
        return (By.XPATH, '//div[@id="catalog"]' +
                f'/a[@class="item-top-cards text-normal-default"][{index}]')

    def GET_CATEGORY_NAME(self, index):
        return (By.XPATH, '//div[@id="catalog"]' +
                f'/a[@class="item-top-cards text-normal-default"]{index}'
                '/div[@id="mainpage_top-category"]')

    GET_CATEGORIES_CONTAINER = (By.ID, 'catalog')

    GET_COUNT_CONTAINER = (
        By.XPATH, '//div[@class="item-card__block__button-add-to-cart"]'
    )

    GET_PLUS_BUTTON = (
        By.XPATH, '//button[contains(@data-selection, "itemcard_button-plus_cart/")]'
    )

    GET_MINUS_BUTTON = (
        By.XPATH, '//button[contains(@data-selection, "itemcard_button-minus_cart/")]'
    )

    GET_ITEM_COUNT_IN_CART = (
        By.XPATH, '//div[@class="catalog__amount-selector__amount"]' +
        '/span[contains(@data-selection, "itemcard_item-count/")]'
    )

    GET_PHOTO = (
        By.XPATH, '//div[@class="item-card"]' +
        '/div[@class="item-card__top"]' +
        '/a[@class="text-normal-small content__sales-image link__no-color"]' +
        '/img[@class="item-card__image"]')
