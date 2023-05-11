from ui.components.changeCartCountButton import ChangeCartCountButton
from ui.locators.cart_count_locators import CartCountLocators
from ui.locators.horizontal_scroll_catalog_locators import HorizontalScrollCatalogLocators
from ui.locators.base_locators import BaseLocators
from ui.locators.comment_titile_locators import CommentTitleLocators
from ui.locators.home_locators import HomeLocators
from ui.locators.catalog_locators import CatalogLocators


class TestChangeItemCountInCart():

    baseLocator = BaseLocators()

    productChangeCount = ChangeCartCountButton(
        CartCountLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.product +
        baseLocator.hrefs.defaultProduct)

    viewComment = ChangeCartCountButton(
        CommentTitleLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.comment +
        baseLocator.hrefs.defaultProduct)

    addComment = ChangeCartCountButton(
        CommentTitleLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.addComment +
        baseLocator.hrefs.defaultProduct)

    homePage = ChangeCartCountButton(
        HomeLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.home)

    recommendationsItemChangeCount = ChangeCartCountButton(
        HorizontalScrollCatalogLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.product +
        baseLocator.hrefs.defaultProduct)

    categoryPage = ChangeCartCountButton(
        CatalogLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.category
        + baseLocator.hrefs.phones)

    favouritesPage = ChangeCartCountButton(
        CatalogLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.userFavorites)

    searchPage = ChangeCartCountButton(
        CatalogLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.search
        + baseLocator.hrefs.defaultSearchQuery)

    def test_product_change_count(self):
        self.productChangeCount.test_unauth_change_count_buttons()
        self.productChangeCount.test_auth_change_count_buttons()

    def test_product_view_comment_change_count(self):
        self.viewComment.test_unauth_change_count_buttons()
        self.viewComment.test_auth_change_count_buttons()

    def test_product_add_comment_change_count(self):
        self.addComment.test_auth_change_count_buttons()

    def test_home_page_change_count(self):
        self.homePage.test_unauth_change_count_buttons()
        self.homePage.test_auth_change_count_buttons()

    def test_recommendation_change_count(self):
        self.recommendationsItemChangeCount.test_unauth_change_count_buttons()

    def test_category_page_change_count(self):
        self.categoryPage.test_unauth_change_count_buttons()
        self.categoryPage.test_auth_change_count_buttons()

    def test_favourite_page_change_count(self):
        self.favouritesPage.test_auth_change_count_buttons()

    def test_search_page_change_count(self):
        self.searchPage.test_unauth_change_count_buttons()
        self.searchPage.test_auth_change_count_buttons()
