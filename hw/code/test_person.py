from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from utils.driver import dvr

class SelectorsPerson:
    # check redirect
    CLASS_NAME_FILM = "film__blackout"
    EXPECTED_REDIRECTED_PAGE_URL = 'https://movie-gate.online/film/28/'

    # check film contains person
    CLASS_NAME_ROLE = "about-film__role"

class TestPersonNotAuthorized(BasePage):
    EXPECTED_PERSON = "Хоакин Феникс"

    def test_film_contains_person(self):
        self.render(f'/person/31/')
        self.find((By.CLASS_NAME, SelectorsPerson.CLASS_NAME_FILM)).click()

        # check redirect
        actual_url = dvr.get_instance().current_url
        if actual_url != SelectorsPerson.EXPECTED_REDIRECTED_PAGE_URL:
            raise Exception("wrong redirect: not expected film", SelectorsPerson.EXPECTED_REDIRECTED_PAGE_URL, actual_url)

        # check film contains person
        actual_person = self.find((By.CLASS_NAME, SelectorsPerson.CLASS_NAME_ROLE)).text
        if self.EXPECTED_PERSON not in actual_person:
            raise Exception("wrong name: not expected name", actual_person, self.EXPECTED_PERSON)
