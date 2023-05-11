import allure

from ui.fixtures import get_driver
from ui.pages.change_cart_count import CartCountChange
from ui.pages.login_page import LoginPage
from ui.pages.header import Header


class ChangeCartCountButton():
    driver = get_driver(browser_name='chrome')
    loginPage = LoginPage(driver)
    header = Header(driver)

    def __init__(self, selectors, url):
        self.cartCountChange = CartCountChange(self.driver, selectors(), url)

    @allure.feature('Test change number of items in cart')
    @allure.story('unauth case')
    def test_unauth_change_count_buttons(self):
        self.cartCountChange.render_page()

        with allure.step('initial checkButtonLabel'):
            self.cartCountChange.checkButtonLabel()

        with allure.step('initially adds item to cart'):
            self.cartCountChange.getAddDefaultButton().click()
            self.cartCountChange.checkNumberOfItemsInCart(1)

        with allure.step('addes one more item to cart'):
            self.cartCountChange.getPlusButton().click()
            self.cartCountChange.checkNumberOfItemsInCart(2)

        with allure.step('removes items from cart'):
            self.cartCountChange.getMinusButton().click()

            self.cartCountChange.checkNumberOfItemsInCart(1)
            self.cartCountChange.getMinusButton().click()

        with allure.step('checks if item successfully deleted from cart'):
            self.cartCountChange.checkButtonLabel()

    @allure.feature('Test change number of items in cart')
    @allure.story('unauth case')
    def test_auth_change_count_buttons(self):
        self.cartCountChange.render_page()

        with allure.step('login'):
            self.header.findLoginPageButton().click()
            self.loginPage.login()

        with allure.step('go back to page page'):
            self.cartCountChange.render_page()

        with allure.step('initial checkButtonLabel'):
            self.cartCountChange.checkButtonLabel()

        with allure.step('initially adds item to cart'):
            self.cartCountChange.getAddDefaultButton().click()

        with allure.step('checks cart count after new added'):
            self.cartCountChange.checkNumberOfItemsInCart(1)

        with allure.step('checks if item is is still in cart after reload'):
            self.cartCountChange.render_page()
            self.cartCountChange.getAddDefaultButton()
            self.cartCountChange.checkNumberOfItemsInCart(1)

        with allure.step('removes item from cart'):
            self.cartCountChange.getMinusButton().click()

        with allure.step('checks if item successfully deleted from cart after reload'):
            self.cartCountChange.render_page()
            self.cartCountChange.checkButtonLabel()

        with allure.step('logout'):
            self.header.logout()
