import pytest
from ui.pages.profile_page import ProfilePage
from ui.base_case.base_case import BaseCase
from ui.pages.login_page import LoginPage
from ui.locators.base_locators import BaseLocators
from ui.tabTitles import TabTitles
import os

import time

class TestProfileWithoutAuth(BaseCase):
    PATH = 'user'
    loginMsg = 'Войдите'

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver):
        self.driver = driver
        self.page = ProfilePage(driver, self.path.domain + self.path.user)
        self.loginPage = LoginPage(driver)

    def test_no_auth_message(self):
        assert str(self.page.get_attribute(
            self.page.locators.MUST_AUTH_MESSAGE, 'innerText')) == self.loginMsg


class TestProfile(BaseCase):
    PATH = 'user'
    baseLocators = BaseLocators()
    tabTitles = TabTitles()
    defaultAvatarPath = baseLocators.hrefs.domain + '/img/UserPhoto.webp'
    testAvatar = '/hw/code/ui/prikol.jpg'
    fieldCantBeEmptyMessage = 'Поле обязательно должно быть заполнено'
    wrongEmail = 'Неверный формат почты'
    phoneMustContain11DigitsMessage = 'Телефон должен содержать 11 цифр. Введено 4/11'
    oldPasswordIncorrectMessage = 'Старый пароль не верный'
    threeDigitsNum = '123'
    password = '123456'
    passwordMustContain6SymbolsMessage = 'Пароль должен содержать минимум 6 символов'
    passwordsUnmatch = 'Введенные пароли не совпадают'

    streetArbat = 'Arbat street'
    streetRedSquare = 'Red Square'
    houseNumber = '1'
    newName = 'new_name'
    defaultName = 'default name'
    new_email = 'new@new'
    defaultPhone = '1122334455'
    newPhone = '+75544332211'
    city = 'Moscow'
    enterCity = 'Введите ваш город'
    enterStreet = 'Введите вашу улицу'
    enterHouse = 'Введите ваш дом'
    cardNumber = '1111222233334444'
    authError = 'Неверная почта или пароль'
    cvcMsg = 'CVC код содержит 3 цифры'
    dateMsg = 'Срок действия карты формата 09/25'
    expireMsg = 'Срок действия карты истек'
    monthMsg = 'Месяц не может быть больше 12'



    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver):
        self.driver = driver
        self.page = ProfilePage(driver, self.path.domain + self.path.user)
        self.loginPage = LoginPage(driver)

    def test_title(self):
        self.loginPage.loginProfile()
        assert self.driver.title == self.tabTitles.profile

    def test_render_with_auth(self):
        self.loginPage.loginProfile()
        assert self.page.get_attribute(
            self.page.locators.CHANGE_PASSWORD_BUTTON, 'innerText') is not None

    def test_default_avatar(self):
        self.loginPage.loginProfile()

        assert self.page.get_attribute(
            self.page.locators.USER_AVATAR, 'src').strip() == (
            self.defaultAvatarPath)

    def test_change_avatar(self):
        self.loginPage.loginProfile()
        img_input = self.page.find(self.page.locators.CHANGE_AVATAR_INPUT)
        img_input.send_keys(os.getcwd() + self.testAvatar)

        assert self.page.get_attribute(
            self.page.locators.USER_AVATAR, 'src') != (
            self.defaultAvatarPath + '/')

        self.page.click(self.page.locators.USER_AVATAR)
        self.page.click(self.page.locators.DELETE_AVATAR_BUTTON)

    def test_change_avatar_with_refresh(self):
        self.loginPage.loginProfile()
        img_input = self.page.find(self.page.locators.CHANGE_AVATAR_INPUT)
        img_input.send_keys(os.getcwd() + self.testAvatar)

        self.page.refresh()

        assert self.page.get_attribute(
            self.page.locators.USER_AVATAR, 'src') != self.defaultAvatarPath + '/'

        self.page.click(self.page.locators.USER_AVATAR)
        self.page.click(self.page.locators.DELETE_AVATAR_BUTTON)

    def test_change_name_not_empty_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_NAME_BUTTON)

        input = self.page.find(self.page.locators.CHANGE_NAME_INPUT)
        input.send_keys(self.newName)
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()
        self.page.open()

        current_name = self.page.get_attribute(
            self.page.locators.NAME_STRING, 'innerText').strip()
        assert current_name == self.newName

        self.page.click(self.page.locators.CHANGE_NAME_BUTTON)
        input = self.page.find(self.page.locators.CHANGE_NAME_INPUT)
        input.send_keys(self.defaultName)
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

    def test_change_name_empty_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_NAME_BUTTON)
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.fieldCantBeEmptyMessage
        )

    def test_change_email_empty_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_EMAIL_BUTTON)
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.fieldCantBeEmptyMessage
        )

    def test_change_email_incorrect_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_EMAIL_BUTTON)
        input = self.page.find(self.page.locators.CHANGE_EMAIL_INPUT)

        input.send_keys('test')
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.wrongEmail)

    def test_change_email_correct_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_EMAIL_BUTTON)

        input = self.page.find(self.page.locators.CHANGE_EMAIL_INPUT)
        input.send_keys(self.new_email)
        self.page.click(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON)

        self.page.refresh()
        current_email = self.page.get_attribute(
            self.page.locators.EMAIL_STRING, 'innerText').strip()
        self.page.refresh()

        self.page.click(self.page.locators.CHANGE_EMAIL_BUTTON)
        input = self.page.find(self.page.locators.CHANGE_EMAIL_INPUT)
        input.send_keys(BaseCase.EMAIL_PROFILE)
        self.page.click(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON)

        assert current_email == self.new_email

    def test_change_phone_empty_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PHONE_BUTTON)
        self.page.find(self.page.locators.CHANGE_PHONE_INPUT).clear()

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.fieldCantBeEmptyMessage
        )

    def test_change_phone_incorrect_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PHONE_BUTTON)
        input = self.page.find(self.page.locators.CHANGE_PHONE_INPUT)

        input.send_keys(self.threeDigitsNum)

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.phoneMustContain11DigitsMessage)

    def test_change_phone_correct_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PHONE_BUTTON)
        self.page.find(self.page.locators.CHANGE_PHONE_INPUT).clear()

        input = self.page.find(self.page.locators.CHANGE_PHONE_INPUT)
        input.send_keys(self.newPhone)
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()
        self.page.refresh()

        current_phone = self.page.get_attribute(
            self.page.locators.PHONE_STRING, 'innerText').strip()

        self.page.click(self.page.locators.CHANGE_PHONE_BUTTON)
        input = self.page.find(self.page.locators.CHANGE_PHONE_INPUT)
        input.send_keys(self.defaultPhone)
        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert current_phone == self.newPhone

    def test_change_password_incorrect_empty_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (self.fieldCantBeEmptyMessage)

    def test_change_password_incorrect_small_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)
        input = self.page.find(self.page.locators.CURRENT_PASSWORD_INPUT)
        input.send_keys(BaseCase.PASSWORD)

        input = self.page.find(self.page.locators.NEW_PASSWORD_INPUT)
        input.send_keys(self.threeDigitsNum)

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (self.passwordMustContain6SymbolsMessage)

    def test_change_password_incorrect_small_str_2(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)
        input = self.page.find(self.page.locators.CURRENT_PASSWORD_INPUT)
        input.send_keys(self.password[:3])

        input = self.page.find(self.page.locators.NEW_PASSWORD_INPUT)
        input.send_keys(self.password)

        input = self.page.find(self.page.locators.REPEAT_PASSWORD_INPUT)
        input.send_keys(self.password)

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.passwordMustContain6SymbolsMessage
        )

    def test_change_password_incorrect_different_str(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)
        input = self.page.find(self.page.locators.CURRENT_PASSWORD_INPUT)
        input.send_keys(BaseCase.PASSWORD)

        input = self.page.find(self.page.locators.NEW_PASSWORD_INPUT)
        input.send_keys(self.password)

        input = self.page.find(self.page.locators.REPEAT_PASSWORD_INPUT)
        input.send_keys(self.password[::-1])

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText') == (
            self.passwordsUnmatch
        )

    def test_change_password_incorrect_wrong_password(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.CHANGE_PASSWORD_BUTTON)
        input = self.page.find(self.page.locators.CURRENT_PASSWORD_INPUT)
        input.send_keys(self.password)

        input = self.page.find(self.page.locators.NEW_PASSWORD_INPUT)
        input.send_keys(self.password)

        input = self.page.find(self.page.locators.REPEAT_PASSWORD_INPUT)
        input.send_keys(self.password)

        self.page.find(self.page.locators.USER_INFO_POPUP_APPLY_BUTTON).click()

        assert self.page.get_attribute(self.page.locators.SERVER_ERROR_MSG, 'innerText') == (
            self.oldPasswordIncorrectMessage
        )

    def test_change_password_correct_str(self):
        self.loginPage.loginProfile()
        self.page.change_password(BaseCase.PASSWORD_PROFILE, self.password)

        self.page.logout()
        self.loginPage.header.findLoginPageButton().click()
        self.loginPage.loginData(BaseCase.EMAIL_PROFILE, BaseCase.PASSWORD_PROFILE)

        errorMsg = self.page.get_attribute(
            self.page.locators.VALIDATION_RESULT_MSG, 'innerText')

        default_password = BaseCase.PASSWORD_PROFILE
        BaseCase.PASSWORD_PROFILE = self.password

        self.loginPage.loginProfile()
        BaseCase.PASSWORD_PROFILE = default_password
        self.page.change_password(self.password, BaseCase.PASSWORD_PROFILE)

        assert errorMsg == self.authError

    def test_payment_card_correct_params(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(
            self.page.locators.PAYMENT_CARD_NUMBER_INPUT, self.cardNumber)
        self.page.send_keys(self.page.locators.PAYMENT_CARD_MONTH_INPUT, '02')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_YEAR_INPUT, '30')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_CVC_INPUT, self.threeDigitsNum)

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.PAYMENT_CARD_NUMBER, 'innerText') == self.cardNumber

        self.page.click(self.page.locators.PAYMENT_CARD_NUMBER)
        self.page.click(self.page.locators.DELETE_PAYMENT_CARD)

    def test_payment_card_incorrect_params_number(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(
            self.page.locators.PAYMENT_CARD_NUMBER_INPUT, self.houseNumber)

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText') == 'Номер карты состоит из 16 цифр. 1/16'

    def test_payment_card_incorrect_params_date(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(
            self.page.locators.PAYMENT_CARD_NUMBER_INPUT, self.cardNumber)
        self.page.send_keys(self.page.locators.PAYMENT_CARD_MONTH_INPUT, '02')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_YEAR_INPUT, '2020')
        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == self.expireMsg

    def test_payment_card_incorrect_params_date_expiration(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(
            self.page.locators.PAYMENT_CARD_NUMBER_INPUT, self.cardNumber)

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == self.dateMsg

    def test_payment_card_incorrect_params_date_wrong_month(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(
            self.page.locators.PAYMENT_CARD_NUMBER_INPUT, self.cardNumber)
        self.page.send_keys(self.page.locators.PAYMENT_CARD_MONTH_INPUT, '15')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_YEAR_INPUT, '30')

        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == self.monthMsg

    def test_payment_card_incorrect_params_cvc(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_PAYMENT_CARD)
        self.page.send_keys(
            self.page.locators.PAYMENT_CARD_NUMBER_INPUT, self.cardNumber)
        self.page.send_keys(self.page.locators.PAYMENT_CARD_MONTH_INPUT, '10')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_YEAR_INPUT, '30')
        self.page.send_keys(self.page.locators.PAYMENT_CARD_CVC_INPUT, '0')
        self.page.find(self.page.locators.PAYMENT_CARD_APPLY_BUTTON).click()

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == self.cvcMsg

    def test_address_card_correct_params_with_flat(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_ADDRESS_CARD)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_CITY_INPUT, self.city)
        self.page.send_keys(
            self.page.locators.ADDRESS_CARD_STREET_INPUT, self.streetRedSquare)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_HOUSE_INPUT, self.houseNumber)
        self.page.click(self.page.locators.ADDRESS_CARD_APPLY_BUTTON)

        assert self.page.get_attribute(
            self.page.locators.ADDRESS_CARD_STREET_TEXT, 'innerText') == (
            self.streetRedSquare)

        self.page.click(self.page.locators.ADDRESS_CARD)
        self.page.click(self.page.locators.DELETE_ADDRESS_CARD)

    def test_address_card_correct_params_without_flat(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_ADDRESS_CARD)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_CITY_INPUT, self.city)
        self.page.send_keys(
            self.page.locators.ADDRESS_CARD_STREET_INPUT, self.streetRedSquare)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_HOUSE_INPUT, self.houseNumber)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_FLAT_INPUT, '15')
        self.page.click(self.page.locators.ADDRESS_CARD_APPLY_BUTTON)

        assert self.page.get_attribute(
            self.page.locators.ADDRESS_CARD_STREET_TEXT, 'innerText') == self.streetRedSquare

        self.page.click(self.page.locators.ADDRESS_CARD)
        self.page.click(self.page.locators.DELETE_ADDRESS_CARD)

    def test_address_card_incorrect_params_city(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_ADDRESS_CARD)
        self.page.click(self.page.locators.ADDRESS_CARD_APPLY_BUTTON)

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == self.enterCity

    def test_address_card_incorrect_params_street(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_ADDRESS_CARD)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_CITY_INPUT, self.city)
        self.page.click(self.page.locators.ADDRESS_CARD_APPLY_BUTTON)

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == self.enterStreet

    def test_address_card_incorrect_params_house(self):
        self.loginPage.loginProfile()

        self.page.click(self.page.locators.ADD_ADDRESS_CARD)
        self.page.send_keys(self.page.locators.ADDRESS_CARD_CITY_INPUT, self.city)
        self.page.send_keys(
            self.page.locators.ADDRESS_CARD_STREET_INPUT, self.streetRedSquare)
        self.page.click(self.page.locators.ADDRESS_CARD_APPLY_BUTTON)

        assert self.page.get_attribute(
            self.page.locators.SERVER_ERROR_MSG, 'innerText').strip() == self.enterHouse
