import pytest
from ui.pages.cart_page import CartPage
from ui.base_case.base_case import BaseCase
from ui.locators.base_locators import BaseLocators
from ui.tabTitles import TabTitles
import datetime


class TestCart(BaseCase):
    paths = BaseLocators().hrefs
    tabTitles = TabTitles()
    emptyCartMessage = "Корзина пуста. Случайно не нужен \nтелефон\n?"
    loginToSeeFavouritesMessage = 'Войдите, чтобы добавить в избранное'
    authToSeeFavouritesMessage = 'Войти или зарегистрироваться, чтобы оформить заказ'
    emptyFavouritesMessage = 'Пока в избранном ничего нет. Может нужен \nкомпьютер\n?'
    loginToCompleteOrderMessage = 'Войти или зарегистрироваться, чтобы оформить заказ'
    loginToCompleteOrderPrompt = 'Чтобы оформить заказ авторизуйтесь'

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver):
        self.driver = driver
        self.page = CartPage(driver, self.path.domain + self.path.cart)

    def test_title(self):
        title = self.tabTitles.cart
        assert self.driver.title == title

    def test_empty_cart(self):
        empty_cart_message = self.emptyCartMessage
        assert self.page.find(
            self.page.locators.EMPTY_CART_MESSAGE).text == empty_cart_message

        self.page.click(self.page.locators.EMPTY_CART_MESSAGE_LINK)
        assert self.page.is_url(self.paths.category + self.path.phones)

    def test_button_clear_cart(self):
        empty_cart_message = self.emptyCartMessage
        self.page.add_product()
        self.page.click(self.page.locators.BUTTON_CLEAR_CART)
        assert self.page.find(
            self.page.locators.EMPTY_CART_MESSAGE).text == empty_cart_message

    def test_all_checkbox_active(self):
        self.page.add_product()
        item_price, item_count = self.page.get_item_count_price()
        total_price = self.page.get_total_price()

        assert self.page.find(self.page.locators.CHECKBOX_SELECT_ALL).is_selected()
        assert self.page.find(self.page.locators.CHECKBOX_ITEM).is_selected()
        assert item_price * item_count == total_price

    def test_checkbox_select_all_inactive(self):
        self.page.add_product()
        self.page.click(self.page.locators.CHECKBOX_SELECT_ALL)
        total_price = self.page.get_total_price()

        assert not self.page.find(self.page.locators.CHECKBOX_SELECT_ALL).is_selected()
        assert not self.page.find(self.page.locators.CHECKBOX_ITEM).is_selected()
        assert total_price == 0

    def test_checkbox_select_all_active(self):
        self.page.add_product()
        self.page.click(self.page.locators.CHECKBOX_SELECT_ALL)
        self.page.click(self.page.locators.CHECKBOX_SELECT_ALL)
        total_price = self.page.get_total_price()
        item_price, item_count = self.page.get_item_count_price()

        assert self.page.find(self.page.locators.CHECKBOX_SELECT_ALL).is_selected()
        assert self.page.find(self.page.locators.CHECKBOX_ITEM).is_selected()
        assert total_price == item_price * item_count

    def test_item_checkbox_inactive(self):
        self.page.add_product()
        total_price = self.page.get_total_price()
        self.page.click(self.page.locators.CHECKBOX_ITEM)
        new_total_price = self.page.get_total_price()
        item_price, item_count = self.page.get_item_count_price()

        assert new_total_price == total_price - item_count * item_price

    def test_item_checkbox_active(self):
        self.page.add_product()
        self.page.click(self.page.locators.CHECKBOX_ITEM)
        total_price = self.page.get_total_price()
        self.page.click(self.page.locators.CHECKBOX_ITEM)
        new_total_price = self.page.get_total_price()
        item_price, item_count = self.page.get_item_count_price()

        assert new_total_price == total_price + item_price * item_count

    def test_product_name_link(self):
        self.page.add_product()
        product_name_link_start = '/product/'
        product_name_link = self.page.find(
            self.page.locators.PRODUCT_NAME_LINK).get_attribute('href')

        assert product_name_link_start in product_name_link

    def test_product_photo(self):
        self.page.add_product()
        product_name_link = self.page.find(
            self.page.locators.PRODUCT_NAME_LINK).get_attribute('href')
        product_photo_link = self.page.find(
            self.page.locators.PRODUCT_PHOTO_LINK).get_attribute('href')

        assert product_name_link == product_photo_link

    def test_favorites_button(self):
        message_for_login = self.loginToSeeFavouritesMessage
        self.page.add_product()
        self.page.click(self.page.locators.BUTTON_FAVORITE)

        assert self.page.find(self.page.locators.POPUP_MESSAGE).is_displayed()
        assert self.page.find(
            self.page.locators.MESSAGE_FOR_LOGIN).text == message_for_login

    def test_delete_product_button(self):
        self.page.add_product()
        self.page.click(self.page.locators.BUTTON_DELETE_PRODUCT)
        total_price = self.page.get_total_price()

        assert total_price == 0

    def test_minus_button(self):
        self.page.add_product()
        self.page.click(self.page.locators.BUTTON_PLUS_PRODUCT)
        _, product_count = self.page.get_item_count_price()
        self.page.click(self.page.locators.BUTTON_MINUS_PRODUCT)
        _, new_product_count = self.page.get_item_count_price()

        assert new_product_count == product_count - 1

        self.page.click(self.page.locators.BUTTON_MINUS_PRODUCT)

        total_price = self.page.get_total_price()
        assert total_price == 0

    def test_plus_button(self):
        self.page.add_product()
        _, product_count = self.page.get_item_count_price()
        self.page.click(self.page.locators.BUTTON_PLUS_PRODUCT)
        _, new_product_count = self.page.get_item_count_price()

        assert new_product_count == product_count + 1

    def test_add_product_to_favorites(self):
        empty_page_message = self.emptyFavouritesMessage
        self.page.authorize()
        self.page.add_product_after_login()
        href_to_product = self.page.find(
            self.page.locators.PRODUCT_NAME_LINK).get_attribute('href')

        self.page.click(self.page.locators.BUTTON_FAVORITE)
        self.page.click(self.page.header_locators.BUTTON_FAVORITE)
        href_to_product_in_favourite = self.page.find(
            self.page.favourites_locators.PRODUCT_NAME_LINK).get_attribute('href')
        assert href_to_product == href_to_product_in_favourite

        self.page.click(self.page.header_locators.BUTTON_CART)
        self.page.click(self.page.locators.BUTTON_FAVORITE)
        self.page.click(self.page.header_locators.BUTTON_FAVORITE)
        assert self.page.find(
            self.page.favourites_locators.EMPTY_PAGE_MESSAGE).text == empty_page_message

    def test_delivery_date(self):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        self.page.add_product()
        assert self.page.find(
            self.page.locators.DELIVERY_DATE).text == tomorrow.strftime('%d / %m / %Y')

    def test_select_delivery_date(self):
        self.page.add_product()
        self.page.click(self.page.locators.DELIVERY_DATE_TABINDEX)
        self.page.click(self.page.locators.DELIVERY_DATE_1)
        assert self.page.find(self.page.locators.DELIVERY_DATE_1).is_displayed()

    def test_delivery_time(self):
        time = '8:00 - 12:00'
        self.page.add_product()
        assert self.page.find(self.page.locators.DELIVERY_TIME).text == time

    def test_select_delivery_time(self):
        self.page.add_product()
        self.page.click(self.page.locators.DELIVERY_TIME_TABINDEX)
        self.page.click(self.page.locators.DELIVERY_TIME_2)
        assert self.page.find(self.page.locators.DELIVERY_TIME_2).is_displayed()

    def test_block_payment_card_unauth(self):
        self.page.add_product()
        assert self.page.find(
            self.page.locators.UNAUTH_PAYMENT_CARD_MESSAGE).text == (
            self.authToSeeFavouritesMessage)

    def test_block_payment_card_unauth_login(self):
        self.page.add_product()
        self.page.click(self.page.locators.UNAUTH_PAYMENT_CARD_MESSAGE_LOGIN_BUTTON)
        assert self.page.is_url(self.paths.login)

    def test_block_payment_card_unauth_registration(self):
        self.page.add_product()
        self.page.click(
            self.page.locators.UNAUTH_PAYMENT_CARD_MESSAGE_REGISTRATION_BUTTON)
        assert self.page.is_url(self.paths.signup)

    def test_block_user_data_unauth(self):
        message = self.authToSeeFavouritesMessage
        self.page.add_product()
        assert self.page.find(self.page.locators.UNAUTH_USER_DATA_MESSAGE).text == message

    def test_block_user_data_unauth_login(self):
        self.page.add_product()
        self.page.click(self.page.locators.UNAUTH_USER_DATA_MESSAGE_LOGIN_BUTTON)
        assert self.page.is_url(self.paths.login)

    def test_block_user_data_unauth_registration(self):
        self.page.add_product()
        self.page.click(self.page.locators.UNAUTH_USER_DATA_MESSAGE_REGISTRATION_BUTTON)
        assert self.page.is_url(self.paths.signup)

    def test_edit_user_data_button(self):
        self.page.authorize()
        self.page.add_product_after_login()
        self.page.click(self.page.locators.BUTTON_EDIT_USER_DATA)
        assert self.page.is_url(self.paths.user)

    def test_sum_total_price_and_discount(self):
        self.page.add_product()
        total_price = self.page.get_total_price()
        discount = self.page.get_discount()
        price_without_discount = self.page.get_price_without_discount()

        assert price_without_discount == total_price + discount

    def test_count_product(self):
        self.page.add_product()

        assert self.page.find(self.page.locators.ITEM_COUNT).text == self.page.find(
            self.page.locators.TOTAL_COUNT_PRODUCT).text.split(' ')[1]

    def test_total_date_delivery(self):
        self.page.add_product()
        assert self.page.find(
            self.page.locators.TOTAL_DATE_DELIVERY).text == self.page.find(
            self.page.locators.DELIVERY_DATE).text

    def test_total_time_delivery(self):
        self.page.add_product()
        assert self.page.find(
            self.page.locators.TOTAL_TIME_DELIVERY).text == self.page.find(
            self.page.locators.DELIVERY_TIME).text

    def test_href_in_block_total_date_time_delivery(self):
        href = self.path.domain + self.path.cart + self.path.cartDeliveryAnchor
        self.page.add_product()

        assert self.page.find(
            self.page.locators.TOTAL_DELIVERY_INFO).get_attribute('href') == href
        assert self.page.find(
            self.page.locators.TOTAL_DATE_DELIVERY).get_attribute('href') == href
        assert self.page.find(
            self.page.locators.TOTAL_TIME_DELIVERY).get_attribute('href') == href

    def test_href_in_block_total_card(self):
        href = self.path.domain + self.path.cart + self.path.cartPaymentMethodAnchor
        self.page.add_product()

        assert self.page.find(self.page.locators.TOTAL_CARD).get_attribute('href') == href

    def test_total_unauth_message(self):
        message = self.loginToCompleteOrderPrompt
        self.page.add_product()
        assert self.page.find(self.page.locators.TOTAL_UNAUTH_MESSAGE).text == message

    def test_total_unauth_message_login_button(self):
        self.page.add_product()
        self.page.click(self.page.locators.TOTAL_UNAUTH_MESSAGE_LOGIN_BUTTON)
        assert self.page.is_url(self.paths.login)

    def test_button_make_order(self):
        self.page.authorize()
        self.page.add_product_after_login()
        assert self.page.find(self.page.locators.BUTTON_MAKE_ORDER).is_displayed()
        self.page.click(self.page.locators.BUTTON_MAKE_ORDER)
        assert self.page.is_url(self.paths.orders)
