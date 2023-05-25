import unittest

from pages.commonPage import CommonPage
from pages.pageFilm import FilmPage


class TestFilmPageUnauthorized(unittest.TestCase, FilmPage):
    MSG_ERR_NO_AUTH = ' Вы должны быть авторизованы '

    def test_click_bookmark_unauth(self):
        self.render_film(film_id=1)
        self.save_to_bookmark()
        self.assertEqual(CommonPage.get_toster_err_msg(self=self), self.MSG_ERR_NO_AUTH)

    def test_click_trailer(self):
        self.render_film(film_id=1)
        self.open_trailer()
        self.assertTrue(self.is_open_trailer())

    def test_click_review_unauth(self):
        self.render_film(film_id=1)

        self.open_review()
        self.assertEqual(CommonPage.get_toster_err_msg(self=self), self.MSG_ERR_NO_AUTH)
