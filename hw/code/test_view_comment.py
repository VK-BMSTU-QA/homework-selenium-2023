import allure
from ui.fixtures import get_driver
from ui.pages.view_comment import ViewComment
from ui.pages.login_page import LoginPage
from ui.pages.header import Header


class TestViewComment():
    driver = get_driver(browser_name='chrome')
    viewComment = ViewComment(driver)
    loginPage = LoginPage(driver)
    header = Header(driver)

    @allure.feature('TestViewComment')
    @allure.story('check tab title')
    @viewComment.render_decorator
    def test_page_title(self):
        self.viewComment.checkTabTitle(' - Отзывы, Reazon')

    @allure.feature('TestViewComment')
    @allure.story('check photo redirect')
    @viewComment.render_decorator
    def test_check_href_photos(self):
        self.viewComment.checkHrefPhoto()

    @allure.feature('TestViewComment')
    @allure.story('check photo is not broken')
    @viewComment.render_decorator
    def test_check_if_photo_broken(self):
        self.viewComment.checkPhotoNotBroken()

    @allure.feature('TestViewComment')
    @allure.story('check error message. Auth add comment button')
    @viewComment.render_decorator
    def test_auth_add_comment_button(self):
        with allure.step('login'):
            self.loginPage.render_page()
            self.loginPage.login()

        with allure.step('checkErrorAddComment'):
            self.viewComment.render_page()
            self.viewComment.checkErrorAddComment()

        with allure.step('logout'):
            self.header.logout()

    @allure.feature('TestViewComment')
    @allure.story('check redirect unauth add comment button')
    @viewComment.render_decorator
    def test_unauth_add_comment_button(self):
        self.viewComment.checkUnauthAddComment()
