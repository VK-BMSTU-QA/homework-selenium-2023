from selenium.webdriver.common.by import By
import unittest

from utils.base_page import BasePage
from utils.driver import dvr


class SelectorsPerson:
    # check redirect
    CLASS_NAME_FILM = "film__blackout"
    EXPECTED_REDIRECTED_PAGE_URL = 'https://movie-gate.online/film/28/'

    # check film contains person
    CLASS_NAME_ROLE = "about-film__role"


class TestPersonNotAuthorized(unittest.TestCase, BasePage):
    EXPECTED_PERSON = "Хоакин Феникс"

    def test_film_contains_person(self):
        self.render(f'/person/31/')
        self.find((By.CLASS_NAME, SelectorsPerson.CLASS_NAME_FILM)).click()

        # check redirect
        actual_url = dvr.get_instance().current_url
        self.assertEqual(actual_url, SelectorsPerson.EXPECTED_REDIRECTED_PAGE_URL, "wrong redirect: not expected film")

        # check film contains person
        actual_person = self.find((By.CLASS_NAME, SelectorsPerson.CLASS_NAME_ROLE)).text
        self.assertIn(self.EXPECTED_PERSON, actual_person, SelectorsPerson.EXPECTED_REDIRECTED_PAGE_URL)
