from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from locators.pagePersonLocators import SelectorsPerson
from utils.driver import dvr


class PersonPage(BasePage):
    def render_page(self):
        self.render(SelectorsPerson.URL_PAGE)

    def get_film_id_person(self):
        self.find((By.CLASS_NAME, SelectorsPerson.CLASS_NAME_FILM)).click()

        url = dvr.get_instance().current_url

        f = filter(str.isdigit, url)

        film_id = "".join(f)

        return film_id

    def get_film_main_actor(self):
        return self.find((By.CLASS_NAME, SelectorsPerson.CLASS_NAME_ROLE)).text
