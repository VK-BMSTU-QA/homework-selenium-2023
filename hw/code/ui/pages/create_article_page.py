from ui.pages.base_page import BasePage

class CreateArticlePage(BasePage):
    url = 'https://95.163.213.142/new_article'

    def __init__(self, driver):
        self.url = self.url
        driver.get(self.url)
        super().__init__(driver)
