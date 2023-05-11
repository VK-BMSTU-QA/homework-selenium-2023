from ui.pages.base_page import BasePage


class Rating(BasePage):

    def __init__(self, driver, selectors):
        super(Rating, self).__init__(driver)
        self.locators = selectors
        self.url = self.locators.hrefs.domain + self.locators.hrefs.product + '/43'

    def checkRatingNumber(self):
        rating = float(self.getInnerText(self.locators.GET_RATING_NUMBER))

        assert int(rating / 10) == 0
        assert rating * 10 <= 50
        assert rating * 10 >= 0

    def checkLinkInRating(self):
        assert self.locators.hrefs.domain + \
            self.locators.hrefs.comment in self.getHref(self.locators.GET_RATING_LINK)
