import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from utils.driver import dvr
from utils.base_page import BasePage
from utils.helper_auth import needed_auth


class TestFilmPageAuthorized(BasePage):
    CLASS_NAME_TOSTER = 'js-errorMessage'
    CLASS_NAME_STAR = 'js-rating__star'
    RATE_9 = 1
    RATE_1 = 9
    CLASS_NAME_CHOOSE_TYPE_REVIEW = 'js-input-review__select-item'
    POSITIVE_TYPE = 0
    NEUTRAL_TYPE = 1
    NEGATIVE_TYPE = 2
    CLASS_NAME_BUTTON_RATE_DELETE = 'rating__setted-delete-btn'
    CLASS_NAME_BUTTON_REVIEW = 'rating__button-write-review'
    CLASS_NAME_BUTTON_REVIEW_CONTAINER = 'input-review__container'
    CLASS_NAME_BUTTON_CHOOSE_TYPE = 'js-input-review__select-head'
    CLASS_NAME_INPUT_TITLE = 'input-review__input-title'
    CLASS_NAME_INPUT_TEXT = 'js-input-review__input-text'
    CLASS_NAME_BUTTON_SEND_REVIEW = 'modal__input__button-review'
    CLASS_NAME_REVIEW_TEXT = 'review__text'
    CLASS_NAME_REVIEW_TITLE = 'review__title'
    TEXT = '200IQ text'
    TITLE = 'title'

    @needed_auth
    def test_click_set_rate(self):
        self.render(f'{self.DOMAIN}/film/1')
        self.find_group((By.CLASS_NAME, self.CLASS_NAME_STAR))[self.RATE_9].click()

        self.find((By.CLASS_NAME, self.CLASS_NAME_TOSTER))
        self.wait_hide((By.CLASS_NAME, self.CLASS_NAME_TOSTER))

    @needed_auth
    def test_click_update_rate(self):
        self.render(f'{self.DOMAIN}/film/1')
        self.find_group((By.CLASS_NAME, self.CLASS_NAME_STAR))[self.RATE_9].click()

        self.find((By.CLASS_NAME, self.CLASS_NAME_TOSTER))
        self.wait_hide((By.CLASS_NAME, self.CLASS_NAME_TOSTER))

        self.find_group((By.CLASS_NAME, self.CLASS_NAME_STAR))[self.RATE_1].click()

        self.find((By.CLASS_NAME, self.CLASS_NAME_TOSTER))
        self.wait_hide((By.CLASS_NAME, self.CLASS_NAME_TOSTER))

    @needed_auth
    def test_click_delete_rate(self):
        self.render(f'{self.DOMAIN}/film/1')
        self.find_group((By.CLASS_NAME, self.CLASS_NAME_STAR))[self.RATE_9].click()

        self.find((By.CLASS_NAME, self.CLASS_NAME_TOSTER))
        self.wait_hide((By.CLASS_NAME, self.CLASS_NAME_TOSTER))

        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_RATE_DELETE)).click()
        self.wait_hide((By.CLASS_NAME, self.CLASS_NAME_BUTTON_RATE_DELETE))

        self.find((By.CLASS_NAME, self.CLASS_NAME_TOSTER))
        self.wait_hide((By.CLASS_NAME, self.CLASS_NAME_TOSTER))

    @needed_auth
    def test_click_review(self):
        self.render(f'{self.DOMAIN}/film/1')
        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REVIEW)).click()
        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REVIEW_CONTAINER))

    @needed_auth
    def test_send_review(self):
        self.render(f'{self.DOMAIN}/film/1')
        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REVIEW)).click()
        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REVIEW_CONTAINER))

        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_CHOOSE_TYPE)).click()
        self.find_group((By.CLASS_NAME, self.CLASS_NAME_CHOOSE_TYPE_REVIEW))[self.NEGATIVE_TYPE].click()


        self.find((By.CLASS_NAME, self.CLASS_NAME_INPUT_TITLE)).send_keys(self.TITLE)
        self.find((By.CLASS_NAME, self.CLASS_NAME_INPUT_TEXT)).send_keys(self.TEXT)

        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_SEND_REVIEW)).click()

        self.find((By.CLASS_NAME, self.CLASS_NAME_TOSTER))
        self.wait_hide((By.CLASS_NAME, self.CLASS_NAME_TOSTER))

    @needed_auth
    def test_error_review(self):
        self.render(f'{self.DOMAIN}/film/1')
        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REVIEW)).click()
        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REVIEW_CONTAINER))

        self.find((By.CLASS_NAME, self.CLASS_NAME_INPUT_TITLE)).send_keys(self.TITLE)
        self.find((By.CLASS_NAME, self.CLASS_NAME_INPUT_TEXT)).send_keys(self.TEXT)

        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_SEND_REVIEW)).click()

        try:
            self.wait_hide((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REVIEW_CONTAINER), 2)
        except:
            self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_SEND_REVIEW))

    @needed_auth
    def test_check_correct_review(self):
        self.render(f'{self.DOMAIN}/film/1')

        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REVIEW)).click()
        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_REVIEW_CONTAINER))

        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_CHOOSE_TYPE)).click()
        self.find_group((By.CLASS_NAME, self.CLASS_NAME_CHOOSE_TYPE_REVIEW))[self.NEGATIVE_TYPE].click()

        self.find((By.CLASS_NAME, self.CLASS_NAME_INPUT_TITLE)).send_keys(self.TITLE)
        self.find((By.CLASS_NAME, self.CLASS_NAME_INPUT_TEXT)).send_keys(self.TEXT)

        self.find((By.CLASS_NAME, self.CLASS_NAME_BUTTON_SEND_REVIEW)).click()

        self.find((By.CLASS_NAME, self.CLASS_NAME_TOSTER))
        self.wait_hide((By.CLASS_NAME, self.CLASS_NAME_TOSTER))

        title = self.find_group((By.CLASS_NAME, self.CLASS_NAME_REVIEW_TITLE))[0].text
        if title != self.TITLE:
            raise Exception("names does not equal", title, self.TITLE)

        text = self.find_group((By.CLASS_NAME, self.CLASS_NAME_REVIEW_TEXT))[0].text
        if text != self.TEXT:
            raise Exception("names does not equal", text, self.TEXT)

