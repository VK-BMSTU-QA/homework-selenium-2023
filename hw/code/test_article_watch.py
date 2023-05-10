import creds

from test_login import BaseCase, MainPage
from selenium.webdriver.common.by import By
from ui.pages.base_page import WrongValue, PageNotOpenedExeption

class TestAricleView(BaseCase):
    authorize = False
    
    def test_title_click(self):
        timeout = 15
        page = MainPage(self.driver)

        url = 'https://95.163.213.142/article/'
        title_xpath = '/html/body/div[2]/div[2]/div[3]/div[1]/div[2]'
        title_el = page.find((By.XPATH, title_xpath), timeout)
        title = title_el.get_attribute("value")

        page.click((By.XPATH, title_xpath), timeout)
        if not page.driver.current_url.startswith(url):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

        title_el = page.find((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[2]'), timeout)
        new_title = title_el.get_attribute("value")
        if title != new_title:
            raise WrongValue(f'title must be {title} but it is {new_title}')
