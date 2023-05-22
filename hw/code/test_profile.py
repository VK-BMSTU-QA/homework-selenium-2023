import time

from selenium.webdriver.common.by import By
import unittest

from utils.base_page import BasePage
from utils.helper_auth import needed_auth


class SelectorsProfile:
    CLASS_CHANGE_SVG = 'profile__change__svg'
    CLASS_FORM_CHANGE = 'profile__change'
    CLASS_FORM_DISPLAY_NONE = 'dysplay-none'
    CLASS_FORM_DISPLAY_FLEX = 'dysplay-flex'
    CLASS_NAME_SAVE_NEW_NAME = 'profile__input__button'
    CLASS_NAME_INFO_VALUE = 'profile__info__value'
    RATES = 1
    COLLS = 2


class TestProfile(unittest.TestCase, BasePage):
    URL_PAGE_PROFILE = '/profile/'

    @needed_auth
    def test_open_change_input(self):
        self.render(self.URL_PAGE_PROFILE)

        self.find((By.CLASS_NAME, SelectorsProfile.CLASS_CHANGE_SVG)).click()

        form_change = self.find((By.CLASS_NAME, SelectorsProfile.CLASS_FORM_CHANGE))
        is_opened = SelectorsProfile.CLASS_FORM_DISPLAY_FLEX in form_change.get_attribute("class").split()

        self.assertTrue(is_opened, "can't open form change")

        self.find((By.CLASS_NAME, SelectorsProfile.CLASS_CHANGE_SVG)).click()
        is_closed = SelectorsProfile.CLASS_FORM_DISPLAY_NONE in form_change.get_attribute("class").split()

        self.assertTrue(is_closed, "can't closen form change")

    @needed_auth
    def test_change_name(self):
        self.render(self.URL_PAGE_PROFILE)
        self.find((By.CLASS_NAME, SelectorsProfile.CLASS_CHANGE_SVG), 3).click()
        field_input_new_name = self.find((By.XPATH, "//input[@placeholder='Введите новое имя пользователя']"), 3)
        field_input_new_name.send_keys('Zxc543')
        self.find((By.CLASS_NAME, SelectorsProfile.CLASS_NAME_SAVE_NEW_NAME), 4).click()

        new_name = self.find((By.XPATH, "//div[contains(text(), 'Zxc543')]"), 3)

        self.assertTrue(bool(new_name), "can't change name")

        self.render(self.URL_PAGE_PROFILE)
        self.find((By.CLASS_NAME, SelectorsProfile.CLASS_CHANGE_SVG), 3).click()
        field_new_name = self.find((By.XPATH, "//input[@placeholder='Введите новое имя пользователя']"), 3)
        field_new_name.send_keys('Admin')
        self.find((By.CLASS_NAME, SelectorsProfile.CLASS_NAME_SAVE_NEW_NAME), 3).click()

        new_name = self.find((By.XPATH, "//div[contains(text(), 'Admin')]"), 3)

        self.assertTrue(bool(new_name), "can't return name")

    @needed_auth
    def test_check_value_num_of_rates(self):
        self.render(self.URL_PAGE_PROFILE)

        field_num_of_rates = self.find_group((By.CLASS_NAME, SelectorsProfile.CLASS_NAME_INFO_VALUE))[SelectorsProfile.RATES].text

        self.assertTrue(field_num_of_rates, "empty field")

        self.assertTrue((field_num_of_rates == "нет оценок" or int(field_num_of_rates) > -1), "wrong format")

    @needed_auth
    def test_check_main_fields(self):
        self.render(self.URL_PAGE_PROFILE)

        date_of_reg = self.find((By.XPATH, "//div[contains(text(), 'Дата регистрации:')]"), 5)
        self.assertTrue(bool(date_of_reg), "can't find 'Дата регистрации:' field")

        num_of_rates = self.find((By.XPATH, "//div[contains(text(), 'Оценок:')]"), 5)
        self.assertTrue(bool(num_of_rates), "can't find 'Оценок:' field")

        num_of_coll = self.find((By.XPATH, "//div[contains(text(), 'Коллекций:')]"), 5)
        self.assertTrue(bool(num_of_coll), "can't find 'Коллекций:' field")

        num_of_reviews = self.find((By.XPATH, "//div[contains(text(), 'Рецензий:')]"), 5)
        self.assertTrue(bool(num_of_reviews), "can't find 'Рецензий:' field")
