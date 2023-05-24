from selenium.webdriver.common.by import By
import unittest

from utils.base_page import BasePage
from utils.helper_auth import needed_auth


class ProfilePageParams:
    URL_PAGE = '/profile/'
    CLASS_CHANGE_SVG = 'profile__change__svg'
    CLASS_FORM_CHANGE = 'profile__change'
    CLASS_FORM_DISPLAY_NONE = 'dysplay-none'
    CLASS_FORM_DISPLAY_FLEX = 'dysplay-flex'
    CLASS_NAME_SAVE_NEW_NAME = 'profile__input__button'
    CLASS_NAME_INFO_VALUE = 'profile__info__value'
    RATES = 1
    COLLS = 2
    CLASS_NAME_FIELD_NAME = "profile__username"


class PagePerson(BasePage):
    def start(self):
        self.render(ProfilePageParams.URL_PAGE)

    def start_change_image_flow(self):
        self.find((By.CLASS_NAME, ProfilePageParams.CLASS_CHANGE_SVG)).click()

    def get_opportunity_change_image(self):
        form_change = self.find((By.CLASS_NAME, ProfilePageParams.CLASS_FORM_CHANGE))

        is_opened = ProfilePageParams.CLASS_FORM_DISPLAY_FLEX in form_change.get_attribute("class").split()

        return is_opened, form_change

    def get_close_opportunity_change_image(self, form_change):
        self.find((By.CLASS_NAME, ProfilePageParams.CLASS_CHANGE_SVG)).click()

        is_closed = ProfilePageParams.CLASS_FORM_DISPLAY_NONE in form_change.get_attribute("class").split()

        return is_closed

    def get_profile_date_registration(self):
        return self.find((By.XPATH, "//div[contains(text(), 'Дата регистрации:')]"))

    def get_profile_count_rates(self):
        return self.find((By.XPATH, "//div[contains(text(), 'Оценок:')]"))

    def get_profile_count_coll(self):
        return self.find((By.XPATH, "//div[contains(text(), 'Коллекций:')]"))

    def get_profile_count_reviews(self):
        return self.find((By.XPATH, "//div[contains(text(), 'Рецензий:')]"))

    def get_count_rates(self):
        return self.find_group((By.CLASS_NAME, ProfilePageParams.CLASS_NAME_INFO_VALUE))[ProfilePageParams.RATES].text

    def update_name(self, name):
        self.find((By.CLASS_NAME, ProfilePageParams.CLASS_CHANGE_SVG)).click()
        field_input_new_name = self.find((By.XPATH, "//input[@placeholder='Введите новое имя пользователя']"))
        field_input_new_name.send_keys(name)
        self.find((By.CLASS_NAME, ProfilePageParams.CLASS_NAME_SAVE_NEW_NAME)).click()

    def get_name(self):
        return self.find((By.CLASS_NAME, ProfilePageParams.CLASS_NAME_FIELD_NAME)).text


class TestProfile(unittest.TestCase, PagePerson):
    @needed_auth
    def test_open_change_input(self):
        self.start()

        self.start_change_image_flow()

        actual_open, form_change = self.get_opportunity_change_image()
        self.assertTrue(actual_open, "change image not available")

        actual_close = self.get_close_opportunity_change_image(form_change)
        self.assertTrue(actual_close, "can't close image change opportunity")

    @needed_auth
    def test_change_name(self):
        self.start()

        cur_name = self.get_name()

        new_name = "SomeSome123"
        self.update_name(new_name)

        actual_new_name = self.get_name()
        self.assertEqual(actual_new_name, new_name, "can't change name")

        self.start()

        self.update_name(cur_name)

        actual_new_name = self.get_name()
        self.assertEqual(actual_new_name, cur_name, "can't return name")

    @needed_auth
    def test_check_value_num_of_rates(self):
        self.start()

        num_of_rates = self.get_count_rates()

        self.assertTrue(num_of_rates, "empty field")

        self.assertTrue((num_of_rates == "нет оценок" or int(num_of_rates) > -1), "wrong format")

    @needed_auth
    def test_check_main_fields(self):
        self.start()

        date_of_reg = self.get_profile_date_registration()
        self.assertTrue(date_of_reg, "date_of_reg not available")

        num_of_rates = self.get_profile_count_rates()
        self.assertTrue(num_of_rates, "num_of_rates not available")

        num_of_coll = self.get_profile_count_coll()
        self.assertTrue(num_of_coll, "num_of_coll not available")

        num_of_reviews = self.get_profile_count_reviews()
        self.assertTrue(num_of_reviews, "num_of_reviews not available")
