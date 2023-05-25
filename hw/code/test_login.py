import unittest

from pages.pageLogin import PageLogin
from locators.pageLoginLocators import SelectorsLogin

from utils.helper_auth import helper

class TestLogin(unittest.TestCase, PageLogin):
    LOGIN = helper.LOGIN
    PASSWD = helper.PASSWD

    EXPECTED_LOGIN = "signup"
    EXPECTED_MODAL_STATUS = 'modal_does_not_exist'

    def test_redirect_signup(self):
        self.render_page()

        actual_position = self.move_to_signup()

        self.assertIn(self.EXPECTED_LOGIN, actual_position, "wrong redirect")

    def test_invalid_email(self):
        self.render_page()

        wrong_email = '123456'

        input_email, _ = self.action_login(wrong_email, self.PASSWD)

        is_wrong = SelectorsLogin.CLASS_WRONG_INPUT in input_email.get_attribute("class").split()
        self.assertTrue(is_wrong, "wrong check")

    def test_invalid_password(self):
        self.render_page()

        wrong_password = 'abcds'

        _, input_password = self.action_login(self.LOGIN, wrong_password)

        is_wrong_input_password = SelectorsLogin.CLASS_WRONG_INPUT in input_password.get_attribute("class").split()
        is_wrong_input_repeat_password = SelectorsLogin.CLASS_WRONG_INPUT in input_password.get_attribute("class").split()

        self.assertTrue(is_wrong_input_password or is_wrong_input_repeat_password, "wrong check")
