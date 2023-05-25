import unittest

from utils.helper_auth import needed_auth
from pages.commonPage import CommonPage
from pages.pageFilm import FilmPage
from locators.pageFilmLocators import SelectorsFilm


class TestFilmPageAuthorized(unittest.TestCase, FilmPage):
    TEXT = '200IQ text'
    TITLE = 'title'

    @needed_auth
    def test_click_set_rate(self):
        self.render_film(film_id=1)
        self.set_rate(9)
        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), 'Успех!')

    @needed_auth
    def test_click_update_rate(self):
        self.render_film(film_id=1)
        self.set_rate(9)
        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), 'Успех!')

        self.set_rate(1)
        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), 'Успех!')

    @needed_auth
    def test_click_delete_rate(self):
        self.render_film(film_id=1)
        self.set_rate(9)
        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), 'Успех!')

        self.del_rate()
        self.assertTrue(self.is_del_block_absent())

        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), 'Оценка успешно удалена')

    @needed_auth
    def test_click_review(self):
        self.render_film(film_id=1)
        self.open_review()
        self.assertTrue(self.is_review_open())

    @needed_auth
    def test_send_review(self):
        self.render_film(film_id=1)
        self.open_review()
        self.assertTrue(self.is_review_open())

        self.write_review(SelectorsFilm.POSITIVE_TYPE, self.TITLE, self.TEXT)

        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), 'Спасибо за вашу рецензию')

    @needed_auth
    def test_error_review(self):
        self.render_film(film_id=1)
        self.open_review()
        self.assertTrue(self.is_review_open())

        self.write_review(None, self.TITLE, self.TEXT)
        self.assertEqual(self.get_err_msg_review(), 'Укажите тип рецензии')


    @needed_auth
    def test_check_correct_review(self):
        self.render_film(film_id=1)
        self.open_review()
        self.assertTrue(self.is_review_open())

        self.write_review(SelectorsFilm.NEGATIVE_TYPE, self.TITLE, self.TEXT)
        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), 'Спасибо за вашу рецензию')

        self.assertEqual(self.get_upper_title_review(), self.TITLE)
        self.assertEqual(self.get_upper_message_review(), self.TEXT)

