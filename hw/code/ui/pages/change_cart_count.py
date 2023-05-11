from ui.pages.base_page import BasePage


class CartCountChange(BasePage):
    defaultAddToCartButtonText = 'В корзину'

    def __init__(self, driver, selectors, url):
        super(CartCountChange, self).__init__(driver)
        self.locators = selectors
        self.url = url

    def checkButtonLabel(self):
        self.scrollToElement(self.locators.GET_COUNT_CONTAINER)

        assert self.defaultAddToCartButtonText in self.getInnerText(
            self.locators.GET_COUNT_CONTAINER)

    def getAddDefaultButton(self):
        return self.find(
            self.locators.GET_COUNT_CONTAINER)

    def getPlusButton(self):
        return self.find(self.locators.GET_PLUS_BUTTON)

    def getMinusButton(self):
        return self.find(self.locators.GET_MINUS_BUTTON)

    def getCountOfItemInCart(self):
        self.waitUntilClickableElement(self.locators.GET_MINUS_BUTTON)
        self.waitUntilClickableElement(self.locators.GET_PLUS_BUTTON)
        self.waitUntilClickableElement(self.locators.GET_ITEM_COUNT_IN_CART)

        return self.getInnerText(
            self.locators.GET_ITEM_COUNT_IN_CART)

    def checkNumberOfItemsInCart(self, number):
        assert int(self.getCountOfItemInCart()) == number

    def scrollToElement(self, selector):
        self.waitUntilVisible(selector)
        self.scrollToLocator(selector)
