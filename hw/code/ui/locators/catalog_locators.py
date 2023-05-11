from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class CatalogLocators(BaseLocators):

    def __init__(self):
        super(CatalogLocators, self).__init__()

    GET_FAVOURITES_LABEL = (
        By.XPATH, '//label[@class="catalog_button-favourite"]'
    )

    GET_FAVOURITES_INPUT = (
        By.XPATH, '//input[@class="favourite-opt"]'
    )

    GET_CATEGORY_NAME = (
        By.XPATH, '//div[@id="catalog_content"]' +
        '/div[@class="catalog__category-name text-normal-huge"]'
    )

    GET_COUNT_CONTAINER = (
        By.XPATH, '//div[@class="catalog-item-card__sale-block"]' +
        '/div[@id="catalog_block-button-add-to-cart"]' +
        '/div[contains(@id, "catalog_button-add-to-cart/")]'
    )

    GET_PLUS_BUTTON = (
        By.XPATH, '//div[@class="catalog-item-card__sale-block"]' +
        '/div[@id="catalog_block-button-add-to-cart"]' +
        '/div[@class="catalog__amount-selector"]' +
        '/button[contains(@id, "catalog_button-plus_cart/")]'
    )

    GET_MINUS_BUTTON = (
        By.XPATH, '//div[@class="catalog-item-card__sale-block"]' +
        '/div[@id="catalog_block-button-add-to-cart"]' +
        '/div[@class="catalog__amount-selector"]'
        '/button[contains(@id, "catalog_button-minus_cart/")]'
    )

    GET_ITEM_COUNT_IN_CART = (
        By.XPATH, '//div[@class="catalog-item-card__sale-block"]' +
        '/div[@id="catalog_block-button-add-to-cart"]' +
        '/div[@class="catalog__amount-selector"]' +
        '/div[@class="catalog__amount-selector__amount"]'
    )

    SORT_RATING_BUTTON = (
        By.ID, 'catalog_sort-rating'
    )

    SORT_PRICE_BUTTON = (
        By.ID, 'catalog_sort-price'
    )

    SORT_ORDER_ICON = (
        By.ID, 'catalog_sort-img'
    )

    GET_PICTURE = (
        By.XPATH, '//div[@id="catalog_item-pic-block"]' +
        '/a/img[@class="catalog-item-card__pic-block__pic"]'
    )

    GET_TEXT_LINK = (
        By.XPATH, '//div[@id="items-block"]'
        + '/div[@class="catalog-item-card"]'
        + '/div[@class="catalog-item-card__description-block"]' +
        '/div[@id="catalog_item-title-block"]'
        + '/a[@id="catalog_item-title"]'
    )

    GET_IMG_LINK = (
        By.XPATH, '//div[@id="items-block"]'
        + '/div[@class="catalog-item-card"]' +
        '/div[@id="catalog_item-pic-block"]/a'
    )
