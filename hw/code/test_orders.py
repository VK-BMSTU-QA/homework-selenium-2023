from ui.pages.orders_page import OrdersPage
from ui.fixtures import get_driver
from ui.pages.header import Header
from ui.tabTitles import TabTitles


class TestOrders():
    driver = get_driver(browser_name='chrome')
    ordersPage = OrdersPage(driver)
    header = Header(driver)

    default_email = 'test@test'
    emailEmptyOrders = 'test2@test'
    password = '123456'

    @ordersPage.render_decorator
    def test_title(self):
        title = TabTitles().orders
        assert self.driver.title == title

    @ordersPage.render_decorator
    def test_no_auth(self):
        self.ordersPage.render(self.ordersPage.url)
        assert self.ordersPage.find(self.ordersPage.locators.BUTTON_NO_AUTH_REDIRECT).is_displayed()

    @ordersPage.render_decorator
    def test_empty_orders(self):
        self.ordersPage.authorize(self.emailEmptyOrders, self.password)
        self.ordersPage.render(self.ordersPage.url)
        assert self.ordersPage.find(self.ordersPage.locators.BUTTON_EMPTY_ORDERS_REDIRECT).is_displayed()
        self.header.findUserPageButton()
        self.header.logout()

    @ordersPage.render_decorator
    def test_button_deny_order(self):
        self.ordersPage.authorize(self.default_email, self.password)
        self.ordersPage.add_product_after_login()
        self.ordersPage.click(self.ordersPage.locators.BUTTON_MAKE_ORDER)
        self.ordersPage.click(self.ordersPage.locators.BUTTON_DENY_ORDER)
        self.ordersPage.waitUntilInvisible(self.ordersPage.locators.MESSAGE)
        assert self.ordersPage.find(self.ordersPage.locators.ORDER_STATUS).text == "Статус: отменен"
        self.header.findUserPageButton()
        self.header.logout()
