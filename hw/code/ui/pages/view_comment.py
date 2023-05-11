from ui.pages.base_page import BasePage
from ui.locators.view_comment_locators import ViewCommentLocators
from ui.pages.login_page import LoginPage
from ui.locators.base_locators import BaseLocators


class ViewComment(BasePage):
    commentAlreadyHaveBeenAdded = 'Вы уже создали отзыв об этом товаре'

    def __init__(self, driver):
        super(ViewComment, self).__init__(driver)
        self.locators = ViewCommentLocators()
        self.baseLocators = BaseLocators()
        self.loginPage = LoginPage(driver)
        self.url = self.locators.hrefs.domain + \
            self.locators.hrefs.comment + self.locators.hrefs.defaultProduct

    def checkErrorAddComment(self):
        self.getAddCommentButton().click()

        self.checkErrorMessage(self.commentAlreadyHaveBeenAdded)

    def getAddCommentButton(self):
        return self.find(self.locators.ADD_COMMENT_BUTTON)

    def checkUnauthAddComment(self):
        id = self.driver.current_url.split('/')[-1]

        self.getAddCommentButton().click()

        self.is_opened(self.locators.hrefs.domain +
                       self.locators.hrefs.addComment + '/' + id)

    def checkTabTitle(self, text):
        self.waitUntilVisible(self.locators.GET_PRODUCT_NAME)
        assert self.getTabTitle() == self.getInnerText(
            self.locators.GET_PRODUCT_NAME) + text

    def checkHrefPhoto(self):
        self.find(self.locators.GET_PHOTO_REDIRECT_HREF)

    def checkPhotoNotBroken(self):
        self.render(self.getSrc(self.locators.GET_PHOTO))

    def verifyComment(self, pros, cons, other):
        self.waitUntilVisible(self.locators.COMMENT_CONTENT)

        self.scrollToLocator(self.baseLocators.GET_BY_TEXT(pros))

        self.scrollToLocator(self.baseLocators.GET_BY_TEXT(cons))

        self.scrollToLocator(self.baseLocators.GET_BY_TEXT(other))
