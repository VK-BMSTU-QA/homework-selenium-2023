import unittest

from pages.pageSignup import SignupPage
from locators.pageSignupLocators import SelectorsSignup


class TestSignup(unittest.TestCase, SignupPage):
    LOGIN = 'Qwe123@a.a'
    PASSWD = 'Qwe123@a.a'
    NICKNAME = 'Admin'

    EXPECTED_ERROR = "Пользователь с таким email уже зарегистрирован", "wrong register msg"
    EXPECTED_LOGIN = "login"

    def test_redirect_login(self):
        self.render_page()

        actual_position = self.move_to_login()

        self.assertIn(self.EXPECTED_LOGIN, actual_position, "wrong redirect")

    def test_short_nick(self):
        self.render_page()

        short_nick = '123'

        input_nickname, _, _, _ = self.action_registration(short_nick, self.LOGIN, self.PASSWD, self.PASSWD)

        is_wrong = SelectorsSignup.CLASS_WRONG_INPUT in input_nickname.get_attribute("class").split()
        self.assertTrue(is_wrong, "wrong check")

    def test_invalid_email(self):
        self.render_page()

        wrong_email = '123456'

        _, input_email, _, _ = self.action_registration(self.NICKNAME, wrong_email, self.PASSWD, self.PASSWD)

        is_wrong = SelectorsSignup.CLASS_WRONG_INPUT in input_email.get_attribute("class").split()
        self.assertTrue(is_wrong, "wrong check")

    def test_invalid_password(self):
        self.render_page()

        wrong_password = 'abcds'

        _, _, input_password, _ = self.action_registration(self.NICKNAME, self.LOGIN, wrong_password, wrong_password)

        is_wrong_input_password = SelectorsSignup.CLASS_WRONG_INPUT in input_password.get_attribute("class").split()
        is_wrong_input_repeat_password = SelectorsSignup.CLASS_WRONG_INPUT in input_password.get_attribute("class").split()

        self.assertTrue(is_wrong_input_password or is_wrong_input_repeat_password, "wrong check")

    def test_such_user_exist(self):
        self.render_page()

        self.action_registration(self.NICKNAME, self.LOGIN, self.PASSWD, self.PASSWD)

        msg_already_register = self.get_error_massage()

        self.assertIn(msg_already_register, self.EXPECTED_ERROR)
