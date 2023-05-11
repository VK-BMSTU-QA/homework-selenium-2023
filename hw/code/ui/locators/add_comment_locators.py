from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class AddCommentLocators(BaseLocators):
    def __init__(self):
        super(AddCommentLocators, self).__init__()

    COMMENT_BLOCK_TITLE = (
        By.CLASS_NAME, 'comment-page-main__header-name-button'
    )

    GET_COUNT_CONTAINER = (
        By.XPATH, '//div[@id="product-block-button-add-to-cart"]'
    )

    GET_PLUS_BUTTON = (
        By.XPATH, '//button[contains(@id, "button-plus_cart")]'
    )

    GET_MINUS_BUTTON = (
        By.XPATH, '//button[contains(@id, "button-minus_cart")]'
    )

    GET_ITEM_COUNT_IN_CART = (
        By.XPATH, '//div[@class="add-to-cart-button_amount-selector__amount"]'
    )

    GET_PHOTO = (
        By.CLASS_NAME, 'product-page-main__photo'
    )

    SUBMIT_COMMENT_BUTTON = (
        By.XPATH, '//button[@id="add-comment-page__submit"]'
    )

    UNAUTH_LOGIN_LINK = (
        By.XPATH, '//div[@id="content-unAuth-page-redirect"]' +
        '/a'
    )

    COMMENT_CONS = (
        By.ID, 'textarea_cons-filed'
    )

    COMMENT_PROS = (
        By.ID, 'textarea_pros-filed'
    )

    COMMENT_OTHER = (
        By.ID, 'textarea_comment-filed'
    )

    def SELECT_STAR(self, index):
        return (
            By.XPATH, f'//label[@for="star{index}"]'
        )
