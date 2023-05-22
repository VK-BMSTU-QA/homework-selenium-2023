from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

from utils.base_page import BasePage


class SelectorsSearch:
    CLASS_NAME_FIRST_FOUNDED_FILM = 'premiere-film__blackout'
    CLASS_NAME_FIRST_FOUNDED_TITLE = 'premiere-film__information-title'
    CLASS_NAME_TITLE_ON_FILM_PAGE = 'about-film__title'
    CLASS_NAME_INPUT_SEARCH = 'js-header__form__input'
    CLASS_NAME_BUTTON_RETURN_MAIN = 'search-page__no-content-btn'
    CLASS_NAME_TITLE_SEARCH = 'search-page__title'
    CLASS_NAME_CATEGORY_TITLE = 'search-list__title'
    CLASS_NAME_SEARCH_GROUP_SERAILS = 1
    CLASS_NAME_SEARCH_GROUP_PERSONS = 2
    ALL_GROUP_SEARCH = 'a'
    CLASS_NAME_SEARCH_GROUP_FILMS = 0


class TestSearch(unittest.TestCase, BasePage):
    TITLE_SEARCH = 'Результаты поиска'
    SEARCH_GROUP_FILMS = 'Найденные фильмы:'
    SEARCH_GROUP_SERAILS = 'Найденные сериалы:'
    SEARCH_GROUP_PERSONS = 'Найденные имена:'

    def test_check_exists(self):
        self.render('/')

        self.find((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_INPUT_SEARCH)).send_keys(Keys.ENTER)
        title = self.find((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_TITLE_SEARCH)).text

        self.assertEqual(title, self.TITLE_SEARCH, "stings does not equal")

    def test_check_empty(self):
        self.render('/')
        self.find((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_INPUT_SEARCH)).send_keys(Keys.ENTER)
        self.find((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_BUTTON_RETURN_MAIN)).click()

    def test_check_group_category(self):
        self.render('/')
        self.find((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_INPUT_SEARCH)).send_keys(SelectorsSearch.ALL_GROUP_SEARCH,
                                                                                      Keys.ENTER)

        films_field = self.find_group((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_CATEGORY_TITLE))[
            SelectorsSearch.CLASS_NAME_SEARCH_GROUP_FILMS].text
        self.assertEqual(films_field, self.SEARCH_GROUP_FILMS, "stings does not equal")

        serials_field = self.find_group((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_CATEGORY_TITLE))[
            SelectorsSearch.CLASS_NAME_SEARCH_GROUP_SERAILS].text
        self.assertEqual(serials_field, self.SEARCH_GROUP_SERAILS, "stings does not equal")

        persons_field = self.find_group((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_CATEGORY_TITLE))[
            SelectorsSearch.CLASS_NAME_SEARCH_GROUP_PERSONS].text
        self.assertEqual(persons_field, self.SEARCH_GROUP_PERSONS, "stings does not equal")

    def test_correct_results(self):
        self.render('/')
        self.find((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_INPUT_SEARCH)).send_keys(SelectorsSearch.ALL_GROUP_SEARCH,
                                                                                      Keys.ENTER)

        films_field = self.find((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_FIRST_FOUNDED_TITLE)).text
        self.find((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_FIRST_FOUNDED_FILM)).click()
        film_title = self.find((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_TITLE_ON_FILM_PAGE)).text

        self.assertEqual(film_title, films_field, "stings does not equal")
