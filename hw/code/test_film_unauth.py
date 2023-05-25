from selenium.webdriver.common.by import By
import unittest

from utils.base_page import BasePage
from pages.commonPage import CommonPage
from pages.pageFilm import FilmPage
from locators.pageFilmLocators import SelectorsFilm



class TestFilmPageUnauthorized(unittest.TestCase, FilmPage):
    def test_click_bookmark_unauth(self):
        self.render_film(film_id=1)
        self.save_to_bookmark()
        self.assertEqual(CommonPage.get_toster_err_msg(self=self), ' Вы должны быть авторизованы ')

    def test_click_trailer(self):
        self.render_film(film_id=1)
        self.open_trailer()
        self.assertTrue(self.is_open_trailer())

    def test_click_review_unauth(self):
        self.render_film(film_id=1)

        self.open_review()
        self.assertEqual(CommonPage.get_toster_err_msg(self=self), ' Вы должны быть авторизованы ')
