from ui.pages.base_page import BasePage


class Favourites(BasePage):
    authToAddToFavourites = 'Войдите, чтобы добавить в избранное'

    def __init__(self, driver, selectors, url):
        super(Favourites, self).__init__(driver)
        self.locators = selectors
        self.url = url

    def unauthFavourites(self):
        favouritesLabel = self.find(self.locators.GET_FAVOURITES_LABEL)

        assert not favouritesLabel.get_attribute('checked')

        favouritesLabel.click()

        assert not favouritesLabel.get_attribute('checked')

        self.checkErrorMessage(self.authToAddToFavourites)

        assert not self.find(
            self.locators.GET_FAVOURITES_LABEL).get_attribute('checked')

    def authFavourites(self):
        favouritesInput = self.find(self.locators.GET_FAVOURITES_INPUT)

        if not favouritesInput.get_attribute('checked'):
            self.find(self.locators.GET_FAVOURITES_LABEL).click()
            assert favouritesInput.get_attribute('checked')

        else:
            self.find(self.locators.GET_FAVOURITES_LABEL).click()
            assert not favouritesInput.get_attribute('checked')
