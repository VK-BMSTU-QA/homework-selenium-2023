from ui.pages.base_page import BasePage
from ui.locators.add_comment_locators import AddCommentLocators
import uuid


class CreateComment(BasePage):
    rating = 4
    prosComment = f'pros-{uuid.uuid4().hex}'
    consComment = f'cons-{uuid.uuid4().hex}'
    otherComment = f'other-{uuid.uuid4().hex}'

    selectRatingMessage = 'Укажите рейтинг товара'

    def __init__(self, driver):
        super(CreateComment, self).__init__(driver)
        self.locators = AddCommentLocators()
        self.url = self.locators.hrefs.domain + \
            self.locators.hrefs.addComment + self.locators.hrefs.defaultProduct

    def logout(self):
        self.header.logout()

    def submitComment(self):
        self.scrollToLocator(self.locators.SUBMIT_COMMENT_BUTTON)
        self.find(self.locators.SUBMIT_COMMENT_BUTTON).click()

    def checkErrorNoRatingSelected(self):

        self.submitComment()

        self.checkErrorMessage(self.selectRatingMessage)

    def checkUnauthAddComment(self):
        assert self.locators.hrefs.login in self.getHref(self.locators.UNAUTH_LOGIN_LINK)

    def writeField(self, selector, text):
        self.scrollToLocator(selector)

        input = self.find(selector)
        input.clear()
        input.send_keys(text)

    def selectRating(self, index):
        self.scrollToLocator(self.locators.COMMENT_BLOCK_TITLE)
        self.waitUntilClickableElement(self.locators.SELECT_STAR(index))
        self.find(self.locators.SELECT_STAR(index)).click()

    def checkSendComment(self):

        self.selectRating(self.rating)

        self.writeField(self.locators.COMMENT_PROS, self.prosComment)

        self.writeField(self.locators.COMMENT_CONS, self.consComment)

        self.writeField(self.locators.COMMENT_OTHER, self.otherComment)

        self.submitComment()
