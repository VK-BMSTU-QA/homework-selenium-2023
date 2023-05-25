from selenium.webdriver.common.by import By
import unittest

from pages.pageNavigation import pageNavigation
from locators.pageNavigationLocators import SelectorsNavigation
from utils.helper_auth import needed_auth

class TestNavigationPanelAuthorized(unittest.TestCase, pageNavigation):
    @needed_auth
    def test_click_collections_button_authorized(self):
        self.render_main()

        title = self.click_collections_button_authorized()

        self.assertEqual(title, SelectorsNavigation.USER_COLLECTION_PAGE_TITLE, "title does not equal")
