from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

from utils.base_page import BasePage


class SearchPageParams:
    URL_PAGE = "/"
    CLASS_NAME_FIRST_FOUNDED_FILM = 'premiere-film__blackout'
    CLASS_NAME_FIRST_FOUNDED_TITLE = 'premiere-film__information-title'
    CLASS_NAME_TITLE_ON_FILM_PAGE = 'about-film__title'
    CLASS_NAME_INPUT_SEARCH = 'js-header__form__input'
    CLASS_NAME_BUTTON_RETURN_MAIN = 'search-page__no-content-btn'
    CLASS_NAME_TITLE_SEARCH = 'search-page__title'
    CLASS_NAME_CATEGORY_TITLE = 'search-list__title'


class PagePerson(BasePage):
    def start(self):
        self.render(SearchPageParams.URL_PAGE)

    def input_search(self, value):
        self.find((By.CLASS_NAME, SearchPageParams.CLASS_NAME_INPUT_SEARCH)).send_keys(value)

    def get_main_title(self):
        return self.find((By.CLASS_NAME, SearchPageParams.CLASS_NAME_TITLE_SEARCH)).text

    def get_search_res_type(self, target):
        return self.find_group((By.CLASS_NAME, SearchPageParams.CLASS_NAME_CATEGORY_TITLE))[target].text

    def get_first_found_film_title(self):
        return self.find((By.CLASS_NAME, SearchPageParams.CLASS_NAME_FIRST_FOUNDED_TITLE)).text


class TestSearch(unittest.TestCase, PagePerson):
    ALL_GROUP_SEARCH = 'a'
    EXPECTED_TITLE_SEARCH = 'Результаты поиска'
    EXPECTED_SEARCH_GROUP_FILMS = 'Найденные фильмы:'
    EXPECTED_SEARCH_GROUP_SERIALS = 'Найденные сериалы:'
    EXPECTED_SEARCH_GROUP_PERSONS = 'Найденные имена:'
    EXPECTED_FOUND_COUNT_SERIALS = 1
    EXPECTED_FOUND_COUNT_PERSONS = 2
    EXPECTED_FOUND_COUNT_FILMS = 0

    def test_check_exists(self):
        self.start()

        self.input_search(Keys.ENTER)

        title = self.get_main_title()
        self.assertEqual(title, self.EXPECTED_TITLE_SEARCH, "stings does not equal")

    def test_check_group_category(self):
        self.start()

        self.input_search([self.ALL_GROUP_SEARCH, Keys.ENTER])

        films_field = self.get_search_res_type(self.EXPECTED_FOUND_COUNT_FILMS)
        self.assertEqual(films_field, self.EXPECTED_SEARCH_GROUP_FILMS, "expected films found")

        serials_field = self.get_search_res_type(self.EXPECTED_FOUND_COUNT_SERIALS)
        self.assertEqual(serials_field, self.EXPECTED_SEARCH_GROUP_SERIALS, "expected serials found")

        persons_field = self.get_search_res_type(self.EXPECTED_FOUND_COUNT_PERSONS)
        self.assertEqual(persons_field, self.EXPECTED_SEARCH_GROUP_PERSONS, "expected persons found")

    def test_correct_results(self):
        self.start()

        self.input_search([self.ALL_GROUP_SEARCH, Keys.ENTER])

        actual_film_title = self.get_first_found_film_title()

        self.assertTrue(actual_film_title.find(self.ALL_GROUP_SEARCH), f"title must contains search {self.ALL_GROUP_SEARCH}")
