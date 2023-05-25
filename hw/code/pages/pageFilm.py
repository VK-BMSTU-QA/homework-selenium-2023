from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from locators.pageFilmLocators import SelectorsFilm

class FilmPage(BasePage):
    def render_film(self, film_id=1):
        self.render(f'/film/{film_id}')

    def set_rate(self, value):
        rates = [10,9,8,7,6,5,4,3,2,1,0]
        self.find_group((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_STAR))[rates[value]].click()

    def del_rate(self):
        self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_BUTTON_RATE_DELETE)).click()

    def is_del_block_absent(self):
        try:
            self.wait_hide((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_BUTTON_RATE_DELETE))
            return True
        except:
            return False

    def is_review_open(self):
        try:
            self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_BUTTON_REVIEW_CONTAINER))
            return True
        except:
            return False

    def write_review(self, type=SelectorsFilm.POSITIVE_TYPE, title='title', message='abc'):
        if type != None:
            self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_BUTTON_CHOOSE_TYPE)).click()
            self.find_group((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_CHOOSE_TYPE_REVIEW))[type].click()

        self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_INPUT_TITLE)).send_keys(title)
        self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_INPUT_TEXT)).send_keys(message)


        self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_BUTTON_SEND_REVIEW)).click()

    def get_err_msg_review(self):
        return self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_REVIEW_ERR_MSG)).text

    def get_upper_title_review(self):
        return self.find_group((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_REVIEW_TITLE))[0].text

    def get_upper_message_review(self):
        return self.find_group((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_REVIEW_TEXT))[0].text

    def add_or_remove_in_collection(self, collection):
        film_title = self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_TITLE_FILM)).text

        self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_LIST_WILL_WATCH_ICON)).click()

        try:
            self.find((By.XPATH, f'//div[contains(text(), \'{collection}\')]'), 2).click()
        except:
            self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_LIST_WILL_WATCH_ICON)).click()
            self.find((By.XPATH, f'//div[contains(text(), \'{collection}\')]'), 1).click()
            None

        return film_title

    def get_title_film(self):
        return self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_TITLE_FILM)).text

    def save_to_bookmark(self):
        # нестабильное поведение в браузере
        try:
            self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_BUTTON_BOOKMARK)).click()
        except:
            self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_BUTTON_BOOKMARK)).click()

    def open_trailer(self):
        self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_BUTTON_TRAILER)).click()

    def is_open_trailer(self):
        try:
            self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_TRAILER_CONTAINER))
            return True
        except:
            return False

    def open_review(self):
        self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_BUTTON_REVIEW)).click()

    def get_prod(self):
        return self.find((By.CLASS_NAME, SelectorsFilm.CLASS_NAME_PRODUCER), 3).text.strip()
