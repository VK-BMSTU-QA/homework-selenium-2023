import unittest

from utils.helper_auth import needed_auth, helper
from pages.commonPage import CommonPage
from pages.pageFilm import FilmPage
from locators.pageFilmLocators import SelectorsFilm


class TestFilmPageAuthorized(unittest.TestCase, FilmPage):
    TEXT = '200IQ text'
    TITLE = 'title'
    MSG_SUCCESS = 'Успех!'
    MSG_SUC_DEL_RATE = 'Оценка успешно удалена'
    MSG_SUC_REVIEW = 'Спасибо за вашу рецензию'
    MSG_ERR_NO_TYPE = 'Укажите тип рецензии'


    def test_click_set_rate(self):
        helper.login()

        self.render_film(film_id=1)
        self.set_rate(9)
        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), self.MSG_SUCCESS)

    def test_click_update_rate(self):
        helper.login()

        self.render_film(film_id=1)
        self.set_rate(9)
        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), self.MSG_SUCCESS)

        self.set_rate(1)
        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), self.MSG_SUCCESS)


    def test_click_delete_rate(self):
        helper.login()

        self.render_film(film_id=1)
        self.set_rate(9)
        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), self.MSG_SUCCESS)

        self.del_rate()
        self.assertTrue(self.is_del_block_absent())

        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), self.MSG_SUC_DEL_RATE)


    def test_click_review(self):
        helper.login()

        self.render_film(film_id=1)
        self.open_review()
        self.assertTrue(self.is_review_open())

    def test_send_review(self):
        helper.login()

        self.render_film(film_id=1)
        self.open_review()
        self.assertTrue(self.is_review_open())

        self.write_review(SelectorsFilm.POSITIVE_TYPE, self.TITLE, self.TEXT)

        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), self.MSG_SUC_REVIEW)

    def test_error_review(self):
        helper.login()

        self.render_film(film_id=1)
        self.open_review()
        self.assertTrue(self.is_review_open())

        self.write_review(None, self.TITLE, self.TEXT)
        self.assertEqual(self.get_err_msg_review(), self.MSG_ERR_NO_TYPE)


    def test_check_correct_review(self):
        helper.login()

        self.render_film(film_id=1)
        self.open_review()
        self.assertTrue(self.is_review_open())

        self.write_review(SelectorsFilm.NEGATIVE_TYPE, self.TITLE, self.TEXT)
        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), self.MSG_SUC_REVIEW)

        self.assertEqual(self.get_upper_title_review(), self.TITLE)
        self.assertEqual(self.get_upper_message_review(), self.TEXT)

