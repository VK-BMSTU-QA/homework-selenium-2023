from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class ViewCommentLocators(BaseLocators):
    def __init__(self):
        super(ViewCommentLocators, self).__init__()

    ADD_COMMENT_BUTTON = (
        By.ID, 'add-comment-btn'
    )

    GET_PRODUCT_NAME = (
        By.XPATH, '//a[@class="text-normal-very-large' +
        ' link__no-color comment-page-header__title"]'
    )

    GET_PHOTO_REDIRECT_HREF = (
        By.XPATH, '//div[@class="comment-page-header' +
        ' content-comment-page-block-background' +
        ' comment-page-header-main_padding"]' +
        '/a[@href=""]'
    )

    GET_PHOTO = (
        By.CLASS_NAME, 'comment-page-header__photo'
    )

    COMMENT_CONTENT = (
        By.CLASS_NAME, 'comment__content'
    )
