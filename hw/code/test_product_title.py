import allure

from ui.fixtures import get_driver
from ui.pages.product_title import ProductTitle
from ui.pages.login_page import LoginPage
from ui.pages.header import Header


class TestProductTitle():
    driver = get_driver(browser_name='chrome')
    productPage = ProductTitle(driver)
    loginPage = LoginPage(driver)
    header = Header(driver)

    @allure.feature('Title')
    @allure.story('tab title, links, rating')
    @productPage.render_decorator
    def test_product_title(self):
        with allure.step('checkTabTitle'):
            self.productPage.checkTabTitle()

        with allure.step('checkLinkInTheTitles'):
            self.productPage.checkLinkInTheTitles()

        with allure.step('checkCategoryLink'):
            self.productPage.checkCategoryLink()

    @allure.feature('Check photo')
    @allure.story('is photo broken')
    @productPage.render_decorator
    def test_is_photo_broken(self):
        self.productPage.checkItemPhoto()
