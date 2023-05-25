from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from locators.pagePremiereLocators import SelectorsPremiere


class PremieresPage(BasePage):
    def render_page(self):
        self.render(SelectorsPremiere.URL_PAGE)

    def get_premiere_title(self):
        return self.find((By.CLASS_NAME, SelectorsPremiere.CLASS_NAME_PREMIERES_TITLE)).text

    def get_premiere_date(self):
        return self.find((By.CLASS_NAME, SelectorsPremiere.CLASS_NAME_PREMIERES_DAY)).text

    def move_to_premiere_film(self):
        return self.find((By.CLASS_NAME, SelectorsPremiere.CLASS_NAME_PREMIERES_FILM_POSTER)).click()

    def get_premiere_film_about(self):
        return self.find((By.CLASS_NAME, SelectorsPremiere.CLASS_NAME_FILM_PAGE_ABOUT)).text
