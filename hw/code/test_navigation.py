from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from utils.helper_auth import needed_auth

class SelectorsNavigation:
    # check logo redirect
    CLASS_NAME_LOGO = 'header__navlink'
    CLASS_NAME_PREVIEW_FILM = 'js-main-page-preview-film'

    # check popular button redirect
    CLASS_NAME_HEADER_POPULAR_BUTTON = 'js-header__navlink-my-films'
    CLASS_NAME_COLLECTION_PAGE_TITLE = 'page__collection__title'
    POPULAR_COLLECTION_PAGE_TITLE = 'Популярное'

    # check premieres button redirect
    CLASS_NAME_HEADER_PREMIERES_BUTTON = 'js-header__navlink-top-250'
    CLASS_NAME_PREMIERES_PAGE_TITLE = 'premiere-page__title'
    PREMIERES_PAGE_TITLE = 'Премьеры'

    # check collections button open modal window
    X_PATH_HEADER_COLLECTIONS_BUTTON = "//a[@class='header__navlink js-header__navlink-my-colls']"
    MODAL_AUTH_CLASS_NAME = 'auth__wrapper'

    # check collections button with auth redirect
    CLASS_NAME_USER_COLLECTION_PAGE_TITLE = 'user-collection-list__title'
    USER_COLLECTION_PAGE_TITLE = 'Ваши коллекции'

    # check login button open modal window
    CLASS_NAME_HEADER_LOGIN_BUTTON = 'js-header__login__btn'

class TestNavigationPanelUnauthorized(BasePage):

    def test_click_logo(self):
        self.render(f'/collection/tag-popular/')

        self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_LOGO)).click()

        assert self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_PREVIEW_FILM))

    def test_click_popular_button(self):
        self.render('/')

        self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_HEADER_POPULAR_BUTTON)).click()

        title = self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_COLLECTION_PAGE_TITLE)).text

        if title != SelectorsNavigation.POPULAR_COLLECTION_PAGE_TITLE:
            raise Exception("title does not equal", title, SelectorsNavigation.POPULAR_COLLECTION_PAGE_TITLE)

    def test_click_premieres_button(self):
        self.render('/')

        self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_HEADER_PREMIERES_BUTTON)).click()

        title = self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_PREMIERES_PAGE_TITLE)).text

        if title != SelectorsNavigation.PREMIERES_PAGE_TITLE:
            raise Exception("title does not equal", title, SelectorsNavigation.PREMIERES_PAGE_TITLE)

    def test_click_collections_button_unauthorized(self):
        self.render('/')

        self.find((By.XPATH, SelectorsNavigation.X_PATH_HEADER_COLLECTIONS_BUTTON)).click()

        assert self.find((By.CLASS_NAME, SelectorsNavigation.MODAL_AUTH_CLASS_NAME))

    def test_click_login_button(self):
        self.render('/')

        self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_HEADER_LOGIN_BUTTON)).click()

        assert self.find((By.CLASS_NAME, SelectorsNavigation.MODAL_AUTH_CLASS_NAME))

    @needed_auth
    def test_click_collections_button_authorized(self):
        self.render('/')

        self.find((By.XPATH, SelectorsNavigation.X_PATH_HEADER_COLLECTIONS_BUTTON)).click()

        title = self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_USER_COLLECTION_PAGE_TITLE)).text

        if title != SelectorsNavigation.USER_COLLECTION_PAGE_TITLE:
            raise Exception("title does not equal", title, SelectorsNavigation.USER_COLLECTION_PAGE_TITLE)
