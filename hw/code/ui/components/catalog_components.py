import allure

from ui.fixtures import get_driver
from ui.pages.catalog_page import CatalogPage


class CatalogComponent():
    driver = get_driver(browser_name='chrome')

    def __init__(self, selectors, url):
        self.catalog = CatalogPage(self.driver, selectors(), url)

    @allure.feature('Catalog tests')
    @allure.story('checkSort')
    def checkSort(self):
        allure.step('checkRatingSort')
        self.catalog.render_page()
        self.catalog.checkRatingSort()

        allure.step('checkPriceSort')
        self.catalog.render_page()
        self.catalog.checkPriceSort()

    @allure.feature('Catalog tests')
    @allure.story('check tab title')
    def checkTab(self):
        self.catalog.checkTabTitle()

    @allure.feature('Catalog tests')
    @allure.story('check if photo broken')
    def checkIfPhotoBroken(self):
        self.catalog.checkIfPhotoBroken()

    @allure.feature('Catalog tests')
    @allure.story('check links')
    def checkLinks(self):
        with allure.step('checkImgLink'):
            self.catalog.checkImgLink()

        with allure.step('checkTitleLink'):
            self.catalog.checkTitleLink()
