import allure
from ui.fixtures import get_driver
from ui.pages.footer import Footer


class TestFooter():
    driver = get_driver(browser_name='chrome')
    footer = Footer(driver)

    @allure.feature('TestFooter')
    @allure.story('is logo broken')
    @footer.render_decorator
    def test_footerLogo(self):
        self.footer.checkLogoBroken()
