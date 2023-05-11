import allure

from ui.fixtures import get_driver
from ui.pages.rating import Rating
from ui.locators.base_locators import BaseLocators


class CheckRatingButton():
    driver = get_driver(browser_name='chrome')
    rating = Rating(driver, BaseLocators())

    def __init__(self, selectors):
        self.rating = Rating(self.driver, selectors())

    @allure.feature('Rating')
    @allure.story('checkRatingNumber')
    @rating.render_decorator
    def test_product_rating_number(self):
        self.rating.checkRatingNumber()

    @allure.feature('Rating')
    @allure.story('checkLinkInRating')
    @rating.render_decorator
    def test_product_link_in_rating(self):
        self.rating.checkLinkInRating()
