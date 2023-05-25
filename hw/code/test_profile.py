import time
import unittest
import random
import string

from utils.helper_auth import needed_auth, helper
from pages.pageProfile import ProfilePage


class TestProfile(unittest.TestCase, ProfilePage):
    @staticmethod
    def generate_alphanum_random_string(length):
        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters_and_digits, length))
        return rand_string

    def test_open_change_input(self):
        helper.login()

        self.render_page()

        self.start_change_image_flow()

        actual_open, form_change = self.get_opportunity_change_image()
        self.assertTrue(actual_open, "change image not available")

        actual_close = self.get_close_opportunity_change_image(form_change)
        self.assertTrue(actual_close, "can't close image change opportunity")


    def test_change_name(self):
        helper.login()

        self.render_page()

        cur_name = self.get_name()

        new_name = self.generate_alphanum_random_string(15)
        self.update_name(new_name)

        self.render_page()
        actual_new_name = self.get_name()
        self.assertEqual(actual_new_name, new_name, "can't change name")

        self.render_page()
        self.update_name(cur_name)

        self.render_page()
        actual_new_name_rollback = self.get_name()
        self.assertEqual(actual_new_name_rollback, cur_name, "can't return name")

        self.render_page()
        self.update_name("Admin")

    def test_check_main_fields(self):
        helper.login()

        self.render_page()

        date_of_reg = self.get_profile_date_registration()
        self.assertTrue(date_of_reg, "date_of_reg not available")

        num_of_rates = self.get_profile_count_rates()
        self.assertTrue(num_of_rates, "num_of_rates not available")

        num_of_coll = self.get_profile_count_coll()
        self.assertTrue(num_of_coll, "num_of_coll not available")

        num_of_reviews = self.get_profile_count_reviews()
        self.assertTrue(num_of_reviews, "num_of_reviews not available")
