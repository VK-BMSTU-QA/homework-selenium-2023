from selenium.webdriver.common.by import By
from utils.driver import dvr

from utils.base_page import BasePage
from locators.pageCollectionsLocators import SelectorsCollections


class PageCollection(BasePage):
    def open_collection(self, collection):
        self.render('/user/collections/')
        self.find((By.XPATH, f'//div[contains(text(), \'{collection}\')]//preceding-sibling::div')).click()

    def open_film_in_collection(self, film_title):
        xpath = f'//div[contains(text(), \'{film_title}\')]//preceding-sibling::div'
        self.find((By.XPATH, xpath)).click()

    def delete_film(self):
        self.find((By.CLASS_NAME, SelectorsCollections.CLASS_NAME_DELETE_BUTTON)).click()

    def get_id_collection(self):
        url = dvr.get_instance().current_url
        f = filter(str.isdigit, url)
        return "".join(f)

    def open_public_collection_by_id(self, id):
        self.render(f'/user/public/collection/{id}/')

    def click_share(self):
        self.find((By.CLASS_NAME, SelectorsCollections.CLASS_NAME_SHARE_ICON)).click()

