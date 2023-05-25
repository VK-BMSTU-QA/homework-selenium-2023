from selenium.webdriver.common.by import By
import unittest


from utils.base_page import BasePage
from utils.helper_auth import needed_auth, helper
from pages.commonPage import CommonPage
from pages.pageFilm import FilmPage
from pages.pageCollection import PageCollection
from locators.pageFilmLocators import SelectorsFilm
from locators.pageCollectionsLocators import SelectorsCollections


class TestPersonalCollectionAddFilm(unittest.TestCase, PageCollection):
    COLL_FAV = "Избранное"
    COLL_WILL = "Буду смотреть"
    COLL_RECOMS = "Мои рекомендации"
    MSG_SUC = 'Фильм удалён из коллекции'
    MSG_SUC_COPY = 'Скопировано!'

    @needed_auth
    def test_adding_film_in_collection(self):
        collection = self.COLL_FAV
        film_id = 39
        FilmPage.render_film(self=self, film_id=film_id)
        film_title = FilmPage.add_or_remove_in_collection(self=self, collection=collection)

        self.open_collection(collection)
        self.open_film_in_collection(film_title)

        self.assertEqual(FilmPage.get_title_film(self=self), film_title)

        FilmPage.add_or_remove_in_collection(self=self, collection=collection)

    @needed_auth
    def test_delete_film_from_collection(self):
        collection = self.COLL_WILL
        film_id = 39
        FilmPage.render_film(self=self, film_id=film_id)
        film_title = FilmPage.add_or_remove_in_collection(self=self, collection=collection)

        self.open_collection(collection)
        self.delete_film()

        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), self.MSG_SUC)

    def test_public_collection_has_film(self):
        helper.login()
        collection = self.COLL_RECOMS
        film_id = 39
        FilmPage.render_film(self=self, film_id=film_id)
        film_title = FilmPage.add_or_remove_in_collection(self=self, collection=collection)

        self.open_collection(collection)
        collection_id = self.get_id_collection()
        self.open_public_collection_by_id(collection_id)
        self.open_film_in_collection(film_title)

        self.assertEqual(FilmPage.get_title_film(self=self), film_title)

        FilmPage.add_or_remove_in_collection(self=self, collection=collection)

    def test_public_collection_copy_url(self):
        helper.login()
        collection = self.COLL_RECOMS
        film_id = 39
        FilmPage.render_film(self=self, film_id=film_id)
        film_title = FilmPage.add_or_remove_in_collection(self=self, collection=collection)

        self.open_collection(collection)
        collection_id = self.get_id_collection()
        self.open_public_collection_by_id(collection_id)

        self.click_share()

        self.assertEqual(CommonPage.get_toster_suc_msg(self=self), self.MSG_SUC_COPY)
        self.delete_film()

