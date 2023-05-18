from selenium.webdriver.common.by import By

from utils.base_page import BasePage


class TestPremieresPage(BasePage):
    # check premiere page's content
    CLASS_NAME_PREMIERES_TITLE = 'premiere-page__title'
    PREMIERES_TITLE = 'Премьеры'
    CLASS_NAME_PREMIERES_DAY = 'premiere-day'

    # check film poster redirect
    CLASS_NAME_PREMIERES_FILM_POSTER = 'premiere-film__poster-container'
    CLASS_NAME_FILM_PAGE_ABOUT = 'js-film-page__about'

    def test_premieres_exist(self):
        self.render(f'{self.DOMAIN}/premieres/')

        title = self.find((By.CLASS_NAME, self.CLASS_NAME_PREMIERES_TITLE)).text

        if title != self.PREMIERES_TITLE:
            raise Exception("title does not equal", title, self.PREMIERES_TITLE)

        assert self.find((By.CLASS_NAME, self.CLASS_NAME_PREMIERES_DAY))

    def test_premiers_film_poster_redirect(self):
        self.render(f'{self.DOMAIN}/premieres/')

        self.find((By.CLASS_NAME, self.CLASS_NAME_PREMIERES_FILM_POSTER)).click()

        assert self.find((By.CLASS_NAME, self.CLASS_NAME_FILM_PAGE_ABOUT))
