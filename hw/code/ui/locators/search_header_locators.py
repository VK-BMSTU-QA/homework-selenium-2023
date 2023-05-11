from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class SearchHeaderLocators(BaseLocators):
    def __init__(self):
        super(SearchHeaderLocators, self).__init__()

    SEARCH_INPUT = (By.NAME, 'search-line')

    SEARCH_BUTTON = (By.ID, 'search-button-submit')

    SEARCH_NO_RESULTS_MESSAGE = (By.ID, 'content-unAuth-page-redirect')

    FIND_FIRST_SEARCH_RESULT_TITLE = (
        By.XPATH, '//div[@id="items-block"]/div[@class="catalog-item-card"][1]' +
        '/div[@class="catalog-item-card__description-block"]' +
        '/div[@id="catalog_item-title-block"]' +
        '/a[@id="catalog_item-title"]')

    GET_THIRD_SEARCH_SUGGESTION = (By.ID, 'search-suggestion:2')

    GET_FIRST_SEARCH_SUGGESTION = (By.ID, 'search-suggestion:0')
