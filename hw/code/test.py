import time
import re

from BasePage import BasePage
from HelperLogin import HelperLogin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Driver import dvr

URL = 'https://movie-gate.online'
helper = HelperLogin(URL)


class TestLogin(BasePage):
    url = URL

    def test_login(self):
        helper.login()
        helper.logout()


class TestFilmPage(BasePage):
    X_BUTTON_PLUS = '/html/body/div/div/div[1]/div/div[2]/div[7]/div/a/div'
    X_BUTTON_BOOKMARK = '/html/body/div/div/div[1]/div/div[2]/div[7]/a[2]/div'
    X_BUTTON_TRAILER = '/html/body/div/div/div[1]/div/div[2]/div[7]/a[1]/div'
    X_PRODUCER = '/html/body/div/div/div[1]/div/div[2]/div[5]/div[2]'
    X_PRODUCER_ON_PAGE = '/html/body/div/div/div[1]/div/div/div/div[1]'
    X_TOSTER = '/html/body/div/div[2]'
    X_TRAILER_CONTAINER = '/html/body/div/div[1]/div/div/iframe'
    X_BUTTON_RATE_9 = '/html/body/div/div/div[2]/div[2]/div[2]/form/div/div[2]/div[1]/button[2]'
    X_BUTTON_RATE_1 = '/html/body/div/div/div[2]/div[2]/div[2]/form/div/div[2]/div[1]/button[10]'
    X_BUTTON_RATE_CONTAINER = '/html/body/div/div/div[2]/div[2]/div[2]/form/div/div[2]/div[1]'
    X_BUTTON_RATE_DELETE = '/html/body/div/div/div[2]/div[2]/div[2]/form/div/div[4]/button'
    X_BUTTON_REVIEW = '/html/body/div/div/div[4]/div[1]/div/div/div[1]/a/div'
    X_BUTTON_REVIEW_CONTAINER = '/html/body/div/div[1]/div/div/div/div'
    X_BUTTON_CHOOSE_TYPE = '/html/body/div/div[1]/div/div/div/div/form/div[1]/div/div'
    X_BUTTON_NEGATIVE_TYPE = '/html/body/div/div[1]/div/div/div/div/form/div[1]/div/ul/li[3]'
    X_BUTTON_NEUTRAL_TYPE = '/html/body/div/div[1]/div/div/div/div/form/div[1]/div/ul/li[2]'
    X_BUTTON_POSITIVE_TYPE = '/html/body/div/div[1]/div/div/div/div/form/div[1]/div/ul/li[1]'
    X_INPUT_TITLE = '/html/body/div/div[1]/div/div/div/div/form/div[2]/input'
    X_INPUT_TEXT = '/html/body/div/div[1]/div/div/div/div/form/div[3]/textarea'
    X_BUTTON_SEND_REVIEW = '/html/body/div/div[1]/div/div/div/div/form/button'
    X_UPPER_REVIEW = '/html/body/div/div/div[4]/div[1]/div/div/div[2]/div[1]/div'
    X_UPPER_REVIEW_TITLE = '/html/body/div/div/div[4]/div[1]/div/div/div[2]/div[1]/div/div[2]'
    X_UPPER_REVIEW_TEXT = '/html/body/div/div/div[4]/div[1]/div/div/div[2]/div[1]/div/div[3]'
    TEXT = '200IQ text'
    TITLE = 'title'

    def test_click_producer(self):
        self.render(f'{URL}/film/1')

        prod = self.find((By.XPATH, self.X_PRODUCER), 3).text.strip()
        self.find((By.XPATH, self.X_PRODUCER), 5).click()

        prod_on_page = self.find((By.XPATH, self.X_PRODUCER_ON_PAGE), 3).text.strip()
        if prod != prod_on_page:
            raise Exception("names does not equal", prod, prod_on_page)

    def test_click_plus_unauth(self):
        self.render(f'{URL}/film/1')
        time.sleep(4)
        self.find((By.XPATH, self.X_BUTTON_PLUS)).click()
        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

        self.find((By.XPATH, self.X_BUTTON_BOOKMARK)).click()
        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

    def test_click_trailer(self):
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_TRAILER)).click()
        self.find((By.XPATH, self.X_TRAILER_CONTAINER))

    def test_click_set_rate(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_RATE_9)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))
        helper.logout()

    def test_click_update_rate(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_RATE_9)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

        self.find((By.XPATH, self.X_BUTTON_RATE_1)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))
        helper.logout()

    def test_click_delete_rate(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_RATE_9)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

        self.find((By.XPATH, self.X_BUTTON_RATE_DELETE)).click()
        self.wait_hide((By.XPATH, self.X_BUTTON_RATE_DELETE))

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))
        helper.logout()

    def test_click_review_unauth(self):
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

    def test_click_review(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()
        self.find((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER))
        helper.logout()

    def test_click_review(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()
        self.find((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER))

        self.find((By.XPATH, self.X_BUTTON_CHOOSE_TYPE)).click()
        self.find((By.XPATH, self.X_BUTTON_NEGATIVE_TYPE)).click()

        self.find((By.XPATH, self.X_INPUT_TITLE)).send_keys(self.TITLE)
        self.find((By.XPATH, self.X_INPUT_TEXT)).send_keys(self.TEXT)

        self.find((By.XPATH, self.X_BUTTON_SEND_REVIEW)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))
        helper.logout()

    def test_error_review(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()
        self.find((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER))

        self.find((By.XPATH, self.X_INPUT_TITLE)).send_keys(self.TITLE)
        self.find((By.XPATH, self.X_INPUT_TEXT)).send_keys(self.TEXT)

        self.find((By.XPATH, self.X_BUTTON_SEND_REVIEW)).click()

        try:
            self.wait_hide((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER), 1)
        except:
            self.find((By.XPATH, self.X_BUTTON_SEND_REVIEW))

        helper.logout()

    def test_check_correct_review(self):
        helper.login()
        self.render(f'{URL}/film/1')
        self.find((By.XPATH, self.X_BUTTON_REVIEW)).click()
        self.find((By.XPATH, self.X_BUTTON_REVIEW_CONTAINER))

        self.find((By.XPATH, self.X_BUTTON_CHOOSE_TYPE)).click()
        self.find((By.XPATH, self.X_BUTTON_NEGATIVE_TYPE)).click()

        self.find((By.XPATH, self.X_INPUT_TITLE)).send_keys(self.TITLE)
        self.find((By.XPATH, self.X_INPUT_TEXT)).send_keys(self.TEXT)

        self.find((By.XPATH, self.X_BUTTON_SEND_REVIEW)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

        title = self.find((By.XPATH, self.X_UPPER_REVIEW_TITLE)).text
        if title != self.TITLE:
            raise Exception("names does not equal", title, self.TITLE)

        text = self.find((By.XPATH, self.X_UPPER_REVIEW_TEXT)).text
        if text != self.TEXT:
            raise Exception("names does not equal", text, self.TEXT)

        helper.logout()


class TestSearch(BasePage):
    X_INPUT_SEARCH = '/html/body/div/header/form/input'
    X_BUTTON_RETURN_MAIN = '/html/body/div/div/div[2]/div[4]/div'
    X_TITLE_SEARCH = '/html/body/div/div/div[1]'
    TITLE_SEARCH = 'Результаты поиска'
    ALL_GROUP_SEARCH = 'a'
    X_SEARCH_GROUP_FILMS = '/html/body/div/div/div[2]/div[1]/div/div/div[1]'
    SEARCH_GROUP_FILMS = 'Найденные фильмы:'
    X_SEARCH_GROUP_SERAILS = '/html/body/div/div/div[2]/div[2]/div/div/div[1]'
    SEARCH_GROUP_SERAILS = 'Найденные сериалы:'
    X_SEARCH_GROUP_PERSONS = '/html/body/div/div/div[2]/div[3]/div/div/div[1]'
    SEARCH_GROUP_PERSONS = 'Найденные имена:'
    X_FIRST_FOUNDED_FILM = '/html/body/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/div[1]/div[1]'
    X_FIRST_FOUNDED_TITLE = '/html/body/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]'
    X_TITLE_ON_FILM_PAGE = '/html/body/div/div/div[1]/div/div[2]/div[1]'

    def test_check_exists(self):
        self.render(URL)
        self.find((By.XPATH, self.X_INPUT_SEARCH)).send_keys(Keys.ENTER)
        title = self.find((By.XPATH, self.X_TITLE_SEARCH)).text
        if title != self.TITLE_SEARCH:
            raise Exception("stings does not equal", title, self.TITLE_SEARCH)

    def test_check_empty(self):
        self.render(URL)
        self.find((By.XPATH, self.X_INPUT_SEARCH)).send_keys(Keys.ENTER)
        self.find((By.XPATH, self.X_BUTTON_RETURN_MAIN)).click()

    def test_check_group_category(self):
        self.render(URL)
        self.find((By.XPATH, self.X_INPUT_SEARCH)).send_keys(self.ALL_GROUP_SEARCH, Keys.ENTER)

        films_field = self.find((By.XPATH, self.X_SEARCH_GROUP_FILMS)).text
        if films_field != self.SEARCH_GROUP_FILMS:
            raise Exception("stings does not equal", films_field, self.SEARCH_GROUP_FILMS)

        serials_field = self.find((By.XPATH, self.X_SEARCH_GROUP_SERAILS)).text
        if serials_field != self.SEARCH_GROUP_SERAILS:
            raise Exception("stings does not equal", serials_field, self.SEARCH_GROUP_SERAILS)

        persons_field = self.find((By.XPATH, self.X_SEARCH_GROUP_PERSONS)).text
        if persons_field != self.SEARCH_GROUP_PERSONS:
            raise Exception("stings does not equal", persons_field, self.SEARCH_GROUP_PERSONS)

    def test_correct_results(self):
        self.render(URL)
        self.find((By.XPATH, self.X_INPUT_SEARCH)).send_keys(self.ALL_GROUP_SEARCH, Keys.ENTER)

        films_field = self.find((By.XPATH, self.X_FIRST_FOUNDED_TITLE)).text
        self.find((By.XPATH, self.X_FIRST_FOUNDED_FILM)).click()
        film_title = self.find((By.XPATH, self.X_TITLE_ON_FILM_PAGE)).text
        if films_field != film_title:
            raise Exception("stings does not equal", films_field, film_title)

class TestPerson(BasePage):
    X_FIRST_FOUNDED_FILM = '/html/body/div/div/div[2]/div/div[2]/div/div/a/div/div[1]'
    REDIRECTED_PAGE_URL = 'https://movie-gate.online/film/'
    url = URL

    def test_person(self):
        self.render(f'{URL}/person/27/')
        self.find((By.XPATH, self.X_FIRST_FOUNDED_FILM)).click()
        pattern = self.REDIRECTED_PAGE_URL
        current__url = dvr.get_instance().current_url
        if (re.search(current__url, pattern)):
            raise Exception("wrong redirect", pattern, current__url)

class TestNavigationPanel(BasePage):
    X_LOGO = '/html/body/div/header/a[1]'
    PREVIEW_FILM_CLASS_NAME = 'js-main-page-preview-film'
    X_POPULAR_HEADER_BUTTON = '/html/body/div/header/a[2]'
    COLLECTION_PAGE_TITLE_CLASS_NAME = 'page__collection__title'
    POPULAR_COLLECTION_PAGE_TITLE = 'Популярное'
    X_PREMIERES_HEADER_BUTTON = '/html/body/div/header/a[4]'
    PREMIERES_PAGE_TITLE_CLASS_NAME = 'premiere-page__title'
    PREMIERES_PAGE_TITLE = 'Премьеры'
    X_COLLECTIONS_HEADER_BUTTON = '/html/body/div/header/a[3]'
    COLLECTIONS_HEADER_BUTTON_CLASS_NAME = 'header__navlink js-header__navlink-my-colls'
    MODAL_AUTH_CLASS_NAME = 'auth__wrapper'
    X_LOGIN_BUTTON = '/html/body/div/header/a[5]'
    USER_COLLECTION_PAGE_TITLE_CLASS_NAME = 'user-collection-list__title'
    USER_COLLECTION_PAGE_TITLE = 'Ваши коллекции'

    def test_click_logo(self):
        self.render(f'{URL}/collection/tag-popular/')

        self.find((By.XPATH, self.X_LOGO), 3).click()

        assert self.find((By.CLASS_NAME, self.PREVIEW_FILM_CLASS_NAME), 3)

    def test_click_popular_button(self):
        self.render(URL)

        self.find((By.XPATH, self.X_POPULAR_HEADER_BUTTON), 3).click()

        title = self.find((By.CLASS_NAME, self.COLLECTION_PAGE_TITLE_CLASS_NAME), 3).text

        if title != self.POPULAR_COLLECTION_PAGE_TITLE:
            raise Exception("title does not equal", title, self.POPULAR_COLLECTION_PAGE_TITLE)

    def test_click_premieres_button(self):
        self.render(URL)

        self.find((By.XPATH, self.X_PREMIERES_HEADER_BUTTON), 3).click()

        title = self.find((By.CLASS_NAME, self.PREMIERES_PAGE_TITLE_CLASS_NAME), 3).text

        if title != self.PREMIERES_PAGE_TITLE:
            raise Exception("title does not equal", title, self.PREMIERES_PAGE_TITLE)

    def test_click_collections_button_unauthorized(self):
        self.render(URL)

        self.find((By.XPATH, self.X_COLLECTIONS_HEADER_BUTTON), 3).click()

        assert self.find((By.CLASS_NAME, self.MODAL_AUTH_CLASS_NAME), 3)

    def test_click_login_button(self):
        self.render(URL)

        self.find((By.XPATH, self.X_LOGIN_BUTTON), 3).click()

        assert self.find((By.CLASS_NAME, self.MODAL_AUTH_CLASS_NAME), 3)

    def test_click_collections_button_authorized(self):
        helper.login()

        self.find((By.XPATH, self.X_COLLECTIONS_HEADER_BUTTON), 5).click()

        title = self.find((By.CLASS_NAME, self.USER_COLLECTION_PAGE_TITLE_CLASS_NAME), 3).text

        if title != self.USER_COLLECTION_PAGE_TITLE:
            raise Exception("title does not equal", title, self.USER_COLLECTION_PAGE_TITLE)

        helper.logout()

class TestNavigationPanel(BasePage):
    X_LOGO = '/html/body/div/header/a[1]'
    PREVIEW_FILM_CLASS_NAME = 'js-main-page-preview-film'
    X_POPULAR_HEADER_BUTTON = '/html/body/div/header/a[2]'
    COLLECTION_PAGE_TITLE_CLASS_NAME = 'page__collection__title'
    POPULAR_COLLECTION_PAGE_TITLE = 'Популярное'
    X_PREMIERES_HEADER_BUTTON = '/html/body/div/header/a[4]'
    PREMIERES_PAGE_TITLE_CLASS_NAME = 'premiere-page__title'
    PREMIERES_PAGE_TITLE = 'Премьеры'
    X_COLLECTIONS_HEADER_BUTTON = '/html/body/div/header/a[3]'
    COLLECTIONS_HEADER_BUTTON_CLASS_NAME = 'header__navlink js-header__navlink-my-colls'
    MODAL_AUTH_CLASS_NAME = 'auth__wrapper'
    X_LOGIN_BUTTON = '/html/body/div/header/a[5]'
    USER_COLLECTION_PAGE_TITLE_CLASS_NAME = 'user-collection-list__title'
    USER_COLLECTION_PAGE_TITLE = 'Ваши коллекции'

    def test_click_logo(self):
        self.render(f'{URL}/collection/tag-popular/')

        self.find((By.XPATH, self.X_LOGO), 3).click()

        assert self.find((By.CLASS_NAME, self.PREVIEW_FILM_CLASS_NAME), 3)

    def test_click_popular_button(self):
        self.render(URL)

        self.find((By.XPATH, self.X_POPULAR_HEADER_BUTTON), 3).click()

        title = self.find((By.CLASS_NAME, self.COLLECTION_PAGE_TITLE_CLASS_NAME), 3).text

        if title != self.POPULAR_COLLECTION_PAGE_TITLE:
            raise Exception("title does not equal", title, self.POPULAR_COLLECTION_PAGE_TITLE)

    def test_click_premieres_button(self):
        self.render(URL)

        self.find((By.XPATH, self.X_PREMIERES_HEADER_BUTTON), 3).click()

        title = self.find((By.CLASS_NAME, self.PREMIERES_PAGE_TITLE_CLASS_NAME), 3).text

        if title != self.PREMIERES_PAGE_TITLE:
            raise Exception("title does not equal", title, self.PREMIERES_PAGE_TITLE)

    def test_click_collections_button_unauthorized(self):
        self.render(URL)

        self.find((By.XPATH, self.X_COLLECTIONS_HEADER_BUTTON), 3).click()

        assert self.find((By.CLASS_NAME, self.MODAL_AUTH_CLASS_NAME), 3)

    def test_click_login_button(self):
        self.render(URL)

        self.find((By.XPATH, self.X_LOGIN_BUTTON), 3).click()

        assert self.find((By.CLASS_NAME, self.MODAL_AUTH_CLASS_NAME), 3)

    def test_click_collections_button_authorized(self):
        helper.login()

        self.find((By.XPATH, self.X_COLLECTIONS_HEADER_BUTTON), 5).click()

        title = self.find((By.CLASS_NAME, self.USER_COLLECTION_PAGE_TITLE_CLASS_NAME), 3).text

        if title != self.USER_COLLECTION_PAGE_TITLE:
            raise Exception("title does not equal", title, self.USER_COLLECTION_PAGE_TITLE)

        helper.logout()


class TestMainPage(BasePage):
    PREVIEW_FILM_CLASS_NAME = 'js-main-page-preview-film'
    PREVIEW_FILM_TITLE_CLASS_NAME = 'preview-film__film-title'

    PAGE_COLLECTION_TITLE_CLASS_NAME = 'page__collection__title'

    X_POPULAR_SECTION_BUTTON = '/html/body/div/div/div[2]/div[1]/div/div[1]'
    X_POPULAR_SECTION_SLIDER_FILM = '/html/body/div/div/div[2]/div[1]/div/div[2]/div/div[2]'
    PAGE_POPULAR_COLLECTION_TITLE = 'Популярное'

    X_IN_CINEMA_SECTION_BUTTON = '/html/body/div/div/div[2]/div[2]/div/div[1]'
    X_IN_CINEMA_SECTION_SLIDER_FILM = '/html/body/div/div/div[2]/div[2]/div/div[2]/div/div[1]'
    PAGE_IN_CINEMA_COLLECTION_TITLE = 'Сейчас в кино'

    X_GENRES_SECTION_BUTTON = '/html/body/div/div/div[2]/div[3]/div/div[1]'
    X_GENRES_SECTION_SLIDER_GENRE = '/html/body/div/div/div[2]/div[3]/div/div[2]/div/div[1]'
    PAGE_GENRES_COLLECTION_TITLE = 'Жанры'

    def test_preview_film_existing(self):
        self.render(URL)

        assert self.find((By.CLASS_NAME, self.PREVIEW_FILM_CLASS_NAME), 3)

        assert self.find((By.CLASS_NAME, self.PREVIEW_FILM_TITLE_CLASS_NAME), 3)

    def test_popular_section(self):
        self.render(URL)

        assert self.find((By.XPATH, self.X_POPULAR_SECTION_SLIDER_FILM), 3)

        self.find((By.XPATH, self.X_POPULAR_SECTION_BUTTON), 3).click()

        title = self.find((By.CLASS_NAME, self.PAGE_COLLECTION_TITLE_CLASS_NAME), 3).text

        if title != self.PAGE_POPULAR_COLLECTION_TITLE:
            raise Exception("title does not equal", title, self.PAGE_POPULAR_COLLECTION_TITLE)

    def test_in_cinema_section(self):
        self.render(URL)

        assert self.find((By.XPATH, self.X_IN_CINEMA_SECTION_SLIDER_FILM), 3)

        self.find((By.XPATH, self.X_IN_CINEMA_SECTION_BUTTON), 3).click()

        title = self.find((By.CLASS_NAME, self.PAGE_COLLECTION_TITLE_CLASS_NAME), 3).text

        if title != self.PAGE_IN_CINEMA_COLLECTION_TITLE:
            raise Exception("title does not equal", title, self.PAGE_IN_CINEMA_COLLECTION_TITLE)

    def test_genres_section(self):
        self.render(URL)

        assert self.find((By.XPATH, self.X_GENRES_SECTION_SLIDER_GENRE), 3)

        self.find((By.XPATH, self.X_GENRES_SECTION_BUTTON), 3).click()

        title = self.find((By.CLASS_NAME, self.PAGE_COLLECTION_TITLE_CLASS_NAME), 3).text

        if title != self.PAGE_GENRES_COLLECTION_TITLE:
            raise Exception("title does not equal", title, self.PAGE_GENRES_COLLECTION_TITLE)

class TestMainPage(BasePage):
    PREVIEW_FILM_CLASS_NAME = 'js-main-page-preview-film'
    PREVIEW_FILM_TITLE_CLASS_NAME = 'preview-film__film-title'

    PAGE_COLLECTION_TITLE_CLASS_NAME = 'page__collection__title'

    X_POPULAR_SECTION_BUTTON = '/html/body/div/div/div[2]/div[1]/div/div[1]'
    X_POPULAR_SECTION_SLIDER_FILM = '/html/body/div/div/div[2]/div[1]/div/div[2]/div/div[2]'
    PAGE_POPULAR_COLLECTION_TITLE = 'Популярное'

    X_IN_CINEMA_SECTION_BUTTON = '/html/body/div/div/div[2]/div[2]/div/div[1]'
    X_IN_CINEMA_SECTION_SLIDER_FILM = '/html/body/div/div/div[2]/div[2]/div/div[2]/div/div[1]'
    PAGE_IN_CINEMA_COLLECTION_TITLE = 'Сейчас в кино'

    X_GENRES_SECTION_BUTTON = '/html/body/div/div/div[2]/div[3]/div/div[1]'
    X_GENRES_SECTION_SLIDER_GENRE = '/html/body/div/div/div[2]/div[3]/div/div[2]/div/div[1]'
    PAGE_GENRES_COLLECTION_TITLE = 'Жанры'

    def test_preview_film_existing(self):
        self.render(URL)

        assert self.find((By.CLASS_NAME, self.PREVIEW_FILM_CLASS_NAME), 3)

        assert self.find((By.CLASS_NAME, self.PREVIEW_FILM_TITLE_CLASS_NAME), 3)

    def test_popular_section(self):
        self.render(URL)

        assert self.find((By.XPATH, self.X_POPULAR_SECTION_SLIDER_FILM), 3)

        self.find((By.XPATH, self.X_POPULAR_SECTION_BUTTON), 3).click()

        title = self.find((By.CLASS_NAME, self.PAGE_COLLECTION_TITLE_CLASS_NAME), 3).text

        if title != self.PAGE_POPULAR_COLLECTION_TITLE:
            raise Exception("title does not equal", title, self.PAGE_POPULAR_COLLECTION_TITLE)

    def test_in_cinema_section(self):
        self.render(URL)

        assert self.find((By.XPATH, self.X_IN_CINEMA_SECTION_SLIDER_FILM), 3)

        self.find((By.XPATH, self.X_IN_CINEMA_SECTION_BUTTON), 3).click()

        title = self.find((By.CLASS_NAME, self.PAGE_COLLECTION_TITLE_CLASS_NAME), 3).text

        if title != self.PAGE_IN_CINEMA_COLLECTION_TITLE:
            raise Exception("title does not equal", title, self.PAGE_IN_CINEMA_COLLECTION_TITLE)

    def test_genres_section(self):
        self.render(URL)

        assert self.find((By.XPATH, self.X_GENRES_SECTION_SLIDER_GENRE), 3)

        self.find((By.XPATH, self.X_GENRES_SECTION_BUTTON), 3).click()

        title = self.find((By.CLASS_NAME, self.PAGE_COLLECTION_TITLE_CLASS_NAME), 3).text

        if title != self.PAGE_GENRES_COLLECTION_TITLE:
            raise Exception("title does not equal", title, self.PAGE_GENRES_COLLECTION_TITLE)

class TestCollectionPage(BasePage):
    CLASS_WILL_WATCH_ICON = "about-film__button_bookmark"
    CLASS_TITLE_FILM_IN_WILL_WATCH = 'about-film__title'
    CLASS_LIST_WILL_WATCH_ICON = 'about-film__button_plus'
    CLASS_DELETE_BUTTON = 'film__delete-svg'
    CLASS_AUTHOR_NAME = 'header__userbar-name'
    CLASS_AVATAR_AUTHOR = 'header__avatar'
    CLASS_SHARE_ICON = 'page__collection__share-icon'
    X_TOSTER = '/html/body/div/div[2]'
    REDIRECTED_PAGE_URL = 'https://movie-gate.online/film/'
    url = URL

    def test_coll_has_film(self):
        helper.logout()
        helper.login()
        self.render(f'{URL}/film/39/')
        time.sleep(2)
        film_title = self.find((By.CLASS_NAME, self.CLASS_TITLE_FILM_IN_WILL_WATCH)).text
        self.find((By.CLASS_NAME, self.CLASS_WILL_WATCH_ICON)).click()

        self.render(f'{URL}/user/collections/')
        self.find((By.XPATH, "//div[contains(text(), 'Буду смотреть')]//preceding-sibling::div")).click()
        xpath = f"//div[contains(text(), '{film_title}')]//preceding-sibling::div"
        self.find((By.XPATH, xpath)).click()
        pattern = self.REDIRECTED_PAGE_URL
        current__url = dvr.get_instance().current_url
        if (re.search(current__url, pattern)):
            raise Exception("wrong redirect", pattern, current__url)

        self.find((By.CLASS_NAME, self.CLASS_WILL_WATCH_ICON)).click()
        helper.logout()

    def test_adding_film_in_col(self):
        helper.logout()
        helper.login()
        self.render(f'{URL}/film/39/')
        time.sleep(2)
        film_title = self.find((By.CLASS_NAME, self.CLASS_TITLE_FILM_IN_WILL_WATCH)).text
        self.find((By.CLASS_NAME, self.CLASS_LIST_WILL_WATCH_ICON)).click()
        time.sleep(2)
        self.find((By.XPATH, "//div[contains(text(), 'Избранное')]")).click()

        self.render(f'{URL}/user/collections/')
        self.find((By.XPATH, "//div[contains(text(), 'Избранное')]//preceding-sibling::div")).click()
        xpath = f"//div[contains(text(), '{film_title}')]//preceding-sibling::div"
        self.find((By.XPATH, xpath)).click()
        pattern = self.REDIRECTED_PAGE_URL
        current__url = dvr.get_instance().current_url
        if (re.search(current__url, pattern)):
            raise Exception("wrong redirect", pattern, current__url)

        self.find((By.CLASS_NAME, self.CLASS_LIST_WILL_WATCH_ICON)).click()
        self.find((By.XPATH, "//div[contains(text(), 'Избранное')]")).click()
        helper.logout()

    def test_delete_film_from_col(self):
        helper.logout()
        helper.login()
        self.render(f'{URL}/film/39/')
        time.sleep(2)
        film_title = self.find((By.CLASS_NAME, self.CLASS_TITLE_FILM_IN_WILL_WATCH)).text
        self.find((By.CLASS_NAME, self.CLASS_WILL_WATCH_ICON)).click()

        self.render(f'{URL}/user/collections/')
        self.find((By.XPATH, "//div[contains(text(), 'Буду смотреть')]//preceding-sibling::div")).click()
        xpath = f"//div[contains(text(), '{film_title}')]"
        self.find((By.XPATH, xpath)).click()
        self.find((By.CLASS_NAME, self.CLASS_DELETE_BUTTON)).click()

        helper.logout()

    def test_public_coll_has_film(self):
        helper.logout()
        helper.login()
        self.render(f'{URL}/film/39/')
        time.sleep(2)
        author_name = self.find((By.CLASS_NAME, self.CLASS_AUTHOR_NAME)).text
        self.find((By.CLASS_NAME, self.CLASS_LIST_WILL_WATCH_ICON)).click()
        time.sleep(2)
        self.find((By.XPATH, "//div[contains(text(), 'Мои рекомендации')]")).click()
        self.render(f'{URL}/user/collections/')
        self.find((By.XPATH, "//div[contains(text(), 'Мои рекомендации')]//preceding-sibling::div")).click()
        helper.logout()

        self.find((By.CLASS_NAME, self.CLASS_AVATAR_AUTHOR)).click()
        xpath = f"//div[contains(text(), '{author_name}')]"
        public_author_name = self.find((By.XPATH, xpath)).text
        if (public_author_name != author_name):
            raise Exception("wrong redirect", public_author_name, author_name)

    def test_public_coll_copy_url(self):
        helper.logout()
        helper.login()
        self.render(f'{URL}/film/39/')
        time.sleep(2)
        self.find((By.CLASS_NAME, self.CLASS_LIST_WILL_WATCH_ICON)).click()
        time.sleep(2)
        self.find((By.XPATH, "//div[contains(text(), 'Мои рекомендации')]")).click()
        self.render(f'{URL}/user/collections/')
        self.find((By.XPATH, "//div[contains(text(), 'Мои рекомендации')]//preceding-sibling::div")).click()
        helper.logout()

        self.find((By.CLASS_NAME, self.CLASS_SHARE_ICON)).click()
        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

class TestPremieresPage(BasePage):
    X_PREMIERES_TITLE_CLASS_NAME = 'premiere-page__title'
    PREMIERES_TITLE = 'Премьеры'
    PREMIERES_DAY_CLASS_NAME = 'premiere-day'

    def test_premieres_exist(self):
        self.render(f'{URL}/premieres/')

        title = self.find((By.CLASS_NAME, self.X_PREMIERES_TITLE_CLASS_NAME), 3).text

        if title != self.PREMIERES_TITLE:
            raise Exception("title does not equal", title, self.PREMIERES_TITLE)

        assert self.find((By.CLASS_NAME, self.PREMIERES_DAY_CLASS_NAME), 3)

class TestPremieresPage(BasePage):
    X_PREMIERES_TITLE_CLASS_NAME = 'premiere-page__title'
    PREMIERES_TITLE = 'Премьеры'
    PREMIERES_DAY_CLASS_NAME = 'premiere-day'

    def test_premieres_exist(self):
        self.render(f'{URL}/premieres/')

        title = self.find((By.CLASS_NAME, self.X_PREMIERES_TITLE_CLASS_NAME), 3).text

        if title != self.PREMIERES_TITLE:
            raise Exception("title does not equal", title, self.PREMIERES_TITLE)

        assert self.find((By.CLASS_NAME, self.PREMIERES_DAY_CLASS_NAME), 3)
