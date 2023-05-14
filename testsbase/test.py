import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from driver import dvr
from base_page import BasePage
from const import *
from helper_auth import needed_auth


class TestFilmPageAuthorized(BasePage):
    X_BUTTON_PLUS = '/html/body/div/div/div[1]/div/div[2]/div[7]/div/a/div'
    X_BUTTON_BOOKMARK = '/html/body/div/div/div[1]/div/div[2]/div[7]/a[2]/div'
    X_BUTTON_TRAILER = '/html/body/div/div/div[1]/div/div[2]/div[7]/a[1]/div'
    X_PRODUCER = '/html/body/div/div/div[1]/div/div[2]/div[5]/div[2]'
    X_PRODUCER_ON_PAGE = '/html/body/div/div/div[1]/div/div/div/div[1]'
    X_TOSTER = '/html/body/div/div[2]'
    X_TRAILER_CONTAINER = '/html/body/div/div[1]/div/div/iframe'
    X_BUTTON_RATE_9 = '/html/body/div/div/div[2]/div[2]/div[2]/form/div/div[2]/div[1]/button[2]'
    X_BUTTON_RATE_1 = '/html/body/div/div/div[2]/div[2]/div[2]/form/div/div[2]/div[1]/button[10]'
    X_BUTTON_RATE_CONTAINER = '/html/body/div/div/div[2]/div[2]/div[2]/form/div/div[2]/div[1]'
    X_BUTTON_RATE_DELETE = '/html/body/div/div/div[2]/div[2]/div[2]/form/div/div[4]/button'
    X_BUTTON_REVIEW = '/html/body/div/div/div[4]/div[1]/div/div/div[1]/a/div'
    X_BUTTON_REVIEW_CONTAINER = '/html/body/div/div[1]/div/div/div/div'
    X_BUTTON_CHOOSE_TYPE = '/html/body/div/div[1]/div/div/div/div/form/div[1]/div/div'
    X_BUTTON_NEGATIVE_TYPE = '/html/body/div/div[1]/div/div/div/div/form/div[1]/div/ul/li[3]'
    X_BUTTON_NEUTRAL_TYPE = '/html/body/div/div[1]/div/div/div/div/form/div[1]/div/ul/li[2]'
    X_BUTTON_POSITIVE_TYPE = '/html/body/div/div[1]/div/div/div/div/form/div[1]/div/ul/li[1]'
    X_INPUT_TITLE = '/html/body/div/div[1]/div/div/div/div/form/div[2]/input'
    X_INPUT_TEXT = '/html/body/div/div[1]/div/div/div/div/form/div[3]/textarea'
    X_BUTTON_SEND_REVIEW = '/html/body/div/div[1]/div/div/div/div/form/button'
    X_UPPER_REVIEW = '/html/body/div/div/div[4]/div[1]/div/div/div[2]/div[1]/div'
    X_UPPER_REVIEW_TITLE = '/html/body/div/div/div[4]/div[1]/div/div/div[2]/div[1]/div/div[2]'
    X_UPPER_REVIEW_TEXT = '/html/body/div/div/div[4]/div[1]/div/div/div[2]/div[1]/div/div[3]'
    TEXT = '200IQ text'
    TITLE = 'title'

    @needed_auth
    def test_click_set_rate(self):
        self.render(f'{DOMAIN}/film/1')
        self.find((By.XPATH, self.X_BUTTON_RATE_9)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

    @needed_auth
    def test_click_update_rate(self):
        self.render(f'{DOMAIN}/film/1')
        self.find((By.XPATH, self.X_BUTTON_RATE_9)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

        self.find((By.XPATH, self.X_BUTTON_RATE_1)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

    @needed_auth
    def test_click_delete_rate(self):
        self.render(f'{DOMAIN}/film/1')
        self.find((By.XPATH, self.X_BUTTON_RATE_9)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

        self.find((By.XPATH, self.X_BUTTON_RATE_DELETE)).click()
        self.wait_hide((By.XPATH, self.X_BUTTON_RATE_DELETE))

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

    @needed_auth
    def test_click_review(self):
        self.render(f'{DOMAIN}/film/1')
        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()
        self.find((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER))

    @needed_auth
    def test_send_review(self):
        self.render(f'{DOMAIN}/film/1')
        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()
        self.find((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER))

        self.find((By.XPATH, self.X_BUTTON_CHOOSE_TYPE)).click()
        self.find((By.XPATH, self.X_BUTTON_NEGATIVE_TYPE)).click()

        self.find((By.XPATH, self.X_INPUT_TITLE)).send_keys(self.TITLE)
        self.find((By.XPATH, self.X_INPUT_TEXT)).send_keys(self.TEXT)

        self.find((By.XPATH, self.X_BUTTON_SEND_REVIEW)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

    @needed_auth
    def test_error_review(self):
        self.render(f'{DOMAIN}/film/1')
        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()
        self.find((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER))

        self.find((By.XPATH, self.X_INPUT_TITLE)).send_keys(self.TITLE)
        self.find((By.XPATH, self.X_INPUT_TEXT)).send_keys(self.TEXT)

        self.find((By.XPATH, self.X_BUTTON_SEND_REVIEW)).click()

        try:
            self.wait_hide((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER), 2)
        except:
            self.find((By.XPATH, self.X_BUTTON_SEND_REVIEW))

    @needed_auth
    def test_check_correct_review(self):
        self.render(f'{DOMAIN}/film/1')

        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()
        self.find((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER))

        self.find((By.XPATH, self.X_BUTTON_CHOOSE_TYPE)).click()
        self.find((By.XPATH, self.X_BUTTON_NEGATIVE_TYPE)).click()

        self.find((By.XPATH, self.X_INPUT_TITLE)).send_keys(self.TITLE)
        self.find((By.XPATH, self.X_INPUT_TEXT)).send_keys(self.TEXT)

        self.find((By.XPATH, self.X_BUTTON_SEND_REVIEW)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

        title = self.find((By.XPATH, self.X_UPPER_REVIEW_TITLE)).text
        if title != self.TITLE:
            raise Exception("names does not equal", title, self.TITLE)

        text = self.find((By.XPATH, self.X_UPPER_REVIEW_TEXT)).text
        if text != self.TEXT:
            raise Exception("names does not equal", text, self.TEXT)

