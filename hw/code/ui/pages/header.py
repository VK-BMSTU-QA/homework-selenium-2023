from ui.pages.base_page import BasePage
from ui.locators.header_locators import HeaderLocators


class Header(BasePage):

    def __init__(self, driver):
        super(Header, self).__init__(driver)
        self.locators = HeaderLocators()
        self.url = self.locators.hrefs.domain + self.locators.hrefs.home

    def findLoginPageButton(self):
        return self.find(self.locators.OPEN_LOGIN_PAGE_BUTTON)

    def findUserPageButton(self):
        return self.find(self.locators.OPEN_USER_PAGE_BUTTON)

    def findLogOutPopUp(self):
        return self.find(self.locators.SIGN_OUT_POP_UP)

    def hoverOverLogout(self):
        logOutPopUp = self.findLogOutPopUp()

        assert logOutPopUp.value_of_css_property(
            "display") == 'none'

        self.hover(self.findUserPageButton())

        assert logOutPopUp.value_of_css_property(
            "display") == 'block'

        return logOutPopUp

    def logout(self):
        self.hoverOverLogout().click()

    def findFavouritesPageButton(self):
        return self.find(self.locators.OPEN_FAVOURITES_PAGE_BUTTON)

    def findCartPageButton(self):
        return self.find(self.locators.OPEN_CART_PAGE_BUTTON)

    def findOrdersPageButton(self):
        return self.find(self.locators.OPEN_ORDERS_PAGE_BUTTON)

    def findLogo(self):
        assert self.getHref(self.locators.GET_LOGO) == '/'
