import allure
from ui.fixtures import get_driver
from ui.pages.view_comment import ViewComment
from ui.pages.create_review_page import CreateComment
from ui.pages.login_page import LoginPage
from ui.pages.header import Header


class TestCreateComment():
    driver = get_driver(browser_name='chrome')
    viewComment = ViewComment(driver)
    createComment = CreateComment(driver)
    loginPage = LoginPage(driver)
    header = Header(driver)

    @allure.feature('TestCreateComment')
    @allure.story('auth checks')
    @createComment.render_decorator
    def test_page_auth(self):
        with allure.step('login'):
            self.loginPage.render_page()
            self.loginPage.login()
            self.createComment.render_page()

        with allure.step('checkTabTitle'):
            self.viewComment.checkTabTitle(' - Отзыв, Reazon')

        with allure.step('checkHrefPhoto'):
            self.viewComment.checkHrefPhoto()

        with allure.step('checkErrorNoRatingSelected'):
            self.createComment.checkErrorNoRatingSelected()

        with allure.step('checkSendComment'):
            self.createComment.checkSendComment()

        with allure.step('verigy vomment'):
            self.viewComment.verifyComment(
                self.createComment.prosComment,
                self.createComment.consComment,
                self.createComment.otherComment
            )

        with allure.step('logout'):
            self.header.logout()

    @allure.feature('TestCreateComment')
    @allure.story('check redirect unauth add comment button')
    @createComment.render_decorator
    def test_unauth(self):
        self.createComment.checkUnauthAddComment()
