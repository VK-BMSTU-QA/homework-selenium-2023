from selenium.webdriver.common.by import By
import unittest

from pages.pageNavigation import pageNavigation
from locators.pageNavigationLocators import SelectorsNavigation
from utils.helper_auth import needed_auth

class TestNavigationPanelUnauthorized(unittest.TestCase, pageNavigation):
    def test_click_logo(self):

        self.render(SelectorsNavigation.URL_TAG_POPULAR)
        film_preview = self.click_logo()

        self.assertIsNotNone(film_preview)

    def test_click_popular_button(self):
        self.render_main()

        title = self.click_popular_button()

        self.assertEqual(title, SelectorsNavigation.POPULAR_COLLECTION_PAGE_TITLE, "title does not equal")

    def test_click_premieres_button(self):
        self.render_main()

        title = self.click_premieres_button()

        self.assertEqual(title, SelectorsNavigation.PREMIERES_PAGE_TITLE, "title does not equal")

    def test_click_collections_button_unauthorized(self):
        self.render_main()

        modal_auth = self.click_collections_button_unauthorized()

        self.assertIsNotNone(modal_auth)

    def test_click_login_button(self):
        self.render_main()

        modal_auth = self.click_login_button()

        self.assertIsNotNone(modal_auth)
