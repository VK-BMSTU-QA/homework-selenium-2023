from ui.components.favourites_component import FavouritesComponent
from ui.locators.favourites_locators import FavouritesLocators
from ui.locators.base_locators import BaseLocators
from ui.locators.catalog_locators import CatalogLocators


class TestCategorySelection():
    baseLocators = BaseLocators()
    product = FavouritesComponent(
        FavouritesLocators,
        baseLocators.hrefs.domain + baseLocators.hrefs.product +
        baseLocators.hrefs.defaultProduct)

    search = FavouritesComponent(
        CatalogLocators,
        baseLocators.hrefs.domain + baseLocators.hrefs.search
        + baseLocators.hrefs.defaultSearchQuery)

    favouritesPage = FavouritesComponent(
        CatalogLocators,
        baseLocators.hrefs.domain + baseLocators.hrefs.userFavorites)

    category = FavouritesComponent(
        CatalogLocators,
        baseLocators.hrefs.domain + baseLocators.hrefs.category
        + baseLocators.hrefs.phones)

    def test_product_category_favourites(self):
        self.product.testFavoritesUnauth()
        self.product.testFavoritesAuth()

    def test_category_search_favourites(self):
        self.search.testFavoritesUnauth()
        self.search.testFavoritesAuth()

    def test_category_favourites_page_favourites(self):
        self.favouritesPage.testFavoritesAuth()

    def test_category_category_favourites(self):
        self.category.testFavoritesUnauth()
        self.category.testFavoritesAuth()
