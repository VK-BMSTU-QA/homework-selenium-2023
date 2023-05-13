from selenium.webdriver.common.by import By

from driver import dvr
from base_page import BasePage
from const import *
from helper_auth import needed_auth, helper


class CollectionHelper(BasePage):
    CLASS_NAME_TITLE_FILM_IN_WILL_WATCH = 'about-film__title'
    CLASS_NAME_LIST_WILL_WATCH_ICON = 'about-film__button_plus'

    # second call is remove
    def add_remove_film_in_collection(self, film_id, collection):
        self.render(f'{DOMAIN}/film/{film_id}/')
        film_title = self.find((By.CLASS_NAME, self.CLASS_NAME_TITLE_FILM_IN_WILL_WATCH)).text

        self.find((By.CLASS_NAME, self.CLASS_NAME_LIST_WILL_WATCH_ICON)).click()

        self.find((By.XPATH, f'//div[contains(text(), \'{collection}\')]')).click()

        return film_title


class TestPersonalCollectionAddFilm(CollectionHelper):
    EXPECTED_REDIRECTED_PAGE_URL_PART = 'https://movie-gate.online/film/'

    CLASS_NAME_FILM_TITLE = 'film__title'
    EXPECTED_FILM_TITLE = 'В эфире'
    X_TOSTER = '/html/body/div/div[2]'

    CLASS_NAME_AUTHOR_NAME = 'header__userbar-name'
    CLASS_NAME_AVATAR_AUTHOR = 'header__avatar'
    CLASS_NAME_SHARE_ICON = 'page__collection__share-icon'

    CLASS_NAME_PREVIEW_FILM = 'preview-film__container'

    @needed_auth
    def test_adding_film_in_collection(self):
        # prepare
        collection = "Избранное"
        film_id = 39
        film_title = self.add_remove_film_in_collection(film_id, collection)

        # action
        # to collections
        self.render(f'{DOMAIN}/user/collections/')
        self.find((By.XPATH, f'//div[contains(text(), \'{collection}\')]//preceding-sibling::div')).click()

        # in collection
        xpath = f'//div[contains(text(), \'{film_title}\')]//preceding-sibling::div'
        self.find((By.XPATH, xpath)).click()

        # check redirect film
        expected_full_url = self.EXPECTED_REDIRECTED_PAGE_URL_PART + f'{film_id}/'
        actual_url = dvr.get_instance().current_url
        if actual_url != expected_full_url:
            raise Exception("wrong redirect: film not expected", expected_full_url, actual_url)

        # rollback env
        self.add_remove_film_in_collection(film_id, collection)


class TestPersonalCollectionDeleteFilm(CollectionHelper):
    CLASS_NAME_WILL_WATCH_ICON = "about-film__button_bookmark"
    CLASS_NAME_DELETE_BUTTON = 'film__delete-svg'

    EXPECTED_REDIRECTED_PAGE_URL_PART = 'https://movie-gate.online/film/'

    CLASS_NAME_FILM_TITLE = 'film__title'
    EXPECTED_FILM_TITLE = 'В эфире'
    X_TOSTER = '/html/body/div/div[2]'

    CLASS_NAME_AUTHOR_NAME = 'header__userbar-name'
    CLASS_NAME_AVATAR_AUTHOR = 'header__avatar'
    CLASS_NAME_SHARE_ICON = 'page__collection__share-icon'

    CLASS_NAME_PREVIEW_FILM = 'preview-film__container'

    @needed_auth
    def test_delete_film_from_collection(self):
        # prepare
        collection = "Избранное"
        film_id = 39
        film_title = self.add_remove_film_in_collection(film_id, collection)

        # action
        # to collections
        self.render(f'{DOMAIN}/user/collections/')
        self.find((By.XPATH, f'//div[contains(text(), \'{collection}\')]//preceding-sibling::div')).click()

        # to film
        xpath = f"//div[contains(text(), '{film_title}')]"
        self.find((By.XPATH, xpath)).click()

        # delete film
        self.find((By.CLASS_NAME, self.CLASS_NAME_DELETE_BUTTON)).click()

        # check result. Exception by timeout if wrong
        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))


