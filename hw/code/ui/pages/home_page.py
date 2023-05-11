from ui.pages.base_page import BasePage
from ui.locators.home_locators import HomeLocators


class HomePage(BasePage):

    def __init__(self, driver, selectors):
        super(HomePage, self).__init__(driver)
        self.locators = HomeLocators
        self.url = self.locators.hrefs.domain + self.locators.hrefs.home

    def checkCategories(self):
        categoriesCount = self.find(
            self.locators.GET_CATEGORIES_CONTAINER).get_attribute('childElementCount')

        for categoryIndex in range(int(categoriesCount)):
            self.locators.CATEGORY_SELECTOR_MENU(categoryIndex + 1)
