from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from locators.pageSearchLocators import SelectorsSearch


class PageSearch(BasePage):
    def render_page(self):
        self.render(SelectorsSearch.URL_PAGE_SEARCH)

    def input_search(self, value):
        self.find((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_INPUT_SEARCH)).send_keys(value)

    def get_main_title(self):
        return self.find((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_TITLE_SEARCH)).text

    def get_search_res_type(self, target):
        return self.find_group((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_CATEGORY_TITLE))[target].text

    def get_first_found_film_title(self):
        return self.find((By.CLASS_NAME, SelectorsSearch.CLASS_NAME_FIRST_FOUNDED_TITLE)).text
