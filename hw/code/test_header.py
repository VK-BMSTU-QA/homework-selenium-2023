import allure
from ui.fixtures import get_driver
from ui.pages.login_page import LoginPage
from ui.pages.header import Header
from ui.pages.search_header import SearchHeader


class TestHeader():
    driver = get_driver(browser_name='chrome')
    login_page = LoginPage(driver)
    header = Header(driver)
    searchHeader = SearchHeader(driver)

    @allure.feature('Tests login / profile button')
    @allure.story('Login and find profile button, then logout')
    @header.render_decorator
    def test_header_profile_button(self):
        with allure.step('findLoginPageButton'):
            self.header.findLoginPageButton().click()

        with allure.step('login'):
            self.login_page.login()

        with allure.step('logout'):
            self.header.logout()

    @allure.feature('Header navigation buttons')
    @allure.story('Checks links in buttons on right side of the header')
    @header.render_decorator
    def test_rightHeaderButtons(self):
        with allure.step('findOrdersPageButton'):
            self.header.findOrdersPageButton()

        with allure.step('findCartPageButton'):
            self.header.findCartPageButton()

        with allure.step('findFavouritesPageButton'):
            self.header.findFavouritesPageButton()

    @allure.feature('Tests search')
    @allure.story('different payloads for search and suggestions')
    @header.render_decorator
    def test_searchTest(self):
        with allure.step('checkPhoneCategory'):
            self.searchHeader.checkPhoneCategory()

        with allure.step('checkProhibitedSymbolsSearch'):
            self.searchHeader.checkProhibitedSymbolsSearch()

        with allure.step('checkSearchSuggestions'):
            self.searchHeader.render_page()
            self.searchHeader.checkSearchSuggestions()

        with allure.step('sendNoResultsRequest'):
            self.searchHeader.sendNoResultsRequest()

        with allure.step('performTooShortSearchRequest'):
            self.searchHeader.performTooShortSearchRequest()

    @allure.feature('Checks logo')
    @allure.story('checks link in logo')
    @header.render_decorator
    def checkLogo(self):
        self.header.findLogo()
