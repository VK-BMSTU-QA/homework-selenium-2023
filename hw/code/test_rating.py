from ui.components.rating import CheckRatingButton
from ui.locators.product_title_locators import ProductTitleLocators
from ui.locators.horizontal_scroll_catalog_locators import HorizontalScrollCatalogLocators


class TestChangeItemCountInCart():
    productTitleRating = CheckRatingButton(ProductTitleLocators)
    recommendationsRating = CheckRatingButton(
        HorizontalScrollCatalogLocators)

    def test_product_change_count(self):
        self.productTitleRating.test_product_rating_number()
        self.productTitleRating.test_product_link_in_rating()

    def test_recommendation_change_count(self):
        self.recommendationsRating.test_product_rating_number()
        self.recommendationsRating.test_product_link_in_rating()
