from ui.pages.base_page import BasePage
from ui.locators.product_title_locators import ProductTitleLocators
from ui.tabTitles import TabTitles


class ProductTitle(BasePage):
    tabTitles = TabTitles()

    def __init__(self, driver):
        super(ProductTitle, self).__init__(driver)
        self.locators = ProductTitleLocators()
        self.url = self.locators.hrefs.domain + \
            self.locators.hrefs.product + self.locators.hrefs.defaultProduct

    def checkTabTitle(self):
        self.getTabTitle() == self.getInnerText(
            self.locators.GET_PRODUCT_TITLE) + self.tabTitles.rightSideOfTheTitle

    def checkLinkInTheTitles(self):
        self.is_opened(self.getHref(self.locators.GET_PRODUCT_TITLE))

    def checkCategoryLink(self):
        assert self.locators.hrefs.category in self.getHref(
            self.locators.GET_CATEGORY_BUTTON)

    def checkItemPhoto(self):
        self.checkPhoto(self.locators.GET_PHOTO)
