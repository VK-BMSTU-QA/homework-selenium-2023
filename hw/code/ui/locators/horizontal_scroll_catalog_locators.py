from ui.locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By


class HorizontalScrollCatalogLocators(BaseLocators):
    def __init__(self):
        super(HorizontalScrollCatalogLocators, self).__init__()

    def GET_SCROLL_CONTAINER(self, index):
        return (
            By.XPATH, f'//div[@class="content__horizontal-scroll"][{index}]'
        )

    def GET_IMAGE_OF_ITEM_BY_INDEX(self, containerIndex, itemIndex):
        return (
            By.XPATH, f'//div[@class="content__horizontal-scroll"][{containerIndex}]' +
            f'/div[{itemIndex}]/div[@class="item-card__top"]/a/img'
        )

    def GET_ITEM_CONTAINER_BY_INDEX(self, containerIndex, itemIndex):
        return (
            By.XPATH, f'//div[@class="content__horizontal-scroll"][{containerIndex}]' +
            f'/div[{itemIndex}]'
        )

    SCROLL_TO_RIGHT_BUTTON = (
        By.XPATH, '//div[@class="right-arrow"]' +
        '/button[@class="arrow-button text-normal-default"]'
    )

    SCROLL_TO_LEFT_BUTTON = (
        By.XPATH, '//div[@class="left-arrow"]' +
        '/button[@class="arrow-button text-normal-default"]'
    )

    GET_COUNT_CONTAINER = (
        By.XPATH, '//div[@class="item-card__block__button-add-to-cart"][1]'
    )

    GET_PLUS_BUTTON = (
        By.XPATH, '//button[contains(@data-selection, "itemcard_button-plus_cart/")][1]'
    )

    GET_MINUS_BUTTON = (
        By.XPATH, '//button[contains(@data-selection, "itemcard_button-minus_cart/")][1]'
    )

    GET_ITEM_COUNT_IN_CART = (
        By.XPATH, '//span[contains(@data-selection, "itemcard_item-count/")][1]'
    )

    GET_RATING_NUMBER = (
        By.XPATH, '//a[@class="item-card__rating link__no-color"][1]' +
        '/span[@class="text-normal-default__bold"]'
    )

    GET_RATING_LINK = (
        By.XPATH, '//a[@class="item-card__rating link__no-color"][1]'
    )

    GET_ITEM_TITLE = (
        By.XPATH, '//a[@class="text-normal-default item-card__title link__no-color"]'
    )

    GET_PHOTO = (
        By.XPATH, '//a[@class="text-normal-small' +
        ' content__sales-image link__no-color"][1]' +
        '/img[@class="item-card__image"][1]'
    )
