import pytest

from selenium.webdriver.common.by import By

from ui.pages.base_page import WrongValue, PageNotOpenedExeption, ElementCheckException
from ui.pages.base_case import BaseCase, cookies, credentials
from ui.pages.main_page import MainPage
from ui.pages.article_page import ArticlePage


class TestAricleMainPageClicks(BaseCase):
    authorize = False

    def test_title_click(self):
        timeout = 15
        page = MainPage(self.driver)

        url = 'https://95.163.213.142/article/'
        title_xpath = '//div[text()=\'«Вкусвилл» начал тестировать продажу наборов еды в Китае под собственным брендом\']'
        title_el = page.find((By.XPATH, title_xpath), timeout)
        title = title_el.get_attribute("value")

        page.click((By.XPATH, title_xpath), timeout)
        if not page.driver.current_url.startswith(url):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

        title_el = page.find((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[2]'), timeout)
        new_title = title_el.get_attribute("value")
        if title != new_title:
            raise WrongValue(f'title must be {title} but it is {new_title}')
    
    def test_commentary_click(self):
        timeout = 15
        page = MainPage(self.driver)

        url = 'https://95.163.213.142/article/'
        endUrl = '?comments'

        title_xpath = '/html/body/div[2]/div[2]/div[1]/div[1]/div[2]'
        title_el = page.find((By.XPATH, title_xpath), timeout)
        title = title_el.get_attribute("value")

        page.click((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]'), timeout)
        if not page.driver.current_url.startswith(url):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')
        
        if not page.driver.current_url.endswith(endUrl):
            raise PageNotOpenedExeption(f'Page isnt scrolled to comments')

        title_el = page.find((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[2]'), timeout)
        new_title = title_el.get_attribute("value")
        if title != new_title:
            raise WrongValue(f'title must be {title} but it is {new_title}')
    
    def test_category_click(self):
        timeout = 15
        page = MainPage(self.driver)

        url = 'https://95.163.213.142/category/%D0%9A%D0%B0%D1%80%D1%8C%D0%B5%D1%80%D0%B0'

        page.click((By.XPATH, '//div[text()=\'Карьера\']'), timeout)
        if not page.driver.current_url.startswith(url):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')
    
    def test_author_click(self):
        timeout = 15
        page = MainPage(self.driver)

        url = 'https://95.163.213.142/author/alexandr'

        page.click((By.XPATH, '//div[text()=\'Александр Опрышко\']'), timeout)
        if not page.driver.current_url.startswith(url):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')
    
    def test_tag_click(self):
        timeout = 15
        page = MainPage(self.driver)

        url = 'https://95.163.213.142/search/tags/%D0%95%D0%B4%D0%B0'

        page.click((By.XPATH, '//div[text()=\'Еда\']'), timeout)
        if not page.driver.current_url.startswith(url):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')
    
    def test_chare_click(self):
        timeout = 15
        page = MainPage(self.driver)

        shareXPATH = '//div[text()=\'Поделиться\']'

        if page.exist((By.XPATH, shareXPATH)):
            raise ElementCheckException('Share box is opened from the start')

        page.click((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]'), timeout)
        if not page.exist((By.XPATH, shareXPATH)):
            raise ElementCheckException('Share box isnt opened')


class TestArticleView(BaseCase):
    authorize = False
    
    def test_category_shown(self):
        page = ArticlePage(self.driver, 1)
        
        if not page.find((By.ID, 'article__category'), 5):
            raise ElementCheckException('No category')
    
    def test_category_not_shown(self):
        page = ArticlePage(self.driver, 3)

        if page.exist((By.ID, 'article__category')):
            raise ElementCheckException('Category')


class TestArticleEditButton(BaseCase):
    authorize=True

    def test_edit_button_shown(self):
        timeout = 15
        page = MainPage(self.driver)

        page.click((By.XPATH, '//div[text()=\'«Вкусвилл» начал тестировать продажу наборов еды в Китае под собственным брендом\']'), timeout)
        #since SPA need to wait until article is opened
        page.exist((By.XPATH, '//div[@class=\'commentary__block__wrapper\']'), 2)

        if not page.exist((By.XPATH, '//div[@class=\'article__edit_button\']'), 2):
            raise ElementCheckException('No edit button in article by user')
            

    def test_category_not_shown(self):
        timeout = 15
        page = MainPage(self.driver)

        page.click((By.XPATH, '//div[text()=\'Непростая ситуация: увольнение за прогул при выезде в Казахстан\']'), timeout)
        #since SPA need to wait until article is opened
        page.exist((By.XPATH, '//div[@class=\'commentary__block__wrapper\']'), 2)
        
        if page.exist((By.XPATH, '//div[@class=\'article__edit_button\']'), 2):
            raise ElementCheckException('Edit button in article not by user')