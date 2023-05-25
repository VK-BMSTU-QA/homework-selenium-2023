from selenium.webdriver.common.keys import Keys
import unittest


from pages.pageSearch import SearchPage


class TestSearch(unittest.TestCase, SearchPage):
    ALL_GROUP_SEARCH = 'a'
    EXPECTED_TITLE_SEARCH = 'Результаты поиска'
    EXPECTED_SEARCH_GROUP_FILMS = 'Найденные фильмы:'
    EXPECTED_SEARCH_GROUP_SERIALS = 'Найденные сериалы:'
    EXPECTED_SEARCH_GROUP_PERSONS = 'Найденные имена:'
    EXPECTED_FOUND_COUNT_SERIALS = 1
    EXPECTED_FOUND_COUNT_PERSONS = 2
    EXPECTED_FOUND_COUNT_FILMS = 0

    def test_check_exists(self):
        self.render_page()

        self.input_search(Keys.ENTER)

        title = self.get_main_title()
        self.assertEqual(title, self.EXPECTED_TITLE_SEARCH, "stings does not equal")

    def test_check_group_category(self):
        self.render_page()

        self.input_search([self.ALL_GROUP_SEARCH, Keys.ENTER])

        films_field = self.get_search_res_type(self.EXPECTED_FOUND_COUNT_FILMS)
        self.assertEqual(films_field, self.EXPECTED_SEARCH_GROUP_FILMS, "expected films found")

        serials_field = self.get_search_res_type(self.EXPECTED_FOUND_COUNT_SERIALS)
        self.assertEqual(serials_field, self.EXPECTED_SEARCH_GROUP_SERIALS, "expected serials found")

        persons_field = self.get_search_res_type(self.EXPECTED_FOUND_COUNT_PERSONS)
        self.assertEqual(persons_field, self.EXPECTED_SEARCH_GROUP_PERSONS, "expected persons found")

    def test_correct_results(self):
        self.render_page()

        self.input_search([self.ALL_GROUP_SEARCH, Keys.ENTER])

        actual_film_title = self.get_first_found_film_title()

        self.assertTrue(actual_film_title.find(self.ALL_GROUP_SEARCH), f"title must contains search {self.ALL_GROUP_SEARCH}")
