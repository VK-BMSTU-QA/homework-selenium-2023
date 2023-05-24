from selenium.webdriver.common.by import By
import unittest

from utils.base_page import BasePage
from utils.driver import dvr


class PersonPageParams:
    URL_PAGE = f'/person/31/'

    # check redirect
    CLASS_NAME_FILM = "film__blackout"

    # check film contains person
    CLASS_NAME_ROLE = "about-film__role"


class PagePerson(BasePage):
    def start(self):
        self.render(PersonPageParams.URL_PAGE)

    def get_film_id_person(self):
        self.find((By.CLASS_NAME, PersonPageParams.CLASS_NAME_FILM)).click()

        url = dvr.get_instance().current_url

        f = filter(str.isdigit, url)

        film_id = "".join(f)

        return film_id

    def get_film_main_actor(self):
        return self.find((By.CLASS_NAME, PersonPageParams.CLASS_NAME_ROLE)).text


class TestPersonNotAuthorized(unittest.TestCase, PagePerson):
    EXPECTED_PERSON = "Хоакин Феникс"
    EXPECTED_FILM_ID = 'https://movie-gate.online/film/28/'

    def test_film_contains_person(self):
        self.start()

        actual_film_id = self.get_film_id_person()

        # check film_id
        self.assertEqual(actual_film_id, self.EXPECTED_FILM_ID, "this film not expected")

        # check film main person
        actual_person = self.get_film_main_actor()
        self.assertIn(self.EXPECTED_PERSON, actual_person, "this film without expected person")
