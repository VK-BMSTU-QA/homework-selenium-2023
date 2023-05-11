from ui.pages.base_page import BasePage
from ui.locators.header_locators import HeaderLocators
from ui.locators.catalog_locators import CatalogLocators
from ui.locators.search_header_locators import SearchHeaderLocators


class SearchHeader(BasePage):
    headerLocators = HeaderLocators()
    categoryLocators = CatalogLocators()
    xssPayload = "<img src onerror=alert(1) />"
    categoryShortSearch = 'т'
    noResultSearchMessage = 'aZАя!?()_./-'
    tooShortSearchErrorMessage = 'Введите не меньше 3 символов'
    tooShortSearchPayload = 'df'
    prohibitedSymbolsMessage = 'Введены недопустимые символы'
    suggestionSearchPayload = 'iphone'

    def __init__(self, driver):
        super(SearchHeader, self).__init__(driver)
        self.locators = SearchHeaderLocators()
        self.url = self.locators.hrefs.domain + self.locators.hrefs.home

    def _noop():
        pass

    def performSearch(self, searchValue, callback=_noop):
        searchInput = self.find(self.locators.SEARCH_INPUT)
        searchInput.clear()
        searchInput.send_keys(searchValue)

        callback()

        self.find(self.locators.SEARCH_BUTTON).click()

    def performTooShortSearchRequest(self):
        self.performSearch(self.tooShortSearchPayload)

        self.checkErrorMessage(self.tooShortSearchErrorMessage)

    def sendNoResultsRequest(self):
        self.performSearch(
            self.noResultSearchMessage,
            lambda: self.waitUntilInvisible(self.locators.GET_FIRST_SEARCH_SUGGESTION))

        self.waitUntilVisible(self.locators.SEARCH_NO_RESULTS_MESSAGE)

    def checkFirstSearchSuggestion(self):
        assert self.find(
            self.locators.GET_FIRST_SEARCH_SUGGESTION)

    def checkPhoneCategory(self):
        self.performSearch(
            self.categoryShortSearch, self.checkFirstSearchSuggestion)
        self.is_opened(
            self.locators.hrefs.domain + self.locators.hrefs.category +
            self.locators.hrefs.phones)

    def checkProhibitedSymbolsSearch(self):
        self.performSearch(self.xssPayload)

        self.checkErrorMessage(self.prohibitedSymbolsMessage)

    def checkSearchSuggestions(self):
        searchInput = self.find(self.locators.SEARCH_INPUT)
        searchInput.clear()
        searchInput.send_keys(self.suggestionSearchPayload)

        thirdSearchSuggestion = self.find(
            self.locators.GET_THIRD_SEARCH_SUGGESTION)

        thirdSuggestionText = thirdSearchSuggestion.get_attribute('innerText')
        thirdSearchSuggestion.click()

        assert self.getInnerText(
            self.locators.FIND_FIRST_SEARCH_RESULT_TITLE
        ) == thirdSuggestionText

        self.waitUntilInvisible(self.locators.GET_THIRD_SEARCH_SUGGESTION)
