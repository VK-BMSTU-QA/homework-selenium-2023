from selenium.webdriver.common.by import By

from base_page import BasePage
from const import *


class TestMainPage(BasePage):
    # check preview film exist
    CLASS_NAME_PREVIEW = 'js-main-page-preview-film'
    CLASS_NAME_PREVIEW_FILM_TITLE = 'preview-film__film-title'

    CLASS_NAME_PAGE_COLLECTION_TITLE = 'page__collection__title'

    # check popular section redirect to collection page
    X_PATH_POPULAR_SECTION_BUTTON = "//div[@class='js-collection-tag-popular']/div/div[1]"
    X_PATH_POPULAR_SECTION_SLIDER_FILM = "//div[@class='js-collection-tag-popular']/div/div[2]"
    PAGE_POPULAR_COLLECTION_TITLE = 'Популярное'

    # check in cinema section redirect to collection page
    X_PATH_IN_CINEMA_SECTION_BUTTON = "//div[@class='js-collection-tag-in_cinema']/div/div[1]"
    X_PATH_IN_CINEMA_SECTION_SLIDER_FILM = "//div[@class='js-collection-tag-in_cinema']/div/div[2]"
    PAGE_IN_CINEMA_COLLECTION_TITLE = 'Сейчас в кино'

    # check genres section redirect to collection page
    X_PATH_GENRES_SECTION_BUTTON = "//div[@class='js-collection-genre-genres']/div/div[1]"
    X_PATH_GENRES_SECTION_SLIDER_GENRE = "//div[@class='js-collection-genre-genres']/div/div[2]"
    PAGE_GENRES_COLLECTION_TITLE = 'Жанры'

    def test_preview_film_existing(self):
        self.render(DOMAIN)

        assert self.find((By.CLASS_NAME, self.CLASS_NAME_PREVIEW))

        assert self.find((By.CLASS_NAME, self.CLASS_NAME_PREVIEW_FILM_TITLE))

    def test_popular_section(self):
        self.render(DOMAIN)

        assert self.find((By.XPATH, self.X_PATH_POPULAR_SECTION_SLIDER_FILM))

        self.find((By.XPATH, self.X_PATH_POPULAR_SECTION_BUTTON)).click()

        title = self.find((By.CLASS_NAME, self.CLASS_NAME_PAGE_COLLECTION_TITLE)).text

        if title != self.PAGE_POPULAR_COLLECTION_TITLE:
            raise Exception("title does not equal", title, self.PAGE_POPULAR_COLLECTION_TITLE)

    def test_in_cinema_section(self):
        self.render(DOMAIN)

        assert self.find((By.XPATH, self.X_PATH_IN_CINEMA_SECTION_SLIDER_FILM))

        self.find((By.XPATH, self.X_PATH_IN_CINEMA_SECTION_BUTTON)).click()

        title = self.find((By.CLASS_NAME, self.CLASS_NAME_PAGE_COLLECTION_TITLE)).text

        if title != self.PAGE_IN_CINEMA_COLLECTION_TITLE:
            raise Exception("title does not equal", title, self.PAGE_IN_CINEMA_COLLECTION_TITLE)

    def test_genres_section(self):
        self.render(DOMAIN)

        assert self.find((By.XPATH, self.X_PATH_GENRES_SECTION_SLIDER_GENRE))

        self.find((By.XPATH, self.X_PATH_GENRES_SECTION_BUTTON)).click()

        title = self.find((By.CLASS_NAME, self.CLASS_NAME_PAGE_COLLECTION_TITLE)).text

        if title != self.PAGE_GENRES_COLLECTION_TITLE:
            raise Exception("title does not equal", title, self.PAGE_GENRES_COLLECTION_TITLE)
