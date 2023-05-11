from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class ProductTitleLocators(BaseLocators):
    def __init__(self):
        super(ProductTitleLocators, self).__init__()

    GET_PRODUCT_TITLE = (
        By.XPATH,
        '//a[@class="text-normal-very-large' +
        ' link__no-color comment-page-header__title"]')
    GET_CATEGORY_BUTTON = (
        By.XPATH, '//div[@class="product-page-header product-page-color-jet-black"]' +
        '/a[@class="text-normal-default link__no-color"]'
    )

    GET_RATING_NUMBER = (
        By.XPATH, '//a[@class="product-page-header__rating link__no-color"]' +
        '/span[@class="text-normal-large-normal"]'
    )

    GET_RATING_LINK = (
        By.XPATH, '//a[@class="product-page-header__rating link__no-color"]'
    )

    GET_PHOTO = (
        By.CLASS_NAME, 'product-page-main__photo'
    )
