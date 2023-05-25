from selenium.webdriver.common.by import By
import unittest

from utils.base_page import BasePage


class TestMainPage(unittest.TestCase, BasePage):
    def test_preview_film_existing(self):
        self.render('/')

        self.assertIsNotNone(self.find((By.CLASS_NAME, MainPageParams.CLASS_NAME_PREVIEW)))

        self.assertIsNotNone(self.find((By.CLASS_NAME, MainPageParams.CLASS_NAME_PREVIEW_FILM_TITLE)))

    def test_popular_section(self):
        self.render('/')

        self.assertIsNotNone(self.find((By.XPATH, MainPageParams.X_PATH_POPULAR_SECTION_SLIDER_FILM)))

        self.find((By.XPATH, MainPageParams.X_PATH_POPULAR_SECTION_BUTTON)).click()

        title = self.find((By.CLASS_NAME, MainPageParams.CLASS_NAME_PAGE_COLLECTION_TITLE)).text

        self.assertEqual(title, MainPageParams.PAGE_POPULAR_COLLECTION_TITLE, "title does not equal")

    def test_in_cinema_section(self):
        self.render('/')

        self.assertIsNotNone(self.find((By.XPATH, MainPageParams.X_PATH_IN_CINEMA_SECTION_SLIDER_FILM)))

        self.find((By.XPATH, MainPageParams.X_PATH_IN_CINEMA_SECTION_BUTTON)).click()

        title = self.find((By.CLASS_NAME, MainPageParams.CLASS_NAME_PAGE_COLLECTION_TITLE)).text

        self.assertEqual(title, MainPageParams.PAGE_IN_CINEMA_COLLECTION_TITLE, "title does not equal")

    def test_genres_section(self):
        self.render('/')

        self.assertIsNotNone(self.find((By.XPATH, MainPageParams.X_PATH_GENRES_SECTION_SLIDER_GENRE)))

        self.find((By.XPATH, MainPageParams.X_PATH_GENRES_SECTION_BUTTON)).click()

        title = self.find((By.CLASS_NAME, MainPageParams.CLASS_NAME_PAGE_COLLECTION_TITLE)).text

        self.assertEqual(title, MainPageParams.PAGE_GENRES_COLLECTION_TITLE, "title does not equal")
