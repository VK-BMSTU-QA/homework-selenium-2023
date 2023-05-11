from ui.pages.base_page import BasePage
from ui.locators.horizontal_scroll_catalog_locators import HorizontalScrollCatalogLocators


class HorizontalScrollCatalog(BasePage):

    def __init__(self, driver):
        super(HorizontalScrollCatalog, self).__init__(driver)
        self.locators = HorizontalScrollCatalogLocators()
        self.url = self.locators.hrefs.domain + \
            self.locators.hrefs.product + self.locators.hrefs.defaultProduct

    def getNumberOfElementsInContainer(self, index):
        return self.find(
            self.locators.GET_SCROLL_CONTAINER(index)).get_attribute('childElementCount')

    def getItemContainerOffsetHeight(self, containerIndex, ItemIndex):
        return int(self.find(
            self.locators.GET_ITEM_CONTAINER_BY_INDEX(
                containerIndex, ItemIndex)).size['width'])

    def getScrollPosition(self, index):
        return int(self.find(
            self.locators.GET_SCROLL_CONTAINER(index)).get_attribute('scrollLeft'))

    def checkScrollShiftLeft(self):
        self.waitUntilClickableElement(self.locators.GET_ITEM_CONTAINER_BY_INDEX(
            1, 1))

        assert self.getScrollPosition(1) == 0

    def checkScrollShiftRight(self):
        self.waitUntilClickableElement(self.locators.GET_ITEM_CONTAINER_BY_INDEX(
            1, 7))

        assert self.getScrollPosition(1) >= self.getItemContainerOffsetHeight(1, 1)

    def scrollRight(self):
        scrollRightButton = self.find(self.locators.SCROLL_TO_RIGHT_BUTTON)
        scrollRightButton.click()
        self.waitUntilClickableElement(self.locators.SCROLL_TO_RIGHT_BUTTON)

    def scrollLeft(self):
        scrollLeftButton = self.find(self.locators.SCROLL_TO_LEFT_BUTTON)
        scrollLeftButton.click()
        self.waitUntilClickableElement(self.locators.SCROLL_TO_LEFT_BUTTON)

    def scrollToTheContainer(self, index=1):
        self.scrollToLocator(self.locators.GET_SCROLL_CONTAINER(index))

    def checkTitleLink(self):
        self.waitUntilVisible(self.locators.GET_ITEM_TITLE, 5)
        assert self.locators.hrefs.product in self.getHref(self.locators.GET_ITEM_TITLE)

    def checkPhotoBroken(self):
        self.checkPhoto(self.locators.GET_IMAGE_OF_ITEM_BY_INDEX(1, 1))
