from ui.pages.base_page import BasePage


class CatalogPage(BasePage):
    rotateImgClass = 'rotate-img-180'
    imgVisibleClass = 'sort-rating__img_visible'

    def __init__(self, driver, selectors, url):
        super(CatalogPage, self).__init__(driver)
        self.locators = selectors
        self.url = url

    def checkSort(self, buttton, param):
        sortOrderIcon = self.find(self.locators.SORT_ORDER_ICON)

        assert self.rotateImgClass not in sortOrderIcon.get_attribute('class')
        assert self.imgVisibleClass not in sortOrderIcon.get_attribute('class')

        buttton.click()

        assert f'sort={param}down' in self.driver.current_url
        assert f'sort={param}up' not in self.driver.current_url
        assert self.rotateImgClass not in sortOrderIcon.get_attribute('class')
        assert self.imgVisibleClass in sortOrderIcon.get_attribute('class')

        buttton.click()

        assert f'sort={param}up' in self.driver.current_url
        assert f'sort={param}down' not in self.driver.current_url
        assert self.rotateImgClass in sortOrderIcon.get_attribute('class')
        assert self.imgVisibleClass in sortOrderIcon.get_attribute('class')

    def checkRatingSort(self):
        sortRatingButton = self.find(self.locators.SORT_RATING_BUTTON)
        self.checkSort(sortRatingButton, 'rating')

    def checkPriceSort(self):
        sortPriceButton = self.find(self.locators.SORT_PRICE_BUTTON)
        self.checkSort(sortPriceButton, 'price')

    def checkTabTitle(self):
        assert self.getInnerText(self.locators.GET_CATEGORY_NAME) in self.getTabTitle()

    def checkIfPhotoBroken(self):
        self.checkPhoto(self.locators.GET_PICTURE)

    def checkTitleLink(self):
        assert self.locators.hrefs.product in self.getHref(self.locators.GET_TEXT_LINK)

    def checkImgLink(self):
        assert self.locators.hrefs.product in self.getHref(self.locators.GET_IMG_LINK)
