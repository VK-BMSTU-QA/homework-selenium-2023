from selenium.webdriver.common.by import By
import unittest

from pages.pageMainPage import PageMainPage


class TestMainPage(unittest.TestCase, PageMainPage):
    EXPECTED_TITLE_POPULAR = 'Популярное'
    EXPECTED_TITLE_IN_CINEMA = 'Сейчас в кино'
    EXPECTED_TITLE_GENRES = 'Жанры'

    def test_preview_film_existing(self):
        self.render_page()

        self.assertIsNotNone(self.get_meny_preview(), "preview meny not available")

        self.assertIsNotNone(self.get_preview_title(), "preview film not available")

    def test_popular_section(self):
        self.render_page()

        self.assertIsNotNone(self.get_meny_popular())

        self.move_to_popular_collection()

        title = self.get_title_cur_collection()

        self.assertEqual(title, self.EXPECTED_TITLE_POPULAR, "title does not equal")

    def test_in_cinema_section(self):
        self.render_page()

        self.assertIsNotNone(self.get_meny_in_cinema(), "meny in cinema collection not available")

        self.move_to_in_cinema_collection()

        title = self.get_title_cur_collection()

        self.assertEqual(title, self.EXPECTED_TITLE_IN_CINEMA, "title does not equal")

    def test_genres_section(self):
        self.render_page()

        self.assertIsNotNone(self.get_meny_genres())

        self.move_to_genres()

        title = self.get_title_cur_collection()

        self.assertEqual(title, self.EXPECTED_TITLE_GENRES, "title does not equal")
