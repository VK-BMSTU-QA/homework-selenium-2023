from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from locators.pageNavigationLocators import SelectorsNavigation
from utils.driver import dvr


class pageNavigation(BasePage):
    def render_main(self):
        self.render(SelectorsNavigation.URL_MAIN)

    def click_logo(self):
        self.render(f'/collection/tag-popular/')

        logo = self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_LOGO))
        logo.click()

        return self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_PREVIEW_FILM))

    def click_popular_button(self):
        self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_HEADER_POPULAR_BUTTON)).click()

        title = self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_COLLECTION_PAGE_TITLE)).text

        return title

    def click_premieres_button(self):
        self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_HEADER_PREMIERES_BUTTON)).click()

        title = self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_PREMIERES_PAGE_TITLE)).text

        return title

    def click_collections_button_unauthorized(self):
        self.find((By.XPATH, SelectorsNavigation.X_PATH_HEADER_COLLECTIONS_BUTTON)).click()

        modal_auth = self.find((By.CLASS_NAME, SelectorsNavigation.MODAL_AUTH_CLASS_NAME))
        return modal_auth

    def click_login_button(self):
       header_login_button = self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_HEADER_LOGIN_BUTTON))
       header_login_button.click()

       modal_auth = self.find((By.CLASS_NAME, SelectorsNavigation.MODAL_AUTH_CLASS_NAME))
       return modal_auth

    def click_collections_button_authorized(self):
        self.find((By.XPATH, SelectorsNavigation.X_PATH_HEADER_COLLECTIONS_BUTTON)).click()

        title = self.find((By.CLASS_NAME, SelectorsNavigation.CLASS_NAME_USER_COLLECTION_PAGE_TITLE)).text

        return title
