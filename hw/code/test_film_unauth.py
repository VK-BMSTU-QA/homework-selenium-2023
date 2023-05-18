import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from utils.driver import dvr
from utils.base_page import BasePage
from utils.helper_auth import needed_auth

class SelectorsFilmUnauth():
    CLASS_NAME_BUTTON_PLUS = 'about-film__button_plus'
    CLASS_NAME_BUTTON_BOOKMARK = 'about-film__button_bookmark'
    CLASS_NAME_BUTTON_TRAILER = 'js-btn-watch-trailer'
    CLASS_NAME_PRODUCER = 'about-film__director'
    CLASS_NAME_PRODUCER_ON_PAGE = 'actor-profile__name'
    CLASS_NAME_TOSTER = 'js-errorMessage'
    CLASS_NAME_TRAILER_CONTAINER = 'trailer__iframe'
    CLASS_NAME_BUTTON_REVIEW = 'js-list-reviews__btn-write-review'

class TestFilmPageUnauthorized(BasePage):

    def test_click_producer(self):
        self.render(f'/film/1')

        prod = self.find((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_PRODUCER), 3).text.strip()
        self.find((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_PRODUCER), 5).click()

        prod_on_page = self.find((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_PRODUCER_ON_PAGE), 3).text.strip()
        if prod != prod_on_page:
            raise Exception("names does not equal", prod, prod_on_page)

    def test_click_plus_unauth(self):
        self.render(f'/film/1')

        self.find((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_BUTTON_PLUS)).click()
        self.find((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_TOSTER))
        self.wait_hide((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_TOSTER))

        self.find((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_BUTTON_BOOKMARK)).click()
        self.find((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_TOSTER))
        self.wait_hide((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_TOSTER))

    def test_click_trailer(self):
        self.render(f'/film/1')
        self.find((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_BUTTON_TRAILER)).click()
        self.find((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_TRAILER_CONTAINER))

    def test_click_review_unauth(self):
        self.render(f'/film/1')

        self.find((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_BUTTON_REVIEW)).click()

        self.find((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_TOSTER))
        self.wait_hide((By.CLASS_NAME, SelectorsFilmUnauth.CLASS_NAME_TOSTER))
