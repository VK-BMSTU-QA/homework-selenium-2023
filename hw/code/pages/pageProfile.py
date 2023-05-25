from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from locators.pageProfileLocators import SelectorsProfile


class PageProfile(BasePage):
    def render_page(self):
        self.render(SelectorsProfile.URL_PAGE_PROFILE)

    def start_change_image_flow(self):
        self.find((By.CLASS_NAME, SelectorsProfile.CLASS_CHANGE_SVG)).click()

    def get_opportunity_change_image(self):
        form_change = self.find((By.CLASS_NAME, SelectorsProfile.CLASS_FORM_CHANGE))

        is_opened = SelectorsProfile.CLASS_FORM_DISPLAY_FLEX in form_change.get_attribute("class").split()

        return is_opened, form_change

    def get_close_opportunity_change_image(self, form_change):
        self.find((By.CLASS_NAME, SelectorsProfile.CLASS_CHANGE_SVG)).click()

        is_closed = SelectorsProfile.CLASS_FORM_DISPLAY_NONE in form_change.get_attribute("class").split()

        return is_closed

    def get_profile_date_registration(self):
        return self.find((By.XPATH, "//div[contains(text(), 'Дата регистрации:')]"))

    def get_profile_count_rates(self):
        return self.find((By.XPATH, "//div[contains(text(), 'Оценок:')]"))

    def get_profile_count_coll(self):
        return self.find((By.XPATH, "//div[contains(text(), 'Коллекций:')]"))

    def get_profile_count_reviews(self):
        return self.find((By.XPATH, "//div[contains(text(), 'Рецензий:')]"))

    def update_name(self, name):
        self.find((By.CLASS_NAME, SelectorsProfile.CLASS_CHANGE_SVG)).click()
        field_input_new_name = self.find((By.XPATH, "//input[@placeholder='Введите новое имя пользователя']"))
        field_input_new_name.send_keys(name)
        self.find((By.CLASS_NAME, SelectorsProfile.CLASS_NAME_SAVE_NEW_NAME)).click()

    def get_name(self):
        return self.find((By.CLASS_NAME, SelectorsProfile.CLASS_NAME_FIELD_NAME)).text
