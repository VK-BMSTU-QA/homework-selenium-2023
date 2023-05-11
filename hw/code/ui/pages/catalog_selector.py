from ui.pages.base_page import BasePage
from ui.locators.catalog_locators import CatalogLocators
from ui.locators.header_locators import HeaderLocators


class CatalogSelector(BasePage):
    categoryLocators = CatalogLocators()
    headerLocators = HeaderLocators()

    def __init__(self, driver, selectors):
        super(CatalogSelector, self).__init__(driver)
        self.locators = selectors
        self.url = self.locators.hrefs.domain + self.locators.hrefs.home

    def selectHeaderCategory(self):
        self.waitUntilInvisible(self.locators.GET_CATEGORIES_CONTAINER)

        self.find(self.locators.OPEN_CATEGORY_SELECTOR_BUTTON).click()

        categories = self.find(self.locators.GET_CATEGORIES_CONTAINER)

        for index in range(int(categories.get_attribute('childElementCount'))):
            category = self.find(self.locators.CATEGORY_SELECTOR_MENU(index + 1))
            category.click()
            self.waitUntilInvisible(self.locators.GET_CATEGORIES_CONTAINER)

            assert self.getInnerText(
                self.categoryLocators.GET_CATEGORY_NAME
            ) == category.get_attribute('innerText')

            self.find(self.locators.OPEN_CATEGORY_SELECTOR_BUTTON).click()

    def selectHomeCategory(self):
        categories = self.find(self.locators.GET_CATEGORIES_CONTAINER)

        for index in range(int(categories.get_attribute('childElementCount'))):
            category = self.find(self.locators.CATEGORY_SELECTOR_MENU(index + 1))
            category.click()
            self.waitUntilInvisible(self.locators.GET_CATEGORIES_CONTAINER)

            self.find(self.headerLocators.GET_LOGO).click()
