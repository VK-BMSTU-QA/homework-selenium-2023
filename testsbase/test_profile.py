from selenium.webdriver.common.by import By

from base_page import BasePage
from driver import dvr
from const import *
from helper_auth import needed_auth

class TestProfile(BasePage):
    CLASS_CHANGE_SVG = 'profile__change__svg'
    CLASS_FORM_CHANGE = 'profile__change'
    CLASS_FORM_DISPLAY_NONE = 'dysplay-none'
    CLASS_FORM_DISPLAY_FLEX = 'dysplay-flex'
    X_SAVE_NEW_NAME = '/html/body/div/div/div[2]/div[2]/div[2]/form[1]/button'
    URL_PAGE_PROFILE = f'{DOMAIN}/profile/'

    @needed_auth
    def test_open_change_input(self):

        self.render(self.URL_PAGE_PROFILE)
        self.find((By.CLASS_NAME, self.CLASS_CHANGE_SVG)).click()
        form_change = self.find((By.CLASS_NAME, self.CLASS_FORM_CHANGE))
        is_opened = self.CLASS_FORM_DISPLAY_FLEX in form_change.get_attribute("class").split()
        if (is_opened != True):
            raise Exception("can't open form change", form_change)
        self.find((By.CLASS_NAME, self.CLASS_CHANGE_SVG)).click()
        is_closed = self.CLASS_FORM_DISPLAY_NONE in form_change.get_attribute("class").split()
        if (is_closed != True):
            raise Exception("can't closen form change", form_change)

    @needed_auth
    def test_change_name(self):

        self.render(self.URL_PAGE_PROFILE)
        self.find((By.CLASS_NAME, self.CLASS_CHANGE_SVG), 3).click()
        field_Input_new_name = self.find((By.XPATH, "//input[@placeholder='Введите новое имя пользователя']"), 3)
        field_Input_new_name.send_keys('Zxc543')
        self.find((By.XPATH, self.X_SAVE_NEW_NAME), 4).click()

        new_name = self.find((By.XPATH, "//div[contains(text(), 'Zxc543')]"), 3)

        if (bool(new_name) != True):
            raise Exception("can't change name", new_name)

        self.render(self.URL_PAGE_PROFILE)
        self.find((By.CLASS_NAME, self.CLASS_CHANGE_SVG), 3).click()
        field_new_name = self.find((By.XPATH, "//input[@placeholder='Введите новое имя пользователя']"), 3)
        field_new_name.send_keys('Admin')
        self.find((By.XPATH, self.X_SAVE_NEW_NAME), 3).click()

        new_name = self.find((By.XPATH, "//div[contains(text(), 'Admin')]"), 3)
        if (bool(new_name) != True):
            raise Exception("can't return name", new_name)

    @needed_auth
    def test_check_value_num_of_rates(self):

        self.render(self.URL_PAGE_PROFILE)

        field_num_of_rates = self.find((By.XPATH, "//div[contains(text(), 'Оценок:')]//following-sibling::div"), 3).text
        if (not field_num_of_rates):
            raise Exception("empty field")
        if (not (field_num_of_rates == "нет оценок" or int(field_num_of_rates) > -1)):
            raise Exception("wrong format")

    @needed_auth
    def test_check_value_num_of_coll(self):

        self.render(self.URL_PAGE_PROFILE)

        field_num_of_coll = self.find((By.XPATH, "//div[contains(text(), 'Коллекций:')]//following-sibling::div"),
                                      3).text
        if (not field_num_of_coll):
            raise Exception("empty field")
        if (not (int(field_num_of_coll) > -1)):
            raise Exception("wrong format")

    @needed_auth
    def test_check_value_num_of_rewiews(self):

        self.render(self.URL_PAGE_PROFILE)

        field_num_of_rewiews = self.find((By.XPATH, "//div[contains(text(), 'Рецензий:')]//following-sibling::div"),
                                         3).text
        if (not field_num_of_rewiews):
            raise Exception("empty field")
        if (not (field_num_of_rewiews == "нет рецензий" or int(field_num_of_rewiews) > -1)):
            raise Exception("wrong format")

    @needed_auth
    def test_check_main_fields(self):

        self.render(self.URL_PAGE_PROFILE)
        date_of_reg = self.find((By.XPATH, "//div[contains(text(), 'Дата регистрации:')]"), 5)
        if not bool(date_of_reg):
            raise Exception("can't find 'Дата регистрации:' field")
        num_of_rates = self.find((By.XPATH, "//div[contains(text(), 'Оценок:')]"), 5)
        if not bool(num_of_rates):
            raise Exception("can't find 'Оценок:' field")
        num_of_coll = self.find((By.XPATH, "//div[contains(text(), 'Коллекций:')]"), 5)
        if not bool(num_of_coll):
            raise Exception("can't find 'Коллекций:' field")
        num_of_rewiews = self.find((By.XPATH, "//div[contains(text(), 'Рецензий:')]"), 5)
        if not bool(num_of_rewiews):
            raise Exception("can't find 'Рецензий:' field")
