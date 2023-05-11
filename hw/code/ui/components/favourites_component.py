import allure

from ui.fixtures import get_driver
from ui.pages.favoirites import Favourites
from ui.pages.login_page import LoginPage
from ui.pages.header import Header


class FavouritesComponent():
    driver = get_driver(browser_name='chrome')
    loginPage = LoginPage(driver)
    header = Header(driver)

    def __init__(self, selectors, url):
        self.favourites = Favourites(self.driver, selectors(), url)

    @allure.feature('Favourites button')
    @allure.story('unauth check')
    def testFavoritesUnauth(self):
        self.favourites.render_page()
        self.favourites.unauthFavourites()

    @allure.feature('Favourites button')
    @allure.story('auth check')
    def testFavoritesAuth(self):
        self.favourites.render_page()

        with allure.step('login'):
            self.header.findLoginPageButton().click()
            self.loginPage.login()

        with allure.step('go back to product page'):
            self.favourites.render_page()

        with allure.step('authFavourites check and unchecked'):
            self.favourites.authFavourites()
            self.favourites.authFavourites()

        with allure.step('logout'):
            self.header.logout()
