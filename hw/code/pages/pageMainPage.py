from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from locators.pageMainPageLocators import SelectorsMainPage


class PageMainPage(BasePage):
    def render_page(self):
        self.render(SelectorsMainPage.URL_PAGE_MAIN)

    def get_title_cur_collection(self):
        return self.find((By.CLASS_NAME, SelectorsMainPage.CLASS_NAME_PAGE_COLLECTION_TITLE)).text

    def move_to_genres(self):
        self.find((By.XPATH, SelectorsMainPage.X_PATH_GENRES_SECTION_BUTTON)).click()

    def move_to_in_cinema_collection(self):
        self.find((By.XPATH, SelectorsMainPage.X_PATH_IN_CINEMA_SECTION_BUTTON)).click()

    def move_to_popular_collection(self):
        self.find((By.XPATH, SelectorsMainPage.X_PATH_POPULAR_SECTION_BUTTON)).click()

    def get_meny_popular(self):
        return self.find((By.XPATH, SelectorsMainPage.X_PATH_POPULAR_SECTION_SLIDER_FILM))

    def get_meny_preview(self):
        return self.find((By.CLASS_NAME, SelectorsMainPage.CLASS_NAME_PREVIEW))

    def get_preview_title(self):
        return self.find((By.CLASS_NAME, SelectorsMainPage.CLASS_NAME_PREVIEW_FILM_TITLE)).text

    def get_meny_in_cinema(self):
        return self.find((By.XPATH, SelectorsMainPage.X_PATH_IN_CINEMA_SECTION_SLIDER_FILM)).text

    def get_meny_genres(self):
        return self.find((By.XPATH, SelectorsMainPage.X_PATH_GENRES_SECTION_SLIDER_GENRE)).text
