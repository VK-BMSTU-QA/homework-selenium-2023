from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from locators.pageMainPageLocators import MainPageLocators
from utils.driver import dvr


class PageMainPAge(BasePage):
    def render_page(self):
        self.render(MainPageLocators.URL_PAGE_MAIN)
