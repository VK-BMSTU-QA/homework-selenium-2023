from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class CommentTitleLocators(BaseLocators):
    def __init__(self):
        super(CommentTitleLocators, self).__init__()

    GET_COUNT_CONTAINER = (
        By.XPATH, '//div[@id="block-button-add-to-cart"]' +
        '/div[contains(@id, "button-add-to-cart/")]'
    )

    GET_PLUS_BUTTON = (
        By.XPATH, '//button[contains(@id, "button-plus_cart/")]'
    )

    GET_MINUS_BUTTON = (
        By.XPATH, '//button[contains(@id, "button-minus_cart/")]'
    )

    GET_ITEM_COUNT_IN_CART = (
        By.XPATH, '//div[@class="add-to-cart-button_amount-selector__amount"]' +
        '/span[contains(@id, "amount/")]'
    )

    GET_PHOTO = (
        By.XPATH, '//div[@class="comment-page-header' +
        ' content-comment-page-block-background' +
        ' comment-page-header-main_padding"]' +
        '/a/img[@class="comment-page-header__photo"]'
    )
