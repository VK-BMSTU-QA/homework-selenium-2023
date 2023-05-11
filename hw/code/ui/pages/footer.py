from ui.pages.base_page import BasePage
from ui.locators.footer_locators import FooterLocators


class Footer(BasePage):

    def __init__(self, driver):
        super(Footer, self).__init__(driver)
        self.locators = FooterLocators()
        self.url = self.locators.hrefs.domain + self.locators.hrefs.home

    def checkLogoBroken(self):
        self.scrollToLocator(self.locators.GET_LOGO)
        self.render(self.getSrc(self.locators.GET_LOGO))
