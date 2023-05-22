from selenium.webdriver.common.by import By
import unittest

from utils.base_page import BasePage


class SelectorsPremierePage:
    # check premiere page's content
    CLASS_NAME_PREMIERES_TITLE = 'premiere-page__title'
    CLASS_NAME_PREMIERES_DAY = 'premiere-day'

    # check film poster redirect
    CLASS_NAME_PREMIERES_FILM_POSTER = 'premiere-film__poster-container'
    CLASS_NAME_FILM_PAGE_ABOUT = 'js-film-page__about'


class TestPremieresPage(unittest.TestCase, BasePage):
    PREMIERES_TITLE = 'Премьеры'

    def test_premieres_exist(self):
        self.render(f'/premieres/')

        title = self.find((By.CLASS_NAME, SelectorsPremierePage.CLASS_NAME_PREMIERES_TITLE)).text

        self.assertEqual(title, self.PREMIERES_TITLE, "title does not equal")

        self.assertIsNotNone(self.find((By.CLASS_NAME, SelectorsPremierePage.CLASS_NAME_PREMIERES_DAY)))

    def test_premiers_film_poster_redirect(self):
        self.render(f'/premieres/')

        self.find((By.CLASS_NAME, SelectorsPremierePage.CLASS_NAME_PREMIERES_FILM_POSTER)).click()

        self.assertIsNotNone(self.find((By.CLASS_NAME, SelectorsPremierePage.CLASS_NAME_FILM_PAGE_ABOUT)))
