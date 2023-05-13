from selenium.webdriver.common.by import By

from base_page import BasePage
from driver import dvr
from const import *


class TestPersonNotAuthorized(BasePage):
    # check redirect
    CLASS_NAME_FILM = "film__blackout"
    EXPECTED_REDIRECTED_PAGE_URL = 'https://movie-gate.online/film/19/'

    # check film contains person
    CLASS_NAME_ROLE = "about-film__role"
    EXPECTED_PERSON = "Хоакин Феникс"

    def test_film_contains_person(self):
        self.render(f'{DOMAIN}/person/31/')
        self.find((By.CLASS_NAME, self.CLASS_NAME_FILM)).click()

        # check redirect
        actual_url = dvr.get_instance().current_url
        if actual_url != self.EXPECTED_REDIRECTED_PAGE_URL:
            raise Exception("wrong redirect: not expected film", self.EXPECTED_REDIRECTED_PAGE_URL, actual_url)

        # check film contains person
        actual_person = self.find((By.CLASS_NAME, self.CLASS_NAME_ROLE)).text
        if self.EXPECTED_PERSON not in actual_person:
            raise Exception("wrong name: not expected name", actual_person, self.EXPECTED_PERSON)
