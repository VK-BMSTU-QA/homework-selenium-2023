from ui.pages.base_page import BasePage

class AuthorPage(BasePage):
    url = 'https://95.163.213.142/author/'

    def __init__(self, driver, slug: str):
        self.url = self.url + slug
        driver.get(self.url)
        super().__init__(driver)