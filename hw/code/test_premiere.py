from selenium.webdriver.common.by import By
import unittest

from utils.base_page import BasePage


class PremierePageParams:
    URL_PAGE = f'/premieres/'

    # check premiere page's content
    CLASS_NAME_PREMIERES_TITLE = 'premiere-page__title'
    CLASS_NAME_PREMIERES_DAY = 'premiere-day'

    # check film poster redirect
    CLASS_NAME_PREMIERES_FILM_POSTER = 'premiere-film__poster-container'
    CLASS_NAME_FILM_PAGE_ABOUT = 'js-film-page__about'


class PagePremieres(BasePage):
    def start(self):
        self.render(PremierePageParams.URL_PAGE)

    def get_premiere_title(self):
        return self.find((By.CLASS_NAME, PremierePageParams.CLASS_NAME_PREMIERES_TITLE)).text

    def get_premiere_date(self):
        return self.find((By.CLASS_NAME, PremierePageParams.CLASS_NAME_PREMIERES_DAY)).text

    def move_to_premiere_film(self):
        return self.find((By.CLASS_NAME, PremierePageParams.CLASS_NAME_PREMIERES_FILM_POSTER)).click()

    def get_premiere_film_about(self):
        return self.find((By.CLASS_NAME, PremierePageParams.CLASS_NAME_FILM_PAGE_ABOUT)).text


class TestPremieresPage(unittest.TestCase, PagePremieres):
    EXPECTED_PREMIERES_TITLE = 'Премьеры'
    EXPECTED_FILM_ABOUT = """В эфире
On the Line
6.7
2023
18+
Режиссёр:
Ромуальд Буланже 
В ролях:
Мэл Гибсон, 
Уильям Моусли 
Трейлер"""

    def test_premieres_exist(self):
        self.start()

        actual_title = self.get_premiere_title()
        self.assertEqual(actual_title, self.EXPECTED_PREMIERES_TITLE, "premieres not available")

        actual_date_premiere = self.get_premiere_date()
        self.assertIsNotNone(actual_date_premiere, "premiere date not available")

    def test_premiers_film_poster_redirect(self):
        self.start()

        self.move_to_premiere_film()

        actual_film_about = self.get_premiere_film_about()
        self.assertEqual(actual_film_about, self.EXPECTED_FILM_ABOUT, "premiere film about not available")
