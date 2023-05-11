import allure

from ui.fixtures import get_driver
from ui.pages.catalog_selector import CatalogSelector
from ui.locators.base_locators import BaseLocators


class CatalogSelectorComponent():
    driver = get_driver(browser_name='chrome')
    catalog = CatalogSelector(driver, BaseLocators())

    def __init__(self, selectors):
        self.catalog = CatalogSelector(self.driver, selectors())

    @allure.feature('Category navigation home')
    @allure.story('are links broken')
    @catalog.render_decorator
    def test_is_home_catalog_links(self):
        self.catalog.selectHomeCategory()

    @allure.feature('Category navigation header')
    @allure.story('are links broken')
    @catalog.render_decorator
    def test_is_header_catalog_links(self):
        self.catalog.selectHeaderCategory()