class TestPersonalCollectionHasFilm(CollectionHelper):
    CLASS_NAME_WILL_WATCH_ICON = "about-film__button_bookmark"
    CLASS_NAME_DELETE_BUTTON = 'film__delete-svg'

    EXPECTED_REDIRECTED_PAGE_URL_PART = 'https://movie-gate.online/film/'

    CLASS_NAME_FILM_TITLE = 'film__title'
    EXPECTED_FILM_TITLE = 'В эфире'
    X_TOSTER = '/html/body/div/div[2]'

    CLASS_NAME_AUTHOR_NAME = 'header__userbar-name'
    CLASS_NAME_AVATAR_AUTHOR = 'header__avatar'
    CLASS_NAME_SHARE_ICON = 'page__collection__share-icon'

    CLASS_NAME_PREVIEW_FILM = 'preview-film__container'

    def test_public_collection_has_film(self):
        # prepare
        helper.login()
        collection = "Мои рекомендации"
        film_id = 39
        film_title = self.add_remove_film_in_collection(film_id, collection)

        # to collections
        self.render(f'{DOMAIN}/user/collections/')
        self.find((By.XPATH, f'//div[contains(text(), \'{collection}\')]//preceding-sibling::div')).click()

        # get collection_id
        actual_collection_id = dvr.get_instance().current_url
        f = filter(str.isdigit, actual_collection_id)
        collection_id = "".join(f)

        self.render(DOMAIN)

        # action
        # to collection
        self.render(f'{DOMAIN}/user/collection/{collection_id}')

        # in collection
        xpath = f'//div[contains(text(), \'{film_title}\')]//preceding-sibling::div'
        self.find((By.XPATH, xpath)).click()

        # check redirect film
        expected_full_url = self.EXPECTED_REDIRECTED_PAGE_URL_PART + f'{film_id}/'
        actual_url = dvr.get_instance().current_url
        if actual_url != expected_full_url:
            raise Exception("wrong redirect: film not expected", expected_full_url, actual_url)

        # rollback env
        self.add_remove_film_in_collection(film_id, collection)



class TestPersonalCollectionHasAuthor(CollectionHelper):
    CLASS_NAME_WILL_WATCH_ICON = "about-film__button_bookmark"
    CLASS_NAME_DELETE_BUTTON = 'film__delete-svg'

    EXPECTED_REDIRECTED_PAGE_URL_PART = 'https://movie-gate.online/film/'

    CLASS_NAME_FILM_TITLE = 'film__title'
    EXPECTED_FILM_TITLE = 'В эфире'
    X_TOSTER = '/html/body/div/div[2]'

    CLASS_NAME_AUTHOR_NAME = 'header__userbar-name'
    CLASS_NAME_AVATAR_AUTHOR = 'header__avatar'
    CLASS_NAME_SHARE_ICON = 'page__collection__share-icon'

    CLASS_NAME_PREVIEW_FILM = 'preview-film__container'

    def test_public_collection_has_author(self):
        # prepare
        helper.login()
        collection = "Мои рекомендации"
        film_id = 39
        self.add_remove_film_in_collection(film_id, collection)

        # to collections
        self.render(f'{DOMAIN}/user/collections/')
        self.find((By.XPATH, f'//div[contains(text(), \'{collection}\')]//preceding-sibling::div')).click()

        # get collection_id
        actual_collection_id = dvr.get_instance().current_url
        f = filter(str.isdigit, actual_collection_id)
        collection_id = "".join(f)

        self.render(DOMAIN)

        # action
        # to collection
        self.render(f'{DOMAIN}/user/collection/{collection_id}')

        author_name = self.find((By.CLASS_NAME, self.CLASS_NAME_AUTHOR_NAME)).text

        # to profile
        self.find((By.CLASS_NAME, self.CLASS_NAME_AVATAR_AUTHOR)).click()

        xpath = f"//div[contains(text(), '{author_name}')]"
        public_author_name = self.find((By.XPATH, xpath)).text
        if public_author_name != author_name:
            raise Exception("wrong redirect: user name not expected", public_author_name, author_name)

        self.add_remove_film_in_collection(film_id, collection)


class TestPersonalCollectionShare(CollectionHelper):
    CLASS_NAME_WILL_WATCH_ICON = "about-film__button_bookmark"
    CLASS_NAME_DELETE_BUTTON = 'film__delete-svg'

    EXPECTED_REDIRECTED_PAGE_URL_PART = 'https://movie-gate.online/film/'

    CLASS_NAME_FILM_TITLE = 'film__title'
    EXPECTED_FILM_TITLE = 'В эфире'
    X_TOSTER = '/html/body/div/div[2]'

    CLASS_NAME_AUTHOR_NAME = 'header__userbar-name'
    CLASS_NAME_AVATAR_AUTHOR = 'header__avatar'
    CLASS_NAME_SHARE_ICON = 'page__collection__share-icon'

    CLASS_NAME_PREVIEW_FILM = 'preview-film__container'

    def test_public_collection_copy_url(self):
        # prepare
        helper.login()
        collection = "Мои рекомендации"
        film_id = 39
        self.add_remove_film_in_collection(film_id, collection)

        # to collections
        self.render(f'{DOMAIN}/user/collections/')
        self.find((By.XPATH, f'//div[contains(text(), \'{collection}\')]//preceding-sibling::div')).click()

        # get collection_id
        actual_collection_id = dvr.get_instance().current_url
        f = filter(str.isdigit, actual_collection_id)
        collection_id = "".join(f)

        self.render(DOMAIN)

        # action
        # to collection
        self.render(f'{DOMAIN}/user/collection/{collection_id}')

        # in collection
        self.find((By.CLASS_NAME, self.CLASS_NAME_SHARE_ICON)).click()

        self.find((By.XPATH, self.X_TOSTER))
        self.wait_hide((By.XPATH, self.X_TOSTER))

        # rollback
        self.add_remove_film_in_collection(film_id, collection)
