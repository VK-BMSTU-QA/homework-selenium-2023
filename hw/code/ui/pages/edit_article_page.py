from ui.pages.base_page import BasePage

class EditArticlePage(BasePage):
    url = 'https://95.163.213.142/article/'

    def __init__(self, driver, id: int):
        self.url = self.url + str(id) + '/edit/'
        driver.get(self.url)
        super().__init__(driver)