from contextlib import contextmanager
import allure
import pytest
from _pytest.fixtures import FixtureRequest
import os
import shutil
import sys
import time
import random

from BasePage import BasePage
from HelperLogin import HelperLogin

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://movie-gate.online'
helper = HelperLogin(URL)


class TestLogin(BasePage):
    url = URL

    def test_login(self):
        helper.login()
        helper.logout()

class TestFilmPage(BasePage):
    X_BUTTON_PLUS = '/html/body/div/div/div[1]/div/div[2]/div[7]/div/a/div'
    X_BUTTON_BOOKMARK = '/html/body/div/div/div[1]/div/div[2]/div[7]/a[2]/div'
    X_BUTTON_TRAILER = '/html/body/div/div/div[1]/div/div[2]/div[7]/a[1]/div'
    X_PRODUCER = '/html/body/div/div/div[1]/div/div[2]/div[5]/div[2]/a'
    X_PRODUCER_ON_PAGE = '/html/body/div/div/div[1]/div/div/div/div[1]'
    X_TOSTER = '/html/body/div/div[2]'
    X_TRAILER_CONTAINER = '/html/body/div/div[1]/div/div/iframe'
    X_BUTTON_RATE_9 = '/html/body/div/div/div[2]/div[2]/div[2]/form/div/div[2]/div[1]/button[2]/div'
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

    def test_click_producer(self):
        self.render(f'{URL}/film/1')

        prod = self.find((By.XPATH, self.X_PRODUCER)).text.strip()
        self.find((By.XPATH, self.X_PRODUCER), 3).click()

        prod_on_page = self.find((By.XPATH, self.X_PRODUCER_ON_PAGE), 3).text.strip()
        if prod != prod_on_page:
            raise Exception("names does not equal", prod, prod_on_page)

    def test_click_plus_unauth(self):
        self.render(f'{URL}/film/1')
        time.sleep(4)
        self.find((By.XPATH, self.X_BUTTON_PLUS)).click()
        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

        self.find((By.XPATH, self.X_BUTTON_BOOKMARK)).click()
        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

    def test_click_trailer(self):
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_TRAILER)).click()
        self.find((By.XPATH, self.X_TRAILER_CONTAINER))

    def test_click_set_rate(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_RATE_9)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))
        helper.logout()

    def test_click_update_rate(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_RATE_9)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

        self.find((By.XPATH, self.X_BUTTON_RATE_1)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))
        helper.logout()

    def test_click_delete_rate(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_RATE_9)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

        self.find((By.XPATH, self.X_BUTTON_RATE_DELETE)).click()
        self.wait_hide((By.XPATH, self.X_BUTTON_RATE_DELETE))

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))
        helper.logout()

    def test_click_review_unauth(self):
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

    def test_click_review(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()
        self.find((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER))
        helper.logout()

    def test_click_review(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()
        self.find((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER))

        self.find((By.XPATH, self.X_BUTTON_CHOOSE_TYPE)).click()
        self.find((By.XPATH, self.X_BUTTON_NEGATIVE_TYPE)).click()

        self.find((By.XPATH, self.X_INPUT_TITLE)).send_keys(self.TITLE)
        self.find((By.XPATH, self.X_INPUT_TEXT)).send_keys(self.TEXT)

        self.find((By.XPATH, self.X_BUTTON_SEND_REVIEW)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))
        helper.logout()

    def test_error_review(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()
        self.find((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER))

        self.find((By.XPATH, self.X_INPUT_TITLE)).send_keys(self.TITLE)
        self.find((By.XPATH, self.X_INPUT_TEXT)).send_keys(self.TEXT)

        self.find((By.XPATH, self.X_BUTTON_SEND_REVIEW)).click()

        try:
            self.wait_hide((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER), 1)
        except:
            self.find((By.XPATH, self.X_BUTTON_SEND_REVIEW))

        helper.logout()

    def test_check_correct_review(self):
        helper.login()
        self.render(f'{URL}/film/1')
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
        if (title != self.TITLE):
            raise Exception("names does not equal", title, self.TITLE)

        text = self.find((By.XPATH, self.X_UPPER_REVIEW_TEXT)).text
        if (text != self.TEXT):
            raise Exception("names does not equal", text, self.TEXT)

        helper.logout()

class TestSearch(BasePage):
    X_INPUT_SEARCH = '/html/body/div/header/form/input'
    X_BUTTON_RETURN_MAIN = '/html/body/div/div/div[2]/div[4]/div'
    X_TITLE_SEARCH = '/html/body/div/div/div[1]'
    TITLE_SEARCH = 'Результаты поиска'
    ALL_GROUP_SEARCH = 'a'
    X_SEARCH_GROUP_FILMS = '/html/body/div/div/div[2]/div[1]/div/div/div[1]'
    SEARCH_GROUP_FILMS = 'Найденные фильмы:'
    X_SEARCH_GROUP_SERAILS = '/html/body/div/div/div[2]/div[2]/div/div/div[1]'
    SEARCH_GROUP_SERAILS = 'Найденные сериалы:'
    X_SEARCH_GROUP_PERSONS = '/html/body/div/div/div[2]/div[3]/div/div/div[1]'
    SEARCH_GROUP_PERSONS = 'Найденные имена:'
    X_FIRST_FOUNDED_FILM = '/html/body/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/div[1]/div[1]'
    X_FIRST_FOUNDED_TITLE = '/html/body/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]'
    X_TITLE_ON_FILM_PAGE = '/html/body/div/div/div[1]/div/div[2]/div[1]'

    def test_check_exists(self):
        self.render(URL)
        self.find((By.XPATH, self.X_INPUT_SEARCH)).send_keys(Keys.ENTER)
        title = self.find((By.XPATH, self.X_TITLE_SEARCH)).text
        if (title != self.TITLE_SEARCH):
            raise Exception("stings does not equal", text, self.TITLE_SEARCH)

    def test_check_empty(self):
        self.render(URL)
        self.find((By.XPATH, self.X_INPUT_SEARCH)).send_keys(Keys.ENTER)
        self.find((By.XPATH, self.X_BUTTON_RETURN_MAIN)).click()

    def test_check_group_category(self):
        self.render(URL)
        self.find((By.XPATH, self.X_INPUT_SEARCH)).send_keys(self.ALL_GROUP_SEARCH, Keys.ENTER)

        films_field = self.find((By.XPATH, self.X_SEARCH_GROUP_FILMS)).text
        if (films_field != self.SEARCH_GROUP_FILMS):
            raise Exception("stings does not equal", text, self.SEARCH_GROUP_FILMS)

        serials_field = self.find((By.XPATH, self.X_SEARCH_GROUP_SERAILS)).text
        if (serials_field != self.SEARCH_GROUP_SERAILS):
            raise Exception("stings does not equal", text, self.SEARCH_GROUP_SERAILS)

        persons_field = self.find((By.XPATH, self.X_SEARCH_GROUP_PERSONS)).text
        if (persons_field != self.SEARCH_GROUP_PERSONS):
            raise Exception("stings does not equal", text, self.SEARCH_GROUP_PERSONS)

    def test_correct_results(self):
        self.render(URL)
        self.find((By.XPATH, self.X_INPUT_SEARCH)).send_keys(self.ALL_GROUP_SEARCH, Keys.ENTER)

        films_field = self.find((By.XPATH, self.X_FIRST_FOUNDED_TITLE)).text
        self.find((By.XPATH, self.X_FIRST_FOUNDED_FILM)).click()
        film_title = self.find((By.XPATH, self.X_TITLE_ON_FILM_PAGE)).text
        if (films_field != film_title):
            raise Exception("stings does not equal", films_field, film_title)



