from selenium.webdriver.common.by import By

from utils.base_page import BasePage

class SelectorsPremierePage:
    # check premiere page's content
    CLASS_NAME_PREMIERES_TITLE = 'premiere-page__title'
    CLASS_NAME_PREMIERES_DAY = 'premiere-day'

    # check film poster redirect
    CLASS_NAME_PREMIERES_FILM_POSTER = 'premiere-film__poster-container'
    CLASS_NAME_FILM_PAGE_ABOUT = 'js-film-page__about'

class TestPremieresPage(BasePage):
    PREMIERES_TITLE = 'Премьеры'

    def test_premieres_exist(self):
        self.render(f'/premieres/')

        title = self.find((By.CLASS_NAME, SelectorsPremierePage.CLASS_NAME_PREMIERES_TITLE)).text

        if title != self.PREMIERES_TITLE:
            raise Exception("title does not equal", title, self.PREMIERES_TITLE)

        assert self.find((By.CLASS_NAME, SelectorsPremierePage.CLASS_NAME_PREMIERES_DAY))

    def test_premiers_film_poster_redirect(self):
        self.render(f'/premieres/')

        self.find((By.CLASS_NAME, SelectorsPremierePage.CLASS_NAME_PREMIERES_FILM_POSTER)).click()

        assert self.find((By.CLASS_NAME, SelectorsPremierePage.CLASS_NAME_FILM_PAGE_ABOUT))
